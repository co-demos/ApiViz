import Vue from 'vue';
import VueRouter from 'vue-router'
import VeeValidate from 'vee-validate'
import { sync } from 'vuex-router-sync'

Vue.use(VeeValidate);
Vue.use(VueRouter)

import store from './store/store.js';
import routerGenerator from './routes/main.js'
// import { getConfigName } from './utils.js';

// because of this call 'beforeEnter' in dynamicRoutesGenerator is triggered first
const router = routerGenerator(store)

const unsync = sync(store, router)
// unsync() to Unsyncs store from router


document.addEventListener('DOMContentLoaded', () => {

  new Vue({
    el: document.querySelector('#vue-content'),
    router,
    store,
    render: h => h( Vue.component('router-view') )
  })

}, {once: true})
