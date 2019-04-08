<template>
  <div>

    <!-- NAVBAR -->
    <NavBar 
      v-if="this.has_navbar"
      :navbarConfig="this.navbarConfig" 
      :logo="this.globalConfig.app_logo"
      :brand="this.globalConfig.app_title.content"
      :appLocales="this.globalConfig.app_languages" 
      :currentDatasetURI="currentDatasetURI"
      :localRouteConfig="localRouteConfig"
    ></NavBar>
      <!-- :currentRouteConfig="this.routeConfig"
      :localRouteConfig="localRouteConfig.field" -->
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
      <!-- routeConfig : <code>{{ this.routeConfig }} </code> <br><br> -->
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
      :dynamicTemplate="localRouteConfig.dynamic_template"
    ></DynamicBanner> 


    <!-- REMOTE STATICS -->
    <DynamicStatic 
      v-if="localRouteConfig.dynamic_template == 'DynamicStatic' "
      :routeConfig="localRouteConfig"
    ></DynamicStatic>

    <!-- LOCAL TEST STATIC -->
    <DynamicStaticTest 
      v-if="localRouteConfig.dynamic_template == 'DynamicStaticTest' "
    ></DynamicStaticTest>


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



    <!-- LOGIN/LOGOUT/REGISTER ROUTES -->
    <LoginScreen 
      v-if="localRouteConfig.dynamic_template == 'Login' "
      :routeConfig="localRouteConfig"
      :endPointConfig="localEndpointConfig"
    ></LoginScreen>

    <LogoutScreen 
      v-if="localRouteConfig.dynamic_template == 'Logout' "
      :routeConfig="localRouteConfig"
      :endPointConfig="localEndpointConfig"
    ></LogoutScreen>

    <RegisterScreen 
      v-if="localRouteConfig.dynamic_template == 'Register' "
      :routeConfig="localRouteConfig"
      :endPointConfig="localEndpointConfig"
    ></RegisterScreen>




    <!-- FOOTERS -->
    <Footer 
      v-if="this.has_footer"
      :footerConfig="this.footerConfig" 
      :appSocials="this.socialsConfig" 
    ></Footer>

    <!-- PROJECT's PARTNERS FOOTER -->
    <DynamicStaticRaw 
      v-if="this.has_credits_footer"
      :templateURL="this.footerConfig.credits_footer_url"
    ></DynamicStaticRaw>

    <!-- CREDITS CODEMOS / REMOTE FOOTER -->
    <DynamicStaticRaw 
      :templateURL="'https://raw.githubusercontent.com/co-demos/structure/master/pages-html/codemos-footer.html'"
    ></DynamicStaticRaw>

  </div>
</template>

<script>
import {mapState} from 'vuex'

import NavBar from '../NavBar.vue';
import Footer from '../Footer.vue';

import DynamicBanner     from '../DynamicBanner.vue';
import DynamicStatic     from '../DynamicStatic.vue';
import DynamicStaticRaw  from '../DynamicStaticRaw.vue';
import DynamicStaticTest from '../DynamicStaticTest.vue';
import DynamicList       from '../DynamicList.vue';
import DynamicMap        from '../DynamicMap.vue';
import DynamicDetail     from '../DynamicDetail.vue';

import LoginScreen       from './LoginScreen.vue';
import LogoutScreen      from './LogoutScreen.vue';
import RegisterScreen    from './RegisterScreen.vue';

export default {
  components: {
    NavBar, 
    Footer, 
    DynamicBanner,
    DynamicStatic, 
    DynamicStaticRaw,
    DynamicStaticTest,
    DynamicList, 
    DynamicMap, 
    DynamicDetail,

    LoginScreen,
    LogoutScreen,
    RegisterScreen
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

    // console.log("\n - - DynamicScreen / beforeMount ... ")
    // console.log(" - - state.config : \n ", this.$store.state.config)
    // console.log(" - - DynamicScreen / this.routeConfig : \n ", this.routeConfig)
    
    // set local route and endpoint config
    this.localRouteConfig = this.routeConfig

    const currentTemplate = this.localRouteConfig.dynamic_template 
    // console.log(" - - DynamicScreen / currentTemplate : ", currentTemplate)
    // console.log(" - - DynamicScreen / localRouteConfig.dynamic_templates  : ", this.localRouteConfig.dynamic_templates )

    if( this.routeConfig.dynamic_template !== 'DynamicStatic' ) {

      // setting localEndpointConfig
      // console.log(" - - DynamicScreen / route IS for a dynamic content ... ")
      let path = this.$router.currentRoute.path
      // console.log(" - - DynamicScreen / path : ", path )
      this.$store.dispatch('setSearchEndpointConfig', { path : path })
      // this.$store.dispatch('setSearchEndpoint')
      this.localEndpointConfig = this.$store.getters.getEndpointConfig
      // console.log(" - - DynamicScreen / localEndpointConfig : ", this.localEndpointConfig )

      // setting localDatasetURI
      // this.currentDatasetURI = this.$store.state.search.dataset_uri
      this.currentDatasetURI = this.localEndpointConfig.dataset_uri
      // console.log(" - - DynamicScreen / currentDatasetURI : ", this.currentDatasetURI)
      
      // setting filters
      // console.log("\n - - DynamicScreen / setting filters ... ")
      this.localFiltersConfig = this.$store.getters.getEndpointConfigFilters
      // console.log(" - - DynamicScreen / this.localFiltersConfig : ", this.localFiltersConfig)
      // this.$store.commit('setDatasetFilters', this.localFiltersConfig )
      this.$store.dispatch('createDatasetFilters')
      
      // setting MapSearch
      this.$store.commit('setIsMapSearch', this.routeConfig)

    }

  },

  mounted: function () {
    // console.log("\n - - DynamicScreen / mounted ... ")
    // here we check what kind of dynamic route we have to provide
    if(!this.routeConfig) {
      this.$router.push({name:'error'})
    }
  },


  watch: {
    
    // watch the route path
    '$route.fullPath': function (newPath, oldPath) {
      // console.log('\n- - DynamicScreen / watch / $route.fullPath : ', this.$route.fullPath);
      // console.log('- - DynamicScreen / newPath : ', newPath);
      // console.log('- - DynamicScreen / oldPath : ', oldPath);
      // console.log('- - DynamicScreen / watch / $route : ', this.$route);
      // console.log('- - DynamicScreen / watch / (before) state : ', this.$store.state);

      // find new route config corresponding to requested path
      this.$store.dispatch('setSearchEndpointConfig', { path : this.$route.path})
      // this.$store.dispatch('setSearchEndpoint')
      // console.log('- - DynamicScreen / watch / (after) state : ', this.$store.state);

      // this.localRouteConfig = this.$store.state.search.currentRouteConfig
      this.localRouteConfig = this.$store.getters.getCurrentRouteConfig( this.$route.path )
      // console.log('- - DynamicScreen / watch / localRouteConfig : ', this.localRouteConfig);

      // let previousDatasetURI = this.$store.getters.getSearchDatasetURI
      // console.log('- - DynamicScreen / watch / previousDatasetURI : ', previousDatasetURI);
      // let currentDatasetURI = this.$store.getters.getSearchDatasetURI
      let currentDatasetURI = this.localRouteConfig.dataset_uri
      // console.log('- - DynamicScreen / watch / this.currentDatasetURI : ', this.currentDatasetURI);
      // console.log('- - DynamicScreen / watch / currentDatasetURI : ', currentDatasetURI);
      // commit('setDatasetURI', currentDatasetURI)

      // check search for Map
      this.$store.commit('setIsMapSearch', this.localRouteConfig)

      if( this.localRouteConfig.dynamic_templates !== 'DynamicStatic' ) {
        // console.log('- - DynamicScreen / watch / localRouteConfig : ', this.localRouteConfig);
        
        this.localEndpointConfig = this.$store.getters.getEndpointConfig
        // console.log('- - DynamicScreen / watch / localEndpointConfig : ', this.localEndpointConfig);
        
        if ( currentDatasetURI !== this.currentDatasetURI ) {
        // if ( this.localEndpointConfig && currentDatasetURI !== this.currentDatasetURI ) {
          // console.log('- - DynamicScreen / watch / need to reinit filters ... ')
          this.currentDatasetURI = currentDatasetURI
          this.localFiltersConfig = this.$store.getters.getEndpointConfigFilters
          this.$store.dispatch('createDatasetFilters')
        }
        if (this.localEndpointConfig) {
          // reload results 
          // console.log('- - DynamicScreen / watch / (after) dispatch search... ');
          this.$store.dispatch('search')
        }

      } else {
        this.localEndpointConfig = undefined
        this.localFiltersConfig = undefined
      }

    },


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
      // console.log(" - - DynamicScreen / this.$router.currentRoute.path : ", this.$router.currentRoute.path)
      let routeConf = this.$store.getters.getCurrentRouteConfig(this.$router.currentRoute.path)
      // console.log(" - - DynamicScreen / routeConf : ", routeConf)
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
    has_credits_footer(){      
      return (this.footerConfig) ? this.footerConfig.has_credits_footer : undefined 
    },
    has_banner(){      
      return (this.localRouteConfig) ? this.localRouteConfig.banner.activated : false 
    },

    // BANNER
    getCurrentBanner () {
      let bannersSet = this.stylesConfig.app_banners.banners_set
      const routeBannerUri = this.localRouteConfig.banner.banner_uri
      let resultSet = bannersSet.find(function(b) {
        return b.banner_uri == routeBannerUri
      })
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

<style lang="scss" scoped>
@import '../../../styles/apiviz-colors.scss';
@import '../../../styles/apiviz-misc.scss';

.extra-footer {
  background-color : $apiviz-primary ;
  color : #ffffff;
  padding-top : 10px ;
  padding-bottom : 10px;

  a {
    color : white;
  }
}

</style>
