
// feature test for AbortController that works in Safari 12
let abortableFetchSupported = false;

try{
  const ac = new AbortController()

  fetch('.', {signal: ac.signal})
  .then(r => r.text())
  .then(result => {
    abortableFetchSupported = false;
  })
  .catch(err => {
    abortableFetchSupported = err.name === 'AbortError'
  })

  ac.abort();
}
catch(e){
  abortableFetchSupported = false;
}

// FUNCTION TO PARSE AN OBJECT GIVEN A PATH
export function getObjectDataFromPath(obj, path, splitter='/') {
  let current = obj; 
  // console.log("+ + + getObjectDataFromPath / current raw : \n", current )
  path.split(splitter).forEach( function(p) { 
    current = current[p]; 
  }); 
  // console.log("+ + + getObjectDataFromPath / current final : \n", current )
  return current;
}

// FUNCTION TO GET THE RUN MODE FROM <HEAD>
export function getConfigName(metaName) {

  const metas = document.getElementsByTagName('meta');
  for (let i = 0; i < metas.length; i++) {
    if (metas[i].getAttribute('name') === metaName) {
      return metas[i].getAttribute('content');
    }
  }
  return '';
}


// server-side end-point to get only one project
export function getItemById(id,endpointConfig){

  // const url = searchEnpointCreator({
  //   page:1,
  //   per_page:1,
  //   baseUrl:root_url,
  //   item_id:id
  // })

  const url = searchEndpointGenerator({
    endpointConfig : endpointConfig,
    questionParams : { itemId : id },
    selectedFilters : [],
  })

  return fetch(url)
  .then(r => r.json())
  .then(({data, query}) =>
    data && data.data_raw && data.data_raw.f_data  && Array.isArray(data.data_raw.f_data)
      ? data.data_raw.f_data[0]
      : undefined
  )
}


export function searchItems(url = undefined){

  // console.log("+ + + searchItems ... ");

  // abort fetch if this is supported
  // abort manually when response arrives otherwise
  const ac = abortableFetchSupported ? new AbortController() : undefined
  let searchAborted = false

  return {
    abort(){
      searchAborted = true
      if(ac)
          ac.abort()
    },
    promise: (ac ? fetch(url, {signal: ac.signal} ) : fetch(url))
    .then(r => r.json())
    .then(({data, query}) => {
      if(searchAborted){
        const error = new Error('Search aborted')
        error.name = 'AbortError'
        throw error
      }
      else{
        // console.log("+ + + searchItems (response) / data :", data);
        return {
          projects: data
          && data.data_raw
          && data.data_raw.f_data
          && Array.isArray(data.data_raw.f_data)
          ? data.data_raw.f_data
          : [],
          total: (data && data.data_raw && data.data_raw.f_data_count) ? data.data_raw.f_data_count : 0
        }
      }
    })

  }

}

export function searchEndpointGenerator(obj) {
  if (!obj) { throw 'error in searchEndpointGenerator: no parameter defined' }

  // console.log("+ + + searchEndpointGenerator / ...")
  // console.log("+ + + searchEndpointGenerator / obj : \n ", obj)

  // endpoint config related
  const endpointConfig = obj.endpointConfig
  const endpointConfigArgs = endpointConfig.args_options

  // question related
  const questionParams = obj.questionParams
  const selectedFilters = obj.selectedFilters

  // base query to be completed with args + questions
  let baseQuery = endpointConfig.root_url + '?'

  const appArgs = ['query', 'forMap', 'page', 'perPage', 'onlyGeocoded', 'itemId', 'shuffleSeed' ]
  
  // loop in routeArgs + queries then append to baseQuery
  let argsArray = []
  for (let key in endpointConfigArgs ) {
    const EndpointArg = endpointConfigArgs[key]
    // console.log("+ + + searchEndpointGenerator / EndpointArg : ", EndpointArg)
    if ( !EndpointArg.optional || appArgs.indexOf(EndpointArg.app_arg) !== -1 ){
      if ( questionParams[EndpointArg.app_arg] ) {
        let argString = EndpointArg.arg + '=' + questionParams[EndpointArg.app_arg]
        argsArray.push(argString)
      }
    }
  }

  // loop in selectedFilters to add filters request if any
  // find corresponding mapper in endPointConfig
  const filterMapper = endpointConfigArgs.find( c => c.app_arg === 'filters')
  // console.log("+ + + searchEndpointGenerator / filterMapper : \n ", filterMapper)
  if (filterMapper && selectedFilters.length > 0 ){
    const EndpointArg = filterMapper.arg
    for (let index in selectedFilters) {
      let argFilterString = EndpointArg + '=' + selectedFilters[index]
      argsArray.push(argFilterString)
    }
  }

  let argsLongString = argsArray.join('&')
  baseQuery += argsLongString


  // console.log("+ + + searchEndpointGenerator / baseQuery : \n ", baseQuery)

  return baseQuery
}

// export function searchEnpointCreator(obj){

//   // (text, tags, page=1, per_page=100, baseUrl = `${APISearchOrigin}`, token = undefined ){
//   if (!obj) { throw 'error in searchEnpointCreator: no parameter defined' }

//   // console.log("+ + + searchEnpointCreator / ...")
//   console.log("+ + + searchEnpointCreator / obj : \n ", obj)

//   // the first argument: no & at the begining
//   const pageArg = (typeof obj.page == 'number') ? 'page='+obj.page : 'page=1';

//   // then come the other arguments
//   const searchArg = (typeof obj.search === 'string' && obj.search.length >= 1) ? '&search_for='+encodeURIComponent( obj.search.trim() ) : '';
//   const shuffle_seedArg = (typeof obj.shuffle_seed == 'number') ? '&shuffle_seed='+obj.shuffle_seed : '&shuffle_seed=' + Math.floor((Math.random() * 10000) + 1) ;
//   const tagsArg = (obj.tags && obj.tags.size >= 1) ? `&search_in_tags=${encodeURIComponent([...obj.tags].join(','))}` : '';
//   const tokenArg = (obj.token) ? `&token=${encodeURIComponent(obj.token)}` : ''

//   //if none, default value provided (otherwise the backend will provide anyway)
//   const per_pageArg = (typeof obj.per_page == 'number') ? '&per_page='+obj.per_page : '&per_page=100';
//   const map_listArg = (typeof obj.map_list == 'boolean') ? '&map_list='+obj.map_list : '&map_list=false';
//   const as_latlngArg = (typeof obj.as_latlng == 'boolean') ? '&as_latlng='+obj.as_latlng : '&as_latlng=false';
//   const only_geocodedArg = (typeof obj.only_geocoded == 'boolean') ? '&only_geocoded='+obj.only_geocoded : '&only_geocoded=true';
//   const geo_precisionArg = (typeof obj.geo_precision == 'number') ? '&geo_precision='+obj.geo_precision : '&geo_precision=6';
//   const get_filtersArg = (typeof obj.get_filters == 'boolean') ? '&get_filters='+obj.get_filters : '&get_filters=false';
//   const is_completeArg = (typeof obj.is_complete == 'boolean') ? '&is_complete='+obj.is_complete : '&is_complete=false';
//   const only_statsArg = (typeof obj.only_stats == 'boolean') ? '&only_stats='+obj.only_stats : '&only_stats=false';
//   const normalizeArg = (typeof obj.normalize == 'boolean') ? '&normalize='+obj.normalize : '&normalize=false';

//   // if none, don't do
//   const search_forArg = (typeof obj.search_for == 'string') ? '&search_for='+obj.search_for : '';
//   const search_inArg = (typeof obj.search_in == 'string') ? '&search_in='+obj.search_in : '';
//   const search_tagsArg = (typeof obj.search_tags == 'string') ? '&search_tags='+obj.search_tags : '';
//   const search_filtersArg = (obj.search_filters && obj.search_filters.length >= 1) ? `&search_filters=${[...obj.search_filters].join('&search_filters=')}` : '';
//   const search_intArg = (typeof obj.search_int == 'number') ? '&search_int='+obj.search_int : '';
//   const search_floatArg = (typeof obj.search_float == 'number') ? '&search_float='+obj.search_float : '';
//   const item_idArg = (typeof obj.item_id == 'string') ? '&item_id='+obj.item_id : '';
//   const sort_byArg = (typeof obj.sort_by == 'string') ? '&sort_by='+obj.sort_by : '';
//   const descendingArg = (typeof obj.descending == 'boolean') ? '&descending='+obj.descending : '';


//   // WITHOUT SHUFFLE
//   // return obj.baseUrl+`?${pageArg}${per_pageArg}${searchArg}${tagsArg}${tokenArg}${map_listArg}${as_latlngArg}${only_geocodedArg}${geo_precisionArg}${get_filtersArg}${is_completeArg}${only_statsArg}${normalizeArg}${search_forArg}${search_inArg}${search_tagsArg}${search_intArg}${search_floatArg}${item_idArg}${sort_byArg}${descendingArg}`

//   // WITH SHUFFLE
//   return obj.baseUrl+`?${pageArg}${per_pageArg}${shuffle_seedArg}${searchArg}${tagsArg}${tokenArg}${map_listArg}${as_latlngArg}${only_geocodedArg}${geo_precisionArg}${get_filtersArg}${is_completeArg}${only_statsArg}${normalizeArg}${search_forArg}${search_inArg}${search_tagsArg}${search_filtersArg}${search_intArg}${search_floatArg}${item_idArg}${sort_byArg}${descendingArg}`
// }



export function makeEmptySelectedFilters(filterDescriptions){
  // console.log("::: makeEmptySelectedFilters / filterDescriptions : ", filterDescriptions)
  const selectedFilters = new Map()
  for(const f of filterDescriptions){
    selectedFilters.set(f.name, new Set())
  }
  return selectedFilters;
}

export function textFromLocale(textsList, locale, field){
  // console.log("::: textFromLocale / textsList : ", textsList)
  // console.log("::: textFromLocale / locale : ", locale)
  // console.log("::: textFromLocale / field : ", field)
  let textObject = textsList.find(t => t.locale == locale )
  let textOut = textObject[field]
  // console.log("::: textFromLocale / textOut : ", textOut)
  return textOut
}

export function createSelectedFiltersForSearch(selectedFiltersMap){
  let filtersUri = []
  selectedFiltersMap.forEach( (val,key,map) => {
    // console.log('val,key,map',val,key,map);
    val.forEach( (v) => {
      filtersUri.push(key + v)
    })
  })
  // console.log(filtersUri);
  return filtersUri
}
