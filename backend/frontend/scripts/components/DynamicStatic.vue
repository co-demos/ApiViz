<template>
  <!-- <section class="is-light skip-navbar"> -->

    <!-- DEBUGGING -->
    <!-- <div>
        - routeConfig : <br><code>{{ this.routeConfig }}</code><br>
        - appConfig : <br><code>{{ this.appConfig }}</code><br>
        - navbarConfig : <br><code>{{ this.navbarConfig }}</code><br>
    </div>

    <hr> 
    s-->


    <!-- MAIN PART -->
    <div class="skip-navbar">

      <span v-html="rawHtml"></span>

    </div>




  <!-- </section> -->
</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios'
import {loadScript, activateCarousel} from '../utils'

export default {
  name: 'DynamicStatic',
  props:[
    'routeConfig',
    'navbarConfig'
  ],
  data: () => {
    return   {
      rawHtml : ''
    }
  },
  computed: {
    ...mapState({
      user: 'user'
    })
  },

  watch : {
    routeConfig(old){
      // console.log("\n - - DynamicStatic / watch / routeConfig ... ")
      this.rawHtml = ''
      this.getRawHtml()
    },
    rawHtml(newRawHtml, oldRawHtml){
      if (oldRawHtml == '' && newRawHtml != ''){
        console.log("rawHtml is not blank anymore")
        this.loadExtScript()
      }
      else{
        // console.log(oldRawHtml, newRawHtml)
      }
    }
  },

  beforeMount: function () {
    // console.log("\n - - DynamicStatic / beforeMount ... ")
  },

  mounted(){
    // console.log("\n - - DynamicStatic / mounted ... ")
    this.getRawHtml()
  },

  methods: {

    getRawHtml(){
      // hack to scroll top because vue-router scrollBehavior thing doesn't seem to work on Firefox on Linux at least
      const int = setInterval(() => {
        if(window.pageYOffset < 50){
            clearInterval(int)
        }
        else{
            window.scrollTo(0, 0)
        }
      }, 100);

      // here we go fetch the raw HTML content of a webpage
      let template_url = (this.routeConfig && this.routeConfig.template_url) ? this.routeConfig.template_url : 'https://co-demos.com/error'
      console.log(template_url + " is template")
      let head = {
        headers: {
        //  'Access-Control-Allow-Origin': '*', // Uncommented, to try
          'accept' : 'text/html',
        }
      }
      this.rawHtml = ''
      axios.get(template_url, head)
        .then( (response) => {
          //console.log(response);
          this.rawHtml = (response && response.data) ? response.data : '<br><br>there is an Error <br><br>'}
        )
        .catch( (err) => {this.rawHtml = '<br><br>there is an <strong> Error </strong><br><br>'} )

    },

    loadExtScript(){
      // IMPORT EXT SCRIPT
      // Cf:
      // https://stackoverflow.com/questions/17341122/link-and-execute-external-javascript-file-hosted-on-github
      // https://stackoverflow.com/questions/45047126/how-to-add-external-js-scripts-to-vuejs-components
      if (this.routeConfig && this.routeConfig.has_ext_script) {

        let ext_script_url = this.routeConfig.ext_script_url;
        console.log(ext_script_url + " is ext_script")
        let extScript = document.createElement('script');
        extScript.setAttribute('src', ext_script_url);
        extScript.setAttribute('type', "text/javascript");
        document.head.appendChild(extScript);

      }

      // ACTIVATE CAROUSELS
      if (this.routeConfig && this.routeConfig.has_carousel){
        console.log("load carousel from utils");
        loadScript("https://cdn.jsdelivr.net/npm/bulma-carousel@4.0.4/dist/js/bulma-carousel.min.js", activateCarousel);
        
        // activateCarousel() 
        // activateCarousel(slidesNumber=2, isInfinite=true, hasPagination=true)
      }
    },

    goBack(e){
      e.preventDefault()
      this.$router.back()
    }

  }

}
</script>
