<template>
    <div>
        <NavBar :logo="logo" :brand="brand"/>

        <section class="hero is-light is-fullheight skip-navbar">

          <div class="hero-body">

            <div class="container has-text-centered">

              <div class="column is-4 is-offset-4" v-if="!user.isLoggedin">

                <p class="subtitle has-text-grey">Vous n'avez pas encore de compte ?</p>
        				<h3 class="title has-text-grey">S'enregistrer</h3>

                <div class="box">
                    <FormRegister/>
                </div>

              </div>

              <div class="column is-4 is-offset-4" v-if="user.isLoggedin">
                <p class="subtitle has-text-grey">Bonjour {{user.infos.email}}, vous etes deja enregistre
                </p>

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
import FormRegister from '../FormRegister.vue';

export default {
    components: {
        NavBar, Footer, FormRegister
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
        }
    }

}
</script>
