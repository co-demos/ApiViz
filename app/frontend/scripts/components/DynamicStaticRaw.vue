<template>
  <span v-html="rawHtml"></span>
</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios'

export default {
    props:[
      'routeConfig',
      'templateURL'
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
    // here we go fetch the raw HTML content of a webpage
    let template_url = (this.templateURL) ? this.templateURL : 'https://co-demos.com/error'
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
