<template>
    <div>

        <NavBar :logo="logo" :brand="brand" v-if="routeConfig.has_navbar"/>

          <component v-bind:is="routeConfig.dynamic_template" v-bind:routeConfig="routeConfig"></component>

        <Footer v-if="routeConfig.has_footer"/>

    </div>
</template>

<script>
import {mapState} from 'vuex'

import NavBar from '../NavBar.vue';
import Footer from '../Footer.vue';
import DynamicStatic from '../DynamicStatic.vue';

export default {
    components: {
      NavBar, Footer, DynamicStatic
    },
    data: () => {
      return{
        routeConfig: undefined
      }
    },
    props: [
        'logo', 'brand'
    ],
    computed: {
      ...mapState({
          user: 'user'
      })
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

        // here we check what kind of dynamic route we have to provide
        let path = this.$router.currentRoute.path

        if (this.$store && this.$store.state && this.$store.state.config && this.$store.state.config.routes) {
            this.routeConfig = getConf()
            if (!this.routeConfig) { this.$router.push({name:'error'}) }
        } else {
            this.$store.dispatch('getRouteConfig')
              .then( (response) => { this.routeConfig = getConf(response.data.app_config); if (!this.routeConfig) { this.$router.push({name:'error'}) } })
              .catch( (err) => {console.log('FAIL in the getConf() funciton ',err); } )
        }

        const getConf = function(routeConf){
          try {
            let routes = (routeConf) ? routeConf : this.$store.state.config.routes
            return routes.find(function(r) {
                return r.urls.indexOf(path) !== -1;
            });
          } catch (e) {
            console.log('error about the route: unkown route',e);
            return false
          }
        }
    },
    methods: {
        goBack(e){
            e.preventDefault()
            this.$router.back()
        }
    }
}
</script>
