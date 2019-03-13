<template>
  <div id="navbar-main" class="navbar-menu">
    <div class="navbar-end">

      <!-- <div class="navbar-item selected">
        <a href="/recherche">Moteur de recherche</a>
      </div> -->

      <!-- {{ linksOptions }} -->

      <template 
        v-for="(link, index) in this.NavbarLinks.extra_buttons"
        >
        <router-link 
          v-if="link.link_type == 'link' && link.is_visible == true"
          :key="index"
          class="navbar-item" 
          :to="link.link_to"
          >
            <span>{{ translate(link, 'link_text' ) }}</span>
        </router-link>
      </template>

      <div class="buttons"> 
        <template 
          v-for="(link, index) in this.NavbarLinks.extra_buttons"
          >
          <router-link 
            :key="index"
            v-if="link.link_type == 'button' && link.is_visible == true"
            class="navbar-item button is-primary is-outlined is-small" 
            :to="link.link_to"
            >
              <span>{{ translate( link,'link_text' ) }}</span>
          </router-link>

        </template>
      </div>

      <!-- <div class="navbar-item">
        <a href="/le-projet">Projet</a>
      </div>

      <div class="navbar-item">
        <a href="/qui-sommes-nous">Qui sommes-nous ?</a>
      </div>

      <div class="navbar-item">
        <a href="/nous-rejoindre">Nous rejoindre</a>
      </div> -->

      <!-- <div class="navbar-item">
        <span lang="fr">FR</span>&nbsp;/&nbsp;<a lang="en" href="/en">EN</a>
      </div> -->

    </div>
  </div>
</template>

<script>

// import { textFromLocale } from '../utilsApiviz.js';

export default {
  props : [
    'NavbarLinks'
  ],
  beforeMount: function () {
    // console.log("// NavbarLinks : ", this.NavbarLinks)
  },

  methods : {
    translate( textsToTranslate, listField ) {
      // console.log("textsToTranslate : ", textsToTranslate )
      let listTexts = textsToTranslate.link_text
      // console.log("listTexts : ", listTexts )
      return this.$store.getters.getTranslation({ texts : listTexts })
    }
  }
}
</script>
