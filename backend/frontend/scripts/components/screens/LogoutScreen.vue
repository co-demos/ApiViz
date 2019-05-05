<template>
  <!-- <div> -->
      <!-- <NavBar :logo="logo" :brand="brand"/> -->

  <section class="hero has-background-white-ter is-fullheight skip-navbar">

    <div class="hero-body">
      <div class="container has-text-centered">
        <div class="columns is-mobile is-centered">

          <div class="column is-6" 
            v-if="!user.isLoggedin">
            <h3 class="title has-text-grey">
              <!-- Vous avez été déconnecté -->
              {{ getText('disconnect_msg') }}
            </h3>
            <div class="box">
              <router-link 
                class="button is-block is-primary is-fullwidth" 
                type="submit" 
                :to="'/login'"
                >
                <!-- Se re-connecter -->
                {{ getText('reconnect') }}
              </router-link>
            </div>
          </div>

          <div class="column is-6" 
            v-if="user.isLoggedin">
            <h3 class="title has-text-grey">
              <!-- Vous voulez vous déconnecter? -->
              {{ getText('want_disconnect') }}
            </h3>
            <div class="box">
              <button 
                class="button is-block is-primary is-fullwidth" 
                type="submit" 
                @click="sendLogout">
                {{ getText('disconnect') }}
              </button>
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

export default {
  components: {
    // NavBar, 
    // Footer
  },
  props: [
    'logo', 
    'brand'
  ],

  computed: mapState({
    user: 'user'
  }),

  mounted(){
    // hack to scroll top because vue-router scrollBehavior thing doesn't seem to work on Firefox on Linux at least
    const int = setInterval(() => {
      if(window.pageYOffset < 50){
        clearInterval(int)
      } else {
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
