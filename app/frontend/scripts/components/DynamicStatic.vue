<template>
  <div>
    <section class="hero is-light is-fullheight skip-navbar">

      <!-- DEBUGGING -->
      <!-- <div>
          - routeConfig : <br><code>{{ this.routeConfig }}</code><br>
          - appConfig : <br><code>{{ this.appConfig }}</code><br>
          - navbarConfig : <br><code>{{ this.navbarConfig }}</code><br>
      </div>

      <hr> 
      s-->

      <div class="hero-body">
          <div class="container has-text-centered">
              <span v-html="rawHtml"></span>
          </div>
      </div>

    </section>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios'

export default {
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

  // here we go fetch the raw HTML content of a webpage
  let template_url = (this.routeConfig && this.routeConfig.template_url) ? this.routeConfig.template_url : 'https://co-demos.com/error'
  let head = { 
    headers: {
      // 'Access-Control-Allow-Origin': '*',
      'accept' : 'text/html',
    }
  }
  axios.get(template_url, head)
    .then( (response) => { 
      // console.log(response); 
      this.rawHtml = (response && response.data) ? response.data : '<br><br>there is an Error <br><br>'} 
    )
    .catch( (err) => {this.rawHtml = '<br><br>there is an <strong> Error </strong><br><br>'} )
  },
  methods: {
  goBack(e){
    e.preventDefault()
    this.$router.back()
  }
  }
}
</script>
