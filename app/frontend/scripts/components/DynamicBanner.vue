<style scoped>

.banner-height {
  padding-top: 90px;
  margin-top: 10px;
  margin-bottom: 30px;
  height: 160px
}
</style>

<template>

  <section >
    <div 
      class="container banner-height has-text-center skip-navbar"
      
      >
      <!-- <span v-html="rawHtml"></span> -->
      <div class="columns is-offset-2" style="background-color:white" >
        <div class="column is-one-third">
            <img src="https://github.com/co-demos/carto-sonum/blob/master/illustrations/illustrations_sonum_png/illu1.png?raw=true" style="height:150px; margin-left:75px">
        </div>
        <div class="column is-two-thirds is-vertical-centered">
            <h1 class="title is-2">
                <span>DECOUVREZ <br>LES</span>
                <span>LIEUX DE MEDIATION <br>NUMERIQUE </span>
                <span class="icon">
                    <i class="fas fa-arrow-down"></i>
                </span>
            </h1>
        </div>
      </div>

    </div>
  </section>
</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios'

export default {
    props:[
      'template_url',
      'navbarConfig'
    ],
  data: () => {
    return   {
      rawHtml : '',
      visible : true,
    }
  },
  computed: {
    ...mapState({
      user: 'user'
    })
  },
  mounted(){
    
    // hack to scroll top because vue-router scrollBehavior thing doesn't seem to work on Firefox on Linux at least
  // here we go fetch the raw HTML content of a webpage
  let template_url = (this.template_url) ? this.template_url : 'https://co-demos.com/error'
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
