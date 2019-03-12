<template>
    <div>

        <NavBar :logo="logo" :brand="brand" v-if="this.has_navbar"/>

          <component v-bind:is="this.dynamic_template" v-bind:routeConfig="this.routeConfig"></component>

        <Footer v-if="this.has_footer"/>

    </div>
</template>

<script>
import {mapState} from 'vuex'

import NavBar from '../NavBar.vue';
import Footer from '../Footer.vue';
import DynamicStatic from '../DynamicStatic.vue';
import DynamicList from '../DynamicList.vue';
import DynamicMap from '../DynamicMap.vue';
import DynamicDetail from '../DynamicDetail.vue';

export default {
    components: {
      NavBar, Footer, DynamicStatic, DynamicList, DynamicMap, DynamicDetail
    },
    props: [
        'logo', 'brand'
    ],
    computed: {
      ...mapState({
          user: 'user'
      }),
      routeConfig(){     return this.$store.getters.getCurrentRouteConfig(this.$router.currentRoute.path)      },
      has_navbar(){      return (this.routeConfig) ? this.routeConfig.has_navbar : undefined },
      has_footer(){      return (this.routeConfig) ? this.routeConfig.has_footer : undefined },
      dynamic_template(){return (this.routeConfig) ? this.routeConfig.dynamic_template : undefined },
    },
    mounted(){
        // here we check what kind of dynamic route we have to provide
        if(!this.routeConfig) {           this.$router.push({name:'error'})        }
    },
    methods: {
        goBack(e){
            e.preventDefault()
            this.$router.back()
        }
    }
}
</script>
