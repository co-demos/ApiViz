<template>
    <div>


        <main v-if="projectFormatted">
            <div class="container">

                <a class="back" @click="goBack">
                    <img src="/static/icons/icon_arrow1.svg">
                    <span>
                        Retour aux résultats de recherche
                    </span>
                </a>

                <div class="columns">

                    <div class="column is-5 is-offset-1">
                        <div class="description">
                            <h1 class="title is-3">{{projectFormatted.title}}</h1>
                            <p v-if="projectFormatted.address">
                                <span class="icon">
                                    <img class="image is-16x16" src="/static/icons/icon_pin.svg">
                                </span>
                                {{projectFormatted.address}}
                            </p>
                            <p>{{projectFormatted.description}}</p>

                            <div v-if="projectFormatted.projectPartners">
                                <h2 class="title is-4">Structure</h2>
                                <p>{{projectFormatted.projectPartners}}</p>
                            </div>

                            <a v-if="projectFormatted.website" :href="projectFormatted.website" target="_blank">Voir le site du projet</a>
                        </div>
                    </div>

                    <div class="column is-5">
                        <div class="added" v-if="spider">
                            <div class="columns">
                                <div class="column is-8">
                                    <div>
                                        Projet ajouté par
                                        <a :href="spider.page_url" target="_blank">
                                            {{spider.name}}
                                        </a>
                                    </div>
                                    <div v-if="projectFormatted.pageAtSourcer">
                                        <a :href="projectFormatted.pageAtSourcer" class="link-at-sourcer" target="_blank">
                                            <img src="/static/icons/icon_link.svg">
                                            Voir ce projet sur le site
                                        </a>
                                    </div>
                                </div>
                                <div class="column is-4 no-left-padding is-vertical-centered">
                                    <a :href="projectFormatted.pageAtSourcer" target="_blank">
                                        <img class="logo" v-if="spider.logo_url" :src="spider.logo_url">
                                    </a>
                                </div>
                            </div>
                        </div>

                        <a :href="projectFormatted.pageAtSourcer" target="_blank">
                            <img class="illustration" :src="projectFormatted.image"/>
                        </a>
                        <div v-if="Array.isArray(projectFormatted.tags) && projectFormatted.tags.length >= 1" class="content">
                            <h2 class="title is-5">Catégories</h2>
                            <span v-for="tag in projectFormatted.tags" class="tag" :key="tag">
                                {{tag}}
                            </span>
                        </div>
                    </div>

                </div>
            </div>
        </main>

        <NotFoundError v-if="!projectFormatted"/>

    </div>
</template>


<script>
export default {
    computed: {
      ...mapState({
          user: 'user'
      })
    },
}
</script>


<script>
import {mapState} from 'vuex'

import NotFoundError from './NotFoundError.vue';

import {getProjectById} from '../utils.js';

export default {
    name: 'DynamicDetail',
    components: {
      NotFoundError,
    },
    props: [
        'routeConfig','logo', 'brand'
    ],

    computed: {
      ...mapState({
        project: 'displayedProject',
        spider({spiders}){ return spiders && this.project && spiders[this.project.spiderId] }
      }),
      ...mapState({
          user: 'user'
      }),
      projectFormatted(){
        if (!this.project) {
          return {
            tags: [],
            image: '',
            logo_url: '',
            title: '',
            address: '',
            description: '',
            projectPartners: '',
            website: '',
            pageAtSourcer: ''
          }
        } else {
          return this.$store.getters.getProjectConfigUniform(this.project)
        }
      },
    },

    mounted(){
        // hack to scroll top because vue-router scrollBehavior thing doesn't seem to work on Firefox on Linux at least
        const int = setInterval(() => {
            if(window.pageYOffset < 50){
                clearInterval(int)
            }
            else{
                window.scrollTo(0, 0)
            }
        }, 100);

        getProjectById(this.$route.query.id,this.$store.state.search.endpoint.root_url)
        .then(project => {
            this.$store.commit('setDisplayedProject', {project})
        })
        .catch(err => console.error('project route error', err))
    },

    methods: {
        goBack(e){
            e.preventDefault()
            this.$router.back()
        }
    }

}
</script>


<style lang="scss" scoped>
@import '../../../styles/apiviz-colors.scss';
@import '../../../styles/apiviz-misc.scss';

main{
    background-color: $apiviz-grey-background;
    margin-top: $apiviz-navbar-height;
}

a.back{
    padding: 1em 0;
    display: block;

    color: $apiviz-text-color;

    img{
        height: 1.5em;
        transform: translateY(0.4em);
    }

    span{
        margin-left: 1em;
    }
}

.columns{
    margin-top: 0;
}

.illustration{
    width: 100%;
    margin-bottom: 1em;
}

.description, .added{
    background-color: white;
    padding: 1em;
    margin-bottom: 1em;
}

.description{
    h1{
        font-weight: bold;
    }

    p{
        margin-bottom: 1em;
    }

    a{
        color: $apiviz-primary;
        border-bottom: 1px solid $apiviz-primary;
    }
}


.added {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: left;

    .link-at-sourcer img{
        max-height: 1.1em;
        transform: translateY(0.2em);
    }

    img{
        height:auto;
    }

    .no-left-padding {
        padding-left: 0em;
    }
    .is-vertical-centered {
        // padding-left: 1em;
        display: flex;
        align-items: center;
    }

    .logo {
        // max-width: 175px;
        height: auto;
        width:100%;
    }

    a{
        color: $apiviz-primary;
        font-weight: bold;
    }
}

.content{
    h2{
        font-weight: bold;
    }

    .tag{
        background-color: #767676;
        color: white;
        margin-right: 1em;
        margin-bottom: 0.5em;
    }
}
</style>
