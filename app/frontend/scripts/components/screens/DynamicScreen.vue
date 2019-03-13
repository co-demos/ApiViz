<template>
    <div>

        <!-- NAVBAR -->
        <NavBar 
          v-if="this.has_navbar"
          :navbarConfig="this.navbarConfig" 

          :logo="this.globalConfig.app_logo"
          :brand="this.globalConfig.app_title.content"
          :appLocales="this.globalConfig.app_languages" 

          :currentRouteConfig="this.routeConfig"
          :localRouteConfig="localRouteConfig.field"
        ></NavBar>
            <!-- :logo="logo" 
            :brand="brand"  -->


        <!-- DYNAMIC COMPONENT -->

        <!-- <component 
          :is="this.dynamic_template" 
          :routeConfig="this.localRouteConfig"
        ></component> -->

        <!-- REMOTE STATICS -->
        <DynamicStatic 
          v-if="localRouteConfig.dynamic_template == 'DynamicStatic' "
          :routeConfig="localRouteConfig"
        ></DynamicStatic>

        <!-- DATA VISUALISATION -->
        <DynamicList 
          v-if="localRouteConfig.dynamic_template == 'DynamicList' "
          :routeConfig="localRouteConfig"
        ></DynamicList>

        <DynamicMap 
          v-if="localRouteConfig.dynamic_template == 'DynamicMap' "
          :routeConfig="localRouteConfig"
        ></DynamicMap>

        <DynamicDetail 
          v-if="localRouteConfig.dynamic_template == 'DynamicDetail' "
          :routeConfig="localRouteConfig"
        ></DynamicDetail>



        <!-- DEBUGGING -->
        <!-- <div> -->
          <!-- <br><br> -->
          <!-- navbarConfig : <br><code> {{ this.navbarConfig }} </code> <br><br>> -->
          globalConfig : <br><code> {{ this.globalConfig }} </code> <br><br>
          <!-- localRouteConfig.field : <code> {{ localRouteConfig.field }} </code> <br><br> -->
          <!-- routeConfig.field : <code>{{ this.routeConfig.field }} </code> <br><br> -->
          <!-- footerConfig : <br><code> {{ this.footerConfig }} </code> <br><br> -->
        <!-- </div> -->


        <!-- FOOTER -->
        <Footer 
          v-if="this.has_footer"
          :footerConfig="this.footerConfig" 
          :appSocials="this.socialsConfig" 
        ></Footer>

    </div>
</template>

<script>
import {mapState} from 'vuex'

import NavBar from '../NavBar.vue';
import Footer from '../Footer.vue';

import DynamicStatic    from '../DynamicStatic.vue';
import DynamicList      from '../DynamicList.vue';
import DynamicMap       from '../DynamicMap.vue';
import DynamicDetail    from '../DynamicDetail.vue';

export default {
    components: {
      NavBar, Footer, DynamicStatic, DynamicList, DynamicMap, DynamicDetail
    },

    // props: [
    //   'logo', 
    //   'brand'
    // ],

    beforeCreate: function () {
      console.log("\n - - DynamicScreen / beforeCreate ... ")
    },
    created: function () {
      console.log("\n - - DynamicScreen / created ... ")
    },
    beforeMount: function () {
      console.log("\n - - DynamicScreen / beforeMount ... ")
      // console.log(" - - state.config : \n ", this.$store.state.config)
      console.log(" - - DynamicScreen / this.routeConfig : \n ", this.routeConfig)
      
      // set local data
      this.localRouteConfig = this.routeConfig

      if( this.routeConfig.dynamic_templates !== 'DynamicStatic' ) {
        console.log(" - - DynamicScreen / not DynamicStatic ... ")
        let path = this.$router.currentRoute.path
        console.log(" - - DynamicScreen / path : ", path )
        this.$store.dispatch('setSearchEndpointConfig', { path : path })
        // this.$store.dispatch('setSearchEndpoint')
      }

    },

    mounted: function () {
      console.log("\n - - DynamicScreen / mounted ... ")
      // here we check what kind of dynamic route we have to provide
      if(!this.routeConfig) {           
        this.$router.push({name:'error'})        
      }
    },

    data: () => {
      return   {
        localRouteConfig : "...",
      }
    },

    watch: {
      
      // watch the route path
      '$route.fullPath': function (newPath, oldPath) {
        console.log('\n- - DynamicScreen / watch $route.fullPath : ', this.$route.fullPath);
        // console.log('- - DynamicScreen / newPath : ', newPath);
        // console.log('- - DynamicScreen / oldPath : ', oldPath);
        console.log('- - DynamicScreen / watch $route : ', this.$route);
        console.log('- - DynamicScreen / (before) state : ', this.$store.state);

        // find new route config corresponding to requested path
        this.$store.dispatch('setSearchEndpointConfig', { path : this.$route.path})
        // this.$store.dispatch('setSearchEndpoint')
        console.log('- - DynamicScreen / (after) state : ', this.$store.state);
        this.localRouteConfig = this.$store.state.search.currentRouteConfig

      },

      // watch the localRouteConfig
      localRouteConf: function (newConf, oldConf) {
        console.log('\n- - DynamicScreen / watch localRouteConf...');
        console.log('- - DynamicScreen / newConf : ', newConf);
        console.log('- - DynamicScreen / oldConf : ', oldConf);

      }
    },



    computed: {
      ...mapState({
          user: 'user'
      }),

      globalConfig(){
        let globalConfig = this.$store.getters.getGlobalConfig
        // console.log(" - - globalConfig : ", globalConfig)
        return globalConfig
      },
      stylesConfig(){
        return this.$store.getters.getStylesConfig
      },
      socialsConfig(){
        let socialsConf = this.$store.getters.getSocialsConfig
        // console.log(" - - socialsConf : ", socialsConf)
        return socialsConf
      },
      navbarConfig(){    
        let navbarConf = this.$store.getters.getNavbarConfig
        // console.log(" - - navbarConf : ", navbarConf)
        return navbarConf
      },
      footerConfig(){    
        return this.$store.getters.getFooterConfig
      },

      routeConfig(){     
        let routeConf =  this.$store.getters.getCurrentRouteConfig(this.$router.currentRoute.path)
        // console.log(" - - routeConf : ", routeConf)
        return routeConf
      },

      has_navbar(){      
        return (this.routeConfig) ? this.routeConfig.has_navbar : undefined 
      },
      has_footer(){      
        return (this.routeConfig) ? this.routeConfig.has_footer : undefined 
      },
      
      dynamic_template(){
        return (this.routeConfig) ? this.routeConfig.dynamic_template : undefined 
      },
    
    },



    methods: {
      goBack(e){
        e.preventDefault()
        this.$router.back()
      }
    }
}
</script>
