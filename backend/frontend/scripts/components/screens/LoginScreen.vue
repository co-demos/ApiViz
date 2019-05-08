<template>
  <!-- <div> -->
      <!-- <NavBar :logo="logo" :brand="brand"/> -->

  <section class="hero has-background-white-ter is-fullheight skip-navbar">

    <div class="hero-body">
      <div class="container has-text-centered">
       
        <!-- DEBUGGING -->
        <!-- user : <code>{{ user }}</code><br> -->
        <!-- jwt : <code>{{ jwt }}</code></br> -->
        
        
        <div class="columns is-mobile is-centered">

          <div class="column is-6" 
            v-if="!user.isLoggedin"
            >

            <p class="subtitle has-text-grey">
              {{ getText('is_account') }}
            </p>

            <!-- main login form -->
            <div class="box">
              <FormLogin/>
            </div>

            <div class="columns is-mobile is-centered">

              <div class="column is-6" >
                <p class="has-text-grey">
                  <router-link :to="'/register'">
                    {{ getText('create_account') }}
                  </router-link>
                </p>
              </div>

              <div class="column is-6" >
                <p class="has-text-grey">
                  <router-link disabled :to="'/forgot-password'">
                    {{ getText('forgot_password') }}
                  </router-link>
                </p>
              </div>

            </div>

            <br>
            <br>

          </div>

          <div class="column is-6" 
            v-if="user.isLoggedin"
            >
            <p class="subtitle has-text-grey">
              <!-- Bonjour  -->
              {{ getText('hello') }}
              {{ user.infos.name }}
            </p>

            <div class="box">
              <FormLogin/>
            </div>

          </div>

        </div>
      </div>
    </div>

  </section>

      <!-- <Footer/> -->
  <!-- </div> -->
</template>

<script>
import { mapState } from 'vuex'

// import NavBar from '../NavBar.vue';
// import Footer from '../Footer.vue';
import FormLogin from '../FormLogin.vue';

export default {
  components: {
    // NavBar, 
    // Footer, 
    FormLogin
  },
  props: [
    'logo', 
    'brand'
  ],

  computed: mapState({
    user : 'user',
    jwt : 'jwt'
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

    getText(textCode) {
      return this.$store.getters.defaultText({txt:textCode})
    },

    goBack(e){
      e.preventDefault()
      this.$router.back()
    }
  }

}
</script>
