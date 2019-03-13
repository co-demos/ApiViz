<template>
  <DynamicSearchScreenSqueleton 
    :logo="logo" 
    :brand="brand" 
    mainClass="list"
    ><SearchResultsList/>
  </DynamicSearchScreenSqueleton>
</template>

<script>
import {mapState} from 'vuex'

import DynamicSearchScreenSqueleton from './DynamicSearchScreenSqueleton.vue'
import SearchResultsList from './SearchResultsList.vue';

export default {
    name: 'DynamicList',
    props:[
      'routeConfig',
      'logo', 
      'brand'
    ],
    components: {
        DynamicSearchScreenSqueleton, SearchResultsList
    },
    computed: {
      ...mapState({
          user: 'user'
      })
    },
}
</script>
<style>
.list .filter-feedback{
    padding-bottom: 0;
}
</style>
