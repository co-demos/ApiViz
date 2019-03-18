
import { textFromLocale } from '../utilsApiviz.js';


const getSearchConfigColumnCount = state => state.search.config.display.columnCount;
const getSearchConfigDefaultShowCount = state => state.search.config.display.defaultShowCount;
const getSearchConfigMoreProjectOnScrollCount = state => state.search.config.display.moreProjectOnScrollCount;
const getSearchConfigScrollBeforeBottomTrigger = state => state.search.config.display.scrollBeforeBottomTrigger;

// FOR TRANSLATIONS
// - - - - - - - - - - - - - - - //
  const getTranslation = (state) => (textsData) => {
    const locale = state.locale
    const textField = 'text'
    // console.log("textsData : ", textsData)
    return textFromLocale( textsData.texts, locale, textField )
  }

// GLOBAL APP CONFIG GETTERS
// - - - - - - - - - - - - - - - //
  const getRootUrlBackend = state => {
    return state.rootUrlBackend
  }
  const getGlobalConfig = state => {
    // console.log("state.config : \n", state.config )
    if (!state.config
      || !state.config.global
      ) {
        console.log('getGlobalConfig - some condition not respected');       return undefined;
    }
    return state.config.global
  }
  const getStylesConfig = state => {
    // console.log("state.config : \n", state.config )
    if (!state.config
      || !state.config.styles
      ) {
        console.log('getStylesConfig - some condition not respected');       return undefined;
    }
    return state.config.styles
  }
  const getSocialsConfig = state => {
    // console.log("state.config : \n", state.config )
    // if (!state.config
    //   || !state.config.socials
    //   ) {
    //     console.log('getSocialsConfig - some condition not respected');       return undefined;
    // }
    return state.config.socials
  }
  const getNavbarConfig = state => {
    // console.log("state.config : \n", state.config )
    if (!state.config
      || !state.config.navbar
      ) {
        console.log('getNavbarConfig - some condition not respected');       return undefined;
    }
    return state.config.navbar.app_navbar
  }
  const getFooterConfig = state => {
    // console.log("state.config : \n", state.config )
    if (!state.config
      || !state.config.footer
      ) {
        console.log('getFooterConfig - some condition not respected');       return undefined;
    }
    return state.config.footer.app_footer
  }


// ROUTE CONFIG GETTERS
// - - - - - - - - - - - - - - - //
  const getCurrentRouteConfig = (state) => (currentRoute) => {
    // console.log('\n ++ getCurrentRouteConfig / currentRoute : \n', currentRoute)
    // console.log(' ++ getCurrentRouteConfig / state.config.routes : \n', state.config.routes)
    try {
      return state.config.routes.find(function(r) {
        return r.urls.indexOf(currentRoute) !== -1;
      });
    } catch (e) {
      console.log('err',e);
      return undefined
    }
  }
  const getRouteConfigListForDataset = state => {
    return state.config.routes.find(function(r) {
      return r.endpoint_type === 'list'
      && r.dataset_uri === state.search.dataset_uri;
    });
  }
  const getRouteConfigMapForDataset = state => {
    return state.config.routes.find(function(r) {
      return r.endpoint_type === 'map'
      && r.dataset_uri === state.search.dataset_uri;
    });
  }
  const getRouteConfigStatForDataset = state => {
    return state.config.routes.find(function(r) {
      return r.endpoint_type === 'stat'
      && r.dataset_uri === state.search.dataset_uri;
    });
  }
  const getRouteConfigDefaultDatasetImages = state => {
    return state.config.styles.app_search_default_images_sets.images_sets.find(function(r) {
      return r.dataset_uri === state.search.dataset_uri;
    });
  }

// DEFAULT TEXTS GETTERS
// - - - - - - - - - - - - - - - //
  const defaultText = (state) => (field) => {
    // default texts fields are :
    // 'reinit_filters', 'no_abstract', 'no_address'
    // 'source', 'no_info'
    const f = field.txt
    const noAbstractDict = state.config.global.app_basic_dict[f]
    let text = noAbstractDict.find(t=>t.locale == state.locale )
    return text.text
  }

// ITEMS CONFIG GETTERS
// - - - - - - - - - - - - - - - //
  const getProjectConfig = (state) => (position) => {
    try {
      return state.search.currentRouteConfig.contents_fields.find( function(f) {  return f.position === position; });
    }
    catch (e) {
      console.log('err',e);
      return undefined
    }
  }

  const getProjectConfigUniform = (state, getters) => (itemData) => {
    // console.log(" ++ getProjectConfigUniform - itemData : ", itemData)
    let res = {}
    const infoTypes = ['id','title','image','address','tags']
    infoTypes.forEach( function(infoType){
      let fieldObj = getters.getProjectConfig('block_'+infoType)
      res[infoType] = (fieldObj && fieldObj.field) ? itemData[fieldObj.field] : undefined
    })
    res.image = getters.getImgUrl(res)
    res.fullItem = itemData
    return res
  }

  const getResults = (state) => {
    return state.search.answer.result && state.search.answer.result.projects
  }

  const getGeoResults = (state, getters) => {
    let allResults = getters.getResults
    console.log(" ++ getGeoResults / allResults : ", allResults)
    if (typeof allResults !== 'undefined'){
      let filtered = allResults.filter(i => !i.lat && !i.lon)
      console.log(" ++ getGeoResults / filtered : ", filtered)
      return filtered
    } else {
      return undefined
    }
  }


// IMAGES CONFIG GETTERS
// - - - - - - - - - - - - - - - //
  const getImgUrl = (state, getters) => (obj) => {
    // console.log("getImgUrl - obj : ", obj)
    let image = obj.image

    if(!image){
      let images_set = undefined
      if (state.search.dataset_uri
        && state.config.styles
        && state.config.styles.app_search_default_images_sets
        && state.config.styles.app_search_default_images_sets.images_sets) {
        let d = state.config.styles.app_search_default_images_sets.images_sets.find(function(d){
          return d.dataset_uri === state.search.dataset_uri;
        })
        images_set  = (d) ? d.images_set : undefined
      }

      if (images_set && images_set.length > 0) {
        const textureCount = images_set.length + 1
        let id = (obj.id) ? parseInt(obj.id.substr(obj.id.length - 6), 16) % textureCount : 111111111111111111
        let reste = id % images_set.length + 1;
        let imageObj = images_set.find(function(i){
          return i.dft_text === 'img_'+reste;
        })
        image = imageObj.src_image
      }else {
        let random = Math.floor(Math.random() * (7 - 1) + 1)
        image = `/static/illustrations/textures/medium_fiche_${ (parseInt(id.substr(id.length - 6), 16)%textureCount) + 1}.png`
      }
    }
    return image
  }

  const getImageUrl = (state, getters) => (obj) => {

    console.log("getImageUrl - obj : ", obj)
    const item = obj.item
    const position = obj.position

    const defaultImages = getters.getRouteConfigDefaultDatasetImages
    console.log("getImageUrl - defaultImages : ", defaultImages)

    const routeContentImagesFields = state.search.currentRouteConfig.images_fields
    console.log("getImageUrl - routeContentImagesFields : ", routeContentImagesFields)

    let fieldToGet = routeContentImagesFields[position]
    let fieldImage = fieldToGet.field
    console.log("getImageUrl - fieldImage : ", fieldImage)

    let image = item[fieldImage]

    if(!image){
      let d = defaultImages
      let images_set  = (d) ? d.images_set : undefined

      if (images_set && images_set.length > 0) {
        const textureCount = images_set.length + 1
        let id = (item.id) ? parseInt(item.id.substr(item.id.length - 6), 16) % textureCount : 111111111111111111
        let tail = id % images_set.length + 1;
        let imageObj = images_set.find(function(i){
          return i.dft_text === 'img_'+tail;
        })
        image = imageObj.src_image
      } else {
        image = `/static/illustrations/textures/medium_fiche_${ (parseInt(id.substr(id.length - 6), 16)%textureCount) + 1}.png`
      }
    }
    return image
  }

// - - - - - - - - - - - - - - - //
// BROADER CONFIG GETTERS
// - - - - - - - - - - - - - - - //
  const getEndpointConfig = state => {
    // console.log("getEndpointConfig - state.config : \n", state.config)
    // if (!state.config
    //   || !state.config.endpoints
    //   || !state.search.endpoint_type
    //   || !state.search.dataset_uri
    //   ) {
    //     console.log('some condition not respected');       return undefined;
    // }
    return state.config.endpoints.find(function(r) {
      return r.endpoint_type === state.search.endpoint_type
      && r.dataset_uri === state.search.dataset_uri;
    });
  }
  const getEndpointConfigFilters = state => {
    // console.log("getEndpointConfigFilters - state.config.endpoints : \n", state.config.endpoints)
    return state.config.endpoints.find(function(r) {
      return r.endpoint_type === 'filters'
      && r.dataset_uri === state.search.dataset_uri;
    });
  }
  const getEndpointConfigList = state => {
    // console.log("getEndpointConfigList - state.config.endpoints : \n", state.config.endpoints)
    return state.config.endpoints.find(function(r) {
      return r.endpoint_type === 'list'
      && r.dataset_uri === state.search.dataset_uri;
    });
  }
  const getEndpointConfigMap = state => {
    // console.log("getEndpointConfigMap - state.config.endpoints : \n", state.config.endpoints)
    return state.config.endpoints.find(function(r) {
      return r.endpoint_type === 'map'
      && r.dataset_uri === state.search.dataset_uri;
    });
  }
  const getEndpointConfigDetail = state => {
    // console.log("getEndpointConfigDetail - state.config.endpoints : \n", state.config.endpoints)
    return state.config.endpoints.find(function(r) {
      return r.endpoint_type === 'detail'
      && r.dataset_uri === state.search.dataset_uri;
    });
  }
  const getEndpointConfigStat = state => {
    // console.log("getEndpointConfigStat - state.config.endpoints : \n", state.config.endpoints)
    return state.config.endpoints.find(function(r) {
      return r.endpoint_type === 'stat'
      && r.dataset_uri === state.search.dataset_uri;
    });
  }


// - - - - - - - - - - - - - - - //
// FINALLY EXPORT GETTERS
// - - - - - - - - - - - - - - - //
  export default {
    getTranslation,

    getRootUrlBackend,
    getSearchConfigColumnCount,
    getSearchConfigDefaultShowCount,
    getSearchConfigMoreProjectOnScrollCount,
    getSearchConfigScrollBeforeBottomTrigger,

    getGlobalConfig,
    getStylesConfig,
    getSocialsConfig,

    getNavbarConfig,
    getFooterConfig,

    getEndpointConfig,
    getCurrentRouteConfig,
    getRouteConfigListForDataset,
    getRouteConfigMapForDataset,
    getRouteConfigStatForDataset,
    getRouteConfigDefaultDatasetImages,

    getEndpointConfigFilters,
    getEndpointConfigList,
    getEndpointConfigMap,
    getEndpointConfigDetail,
    getEndpointConfigStat,

    defaultText,

    getResults,
    getGeoResults,
    getProjectConfig,
    getProjectConfigUniform,
    getImgUrl,
    getImageUrl,

  };
