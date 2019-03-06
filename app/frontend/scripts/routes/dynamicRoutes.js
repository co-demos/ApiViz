import DynamicScreen from '../components/screens/DynamicScreen.vue'
import axios from 'axios';
import { BRAND_DATA } from '../config/brand.js';

export const dynamicRoutesGenerator = function(store){
  return [
      {
          name: 'dynamic',
          path: '/app/:routeName',
          component: DynamicScreen,
          props(route){
              return {
                  ...BRAND_DATA
              }
          },
          beforeEnter(to, from, next){
              console.info('beforeEnter /dynamic')
              next()
          }
      }
  ]
}
