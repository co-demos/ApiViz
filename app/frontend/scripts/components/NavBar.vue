<template>
    <nav class="navbar is-white is-fixed-top" role="navigation" aria-label="main navigation">

        <div class="container">
            
            <Brand 
                :logo="logo" 
                :brand="brand"
            />

            {{ currentRouteConfig.field }}
            <NavBarContent 
                :NavbarLinks="navbarConfig.links_options"
                :user="user"
            />

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
        'logo', 
        
        'currentRouteConfig',

        'brand', 
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