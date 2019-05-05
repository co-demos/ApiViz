<template>
    <div>

      <h5 class="title has-text-grey"
        v-if="!user.isLoggedin"
        >
        {{ getText('login') }}
      </h5>

      <form 
        v-if="!user.isLoggedin"
        v-on:submit.prevent="sendLoginForm" 
        name="form" 
        >
        <span>{{ this.customformError }}</span>

      	<div class="field">
      		<div class="control has-icons-left">
            <input class="input" 
              v-model="userEmail"
              v-validate="'required|email'" 
              name="userEmail" 
              :placeholder="getText('email')"
              type="email" 
              >
            <span>{{ errors.first('userEmail') }}</span>
      			<span class="icon is-small is-left">
      				<i class="fas fa-envelope"></i>
      			</span>
      		</div>
      	</div>

      	<div class="field">
      		<div class="control has-icons-left">
            <input class="input" 
              v-validate="'required'" 
              v-model="userPassword"
              name="userPassword" 
              :placeholder="getText('password')"
              type="password" 
              >
            <span>{{ errors.first('userPassword') }}</span>
      			<span class="icon is-small is-left">
      				<i class="fas fa-key"></i>
      			</span>
      		</div>
      	</div>

      	<div class="field">
          <!-- <div class="control has-icons-left"> -->
            <input 
              class="checkbox" 
              name="userRememberMe" 
              type="checkbox" 
              value=""
            >
            <label for="checkbox">
              <!-- remember me -->
              {{ getText('remember_me') }}
            </label>
          <!-- </div> -->
      	</div>

        <br>

      	<button 
          class="button is-block is-primary is-fullwidth" 
          type="submit" 
          >
          <!-- @click="sendLoginForm" -->
      		{{ getText('connect') }}
      	</button>

      </form>

      <button 
        v-if="user.isLoggedin" 
        class="button is-block is-primary is-fullwidth" 
        type="submit" 
        @click="sendLogout"
        >
        {{ getText('disconnect') }}
      </button>

    </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios';
// import { apiConfig } from '../config/api.js';
// import { getConfigName } from '../utils.js';


export default {
  data: function () {
    return {
      userEmail: '',
      userPassword: '',
      userRememberMe: true,
      customformError: ''
    }
  },
  computed: mapState({
    user: 'user'
  }),
  methods: {

    getText(textCode) {
      return this.$store.getters.defaultText({txt:textCode})
    },

    sendLoginForm(e){
      this.customformError = ''
      e.preventDefault()

      const urlAuthRoot = this.$store.getters.getRootUrlAuth
      // console.log("urlAuthRoot : ", urlAuthRoot)

      const urlAuthLogin = this.$store.getters.getEndpointConfigAuthSpecific('login')
      const urlAuthLoginSuffix = urlAuthLogin.root_url
      // console.log("urlAuthLoginSuffix : ", urlAuthLoginSuffix)

      let payload = {
        email:this.userEmail,
        pwd:this.userPassword
      }

      axios
        .post( urlAuthRoot + urlAuthLoginSuffix, payload)
        .catch( (error) => {
          console.log(error)
          this.customformError = 'Login failed'
        })
        .then(response => this.$store.dispatch('saveLoginInfos',{APIresponse:response}) )
      this.userPassword = ''
    },

    sendLogout(e){
      e.preventDefault()
      this.userEmail = ''
      this.userPassword = ''
      this.$store.dispatch('logout')
      this.$router.push('logout')
    },

  }
}
</script>
