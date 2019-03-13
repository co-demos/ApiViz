import Vue from 'vue';
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import { userRoutesGenerator } from './userRoutes.js';
import { dynamicRoutesGenerator } from './dynamicRoutes.js';


const routerGenerator = function(store){

  const routes = [
    ...userRoutesGenerator(store),
    ...dynamicRoutesGenerator(store)
  ]

  return new VueRouter({
      mode: 'history',
      routes,
      props:true,
      scrollBehavior (to, from, savedPosition) {
          return savedPosition ? savedPosition : { x: 0, y: 0 };
      }
  })
}

export default routerGenerator
