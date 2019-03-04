<template>
    <div>

      <form v-on:submit.prevent="sendLoginForm" name="form" v-if="!user.isLoggedin">
        <span>{{ this.customformError }}</span>


      	<div class="field">
      		<div class="control has-icons-left">
            <input v-validate="'required|email'" name="userEmail" type="email" v-model="userEmail">
            <span>{{ errors.first('userEmail') }}</span>
      			<span class="icon is-small is-left">
      				<i class="fas fa-envelope"></i>
      			</span>
      		</div>
      	</div>

      	<div class="field">
      		<div class="control has-icons-left">
            <input v-validate="'required'" name="userPassword" type="password" v-model="userPassword">
            <span>{{ errors.first('userPassword') }}</span>
      			<span class="icon is-small is-left">
      				<i class="fas fa-key"></i>
      			</span>
      		</div>
      	</div>

      	<div class="field">
          <input type="checkbox" name="userRememberMe" value="">
          <label for="checkbox">remember me</label>
      	</div>


      	<button class="button is-block is-primary is-large is-fullwidth" type="submit" v-model="userRememberMe">
      		Se connecter
      	</button>

      </form>

      <button class="button is-block is-primary is-large is-fullwidth" type="submit" v-if="user.isLoggedin" @click="sendLogout">
        Se deconnecter
      </button>

    </div>
</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios';
import { apiConfig } from '../config/api.js';


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
        sendLoginForm(e){
          this.customformError = ''
          e.preventDefault()
          axios
            .post(apiConfig.toktokURL+'/auth/login/',
            {
              email:this.userEmail,
              pwd:this.userPassword
            })
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
        },
    }
}
</script>
