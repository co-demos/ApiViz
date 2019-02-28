<template>
    <div>
        <NavBar :logo="logo" :brand="brand"/>

        <section class="hero is-light is-fullheight skip-navbar">

        	<div class="hero-body">

        		<div class="container has-text-centered">

        			<div class="column is-4 is-offset-4" v-if="!user.isLoggedin">


        				<p class="subtitle has-text-grey">Vous avez déjà un compte ?</p>
        				<h3 class="title has-text-grey">Se connecter</h3>

        				<div class="box">
                    <FormLogin/>
        				</div>

        				<p class="has-text-grey">
        					<a href="/app/register">créer un compte</a> &nbsp;·&nbsp;
        					<a href="/app/forgot-password" disabled>password oublié ?</a> &nbsp;·&nbsp;
        				</p>


        				<br>


        				<p class="subtitle has-text-grey">Pas encore de compte ?</p>
        				<h3 class="title has-text-grey">Enregistrez-vous</h3>

        				<div class="box">
        					<div class="content is-size-7">
        						<p>
        							Profitez d’un compte sur la plateforme, et
        							participez à l’amélioration du site.
        						</p>
        					</div>
        					<a 	id="btn_register"
        						class="button is-primary is-large is-outlined is-fullwidth tooltip is-tooltip-right is-tooltip-multiline"
        						data-tooltip="Le site est-il agréable à utiliser ? Vous avez des idées pour améliorer le moteur de recherche ? Certains boutons ne fonctionnent pas ?"
        						href="/register" >
        						<strong>S'inscrire</strong>
        					</a>
                </div>

        			</div>

              <div class="column is-4 is-offset-4" v-if="user.isLoggedin">
                <p class="subtitle has-text-grey">Bonjour {{user.infos.email}}</p>

                <div class="box">
                    <FormLogin/>
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
import FormLogin from '../FormLogin.vue';

export default {
    components: {
        NavBar, Footer, FormLogin
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
