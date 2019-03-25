<style lang="scss" scoped>
  @import '../../styles/apiviz-colors.scss';
  .router-link-active{
    // text-decoration: underline;
    color: $apiviz-primary ;
  }
  .is-underlined{
    border-bottom: solid;
    border-color: $apiviz-primary;
  }
  .navbar-dropdown {
    z-index: 100;
  }
</style>

<template>
  <div id="navbar-main" class="navbar-menu">
    <div class="navbar-end">


      <!-- NAVBAR ITEMS -->
      <template
        v-for="(link, index) in this.NavbarLinks.extra_buttons"
        >
        <router-link
          v-if="link.link_type == 'link' && link.is_visible == true"
          :key="index"
          :class="`navbar-item ${ link.has_dropdown ? 'has-dropdown is-hoverable' : '' }  `"
          :to="link.link_to"
          >

          <!-- MAIN LINK -->
          <div 
            :class="`${ link.has_dropdown ? 'navbar-link' : '' } ${ isItemActive(link) ? 'has-text-primary' : '' }`"
            >
            <span :class="`${ isItemActive(link) ? 'is-underlined' : '' }`">
              {{ translate(link, 'link_text' ) }}
            </span>
          </div>

          <!-- DROPDOWNS -->
          <div
            v-if="link.has_dropdown"
            class="navbar-dropdown"
            >

            <div 
              v-for="(sublink, i) in link.dropdowns"
              :key="i"
              >

              <div
                v-if="!sublink.is_divider"
                >

                <a 
                  v-if="sublink.is_external_link"
                  :class="`navbar-item ${ isActiveLink(sublink.link_to) ? 'has-text-white has-background-primary' : '' }`"
                  :href="sublink.link_to"
                  >
                  {{ translate(sublink, 'link_text' ) }}
                </a>

                <router-link
                  v-if="!sublink.is_external_link"
                  :class="`navbar-item ${ isActiveLink(sublink.link_to) ? 'has-text-white has-background-primary' : '' }`"
                  :to="sublink.link_to"
                  >
                  {{ translate(sublink, 'link_text' ) }}
                </router-link>

              </div>

              <hr 
                v-if="sublink.is_divider"
                class="navbar-divider"
              >

            </div>
          
          </div>

        </router-link>
      </template>


      <!-- BUTTONS LINKS -->
      <div class="buttons">

        <template
          v-for="(link, index) in this.NavbarLinks.extra_buttons"
          >

          <router-link
            v-if="!link.has_dropdown && !link.is_external_link && link.link_type == 'button' && link.is_visible == true"
            :key="index"
            :class="`navbar-item button is-primary is-outlined is-small`"
            :to="link.link_to"
            >
            <span>{{ translate( link,'link_text' ) }}</span>
          </router-link>

          <a
            v-if="!link.has_dropdown && link.is_external_link && link.link_type == 'button' && link.is_visible == true"
            :key="index"
            :class="`navbar-item button is-primary is-outlined is-small`"
            :href="link.link_to"
            target="_blank"
            >
            <span>{{ translate( link,'link_text' ) }}</span>
          </a>

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
export default {
  props : [
    'NavbarLinks',
    'localRouteConfig'
    // 'currentDatasetURI'
  ],
  beforeMount: function () {
    // console.log("// NavbarLinks : ", this.NavbarLinks)
    // console.log("// currentDatasetURI : ", this.currentDatasetURI)
  },
  computed : {
  },
  methods : {
    // isCurrentRoute(linkTo){
    //   console.log("\n...... linkTo : ", linkTo)
    //   let path = this.$router.currentRoute.path
    //   console.log("...... path : ", path)
    //   return ( path === linkTo ) ? true : false
    // },
    isActiveLink(link_to){
      const currentRoute = this.$route.path
      // console.log("isActiveLink / currentRoute : ", currentRoute)
      const routeURL = this.localRouteConfig.urls
      // console.log("isActiveLink / routeURL : ", routeURL)
      return link_to === currentRoute || routeURL.indexOf(link_to) != -1
    },
    isItemActive(link){
      const currentRoute = this.$route.path
      const isLinkToRoute = this.isActiveLink(link.link_to)
      let isSublinkRoute = false
      if (link.has_dropdown){
        const linkDropdowns = link.dropdowns
        const linkDropdownsList = linkDropdowns.map(e => e.link_to);
        isSublinkRoute = linkDropdownsList.indexOf(currentRoute) != -1
        console.log("isItemActive / linkDropdownsList : ", linkDropdownsList)
      }
      return isLinkToRoute || isSublinkRoute
    },
    translate( textsToTranslate, listField ) {
      // console.log("textsToTranslate : ", textsToTranslate )
      let listTexts = textsToTranslate.link_text
      // console.log("listTexts : ", listTexts )
      return this.$store.getters.getTranslation({ texts : listTexts })
    }
  }
}
</script>

