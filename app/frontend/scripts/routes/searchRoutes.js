import SearchListScreen from '../components/screens/SearchListScreen.vue';
import SearchMapScreen from '../components/screens/SearchMapScreen.vue'
import CISProjectScreen from '../components/screens/CISProjectScreen.vue'
import NotFoundScreen from '../components/screens/NotFoundScreen.vue'

import {getProjectById, getSpiders} from '../cisProjectSearchAPI.js';

import { BRAND_DATA } from '../config/brand.js';

// const BRAND_DATA = Object.freeze({
//     logo: '/static/logos/CIS/CIS_logo.png',
//     brand: 'Carrefour des Innovations Sociales',
// })

export const searchRoutesGenerator = function(store){
  return [
      {
          path: '/app/recherche',
          component: SearchListScreen,
          props(route){
              return {
                  ...BRAND_DATA
              }
          },
          beforeEnter(to, from, next){
              console.info('beforeEnter /recherche')

              // get spiders data if they're not already here
              if(!store.state.spiders){
                  store.dispatch('getSpiders');
              }

              next()
          }
      },
      {
          path: '/app/recherche/carte',
          component: SearchMapScreen,
          props(route){
              return {
                  ...BRAND_DATA
              }
          },
          beforeEnter(to, from, next){
              console.info('beforeEnter /recherche/carte')

              // get spiders data if they're not already here
              if(!store.state.spiders){
                  store.dispatch('getSpiders');
              }

              next()
          }
      },
      {
          path: '/app/project/:id',
          component: CISProjectScreen,
          props(route){
              return {
                  ...BRAND_DATA
              }
          },
          beforeEnter(to, from, next){
              const {id} = to.params;
              console.info('beforeEnter /project/:id', id)

              const result = store.state.search.answer.result

              const project = result && result.projects.find(p => p.id === id)

              // get project data
              if(!project){
                  getProjectById(id)
                  .then(project => {
                      store.commit('setDisplayedProject', {project})
                  })
                  .catch(err => console.error('project route error', err))
              }

              store.commit('setDisplayedProject', {project: project || {}})

              // get spiders data if they're not already here
              if(!store.state.spiders){
                  store.dispatch('getSpiders');
              }

              next()
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
