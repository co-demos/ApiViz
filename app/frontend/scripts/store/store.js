import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

import getters from './getters';
import actions from './actions';
import mutations from './mutations';

Vue.use(Vuex)

const INITIAL_FILTER_DESCRIPTIONS = CHOICES_FILTERS_TAGS.filter(c => c.name !== 'methods_')


function makeEmptySelectedFilters(filterDescriptions){
  const selectedFilters = new Map()
  for(const f of filterDescriptions){
    selectedFilters.set(f.name, new Set())
  }
  return selectedFilters;
}


const storeGenerator = new Vuex.Store({
  strict: true,

  state: {
      
    locale: 'fr',

    user: {
        infos: undefined,
        role: undefined,
        isLoggedin: false
    },
    jwt:undefined,

    geolocByProjectId: new Map(),
    spiders: undefined,
    
    displayedProject: undefined,
    
    filterDescriptions: INITIAL_FILTER_DESCRIPTIONS,
    
    // the current route to watch
    // currentRouteConfig : undefined,

    // global config for ApiViz instance 
    config: {},

    // search parameters
    search: {
        dataset_uri: undefined,
        endpoint_type: undefined,
        endpoint: undefined,
        question: {
            query: new URL(location).searchParams.get('text') || '',
            selectedFilters: makeEmptySelectedFilters(INITIAL_FILTER_DESCRIPTIONS)
        },
        answer: {
            pendingAbort: undefined, // function that can be used to abort the current pending search
            result: undefined, // search results {projects, total}
            error: undefined // if last search ended in an error
        },
        config:{
          display: {
            columnCount : undefined,
            defaultShowCount : undefined,
            moreProjectOnScrollCount : undefined,
            scrollBeforeBottomTrigger : undefined
          }
        }
      }

    },
    getters,
    mutations,
    actions
})

export default storeGenerator
