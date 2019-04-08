import LoginScreen from '../components/screens/LoginScreen.vue'
import LogoutScreen from '../components/screens/LogoutScreen.vue'
import RegisterScreen from '../components/screens/RegisterScreen.vue'

import axios from 'axios';
import { apiConfig } from '../config/api.js';
import { getConfigName } from '../utils.js';

// import { BRAND_DATA } from '../config/brand.js';

export const userRoutesGenerator = function(store){
  return [
    {
      name: 'login',
      path: '/login',
      component: LoginScreen,
      beforeEnter(to, from, next){
        // SET RUN MODE AND rootUrlBackend FOR SEARCHES
        if ( typeof store.state.runMode === 'undefined' || typeof store.state.rootUrlBackend === 'undefined' ) {
          const configName = getConfigName('config_name')
          store.commit('setRunMode', configName)
        }
        console.info('beforeEnter /login')
        next()
      }
    },
    {
      name: 'register',
      path: '/register',
      component: RegisterScreen,
      beforeEnter(to, from, next){
        console.info('beforeEnter /register')
        next()
      }
    },
    {
      name: 'registerConfirmEmail',
      path: '/registerconfirmemail',
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
      path: '/logout',
      component: LogoutScreen,
      beforeEnter(to, from, next){
          console.info('beforeEnter /logout')
          next()
      }
    }
  ]
}
