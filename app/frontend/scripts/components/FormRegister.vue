<template>
    <div>


      <form v-on:submit.prevent="sendRegisterForm" name="form" v-if="!user.isLoggedin">
        <span>{{ this.customformError }}</span>



        <div class="field">
      		<div class="control has-icons-left">
            <input v-validate="'required'" name="userName" type="text" placeholder="Name" v-model="userName">
            <span>{{ errors.first('userName') }}</span>
      			<span class="icon is-small is-left">
      				<i class="fas fa-user"></i>
      			</span>
      		</div>
      	</div>



        <div class="field">
          <div class="control has-icons-left">
            <input v-validate="'required'" name="userSurname" type="text" placeholder="Surname" v-model="userSurname">
            <span>{{ errors.first('userSurname') }}</span>
            <span class="icon is-small is-left">
              <i class="fas fa-user"></i>
            </span>
          </div>
        </div>



      	<div class="field">
      		<div class="control has-icons-left">
            <input v-validate="'required|email'" name="userEmail" type="email" placeholder="email" v-model="userEmail">
            <span>{{ errors.first('userEmail') }}</span>
      			<span class="icon is-small is-left">
      				<i class="fas fa-envelope"></i>
      			</span>
      		</div>
      	</div>

      	<div class="field">
      		<div class="control has-icons-left">
            <input v-validate="'required'" name="userPassword" type="password" placeholder="Password" ref="userPassword" v-model="userPassword">
            <span>{{ errors.first('userPassword') }}</span>
      			<span class="icon is-small is-left">
      				<i class="fas fa-key"></i>
      			</span>
      		</div>
      	</div>

        <div class="field">
          <div class="control has-icons-left">
            <input v-validate="'required|confirmed:userPassword'" name="userConfirmPassword" type="password" data-vv-as="userPassword" placeholder="Password, Again">
            <span>{{ errors.first('userConfirmPassword') }}</span>
            <span class="icon is-small is-left">
              <i class="fas fa-key"></i>
            </span>
          </div>
        </div>

        <div class="field">
          <div class="control has-icons-left">
            <input v-validate="'required'" name="userAcceptCGU" type="checkbox" v-model="userAcceptCGU">
            <span>{{ errors.first('userAcceptCGU') }}</span>
            <label for="userAcceptCGU">
              J'accepte les
              <a class="modal-button has-text-primary" data-target="modal_legal" aria-haspopup="true">
                Conditions Générales d'Utilisation
              </a>
            </label>
          </div>
        </div>

      	<button class="button is-block is-primary is-large is-fullwidth " :disabled="!enableBtn" type="submit">
      		S'enregistrer
      	</button>

        <br>

        <p class="has-text-grey">
          <router-link :to="{ name: 'login'}">Se connecter</router-link>
        </p>

      </form>

      <p class="button is-block is-primary is-large is-fullwidth" type="submit" v-if="user.isLoggedin">
        deja connecte
      </p>

    </div>
</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios';
import { apiConfig } from '../config/api.js';


export default {
    data: function () {
      return {
        userName: '',
        userSurname: '',
        userEmail: '',
        userPassword: '',
        userAcceptCGU: '',
        customformError: ''
      }
    },
    computed: {
      ...mapState({
          user: 'user'
      }),
      enableBtn() {
        return (this.errors.all().length === 0) ? true : false
      }
    },
    methods: {
        sendRegisterForm(e){
          this.customformError = ''
          e.preventDefault()

          this.$validator.validate().then(boo => {
            // if some fields in the form aren't properly filled
            if (!boo) {
                this.customformError = 'Register failed - ' + this.errors.all();
            }else{
              // if the form looks good, we send it to the backend
              axios
                .post(apiConfig.toktokURL+'/usr/register/',
                {
                  name: this.userName,
                  surname: this.userSurname,
                  email:this.userEmail,
                  pwd:this.userPassword,
                  lang: "en",
                  agreement: this.userAcceptCGU
                })
                .then(response =>
                {
                    // case where code is 200 => success
                    this.$store.dispatch('saveLoginInfos',{APIresponse:response})
                    this.$router.push('login')
                })
                .catch( error =>
                {
                  // in case we catch something, let's display it for easier debug
                  try {
                    let msg = (error.response.data && error.response.data.msg) ? ' - ' + error.response.data.msg : ''
                    switch (error.response.status) {
                      case 401:
                        this.customformError = 'Register failed' + msg
                        break;
                      default:
                        console.log('error unkown',error,Object.keys(error));
                        this.customformError = 'Register failed - contact the webmaster'
                        break;
                    }
                  } catch (e) {
                    console.log('we cannot read the error message from the API',e);
                    this.customformError = 'Register failed'
                  }
                })
                .then(() =>
                  {
                    // in the end, if we need to do something
                    this.userPassword = ''
                    this.userConfirmPassword = ''
                  }
                )
            }
          });
        }
    }
}
</script>
