<template>

    <!-- TABS -->
    <div class="tabs is-centered">
      <ul>
        <li
          v-for="(tab, index) in tabsConfig" 
          :key="index"
          :class="`${tab.tab_code == activeTab ? 'is-active' : ''}`"
          >
          <router-link
            :to="tab.link_to" 
            >
            {{ tab.link_text }}
          </router-link>
        </li>
      </ul>
    </div>

</template>

<script>

export default {
  components: {
  },

  props: [
    'tabsConfig',
    'localRouteConfig',
  ],

  data: function () {
    return {
      activeTab : '',
    }
  },

  methods : {
    getText(textCode) {
      return this.$store.getters.defaultText({txt:textCode})
    },
  }

}
</script>

<style>

</style>