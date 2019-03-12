const getSearchConfigColumnCount = state => state.search.config.display.columnCount;
const getSearchConfigDefaultShowCount = state => state.search.config.display.defaultShowCount;
const getSearchConfigMoreProjectOnScrollCount = state => state.search.config.display.moreProjectOnScrollCount;
const getSearchConfigScrollBeforeBottomTrigger = state => state.search.config.display.scrollBeforeBottomTrigger;
const getCurrentRouteConfig = (state) => (currentRoute) => {
  try {
    return state.config.routes.find(function(r) {
        return r.urls.indexOf(currentRoute) !== -1;
    });
  } catch (e) { console.log('err',e); return undefined }
}
const getProjectConfig = (state) => (position) => {
  try {   return state.search.currentRouteConfig.contents_fields.find(function(f) {  return f.position === position; });
  }       catch (e) { console.log('err',e); return undefined }
}
const getProjectConfigUniform = (state, getters) => (project) => {
  let res = {}
  const infoTypes = ['id','title','image','address','tags']

  infoTypes.forEach( function(infoType){
    let fieldObj = getters.getProjectConfig('block_'+infoType)
    res[infoType] = (fieldObj && fieldObj.field) ? project[fieldObj.field] : undefined
  })

  res.image = getters.getImgUrl(res)

  return res
}
const getEndpointConfig = state => {
  if (!state.config
    || !state.config.endpoints
    || !state.search.endpoint_type
    || !state.search.dataset_uri) {
      console.log('some condition not respected');       return undefined;
  }
  return state.config.endpoints.find(function(r) {
    return r.endpoint_type === state.search.endpoint_type
    && r.dataset_uri === state.search.dataset_uri;
  });
}
const getImgUrl = (state, getters) => (obj) => {
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

export default {
  getSearchConfigColumnCount,
  getSearchConfigDefaultShowCount,
  getSearchConfigMoreProjectOnScrollCount,
  getSearchConfigScrollBeforeBottomTrigger,
  getEndpointConfig,
  getCurrentRouteConfig,
  getProjectConfig,
  getProjectConfigUniform,
  getImgUrl,
};
