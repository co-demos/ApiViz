import LoginScreen from '../components/screens/LoginScreen.vue'
import LogoutScreen from '../components/screens/LogoutScreen.vue'
import RegisterScreen from '../components/screens/RegisterScreen.vue'

import axios from 'axios';
import { apiConfig } from '../config/api.js';


import { BRAND_DATA } from '../config/brand.js';

export const userRoutesGenerator = function(store){
  return [
      {
          name: 'login',
          path: '/app/login',
          component: LoginScreen,
          props(route){
              return {
                  ...BRAND_DATA
              }
          },
          beforeEnter(to, from, next){
              console.info('beforeEnter /login')
              next()
          }
      },
      {
          name: 'register',
          path: '/app/register',
          component: RegisterScreen,
          props(route){
              return {
                  ...BRAND_DATA
              }
          },
          beforeEnter(to, from, next){
              console.info('beforeEnter /register')
              next()
          }
      },
      {
          name: 'registerConfirmEmail',
          path: '/app/registerconfirmemail',
          props(e){
              return {
                  ...BRAND_DATA
              }
          },
          beforeEnter(to, from, next){
              let token = (to && to.query && to.query.token) ? to.query.token : ''
              console.info('beforeEnter /registerConfirmEmail -> token=',token);
              axios
                .get(apiConfig.toktokURL+'/usr/register/confirm_email?token='+token)
                .then(response =>
                {
                    // case where code is 200 => success
                    // this.$store.dispatch('saveLoginInfos',{APIresponse:response})
                    next({ name: 'login' })
                })
                .catch(e =>
                {
                    // in case we catch something, let's display it for easier debug
                    console.log('could not verify your email',e)
                    next({ name: 'error' })
                })
          }
      },
      {
          name: 'logout',
          path: '/app/logout',
          component: LogoutScreen,
          props(route){
              return {
                  ...BRAND_DATA
              }
          },
          beforeEnter(to, from, next){
              console.info('beforeEnter /logout')
              next()
          }
      }
      // {
      //     path: '/app/preferences/user_infos',
      //     component: LoginScreen,
      //     props(route){
      //         return {
      //             ...BRAND_DATA
      //         }
      //     },
      //     beforeEnter(to, from, next){
      //         console.info('beforeEnter /preferences/user_infos')
      //         next()
      //     }
      // },
      // {
      //     path: '/app/preferences/user_password',
      //     component: LoginScreen,
      //     props(route){
      //         return {
      //             ...BRAND_DATA
      //         }
      //     },
      //     beforeEnter(to, from, next){
      //         console.info('beforeEnter /preferences/user_password')
      //         next()
      //     }
      // }
  ]
}
