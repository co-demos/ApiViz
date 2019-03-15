
// import { apiConfig } from '../config/api.js';

import DynamicScreen from '../components/screens/DynamicScreen.vue'
import NotFoundScreen from '../components/screens/NotFoundScreen.vue'

// import axios from 'axios';
// import { BRAND_DATA } from '../config/brand.js';

// FUNCTION TO GET THE RUN MODE FROM <HEAD>
function getConfigName(metaName) {
  const metas = document.getElementsByTagName('meta');
  for (let i = 0; i < metas.length; i++) {
    if (metas[i].getAttribute('name') === metaName) {
      return metas[i].getAttribute('content');
    }
  }
  return '';
}

export const dynamicRoutesGenerator = function(store){
  return [
    {
      name: 'dynamic',
      path: '/*',
      component: DynamicScreen,
      // props(route){
      //   return {
      //       ...BRAND_DATA
      //   }
      // },

      // beforeEach(to, from, next) {
      //   console.log("\n... dynamicRoutesGenerator / beforeEach ... ")
      //   console.log("... dynamicRoutesGenerator / to : ", to)
      // },

      beforeEnter(to, from, next){

        console.log("\n... dynamicRoutesGenerator / beforeEnter ... ")
        
        // SET RUN MODE AND rootUrlBackend FOR SEARCHES
        if ( typeof store.state.runMode === 'undefined' || typeof store.state.rootUrlBackend === 'undefined' ) {
          console.log("... dynamicRoutesGenerator / configName not defined")
          const configName = getConfigName('config_name')
          console.log("... dynamicRoutesGenerator / configName : ", configName)
          store.commit('setRunMode', configName)
        }
        console.log("... dynamicRoutesGenerator / store.state.runMode : ", store.state.runMode)
        console.log("... dynamicRoutesGenerator / store.state.rootUrlBackend : ", store.state.rootUrlBackend)


        console.log("... dynamicRoutesGenerator / store.state :  \n ", store.state)
        console.log("... dynamicRoutesGenerator / store.state.config :  \n ", store.state.config)


        // CHECK IF config.global is undefined yet
        if ( typeof store.state.config.global === 'undefined' ) {
          console.log("... dynamicRoutesGenerator / store.state.config.global is undefined ...")
          store.dispatch('getConfigAll')
          .then(() => {
            console.log("... dynamicRoutesGenerator / after getConfigAll ... ");
            next()
          })
          .catch(() => {console.log( 'error...'); next('error')})
        } else { 
          next() 
        }
      }
      
    },

    {
      path: '*',
      name: 'error',
      component: NotFoundScreen,
      // props(route){
      //   return {
      //       ...BRAND_DATA
      //   }
      // },
    }
  ]
}
