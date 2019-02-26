import Vue from 'vue';
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const SOURCE_FILTER_NAME = 'source_';

function makeSourceFilterFromSpiders(spiders){
    return {
        "fullname": "Source",
        "name": SOURCE_FILTER_NAME,
        "choices": [ ...Object.entries(spiders)]
            .map(([id, {name}]) => ({
                "fullname": name,
                "id": id,
                "spiderId": id,
                "name": name
            }))
            .sort((a, b) => a.name.localeCompare(b.name))
    }
}


function filterValuesToCISTags(filterValues){
    const cisTags = new Set();

    const categoriesByUITag = CATEGORIES_CIS_DICT_FLAT;
    const cisTagByCategory = NORMALIZATION_TAGS_SOURCES_CIS_DICT;

    let uiTags = [];
    for(const [filter, tags] of filterValues.entries()){
        uiTags = [...uiTags, ...([...tags].map(t => filter+t))]
    }

    for(const uiTag of uiTags){
        const categories = categoriesByUITag[uiTag];

        for(const category of categories){
            const categoriesCISTags = cisTagByCategory[category];

            for(const tag of categoriesCISTags){
                cisTags.add(tag);
            }
        }
    }

    return cisTags;
}

const INITIAL_FILTER_DESCRIPTIONS = CHOICES_FILTERS_TAGS.filter(c => c.name !== 'methods_')


function makeEmptySelectedFilters(filterDescriptions){
    const selectedFilters = new Map()
    for(const f of filterDescriptions){
        selectedFilters.set(f.name, new Set())
    }
    return selectedFilters;
}


import { storeGenerator } from './store.js';
const store = storeGenerator

import { searchRoutesGenerator } from './routes/searchRoutes.js';
import { userRoutesGenerator } from './routes/userRoutes.js';
const routes = [...searchRoutesGenerator(store),...userRoutesGenerator(store)]

const router = new VueRouter({
    mode: 'history',
    routes,
    scrollBehavior (to, from, savedPosition) {
        return savedPosition ? savedPosition : { x: 0, y: 0 };
    }
})

document.addEventListener('DOMContentLoaded', () => {

    new Vue({
        el: document.querySelector('#vue-content'),
        router,
        store,
        mounted: function () {
          store.dispatch('getConfig');
        },
        render: h => h( Vue.component('router-view') )
    })

}, {once: true})
