<template>
  <footer class="footer">
    <div class="container">
      <div class="columns">


        <div class="column is-3 is-offset-1"
          v-for="(block_pos, index) in ['block_center_left', 'block_center_right','block_right']"
          :key="index"
          >

          <h3 class="has-text-left has-text-primary"> 
            {{ translate(footerLinks(block_pos), 'title_block') }}
          </h3>

          <template 
            v-if="isVisible( footerLinks(block_pos) )"
            >
            <ul>
              <li v-for="(link, index) in footerLinks(block_pos)['links']">
                <a :href="link.link_to" target="_blank"> 
                  {{ translate(link, 'link_text') }}
                </a>
              </li>
            </ul>
          </template>

          <!-- ADD SOCIAL AT THE END -->
          <template v-if="block_pos === 'block_right' ">
            
            <br>
            <div class="content">
              <template  
                v-for="icon in appSocials"
                >
                <!-- {{ icon }} -->
                <a
                  class="button is-primary" 
                  :href="icon.url" >
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

            <!-- {{ appSocials }} -->


        <!-- <div class="column is-4">

          <h2 class="has-text-primary">Newsletter</h2>


            <h2 class="has-text-primary"><a href="/contact">Contactez-nous</a></h2>

          <h2 class="has-text-primary">Suivez-nous</h2>



          <div class="content">
            
            <a 	id="btn_cis_facebook"
              class="button is-primary" 
              href="https://www.facebook.com/TouteslesInnoSo/" >
              <span class="icon">
                <i class="fab fa-lg fa-facebook"></i>
              </span>
            </a>
            
            &nbsp;&nbsp;&nbsp;

            <a 	id="btn_cis_twitter"
              class="button is-primary" 
              href="https://twitter.com/touteslesinnoso" >
              <span class="icon ">
                <i class="fab fa-lg fa-twitter"></i>
              </span>
            </a>
            
          </div>

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

    isVisible(block) {
      console.log("block : ", block)
      return block.is_visible
    },

    translate( textsToTranslate, listField ) {
      let listTexts = textsToTranslate[listField]
      return this.$store.getters.getTranslation({ texts : listTexts })
    }
  }

}
</script>
