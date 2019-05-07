<template>

  <!-- cf : https://codepen.io/andreich1980/pen/OmobJQ -->
  <section class="main-content skip-navbar columns is-fullheight">
    
    <!-- SIDE MENU -->
    <aside class="column is-3 is-narrow-mobile is-fullheight section">
      
      <p 
        v-if="user.isLoggedin"
        class="menu-label is-hidden-touch"
        >
        PREFERENCES
      </p>
      <ul 
        v-if="user.isLoggedin"
        class="menu-list">
        <li 
          v-for="uMenu in userMenu"
          >
          <a 
            href="#" 
            :class="`${uMenu == activeMenu ? 'is-active' : ''}`"
            @click="setActiveMenu(uMenu)"
            >
            <!-- <span class="icon">
              <i :class="uMenu.icon"></i>
            </span>  -->
            {{ uMenu }}
          </a>
        </li>
      </ul>

      <p 
        class="menu-label is-hidden-touch"
        >
        APP SETTINGS
      </p>

      <!-- MENUS -->
      <ul class="menu-list">
        <li 
          v-for="menu in backOfficeMenu"
          >
          <a 
            href="#" 
            :class="`${menu.config_field == activeMenu ? 'is-active' : ''}`"
            @click="setActiveMenu(menu.config_field)"
            >
            <span class="icon">
              <i :class="menu.icon"></i>
            </span> 
            {{ menu.title }}
          </a>
        </li>
      </ul>

    </aside>

    <div class="container column is-9">
      <div class="section">

        <!-- TABS -->
        <div class="tabs is-centered">
          <ul>
            <li
              v-for="tab in menuTabs(activeMenu)" 
              :class="`${tab.tab_code == activeTab ? 'is-active' : ''}`"
              >
              <a
                @click="setActiveTab(tab.tab_code)"  
                >
                {{ tab.title }}
              </a>
            </li>
          </ul>
        </div>

        <!-- CONTENTS -->
        <!-- <div class="card">
          <div class="card-header"><p class="card-header-title">Header</p></div>
          <div class="card-content"><div class="content">Content</div></div>
        </div>
        <br /> -->
        
        <template
          v-for="fieldConfig in tabFields()"
          >

          <BackOfficeForm
            :fieldConfig="fieldConfig"
            :config="config[activeMenu]"
            >
          </BackOfficeForm>

          <br />
        </template>

      </div>
    </div>
    
  </section>

</template>

<script>
import { mapState } from 'vuex'

import BackOfficeForm from '../backoffice/BackOfficeForm.vue';

export default {
  components: {
    BackOfficeForm
  },
  props: [
    'logo', 
    'brand'
  ],
  data: function () {
    return {
      
      activeMenu : 'global',
      activeTab : 'gl_general',

      userMenu : [
        'infos',
        'password'
      ],

      backOfficeMenu: [

        { 'config_field' : 'global', 
          'title' : 'global settings',
          "is_divider" : false,
          'icon' : 'fas fa-cog',
          'tabs'  : [
            { 'tab_code' : 'gl_general' , 
              'title' : 'general',
              'fields' : [
                { 'field' : 'app_title',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'content', 'type' : 'text', 'list' : false}
                  ], 
                },
                { 'field' : 'app_description',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'content', 'type' : 'text-lang', 'list' : false}
                  ], 
                },
                { 'field' : 'app_languages',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'locale', 'type' : 'text', 'list' : false}, 
                    {'subfield' : 'languages', 'type' : 'text', 'list' : true}
                  ], 
                },
              ]
            },
            { 'tab_code' : 'gl_identity', 
              'title' : 'site identity',
              'fields' : [
                { 'field' : 'app_logo',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'url', 'type' : 'text', 'list' : false}
                  ], 
                },
                { 'field' : 'app_favicon',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'url', 'type' : 'text', 'list' : false}
                  ], 
                },
                { 'field' : 'app_welcome',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'content', 'type' : 'text-lang', 'list' : false}
                  ], 
                },
                { 'field' : 'app_pitch',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'content', 'type' : 'text-lang', 'list' : false}
                  ], 
                }
              ]
            },
            { 'tab_code' : 'gl_meta', 
              'title' : 'meta',
              'fields' : [
                { 'field' : 'app_keywords',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'content', 'type' : 'text', 'list' : false}
                  ], 
                },
                { 'field' : 'app_code',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'url', 'type' : 'text', 'list' : false},
                    {'subfield' : 'content', 'type' : 'text-lang', 'list' : false}
                  ], 
                },
              ]
            },
            { 'tab_code' : 'gl_seo', 
              'title' : 'seo',
              'fields' : [
                { 'field' : 'app_analytics',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'content', 'type' : 'text', 'list' : false},
                    {'subfield' : 'url', 'type' : 'text', 'list' : false},
                    {'subfield' : 'activated', 'type' : 'bool', 'list' : false}
                  ], 
                },
                { 'field' : 'app_support',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'content', 'type' : 'text', 'list' : false},
                    {'subfield' : 'url', 'type' : 'text', 'list' : false},
                    {'subfield' : 'activated', 'type' : 'bool', 'list' : false}
                  ], 
                },
                { 'field' : 'app_indexing',
                  'type' : 'bloc', 
                  'edit' : [
                    {'subfield' : 'content', 'type' : 'text', 'list' : false},
                    {'subfield' : 'activated', 'type' : 'bool', 'list' : false}
                  ], 
                },
              ]
            },
            { 'tab_code' : 'gl_lang', 
              'title' : 'international',
              'fields' : [
                {
                  'field' : 'app_basic_dict',
                  'type' : 'bloc', 
                  'edit' : ['content'], 
                }
              ]
            },
          ]
        },

        { 'config_field' : 'navbar',
          'title' : 'navbar',
          "is_divider" : false,
          'icon' : 'fas fa-cog',
          'tabs'  : [
            { 
              'tab_code' : 'na_logo', 
              'title' : 'logo' 
            },
            { 
              'tab_code' : 'na_links', 
              'title' : 'links' 
            },
            { 
              'tab_code' : 'na_btn'  , 
              'title' : 'call_button' 
            },
          ]
        },
  
        { 'config_field' : 'routes',
          'title' : 'routes',
          "is_divider" : false,
          'icon' : 'fas fa-cog',
          'tabs'  : [
            { 
              'tab_code' : 'ro_home', 
              'title' : 'home page' 
            },
            { 
              'tab_code' : 'ro_data', 
              'title' : 'datasets pages' 
            },
            { 
              'tab_code' : 'ro_statics', 
              'title' : 'static pages' 
            },
          ]
        },
        
        { 'config_field' : 'endpoints',
          'title' : 'API endpoints',
          "is_divider" : false,
          'icon' : 'fas fa-cog',
          'tabs'  : [
            { 
              'tab_code' : 'ep_data', 
              'title' : 'datasets' 
            },
            { 
              'tab_code' : 'ep_user', 
              'title' : 'user' 
            },
          ]
        },

        { 'config_field' : 'footer',
          'title' : 'footer',
          "is_divider" : false,
          'icon' : 'fas fa-cog',
          'tabs'  : [
            { 
              'tab_code' : 'fo_settings', 
              'title' : 'settings' 
            },
            { 
              'tab_code' : 'fo_contents', 
              'title' : 'contents' 
            },
            { 
              'tab_code' : 'fo_ui', 
              'title' : 'ui' 
            },
            { 
              'tab_code' : 'fo_links', 
              'title' : 'links' 
            },
          ]
        },

        { 'config_field' : 'socials',
          'title' : 'socials',
          "is_divider" : false,
          'icon' : 'fas fa-cog',
          'tabs'  : [
            { 
              'tab_code' : 'so_settings', 
              'title' : 'settings' 
            },
          ]
        },

        { 'config_field' : 'styles',
          'title' : 'styles',
          "is_divider" : false,
          'icon' : 'fas fa-cog',
          'tabs'  : [
            { 
              'tab_code' : 'st_colors', 
              'title' : 'app colors' 
            },
            { 
              'tab_code' : 'st_typo', 
              'title' : 'app typo' 
            },
            { 
              'tab_code' : 'st_typocolors', 
              'title' : 'app typo colors' 
            },
            { 
              'tab_code' : 'st_banners', 
              'title' : 'app banners' 
            },
            { 
              'tab_code' : 'st_images', 
              'title' : 'app default images sets' 
            },
          ]
        },

        { 'config_field' : 'users',
          'title' : 'users',
          "is_divider" : false,
          'icon' : 'fas fa-cog',
          'tabs'  : [
            { 
              'tab_code' : 'us_users', 
              'title' : 'users',
              'fields' : [

              ]
            },
            { 
              'tab_code' : 'us_teams', 
              'title' : 'teams',
              'fields' : [

              ]
            },
          ]
        }

      ],
    }
  },
  computed: {
    ...mapState({
      user: 'user',
      config: 'config'
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

    getMenuConfig(menuConfigField) {
      let menuConfig = this.backOfficeMenu.find(function(menu) {
        return menu.config_field === menuConfigField
      });
      return menuConfig
    },

    menuTabs(menuConfigField) {
      let menuConfig = this.getMenuConfig(menuConfigField)
      return menuConfig.tabs
    },

    getTabConfig() {
      let menuTabs = this.menuTabs(this.activeMenu)
      let activeTab = this.activeTab
      // console.log('menuTabs : ', menuTabs)
      let tabConfig = menuTabs.find(function(tab) {
        return tab.tab_code === activeTab
      });
      // console.log('tabConfig : ', tabConfig)
      return tabConfig
    },

    tabFields() {
      let tabConfig = this.getTabConfig()
      return tabConfig.fields
    },

    setActiveMenu(menuConfigField) {
      this.activeMenu = menuConfigField
      let menuConfig = this.getMenuConfig(menuConfigField)
      this.activeTab = menuConfig.tabs[0]['tab_code']
    },

    setActiveTab(tabCode) {
      this.activeTab = tabCode
    },

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
