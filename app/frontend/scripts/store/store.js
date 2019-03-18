import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

import getters from './getters';
import actions from './actions';
import mutations from './mutations';

import {makeEmptySelectedFilters} from '../utilsApiviz';

Vue.use(Vuex)

// >>> LEGACY FILTERS
const INITIAL_FILTER_DESCRIPTIONS = CHOICES_FILTERS_TAGS.filter(c => c.name !== 'methods_')

// >>> LEGACY FILTERS / CREATION - LOW LEVEL FUNCTION
// function makeEmptySelectedFilters(filterDescriptions){
//   const selectedFilters = new Map()
//   for(const f of filterDescriptions){
//     selectedFilters.set(f.name, new Set())
//   }
//   return selectedFilters;
// }


// MAIN STORE
const storeGenerator = new Vuex.Store({
  strict: true,

  state: {
    
    // APP MODE : default | preprod | prod
    runMode : undefined,
    rootUrlBackend : undefined,

    // FOR TRANSLATIONS
    locale: 'fr',

    // USER-RELATED
    user: {
        infos: undefined,
        role: undefined,
        isLoggedin: false
    },
    jwt:undefined,

    // LEGACY
    geolocByProjectId: new Map(),
    spiders: undefined,
    
    // CURRENT 
    displayedProject: undefined,
    
    // FILTERS
    filterDescriptions: INITIAL_FILTER_DESCRIPTIONS,
    datasetFilters: undefined,

    // APIVIZ CONFIG
    config: {},

    // SEARCH PARAMETERS
    search: {

      // DATASET
      dataset_uri: undefined,
      endpoint_type: undefined,
      endpoint: undefined,

      // QUERY FROM USER
      question: {
        query: new URL(location).searchParams.get('text') || '',
        forMap : false,
        shuffleSeed : 1234,
        page:1,
        perPage:100,
        selectedDatasetFilters: undefined,
        selectedFilters: makeEmptySelectedFilters(INITIAL_FILTER_DESCRIPTIONS),
      },
      // RESULTS
      answer: {
        pendingAbort: undefined, // function that can be used to abort the current pending search
        result: undefined, // search results {projects, total}
        resultMap : undefined, // complete search results with minimal items as { _id, latlng } --> to be loaded just once for better experience + getters
        error: undefined // if last search ended in an error
      },
      // UI IN SEARCH PAGES CONFIG
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

    // STORE MODULES
    getters,
    mutations,
    actions
})

export default storeGenerator
