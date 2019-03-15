<template>
  <DynamicSearchScreenSqueleton 
    :filtersConfig="filtersConfig"
    mainClass="list"
    >
    <!-- :logo="logo" 
    :brand="brand"  -->
      <SearchResultsMap
        :routeConfig="routeConfig"
        :endPointConfig="endPointConfig"
      />
  </DynamicSearchScreenSqueleton>
</template>

<script>
import {mapState} from 'vuex'

import DynamicSearchScreenSqueleton from './DynamicSearchScreenSqueleton.vue'
import SearchResultsMap from './SearchResultsMap.vue';

export default {
  name: 'DynamicMap',  
  props:[
    'routeConfig',
    'endPointConfig',
    'filtersConfig',
    // 'logo', 
    // 'brand'
  ],
  components: {
    DynamicSearchScreenSqueleton, 
    SearchResultsMap
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
