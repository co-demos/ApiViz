<template>
    <nav class="navbar is-white is-fixed-top" role="navigation" aria-label="main navigation">

      <div class="container">
          
        <Brand 
          :logo="logo" 
          :brand="brand"
        ></Brand>

        <!-- DEBUGGING -->
        <!-- currentRouteConfig : {{ currentRouteConfig.field }} -
        localRouteConfig : {{ localRouteConfig }} -->

        <NavBarContent 
          :NavbarLinks="this.navbarConfig.links_options"
          :user="user"
        ></NavBarContent>

      </div>

    </nav>
</template>

<script>
import Brand from './Brand.vue';
import NavBarContent from './NavBarContent.vue';

export default {
  components: {
    Brand,
    NavBarContent
  },
  props: [
    'navbarConfig',
    'appLocales',
    'logo', 
    'brand', 
    
    // 'currentRouteConfig',
    // 'localRouteConfig',

    'user'
  ]
}
</script>

<style>
nav {
    height: 60px;
    z-index: 10;
}
</style>