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

    <!-- DEBUGGING -->
    <!-- <div> -->
      <!-- <br><br><br><br><br> -->
      <!-- navbarConfig : <br><code> {{ this.navbarConfig }} </code> <br><br>> -->
      <!-- globalConfig : <br><code> {{ this.globalConfig }} </code> <br><br> -->
      <!-- stylesConfig : <br><code> {{ this.stylesConfig }} </code> <br><br> -->
      <!-- routeConfig.field : <code>{{ this.routeConfig.field }} </code> <br><br> -->
      <!-- footerConfig : <br><code> {{ this.footerConfig }} </code> <br><br> -->
      <!-- search.endpoint_type : <br><code> {{ this.$store.state.search.endpoint_type }} </code> <br><br> -->
      <!-- search.endpoint : <br><code> {{ this.$store.state.search.endpoint }} </code> <br><br> -->
      <!-- getCurrentBanner : <br><code> {{ this.getCurrentBanner }} </code> <br><br> -->

      <!-- localRouteConfig.field :<br><code> {{ localRouteConfig.field }} </code> <br><br> -->
      <!-- localEndpointConfig :<br><code> {{ localEndpointConfig }} </code> <br><br> -->
      <!-- localFiltersConfig :<br><code> {{ localFiltersConfig }} </code> <br><br> -->
      <!-- <br><br> -->

    <!-- </div> -->


    <!-- BANNER -->
    <DynamicBanner 
      v-if="this.has_banner"
      :template_url="this.getCurrentBanner.template_url"
    ></DynamicBanner> 


    <!-- REMOTE STATICS -->
    <DynamicStatic 
      v-if="localRouteConfig.dynamic_template == 'DynamicStatic' "
      :routeConfig="localRouteConfig"
    ></DynamicStatic>



    <!-- DATA VISUALISATION -->
    <DynamicList 
      v-if="localRouteConfig.dynamic_template == 'DynamicList' "
      :routeConfig="localRouteConfig"
      :endPointConfig="localEndpointConfig"
      :filtersConfig="localFiltersConfig"
    ></DynamicList>

    <DynamicMap 
      v-if="localRouteConfig.dynamic_template == 'DynamicMap' "
      :routeConfig="localRouteConfig"
      :endPointConfig="localEndpointConfig"
      :filtersConfig="localFiltersConfig"
    ></DynamicMap>

    <DynamicDetail 
      v-if="localRouteConfig.dynamic_template == 'DynamicDetail' "
      :routeConfig="localRouteConfig"
      :endPointConfig="localEndpointConfig"
    ></DynamicDetail>



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

import DynamicBanner    from '../DynamicBanner.vue';
import DynamicStatic    from '../DynamicStatic.vue';
import DynamicList      from '../DynamicList.vue';
import DynamicMap       from '../DynamicMap.vue';
import DynamicDetail    from '../DynamicDetail.vue';

export default {
  components: {
    NavBar, 
    Footer, 
    DynamicBanner,
    DynamicStatic, 
    DynamicList, 
    DynamicMap, 
    DynamicDetail
  },

  props: [
  //   'logo', 
  //   'brand'
  ],

  data: () => {
    return   {
      localRouteConfig : undefined,
      localEndpointConfig : undefined,
      localFiltersConfig : undefined,
      currentDatasetURI : undefined
    }
  },

  // beforeCreate: function () {
  //   console.log("\n - - DynamicScreen / beforeCreate ... ")
  // },
  // created: function () {
  //   console.log("\n - - DynamicScreen / created ... ")
  // },
  
  beforeMount: function () {

    console.log("\n - - DynamicScreen / beforeMount ... ")
    // console.log(" - - state.config : \n ", this.$store.state.config)
    console.log(" - - DynamicScreen / this.routeConfig : \n ", this.routeConfig)
    
    // set local route and endpoint config
    this.localRouteConfig = this.routeConfig

    const currentTemplate = this.localRouteConfig.dynamic_templates 
    console.log(" - - DynamicScreen / currentTemplate : ", currentTemplate)
    console.log(" - - DynamicScreen / localRouteConfig.dynamic_templates  : ", this.localRouteConfig.dynamic_templates )

    if( this.routeConfig.dynamic_templates !== 'DynamicStatic' ) {

      // setting localDatasetURI
      this.currentDatasetURI = this.$store.state.search.dataset_uri
      console.log(" - - DynamicScreen / currentDatasetURI : ", this.currentDatasetURI)

      // setting localEndpointConfig
      console.log(" - - DynamicScreen / route IS for a dynamic content ... ")
      let path = this.$router.currentRoute.path
      console.log(" - - DynamicScreen / path : ", path )
      this.$store.dispatch('setSearchEndpointConfig', { path : path })
      // this.$store.dispatch('setSearchEndpoint')
      this.localEndpointConfig = this.$store.getters.getEndpointConfig
      console.log(" - - DynamicScreen / localEndpointConfig : ", this.localEndpointConfig )

      // setting filters
      console.log("\n - - DynamicScreen / setting filters ... ")
      this.localFiltersConfig = this.$store.getters.getEndpointConfigFilters
      console.log("\n - - DynamicScreen / this.localFiltersConfig : ", this.localFiltersConfig)
      // this.$store.commit('setDatasetFilters', this.localFiltersConfig )
      this.$store.dispatch('createDatasetFilters' )
      
      // setting MapSearch
      this.$store.commit('setIsMapSearch', this.routeConfig)

    }

  },

  mounted: function () {
    console.log("\n - - DynamicScreen / mounted ... ")
    // here we check what kind of dynamic route we have to provide
    if(!this.routeConfig) {
      this.$router.push({name:'error'})
    }
  },


  watch: {
    
    // watch the route path
    '$route.fullPath': function (newPath, oldPath) {
      console.log('\n- - DynamicScreen / watch / $route.fullPath : ', this.$route.fullPath);
      // console.log('- - DynamicScreen / newPath : ', newPath);
      // console.log('- - DynamicScreen / oldPath : ', oldPath);
      console.log('- - DynamicScreen / watch / $route : ', this.$route);
      console.log('- - DynamicScreen / watch / (before) state : ', this.$store.state);

      // find new route config corresponding to requested path
      this.$store.dispatch('setSearchEndpointConfig', { path : this.$route.path})
      // this.$store.dispatch('setSearchEndpoint')
      console.log('- - DynamicScreen / watch / (after) state : ', this.$store.state);
      this.localRouteConfig = this.$store.state.search.currentRouteConfig
      this.currentDatasetURI = this.$store.state.search.dataset_uri

      // check search for Map
      this.$store.commit('setIsMapSearch', this.localRouteConfig)

      if( this.routeConfig.dynamic_templates !== 'DynamicStatic' ) {
        console.log('- - DynamicScreen / watch / (after) setIsMapSearch : ', this.$store.state);
        this.localEndpointConfig = this.$store.getters.getEndpointConfig
        console.log('- - DynamicScreen / watch / (after) localEndpointConfig : ', this.localEndpointConfig);
        if (this.currentDatasetURI !== this.localEndpointConfig.dataset_uri ) {
          this.currentDatasetURI = this.currentDatasetURI
          this.localFiltersConfig = this.$store.getters.getEndpointConfigFilters
        }
      } else {
        this.localEndpointConfig = undefined
        this.localFiltersConfig = undefined
      }

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
    
    // GLOBAL CONFIG ELEMENTS
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

    // ROUTE AND ENDPOINT CONFIG ELEMENTS
    dynamic_template(){
      return (this.routeConfig) ? this.routeConfig.dynamic_template : undefined 
    },
    routeConfig(){
      let routeConf = this.$store.getters.getCurrentRouteConfig(this.$router.currentRoute.path)
      console.log(" - - DynamicScreen / routeConf : ", routeConf)
      return routeConf
    },
    // endPointConfig(){     
    //   let endPointConfig =  this.$store.getters.getEndpointConfig
    //   // console.log(" - - endPointConfig : ", endPointConfig)
    //   return endPointConfig
    // },

    // SWITCHERS
    has_navbar(){      
      return (this.routeConfig) ? this.routeConfig.has_navbar : undefined 
    },
    has_footer(){      
      return (this.routeConfig) ? this.routeConfig.has_footer : undefined 
    },
    has_banner(){      
      return (this.localRouteConfig) ? this.localRouteConfig.banner.activated : false 
    },

    // BANNER
    getCurrentBanner () {
      let bannersSet = this.stylesConfig.app_banners.banners_set
      console.log("- - DynamicScreen / bannersSet : ", bannersSet)

      console.log(" - - DynamicScreen / localRouteConfig : ", this.localRouteConfig )
      const routeBannerUri = this.localRouteConfig.banner.banner_uri
      console.log("- - DynamicScreen / routeBannerUri : ", routeBannerUri )

      let resultSet = bannersSet.find(function(b) {
        return b.banner_uri == routeBannerUri
      })
      console.log("- - DynamicScreen / resultSet : ", resultSet)
      return resultSet
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
