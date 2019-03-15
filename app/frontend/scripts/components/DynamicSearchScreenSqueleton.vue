<template>
  <div>
    <SearchWithFilters
      :filtersConfig="filtersConfig"
    />
    <main :class="mainClass">
      <FiltersFeedback/>
      <slot/>
    </main>

    <!-- DEBUGGING -->
      <!-- 
        <br><br>
      DynamicSearchSqueleton // endpointConfig : <br><code>{{ this.endpointConfig }}</code>
      <br><br>
      DynamicSearchSqueleton // getEndpointConfigFilters : <br><code>{{ this.getEndpointConfigFilters }}</code> 
    --> 

  </div>
</template>

<script>
// import NavBar from './NavBar.vue';
import SearchWithFilters from './SearchWithFilters.vue';
import FiltersFeedback from './FiltersFeedback.vue';
// import Footer from './Footer.vue';

export default {
  name: 'DynamicSearchScreenSqueleton',
  components: {
    // NavBar, 
    SearchWithFilters, 
    FiltersFeedback, 
    // Footer
  },
	props: [
    // 'logo', 
    // 'brand', 
    'filtersConfig',
    'mainClass'
  ],
  computed : {
    // endpointConfig() {
    //   return this.$store.getters.getEndpointConfig
    // },
    // getEndpointConfigFilters() {
    //   return this.$store.getters.getEndpointConfigFilters
    // }
  }
}
</script>

<style lang="scss">
@import '../../styles/apiviz-misc.scss';

main{
  margin-top: $apiviz-navbar-height + $apiviz-search-bar-height;
}
</style>
