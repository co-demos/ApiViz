import DynamicScreen from '../components/screens/DynamicScreen.vue'
import NotFoundScreen from '../components/screens/NotFoundScreen.vue'

import axios from 'axios';
import { BRAND_DATA } from '../config/brand.js';

export const dynamicRoutesGenerator = function(store){
  return [
      {
          name: 'dynamic',
          path: '/*',
          component: DynamicScreen,
          props(route){
              return {
                  ...BRAND_DATA
              }
          },
          beforeEnter(to, from, next){
            store.dispatch('setCurrentRouteAndEndpointConfig')
            .then(() =>
              store.dispatch('setSearchEndpointConfig',{path:to.path})
              .then(() =>
                  store.dispatch('setSearchEndpoint')
                .then(() => next())
                .catch(() => {console.log( 'err setSearchEndpoint'); next('error') })
              )
              .catch((err) => {console.log( 'err setSearchEndpointConfig',err); next('error')})
            )
            .catch(() => {console.log( 'err setCurrentRouteAndEndpointConfig'); next('error')})
          }
      },
      {
          path: '*',
          name: 'error',
          component: NotFoundScreen,
          props(route){
              return {
                  ...BRAND_DATA
              }
          },
      }
  ]
}
