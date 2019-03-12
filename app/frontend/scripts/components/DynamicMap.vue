<template>
  <DynamicSearchScreenSqueleton :logo="logo" :brand="brand" mainClass="list">
      <SearchResultsMap/>
  </DynamicSearchScreenSqueleton>
</template>

<script>
import {mapState} from 'vuex'

import DynamicSearchScreenSqueleton from './DynamicSearchScreenSqueleton.vue'
import SearchResultsMap from './SearchResultsMap.vue';

export default {
    name: 'DynamicMap',  
    props:[
      'routeConfig','logo', 'brand'
    ],
    components: {
        DynamicSearchScreenSqueleton, SearchResultsMap
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
