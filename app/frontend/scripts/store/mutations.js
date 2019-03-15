import { apiConfig } from '../config/api.js';
import {makeEmptySelectedFilters} from '../utilsApiviz';

const SOURCE_FILTER_NAME = 'source_';

export default {

  // APP MODE AND ROOT URL BACKEND
  setRunMode(state, runMode ){
    console.log("\n=== setRunMode / runMode : ", runMode )
    state.runMode = runMode
    console.log("=== setRunMode / apiConfig : \n ", apiConfig )
    const roots = apiConfig[runMode]
    state.rootUrlBackend = roots.rootURL
  },


  // FILTERS-RELATED
  setDatasetFilters(state, datasetFilter ){
    console.log("\n=== setDatasetFilters / datasetFilter : ", datasetFilter )
    const filterOptions = datasetFilter.filter_options
    console.log("=== setDatasetFilters / filterOptions : ", filterOptions )
    state.datasetFilters = filterOptions
  },
  // LEGACY - SPIDERS RELATED
  setSourceFilter(state, {sourceFilter}){
    const sourceFilterIndex = state.filterDescriptions.findIndex(fd => fd.name === SOURCE_FILTER_NAME)

    if(sourceFilterIndex !== -1){
      state.filterDescriptions[sourceFilterIndex] = sourceFilter
    }
    else{
      state.filterDescriptions.push(sourceFilter);
      state.search.question.selectedFilters.set(SOURCE_FILTER_NAME, new Set())
      //state.filterDescriptions = state.filterDescriptions
    }
  },
  // LEGACY
  setSpiders(state, {spiders}){
    state.spiders = spiders
  },

  // SEARCH-RELATED
  setIsMapSearch (state, routeConfig) {
    console.log("\n=== setIsMapSearch / routeConfig : ", routeConfig )
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
    console.log("== setSearchResult / result : ", result)
    state.search.answer = {
      pendingAbort: undefined,
      result,
      error: undefined
    }
  },
  setSearchPending(state, {pendingAbort}){
    state.search.answer = {
      pendingAbort,
      result: undefined,
      error: undefined
    }
  },
  setSearchError(state, {error}){
    console.error('search error', error)
    state.search.answer = {
      pendingAbort: undefined,
      result: undefined,
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
