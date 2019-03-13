<template>

  <div class="navbar-brand" :title="brand">

      <!-- <a href="/" class="navbar-item">
        <img id="navbar-logo" :src="logo" :alt="'Logo '+ brand">
      </a> -->

      <router-link 	
        id="logo_home"
        class="navbar-item" 
        to="/">
        <img 
            id="navbar-logo" 
            :src="this.logo.url"
            :alt="'Logo ' + brand"
        ></img>
      </router-link>

    </div>


</template>

<script>
export default {
  props: [
    'logo', 
    'brand'
  ]
}
</script>
