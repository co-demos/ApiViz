import { apiConfig } from '../config/api.js';
import {makeEmptySelectedFilters} from '../utils';

export default {

  // APP MODE AND ROOT URL BACKEND
  setRunMode(state, runMode ){
    // console.log("\n=== setRunMode / runMode : ", runMode )
    state.runMode = runMode
    // console.log("=== setRunMode / apiConfig : \n ", apiConfig )
    const roots = apiConfig[runMode]
    state.rootUrlBackend = roots.rootURL
  },

  // UX OPTIONS-RELATED
  disableBanners(state){
    state.bannerVisible = false
  },
  switchNavbarMenu(state){
    state.showNav = !state.showNav
  },

  // FILTERS-RELATED
  setDatasetFilters(state, datasetFilter ){
    // console.log("\n=== setDatasetFilters / datasetFilter : ", datasetFilter )
    const filterOptions = datasetFilter.filter_options
    // console.log("=== setDatasetFilters / filterOptions : ", filterOptions )
    state.datasetFilters = filterOptions
  },
  
  // SEARCH-RELATED
  setDatasetURI(state, datasetURI){
    state.search.dataset_uri = datasetURI
  },
  setIsMapSearch (state, routeConfig) {
    // console.log("\n=== setIsMapSearch / routeConfig : ", routeConfig )
    state.search.question.forMap = ( routeConfig.dynamic_template === 'DynamicMap' ) ? true : false
    // console.log("=== setIsMapSearch / state.search : ", state.search )
  },
  setSearchedText (state, {searchedText}) {
    state.search.question.query = searchedText
  },
  setSelectedFilters (state, {selectedFilters}) {
    // trigger re-render
    state.search.question.selectedFilters = new Map(selectedFilters)
  },
  setFilterDescriptions (state, filterDescriptions) {
    state.filterDescriptions = filterDescriptions
  },
  emptyOneFilter (state, {filter}) {
      state.search.question.selectedFilters.set(filter, new Set())

      // trigger re-render
      state.search.question.selectedFilters = new Map(state.search.question.selectedFilters)
  },
  clearAllFilters(state){
      state.search.question.selectedFilters = makeEmptySelectedFilters(state.filterDescriptions)
  },
  setSearchParam(state,{type,result}){
    // console.log("\n== setSearchParam / state.search : ", state.search)
    // console.log("== setSearchParam / type : ", type)
    // console.log("== setSearchParam / result : ", result)
    state.search[type] = result
  },
  setSearchConfig(state, {type,result}) {
    state.search.config[type] = result
  },

  // RESULTS-RELATED
  setSearchResult(state, {result}){
    // console.log("== setSearchResult / result : ", result)
    state.search.answer = {
      pendingAbort: undefined,
      result,
      // resultMap: undefined,
      error: undefined
    }
  },
  // setSearchResultMap(state, {resultMap}){
  //   console.log("== setSearchResultMap / resultMap : ", resultMap)
  //   state.search.answer = {
  //     pendingAbort: undefined,
  //     result:undefined,
  //     // resultMap,
  //     error: undefined
  //   }
  // },
  setSearchPending(state, {pendingAbort}){
    state.search.answer = {
      pendingAbort,
      result: undefined,
      // resultMap: undefined,
      error: undefined
    }
  },
  setSearchError(state, {error}){
    console.error('search error', error)
    state.search.answer = {
      pendingAbort: undefined,
      result: undefined,
      // resultMap: undefined,
      error
    }
  },

  setDisplayedProject(state, {project}){
    state.displayedProject = project;
  },


  ///GEOLOC
  addGeolocs(state, {geolocByProjectId}){
      state.geolocByProjectId = new Map([...state.geolocByProjectId, ...geolocByProjectId])
  },

  // CONFIG
  setConfig(state, {type,result}) {
      // console.log("result : ", result)
      state.config[type] = result
  },

  // USER-RELATED
  setTokens (state, {tokens}) {
      state.jwt = (tokens && tokens.access_token && tokens.refresh_token) ? tokens : undefined
  },
  setInfos (state, {infos}) {
      state.user.infos = (infos && infos.email) ? infos : undefined
      state.user.isLoggedin = (infos && infos.email) ? true : false
  },
  setRole (state, {role}) {
      state.user.role = (typeof role === 'string') ? role : undefined
  },


}
