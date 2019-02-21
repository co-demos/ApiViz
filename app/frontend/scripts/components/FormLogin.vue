<template>
    <div>

      <!-- {# -->
      <!-- <figure class="avatar">
      	<img src="https://placehold.it/128x128">
      </figure> -->
      <!-- #} -->

      <form action="" method="POST" name="form">

      	<!-- {{ form.hidden_tag() }} -->
      	<!-- {# {{ form.csrf_token }} #} -->

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
      			<input type="password" name="userPassword" value="">
      			<span class="icon is-small is-left">
      				<i class="fas fa-key"></i>
      			</span>
      		</div>
      	</div>


      	<div class="field">
          <input type="checkbox" name="userRememberMe" value="">
          <label for="checkbox">remember me</label>
      		<!-- {{ form.userRememberMe }}
      		{{ form.userRememberMe.label }} -->
      	</div>


      	<button class="button is-block is-primary is-large is-fullwidth" type="submit">
      		Se connecter
      	</button>


      	<!-- {# <div class="field ">
      		<div class="control is-large has-text-centered is-fullwidth">
      			<label 	for="postLogin"
      					class="button is-block is-primary is-large">
      				<span>
      					s'enregistrer
      				</span>
      			</label>
      			<input 	id="postLogin"
      					class="is-hidden"
      					type="submit"
      				>
      			</input>
      		</div>
      	</div>
      	#} -->

      </form>
    </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
    props: [
        'logo', 'brand'
    ],

    computed: mapState({
        user: 'user'
    }),

    methods: {
        goBack(e){
            e.preventDefault()
            this.$router.back()
        }
    }

}
</script>
