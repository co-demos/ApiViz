import axios from 'axios';
// import {apiConfig} from '../config/api.js';
import {csvParse} from 'd3-dsv';
import {searchItems, searchEnpointCreator, searchEndpointGenerator, createSelectedFiltersForSearch} from '../utils.js';


export default {



  // FOR FILTERS
  createDatasetFilters({state, getters, commit}){
    // console.log("\n// createDatasetFilters / state : ", state )
    const currentFiltersConfig = getters.getEndpointConfigFilters
    // console.log("// createDatasetFilters / currentFiltersConfig : ", currentFiltersConfig)
    if (currentFiltersConfig && currentFiltersConfig.filter_options){
      let filterDescriptions = currentFiltersConfig.filter_options
      commit('setFilterDescriptions', filterDescriptions)
      commit('clearAllFilters')
    }
  },

  // FOR QUERY SEARCH FILTERS
  toggleFilter({state, commit, dispatch, getters}, {filter, value}){
    // console.log("\n// toggleFilter ..." )
    const selectedFilters = new Map(getters.getSelectedFilters)
    // console.log("// toggleFilter / selectedFilters : ", selectedFilters);
    const selectedValues = selectedFilters.get(filter)
    if(selectedValues.has(value))
      selectedValues.delete(value)
    else
      selectedValues.add(value)

    commit('setSelectedFilters', {selectedFilters})
    dispatch('search')
  },

  emptyOneFilter({state, commit, dispatch, getters}, {filter}){
    // console.log("\n// emptyOneFilter ..." )
    const selectedFilters = new Map(getters.getSelectedFilters)
    selectedFilters.set(filter, new Set())

    commit('setSelectedFilters', {selectedFilters})
    dispatch('search')
  },

  clearAllFilters({commit, dispatch}){
    // console.log("\n// clearAllFilters ..." )
    commit('clearAllFilters')
    dispatch('search')
  },

  // FOR QUERY SEARCH TEXT
  searchedTextChanged({commit, dispatch}, {searchedText}){
    // console.log("\n// searchedTextChanged ..." )
    commit('setSearchedText', {searchedText})
    dispatch('search')
  },


  // MAIN SEARCH ACTION
  search({state, commit, dispatch, getters}){

    // console.log("\n// search / main action to query endpoint..." )
    const {search} = state;
    // console.log("// search / search : ", search )

    const selectedFilters = createSelectedFiltersForSearch(getters.getSelectedFilters)
    // console.log('selectedFilters',selectedFilters);
    // abort previous search if any
    if(search.answer.pendingAbort){
      search.answer.pendingAbort.abort()
    }


    //create the endpoints
    // let root_url = (state.search && state.search.endpoint) ? state.search.endpoint.root_url : dispatch('getConfigType',{type:'endpoints',configTypeEndpoint:'endpoints'})

    // let endpoint = searchEnpointCreator({
    //   baseUrl:root_url,
    //   // query from main input in search bar
    //   search: search.question.query,
    //   // tags / filters
    //   search_filters:selectedFilters,
    //   // pagination
    //   page:1,
    //   per_page:100,
    //   // here for map requests
    //   map_list : search.question.for_map,
    //   as_latlng : search.question.for_map

    // })
    // console.log("-- search / endpoint : \n", endpoint )

    // ENDPOINT GENERATOR
    let endpointGenerated = searchEndpointGenerator({
      endpointConfig : state.search.endpoint,
      questionParams : state.search.question,
      selectedFilters : selectedFilters,
    })
    // console.log("-- search / endpointBis : \n", endpointGenerated )


    // perform search --> !!! only request map search if map search results empty in store !!! 
    // const searchPendingAbort = searchItems(endpoint)
    const searchPendingAbort = searchItems(endpointGenerated)
    commit('setSearchPending', { pendingAbort: searchPendingAbort })

    searchPendingAbort.promise
      .then(({projects, total}) => {
        // console.log("-- search / total : \n", total )
        // console.log("-- search / projects : \n", projects )

        // if search is for map either fill resultMap if empty or do nothing
        commit('setSearchResult', {result: {projects, total}})
        // commit ('setSearchResultMap', {resultMap: {projects, total}})
      })
      .catch(error => {
        // don't report aborted fetch as errors
        if (error.name !== 'AbortError')
          commit('setSearchError', {error})
      })
  },


  ////////////////////////////////////////////////
  // TO COMMENT ABSOLUTLY -> data must be pre-geocoded when arriving as response
  findProjectsGeolocs({commit}, projects){
    const projectWithValidAddress = projects.filter(p => p['address'])
    const addresses = projectWithValidAddress.map(p => p['address'].replace(/[^(\w|\s)]/g, '').slice(0, 200) )

    const adressesCSV = 'adresse\n' + addresses.join('\n')
    const adresseCSVBANBody = new FormData();
    adresseCSVBANBody.append('data', new File([adressesCSV], 'adresses.csv'))

    return fetch('https://api-adresse.data.gouv.fr/search/csv/', {
      method: 'POST',
      body: adresseCSVBANBody,
    })
    .then(r => r.text())
    .then(geolocsTxt => {
      const geolocs = csvParse(geolocsTxt);

      const geolocByProjectId = new Map();

      projectWithValidAddress.forEach(({id}, i) => {
        const {latitude, longitude} = geolocs[i];

        geolocByProjectId.set(
          id,
          (Number.isFinite(parseFloat(latitude)) && Number.isFinite(parseFloat(longitude))) ?
            {latitude: parseFloat(latitude), longitude: parseFloat(longitude)} :
            false
        )
      })

      projects.forEach(({id}) => {
        if(!geolocByProjectId.has(id)){
          geolocByProjectId.set(id, false)
        }
      })

      commit('addGeolocs', {geolocByProjectId})
    });
  },
  /////////////////////////:



  // FOR CONFIGs
  getConfigAll({dispatch}) {
    let arr = []
    arr.push(dispatch('getConfigType',{type:'global',configTypeEndpoint:'global'}) )
    arr.push(dispatch('getConfigType',{type:'styles',configTypeEndpoint:'styles'}) )
    arr.push(dispatch('getConfigType',{type:'socials',configTypeEndpoint:'socials'}) )
    arr.push(dispatch('getConfigType',{type:'footer',configTypeEndpoint:'footer'}) )
    arr.push(dispatch('getConfigType',{type:'navbar',configTypeEndpoint:'navbar'}) )
    arr.push(dispatch('getConfigType',{type:'routes',configTypeEndpoint:'routes?as_list=true'}) )
    arr.push(dispatch('getConfigType',{type:'endpoints',configTypeEndpoint:'endpoints?as_list=true'}) )
    return Promise.all(arr)
  },

  getConfigType({commit, getters},{type,configTypeEndpoint}) {
    const rootURLbackend = getters.getRootUrlBackend
    return axios
    .get(rootURLbackend+'/config/'+configTypeEndpoint)
    // .get(apiConfig.rootURL+'/config/'+configTypeEndpoint)
    .then(response => {
      // console.log("type : ", type," / response : ", response)
      let app_config = (response && response.data && response.data.app_config) ? response.data.app_config : undefined
      commit('setConfig', {type:type,result:app_config}); 
      return app_config
    })
    .catch( err => console.log('there was an error trying to fetch some configuration file',err) )
  },


  // TO VARIABILIZE
  setSearchConfigDisplay({commit}) {
    // here this function will probably change when this may be inherited from the configuration files
    const defaultDisplay = {
      columnCount : 4,
      defaultShowCount : 50,
      moreProjectOnScrollCount : 20,
      scrollBeforeBottomTrigger : 500
    }
    commit('setSearchConfig', {type:'display',result:defaultDisplay});
  },

  // USER-RELATED
  saveLoginInfos({commit}, {APIresponse}){
    let r = APIresponse
    let tokens = (r && r.data && r.data.tokens) ? r.data.tokens : undefined
    let infos = (r && r.data && r.data.data && r.data.data.infos) ? r.data.data.infos : undefined
    let role = (r && r.data && r.data.data && r.data.data.auth && r.data.data.auth.role) ? r.data.data.auth.role : undefined

    commit('setTokens', {tokens})
    commit('setInfos', {infos})
    commit('setRole', {role})
  },
  logout({commit}){
    commit('setTokens', {})
    commit('setInfos', {})
    commit('setRole', {})
  },


  // FOR ENDPOINT CONFIG
  setSearchEndpointConfig({commit,getters,state},{path}) {

    let routeConfig = getters.getCurrentRouteConfig(path)

    commit('setSearchParam',{type:'currentRouteConfig',result:routeConfig})
    commit('setSearchParam',{type:'dataset_uri',result:routeConfig.dataset_uri})
    commit('setSearchParam',{type:'endpoint_type',result:routeConfig.endpoint_type})
    
    let endpointConfig = getters.getEndpointConfig
    commit('setSearchParam',{type:'endpoint',result:endpointConfig})

  },
  
}
