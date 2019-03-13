<template>
  <DynamicSearchScreenSqueleton 
    mainClass="list"
    >
    <SearchResultsList
      :routeConfig="routeConfig"
      :projectContentsFields="routeConfig.contents_fields"
      />
    <!-- :logo="logo" 
    :brand="brand"  -->
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
    // 'logo', 
    // 'brand'
  ],

  // beforeCreate: function () {
  //   console.log("\n - - DynamicList / beforeCreate ... ")
  // },
  // created: function () {
  //   console.log("\n - - DynamicList / created ... ")
  // },
  // beforeMount: function () {
  //   console.log("\n - - DynamicList / beforeMount ... ")
  //   console.log(" - - DynamicScreen / this.routeConfig : \n ", this.routeConfig)

  // },
  // mounted: function () {
  //   console.log("\n - - DynamicList / mounted ... ")
  //   console.log("- - DynamicList / this.routeConfig", this.routeConfig)
  // },

  components: {
    DynamicSearchScreenSqueleton, 
    SearchResultsList
  },
  computed: {
    ...mapState({
      user: 'user'
    }),

  },
}
</script>
<style>
.list .filter-feedback{
  padding-bottom: 0;
}
</style>
