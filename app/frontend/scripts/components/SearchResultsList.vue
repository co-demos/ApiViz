<template>
    <section class="search-results-list">
        <div class="container" v-if="pending">
            <div class="pending">Recherche en cours...</div>
        </div>

        <div class="container" v-if="!pending">
            <CISSearchResultsCountAndTabs :view="VIEW_LIST"/>

            <div class="columns" v-if="total > 0" >
                <div class="column is-3" v-for="(projectColumn, i) in projectColumns" :key="i">
                    <div class="columns is-multiline">
                        <ProjectCard v-for="project in projectColumn" :key="project.id" :project="project"/>
                    </div>
                </div>
            </div>

            <div class="no-result error" v-if="total === 0">
                <img src="/static/illustrations/erreur_no_results.png">
                <div>
                    <h1 class="title is-1 is-primary">Aucun projet trouvé !</h1>
                    <p>Pour obtenir plus de résultats, modifier vos critères de recherche</p>
                    <button v-if="hasSelectedFilters" href="/" class="button is-primary is-outlined" @click="clearAllFilters">
                        Supprimer tous les filtres
                    </button>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import {mapState} from 'vuex'
import ProjectCard from './ProjectCard.vue'

import CISSearchResultsCountAndTabs from './CISSearchResultsCountAndTabs.vue'

import {VIEW_LIST} from '../constants.js'

let scrollListener;

export default {
    name: 'SearchResultsList',

    components: {
        ProjectCard,
        CISSearchResultsCountAndTabs
    },

    data(){
        return {
            VIEW_LIST,
            showCount: undefined
        }
    },

    watch: {
        projects(prev, next){
            this.showCount = this.$store.getters.getSearchConfigDefaultShowCount;
        }
    },

    computed: {
        projectColumns(){
            const {projects} = this.$store.state.search.answer.result;
            const getSearchConfigColumnCount = this.$store.getters.getSearchConfigColumnCount

            if(projects && getSearchConfigColumnCount){
                const columnsData = Array(getSearchConfigColumnCount).fill().map(() => []);

                projects.slice(0, this.showCount).forEach((p, i) => {
                    columnsData[i%getSearchConfigColumnCount].push(p);
                })

                return columnsData
            }
        },
        ...mapState({
            pending: ({search}) => !!search.answer.pendingAbort,
            projects: ({search}) => search.answer.result && search.answer.result.projects,
            total: ({search}) => search.answer.result && search.answer.result.total,
            hasSelectedFilters: ({search}) => {
                const selectedFilters = search.question && search.question.selectedFilters;
                if(!selectedFilters)
                    return false;

                return [...selectedFilters.values()].some(selectedFilterValues => selectedFilterValues.size >= 1)
            }
        })
    },

    methods: {
        clearAllFilters(){
            this.$store.dispatch( 'clearAllFilters' )
        }
    },

    mounted(){
          this.$store.dispatch('setSearchConfigDisplay');

          this.showCount = this.$store.getters.getSearchConfigDefaultShowCount

          scrollListener = () => {
              const getSearchConfigScrollBeforeBottomTrigger = this.$store.getters.getSearchConfigScrollBeforeBottomTrigger
              const getSearchConfigMoreProjectOnScrollCount = this.$store.getters.getSearchConfigMoreProjectOnScrollCount

              if (getSearchConfigMoreProjectOnScrollCount && getSearchConfigScrollBeforeBottomTrigger &&
                  window.innerHeight + window.scrollY >= (document.body.offsetHeight - getSearchConfigScrollBeforeBottomTrigger)
              ) {
                  if(this.$store.state.search.answer.result && this.showCount < this.$store.state.search.answer.result.projects.length){
                      this.showCount = this.showCount + getSearchConfigMoreProjectOnScrollCount
                  }
              }
          }

          window.addEventListener('scroll', scrollListener, {passive: true})
    },

    beforeDestroy(){
        window.removeEventListener('scroll', scrollListener)

        scrollListener = undefined;
    }

}
</script>

<style scoped>

/* TODO SASS : make a variable out of this background-value. Also used in CISSearchResultsCountAndTabs */
.search-results-list{
    background-color: #F6F6F6;
    width: 100%;

    padding-bottom: 0;
    padding-top: 1rem;
}


.pending{
    text-align: center;
    padding: 2em;
}
</style>
