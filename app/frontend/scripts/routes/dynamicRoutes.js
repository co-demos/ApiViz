import DynamicScreen from '../components/screens/DynamicScreen.vue'
import NotFoundScreen from '../components/screens/NotFoundScreen.vue'

// import axios from 'axios';
// import { BRAND_DATA } from '../config/brand.js';

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
        console.log("... store.state.config :  \n ", store.state.config)

        if ( typeof store.state.config.global === 'undefined' ) {
          
          store.dispatch('getConfigAll')
          .then(() => {
              console.log("... dynamicRoutesGenerator / after getConfigAll ... "),
              next()
          })
          .catch(() => {console.log( 'error...'); next('error')})
        
        } else { next() }
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
