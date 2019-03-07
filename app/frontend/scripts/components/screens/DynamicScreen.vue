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
        // here we check what kind of dynamic route we have to provide
        this.$store.dispatch('getCurrentRouteConfig',{currentRoute:this.$router.currentRoute.path})
            .then( (response) => {
              this.routeConfig = response;
              if (!this.routeConfig) { this.$router.push({name:'error'}) }
            })
            .catch( (err) => {console.log('error in the DISPATCH of getCurrentRouteConfig()',err); })
    },
    methods: {
        goBack(e){
            e.preventDefault()
            this.$router.back()
        }
    }
}
</script>
