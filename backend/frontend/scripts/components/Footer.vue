<template>
  <footer class="footer">
    <div class="container">
      <div class="columns">


        <div 
          v-bind:class="footerClass(block_pos)"
          v-for="(block_pos, index) in getActiveColumns()"
          v-if="isVisible( footerLinks(block_pos) )"
          :key="index"
          >

          <template 
            v-if="isVisible( footerLinks(block_pos) )"
            >
            <h3 class="is-left has-text-primary"> 
              {{ translate(footerLinks(block_pos), 'title_block') }}
            </h3>

            <ul>
              <li 
                v-for="(link, index) in footerLinks(block_pos)['links']"
                :key="index"
              >
                <a :href="link.link_to" target="_blank"> 
                  {{ translate(link, 'link_text') }}
                </a>
              </li>
            </ul>
          </template>

          <!-- ADD SOCIAL AT THE END -->
          <template v-if="block_pos === getLastBlock() ">
            
            <br>
            <div class="content">
              <template  
                  v-for="(icon, index) in appSocials"
                >
                <!-- {{ icon }} -->
                <a
                  class="button is-primary" 
                  :key="index"
                  :href="icon.url" 
                >
                  <span class="icon">
                    <i 
                      :class="icon.icon_class"
                    ></i>
                  </span>
                </a>
                &nbsp;&nbsp;&nbsp;
              </template>
            </div>

          </template>

        </div>





        <!-- <div class="column is-4">

          <h2 class="has-text-primary"> 
          </h2>
          
          <ul>

            <li>
              <a href="https://github.com/co-demos/ApiViz" target="_blank"> 
                Code source 
              </a>
            </li>
            <li>
              <a href="/login">Login</a>
            </li>
            <li>
              <a href="/admin">Admin</a>
            </li>

          </ul>

        </div> -->



      </div>
    </div>
  </footer>
</template>

<script>
// import MailchimpSubscribe from './MailchimpSubscribe.vue'

export default {

  components: {
    // MailchimpSubscribe
  },

  props : [
    'footerConfig',
    'appSocials'
  ],

  computed : {
    footerUI() {
      return this.footerConfig.ui_options
    },
  },

  methods : {

    footerLinks(position) {
      let allLinks = this.footerConfig.links_options
      let blockLinks = allLinks[position]
      return blockLinks
    },
    footerContents(position) {
      let allContents = this.footerConfig.contents_fields
      let blockContents = allContents[position]
      return blockContents
    },
    footerClass(block_pos) {
        //console.log(block_pos, this.footerConfig.active_columns[0])
        //console.log(this.footerConfig)
        let num_of_cols = this.footerConfig.active_columns.length
        let class_ = "column"
        //console.log(num_of_cols)
        if (num_of_cols === 0){
            // Should not happen, but still
            class_ = class_ + " is-12"
        } else if(num_of_cols === 1){
            class_ = class_ + " is-6"
            if (block_pos === this.footerConfig.active_columns[0]){
                class_ = class_ + " is-offset-3"
            }
        } else if(num_of_cols === 2){
            class_ = class_ + " is-3"
            if (block_pos === this.footerConfig.active_columns[0]){
                class_ = class_ + " is-offset-3"
            }
        } else if(num_of_cols === 3){
            class_ = class_ + " is-3"
            if (block_pos === this.footerConfig.active_columns[0]){
                class_ = class_ + " is-offset-1"
            }
        } else if(num_of_cols === 4){
            class_ = class_ + " is-3"
        }

        return class_
    },
    
    getActiveColumns() {
        return this.footerConfig.active_columns
    },

    getLastBlock(){
        console.log(this.footerConfig.active_columns.slice(-1).pop())
        return this.footerConfig.active_columns.slice(-1).pop()
    },
    isVisible(block) {
      // console.log("block : ", block, block.is_visible)
      return block.is_visible
    },

    translate( textsToTranslate, listField ) {
      let listTexts = textsToTranslate[listField]
      return this.$store.getters.getTranslation({ texts : listTexts })
    }
  }

}
</script>
