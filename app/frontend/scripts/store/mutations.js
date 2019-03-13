const SOURCE_FILTER_NAME = 'source_';

export default {

    setAsMapSearch (state, isForMap) {
        state.search.question.for_map = isForMap
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

    setSearchResult(state, {result}){
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

    setDisplayedProject(state, {project}){
        state.displayedProject = project;
    },
    setSpiders(state, {spiders}){
        state.spiders = spiders
    },
    addGeolocs(state, {geolocByProjectId}){
        state.geolocByProjectId = new Map([...state.geolocByProjectId, ...geolocByProjectId])
    },

    setConfig(state, {type,result}) {
        // console.log("result : ", result)
        state.config[type] = result
    },

    setSearchConfig(state, {type,result}) {
        state.search.config[type] = result
    },
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
    setSearchParam(state,{type,result}){
        // console.log("\n== setSearchParam / state.search : ", state.search)
        // console.log("== setSearchParam / type : ", type)
        // console.log("== setSearchParam / result : ", result)
        state.search[type] = result
    }
}
