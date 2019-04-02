<template>
    <div>
        <NavBar :logo="logo" :brand="brand"/>

        <section class="hero is-light is-fullheight skip-navbar">

        	<div class="hero-body">

        		<div class="container has-text-centered">

        			<div class="column is-4 is-offset-4" v-if="!user.isLoggedin">

        				<h3 class="title has-text-grey">Vous avez été déconnecté</h3>
                <p class="subtitle has-text-grey">avec succes</p>
        				<p class="has-text-grey">

                  <router-link class="button is-block is-primary is-large is-fullwidth" type="submit" :to="{ name: 'login'}">Se re-connecter</router-link>

                </p>

        			</div>


              <div class="column is-4 is-offset-4" v-if="user.isLoggedin">

                <h3 class="title has-text-grey">Vous voulez vous deconnecter?</h3>
                <div class="box">

                  <button class="button is-block is-primary is-large is-fullwidth" type="submit" @click="sendLogout">Se deconnecter</button>

                </div>

              </div>

            </div>

        	</div>

        </section>

        <Footer/>
    </div>
</template>

<script>
import {mapState} from 'vuex'

import NavBar from '../NavBar.vue';
import Footer from '../Footer.vue';

export default {
    components: {
        NavBar, Footer
    },
    props: [
        'logo', 'brand'
    ],

    computed: mapState({
        user: 'user'
    }),

    mounted(){
        // hack to scroll top because vue-router scrollBehavior thing doesn't seem to work on Firefox on Linux at least
        const int = setInterval(() => {
            if(window.pageYOffset < 50){
                clearInterval(int)
            }
            else{
                window.scrollTo(0, 0)
            }
        }, 100);
    },

    methods: {
        goBack(e){
            e.preventDefault()
            this.$router.back()
        },
        sendLogout(e){
          e.preventDefault()
          this.userEmail = ''
          this.userPassword = ''
          this.$store.dispatch('logout')
        }
    }

}
</script>
