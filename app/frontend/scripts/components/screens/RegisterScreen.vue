<template>
    <div>
        <NavBar :logo="logo" :brand="brand"/>

        <section class="hero is-light is-fullheight skip-navbar">

          <div class="hero-body">

            <div class="container has-text-centered">

              <div class="column is-4 is-offset-4">

                <form action="/register" method="POST" name="form">
                  <p>Ce formulaire a été utilisé malicieusement pour nous envoyer du spam et est actuellement désactivé le temps que nous trouvions une solutions pérenne

                  <p>En attendant, pour toute question, n'hésitez pas à nous écrire à contact@carrefourdesinnovationssociales.fr

                  <fieldset disabled>
                    <!-- {{ form.hidden_tag() }} -->
                    <!-- {# { { form.csrf_token }} #} -->

                    <div class="field">
                      <label class="label">vos informations</label>
                      <div class="control has-icons-left">
                        <input type="" name="userName" value="">
                        <span class="icon is-small is-left">
                          <i class="fas fa-user"></i>
                        </span>
                      </div>
                    </div>

                    <div class="field">
                      <div class="control has-icons-left">
                        <input type="" name="userSurname" value="">
                        <span class="icon is-small is-left">
                          <i class="fas fa-user"></i>
                        </span>
                      </div>
                    </div>

                    <div class="field">
                      <div class="control has-icons-left">
                        <input type="email" name="userEmail" value="">
                        <span class="icon is-small is-left">
                          <i class="fas fa-envelope"></i>
                        </span>
                      </div>
                    </div>

                    <div class="field">
                      <div class="control has-icons-left">
                        <input type="password" name="registerPassword" value="">
                        <span class="icon is-small is-left">
                          <i class="fas fa-key"></i>
                        </span>
                      </div>
                    </div>

                    <div class="field">
                      <div class="control has-icons-left">
                        <input type="password" name="userConfirmPassword" value="">
                        <span class="icon is-small is-left">
                          <i class="fas fa-key"></i>
                        </span>
                      </div>
                    </div>
                    <p class="help is-light">* champs requis</p>



                    <div class="is-divider" data-content="votre profil métier (optionnel)"></div>


                    <div class="field">
                      <div class="control">
                        <div class="select is-fullwidth">
                          <input type="radio" name="userProfile" value="">
                          <!-- {{ form.userProfile }} -->
                        </div>
                      </div>
                    </div>



                    <div class="is-divider" data-content="votre structure (optionnel) "></div>


                    <div class="field">
                      <div class="control">
                        <div class="select is-fullwidth">
                          <input type="radio" name="userPartnerStructure" value="">
                          <!-- {{ form.userPartnerStructure }} -->
                        </div>
                      </div>
                    </div>


                    <div class="field" style='display:none' id="userOtherStructureField">
                      <div class="control has-icons-left">
                        <input type="text" name="userOtherStructure" value="">
                        <!-- {{ form.userOtherStructure }} -->
                        <span class="icon is-small is-left">
                          <i class="fas fa-building"></i>
                        </span>
                      </div>
                    </div>

                    {# <div class="field" style='display:none' id="userSiretField">
                      <div class="control has-icons-left">
                        <input type="text" name="userSiret" value="">
                        <!-- {{ form.userSiret }} -->
                        <span class="icon is-small is-left">
                          <i class="fas fa-building"></i>
                        </span>
                      </div>
                      <p class="help is-light">(optionnel)</p>
                    </div> #}


                    <div class="field" style='display:none' id="userStructureProfileField">
                      <div class="control">
                        <div class="select is-fullwidth">
                          <!-- {{ form.userStructureProfile }} -->
                        </div>
                      </div>
                    </div>


                    <div id="userWishesFields" style='display:none'>

                      <div class="is-divider" data-content="vos envies"></div>

                      <div class="field is-pulled-left">
                        <input type="checkbox" name="userHaveProjects" value="">
                        <!-- {{ form.userHaveProjects( class ='is-checkradio is-black is-normal') }}-->
                        <label for="userHaveProjects"></label>
                        <!-- {{ form.userHaveProjects.label }}  -->
                      </div>
                      <br>
                      <div class="field is-pulled-left">
                        <!-- {{ form.userJoinCollective( class ='is-checkradio is-black is-normal') }}
                        {{ form.userJoinCollective.label }} -->
                      </div>
                      <br><br>

                    </div>




                    {#
                    <br>

                    <div class="field">
                      <input type="checkbox" name="userRememberMe" value="">
                      <label for="checkbox">remember me</label>
                      <!-- {{ form.userRememberMe }}
                      {{ form.userRememberMe.label}} -->
                    </div>
                    #}


                    <div class="is-divider" data-content="une remarque, un commentaire ? (optionnel)"></div>


                    <div class="field is-horizontal">
                      <div class="field-body">
                        <div class="field">
                          <div class="control">
                            <!-- {{ form.userMessage() }} -->
                          </div>
                        </div>
                      </div>
                    </div>


                    <br>

                    <div class="field has-text-left">
                      <!-- {{ form.userNewsletter( class='is-checkradio is-black is-normal') }} -->
                      <input type="checkbox" name="userNewsletter" value="">
                      <label for="userNewsletter">
                        Je souhaite recevoir la newsletter
                        {# du Carrefour des innovations sociales #}
                      </label>
                    </div>


                    <div class="field has-text-left">
                      <!-- {{ form.userAcceptCGU( class ='is-checkradio is-black is-normal') }} -->
                      <input type="checkbox" name="userAcceptCGU" value="">
                      <!-- {# { { form.userAcceptCGU.label }} #}  -->
                      <label for="userAcceptCGU">
                        J'accepte les
                        <a class="modal-button has-text-primary" data-target="modal_legal" aria-haspopup="true">
                          Conditions Générales d'Utilisation
                        </a>
                      </label>
                    </div>

                    <br>



                    <button class="button is-block is-primary is-large is-fullwidth tooltip is-tooltip-danger is-tooltip-bottom is-tooltip-multiline"
                        data-tooltip="Soyez parmi les premiers à être informé.e de la sortie de la première version du moteur de recherche"
                        type="submit">
                      S'enregistrer
                    </button>

                  </fieldset>
                </form>

                <!-- // <script type="text/javascript" language="javascript" src="{{ url_for('static', filename='js/form-display-other-structure-name.js') }}"></script> -->
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
        }
    }

}
</script>
