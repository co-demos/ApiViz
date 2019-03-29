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
    }
  },

  beforeMount: function () {
    // console.log("\n - - DynamicStatic / beforeMount ... ")
  },

  mounted(){
    // console.log("\n - - DynamicStatic / mounted ... ")

    this.getRawHtml()
    // // hack to scroll top because vue-router scrollBehavior thing doesn't seem to work on Firefox on Linux at least
    // const int = setInterval(() => {
    //   if(window.pageYOffset < 50){
    //       clearInterval(int)
    //   }
    //   else{
    //       window.scrollTo(0, 0)
    //   }
    // }, 100);

    // // here we go fetch the raw HTML content of a webpage
    // let template_url = (this.routeConfig && this.routeConfig.template_url) ? this.routeConfig.template_url : 'https://co-demos.com/error'
    // let head = { 
    //   headers: {
    //     // 'Access-Control-Allow-Origin': '*',
    //     'accept' : 'text/html',
    //   }
    // }
    // this.rawHtml = ''
    // axios.get(template_url, head)
    //   .then( (response) => { 
    //     // console.log(response); 
    //     this.rawHtml = (response && response.data) ? response.data : '<br><br>there is an Error <br><br>'} 
    //   )
    //   .catch( (err) => {this.rawHtml = '<br><br>there is an <strong> Error </strong><br><br>'} )
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
      let head = { 
        headers: {
          // 'Access-Control-Allow-Origin': '*',
          'accept' : 'text/html',
        }
      }
      this.rawHtml = ''
      axios.get(template_url, head)
        .then( (response) => { 
          // console.log(response); 
          this.rawHtml = (response && response.data) ? response.data : '<br><br>there is an Error <br><br>'} 
        )
        .catch( (err) => {this.rawHtml = '<br><br>there is an <strong> Error </strong><br><br>'} )
    },
    goBack(e){
      e.preventDefault()
      this.$router.back()
    }
  }

}
</script>
