<style scoped>

  .banner-height-with-filters {
    /* padding-top: 125px; */
    margin-top: 100px;
    margin-bottom: 30px;
    max-height: 170px
  }
  .banner-height-without-filters {
    padding-top: 60px;
    margin-top: 10px;
    margin-bottom: 30px;
    height: 160px
  }

  .buttons{
    margin-right: 3em;
  }

  .close{
    z-index: 2;
    position:absolute;

    /* float: right;
    display: flex;  */
    /* align-self: flex-end; */
    /* justify-content: flex-end !important; */
    /* justify-content: flex-end; */
}

</style>

<template>

  <section 
    v-show="rawHtml !== '' "
    :class="`${ hasFilters ? 'banner-height-with-filters' : 'banner-height-without-filters' } has-text-center skip-navbar`"
    >

    <!-- RAW HTML FOR BANNER -->
    <!-- <div
      :class="`container `"
      > -->

      <!-- BUTTON TO CLOSE PREVIEW -->
      <!-- <div class=""> -->

        <div class="buttons is-right">
          <button 
            class="button close is-primary is-inverted" 
            @click="rawHtml = ''"
            >
            <span class="icon is-small">
              <i class="fas fa-times"></i>
            </span>
          </button>
        </div>

      <div class="container">
        <div class="content">
          <span v-html="rawHtml"></span>
        </div>
      </div>

    <!-- </div> -->


  </section>

</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios'

export default {
    props:[
      'template_url',
      'dynamicTemplate',
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
    }),
    hasFilters(){
      return (this.dynamicTemplate === 'DynamicStatic' )? false : true
    }
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
