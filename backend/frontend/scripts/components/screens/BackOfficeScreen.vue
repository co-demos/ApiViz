<template>

  <section class="skip-navbar">

    <div class="container">
      
      <!-- BACK OFFICE MENU -->
      <aside class="column is-4 menu">
        <p class="menu-label">
          General
        </p>
        <ul class="menu-list">
          <li><a>Dashboard</a></li>
          <li><a>Customers</a></li>
        </ul>
        <p class="menu-label">
          Administration
        </p>
        <ul class="menu-list">
          <li><a>Team Settings</a></li>
          <li>
            <a class="is-active">Manage Your Team</a>
            <ul>
              <li><a>Members</a></li>
              <li><a>Plugins</a></li>
              <li><a>Add a member</a></li>
            </ul>
          </li>
          <li><a>Invitations</a></li>
          <li><a>Cloud Storage Environment Settings</a></li>
          <li><a>Authentication</a></li>
        </ul>
        <p class="menu-label">
          Transactions
        </p>
        <ul class="menu-list">
          <li><a>Payments</a></li>
          <li><a>Transfers</a></li>
          <li><a>Balance</a></li>
        </ul>
      </aside>

      <!-- DEBUGGING -->
      <!-- {{ user }} -->

      <!-- BACK OFFICE TABS AND FORMS -->
      <div class="column is-8" 
        v-if="user.isLoggedin"
        >
        <p class="subtitle has-text-grey">
          {{ getText('hello') }}
          {{ user.infos.name }}
        </p>

      </div>

    </div>

  </section>

</template>

<script>
import { mapState } from 'vuex'

import FormLogin from '../FormLogin.vue';

export default {
  components: {
    FormLogin
  },
  props: [
    'logo', 
    'brand'
  ],
  data: function () {
    return {
      backOfficeMenu: [
        {'global' : {
          'title' : 'global settings',
          'tabs'  : [
            { 'title' : 'general' },
            { 'title' : 'site identity' },
            { 'title' : 'meta' },
            { 'title' : 'traffic' },
          ]
        }},
        {'endpoints' : {
          'title' : 'API',
          'tabs'  : [
            { 'title' : 'datasets' },
            { 'title' : 'user' },
          ]
        }},
        {'styles' : {
          'title' : 'styles',
          'tabs'  : [
            { 'title' : 'app colors' },
            { 'title' : 'app typo' },
            { 'title' : 'app typo colors' },
            { 'title' : 'app banners' },
            { 'title' : 'app default images sets' },
          ]
        }},
        {'navbar' : {
          'title' : 'navbar',
          'tabs'  : [
            { 'title' : 'logo' },
            { 'title' : 'links' },
            { 'title' : 'call_button' },
          ]
        }},
        {'footer' : {
          'title' : 'footer',
          'tabs'  : [
            { 'title' : 'settings' },
            { 'title' : 'contents' },
            { 'title' : 'ui' },
            { 'title' : 'links' },
          ]
        }},
        {'routes' : {
          'title' : 'routes',
          'tabs'  : [
            { 'title' : 'home page' },
            { 'title' : 'datasets pages' },
            { 'title' : 'static pages' },
          ]
        }},
        {'users' : {
          'title' : 'users',
          'tabs'  : [
            { 'title' : 'users' },
            { 'title' : 'teams' },
          ]
        }}
      ],
    }
  },
  computed: {
    ...mapState({
      user: 'user'
    }),
    isUserAdmin () {
      return this.$store.getters.getCheckUserRole('admin')
    },
    isUserStaff () {
      return this.$store.getters.getCheckUserRole('staff')
    },
  },

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
