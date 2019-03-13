import Vue from 'vue';
import VueRouter from 'vue-router'
import VeeValidate from 'vee-validate'
import { sync } from 'vuex-router-sync'

Vue.use(VeeValidate);
Vue.use(VueRouter)

const SOURCE_FILTER_NAME = 'source_';
const INITIAL_FILTER_DESCRIPTIONS = CHOICES_FILTERS_TAGS.filter(c => c.name !== 'methods_')


import store from './store/store.js';
import routerGenerator from './routes/main.js'

const router = routerGenerator(store)

const unsync = sync(store, router)
// unsync() to Unsyncs store from router


document.addEventListener('DOMContentLoaded', () => {

    new Vue({
        el: document.querySelector('#vue-content'),
        router,
        store,
        // mounted: function () {
        //   console.log("document.addEventListener / beforeCreate ... ")
        //   store.dispatch('getConfigAll');
        // },
        render: h => h( Vue.component('router-view') )
    })

}, {once: true})
