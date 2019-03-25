<template>
  <div>

    <main v-if="displayableItem">
      
      <div class="container">

        <a class="back" @click="goBack">
          <!-- <img src="/static/icons/icon_arrow1.svg"> -->
          <span class="icon">
            <i class="fas fa-arrow-left"></i>
          </span>
          <span>
            <!-- Retour aux résultats de recherche -->
            {{ backToResults }}
          </span>
        </a>


        <!-- DEBUGGING  -->
        <!-- {{ displayableItem }} -->


        <div class="columns">
          
          <!-- //// COLUMN LEFT //// -->

          <div class="column is-5 is-offset-1">
            <div class="description">

              <!-- BLOCK TITLE -->
              <h1 class="title is-3">
                <!-- {{projectFormatted.title}} -->
                 {{ matchProjectWithConfig('block_title')}}
              </h1>

              <!-- BLOCK ADDRESS -->
              <p
              >
                <!-- v-if="projectFormatted.address" -->
                <span class="icon">
                  <img class="image is-16x16" src="/static/icons/icon_pin.svg">
                </span>
                <!-- {{projectFormatted.address}} -->
                {{ matchProjectWithConfig('block_address')}}
                <!-- {{ matchProjectWithConfig('block_cp')}} -->
              </p>

              <!-- BLOCK ABSTRACT -->
              <p>
                <!-- {{projectFormatted.description}} -->
                {{ matchProjectWithConfig('block_abstract')}}
              </p>
              
              <!-- BLOCK PARTNERS -->
              <!-- <div v-if="projectFormatted.projectPartners">
                  <h2 class="title is-4">Structure</h2>
                  <p>{{projectFormatted.projectPartners}}</p>
              </div> -->

              <div class="columns">

                <!-- BLOCK WEBSITE -->
                <div class="column is-5 is-offset-1 link">
                  <a
                    :class="matchProjectWithConfig('block_wesite') === noData ? 'disabled has-text-grey' : '' "
                    v-if="matchProjectWithConfig('block_wesite')"
                    :href="matchProjectWithConfig('block_wesite') === noData ? '' : matchProjectWithConfig('block_wesite') "
                    target="_blank">
                    {{ seeWebsite }}
                  </a>
                </div>
                
                <!-- BLOCK CONTACT -->
                <div class="column is-5 is-offset-1 link">
                  <a
                    class=""
                    :class="matchProjectWithConfig('block_contact') === noData ? 'disabled has-text-grey' : '' "
                    v-if="matchProjectWithConfig('block_contact')"
                    :href="matchProjectWithConfig('block_wesite') === noData ? '' :'mailto:' + matchProjectWithConfig('block_contact') "
                    target="_blank">
                    {{ seeContact }}
                  </a>
                </div>
              </div>

            </div>

            <div class="added">
              <div class="columns">

                <div class="column is-12">
                  
                  <!-- BLOCK TAGS -->
                  <div>
                    <span class="has-text-weight-semibold">
                      {{ servicesData }} : <br><br>
                    </span>
                    <span>
                      {{ matchProjectWithConfig('block_left_bottom_1')}}
                    </span>
                  </div>

                </div>

              </div>
            </div>

          </div>



          <!-- //// COLUMN RIGHT //// -->

          <div class="column is-5">

            <!-- BLOCK MAIN ILLUSTRATION -->
            <a :href="matchProjectWithConfig('block_wesite')" target="_blank">
              <img
                class="illustration"
                :src="itemImage('card_img_main')"
                :alt="matchProjectWithConfig('block_title')"
              />
                <!-- :src="projectFormatted.image" -->
            </a>


            <div class="added">
              <div class="columns">

                <div class="column is-12">
                  
                  <!-- BLOCK SOURCE -->
                  <div>
                    <!-- <span class="icon is-small">
                      <i class="fas fa-info-circle"></i>
                    </span> &nbsp; -->
                    <span class="has-text-weight-semibold">
                      <!-- <img src="/static/icons/icon_link.svg"> -->
                      {{ sourceData }} : 
                    </span>
                    <span>
                      {{ matchProjectWithConfig('block_src')}}
                    </span>
                  </div>

                </div>

              </div>
            </div>



            <div class="added">
              <div class="columns">

                <div class="column is-12">
                  
                  <!-- BLOCK RIGHT BOTTOM 1 / INFOS -->
                  <div>
                    <span class="has-text-weight-semibold">
                      {{ infosData }} : <br><br>
                    </span>
                  </div>

                  <div>
                    <span class="icon is-small">
                      <i class="fas fa-angle-right"></i>
                    </span>
                    <span>
                      {{ infosTel }} : 
                      {{ matchProjectWithConfig('block_tel')}} <br>
                    </span>
                  </div>

                  <div>
                    <span class="icon is-small">
                      <i class="fas fa-angle-right"></i>
                    </span>
                    <span>
                      {{ infosOpen }} : <br>
                      {{ matchProjectWithConfig('block_open_infos')}} <br>
                    </span>
                  </div>

                  <div>
                    <span class="icon is-small">
                      <i class="fas fa-angle-right"></i>
                    </span>
                    <span>
                      {{ infosMore }} : 
                      {{ matchProjectWithConfig('block_right_bottom_1')}}
                    </span>
                  </div>

                </div>

              </div>
            </div>



          </div>

        </div>
      </div>
    </main>

    <NotFoundError v-if="isError"/>

    <br>

  </div>
</template>


<script>
export default {
  computed: {
    ...mapState({
        user: 'user'
    })
  },
}
</script>


<script>
import {mapState} from 'vuex'

import NotFoundError from './NotFoundError.vue';

import {getItemById} from '../utils.js';

export default {
  name: 'DynamicDetail',
  components: {
    NotFoundError,
  },

  props: [
    'routeConfig',
    'endPointConfig',
    // 'logo',
    // 'brand'
  ],

  data: () => {
    return   {
      displayableItem : null,
      contentFields : null,
      isError: false
    }
  },

  beforeMount: function () {
    // console.log("\n - - DynamicDetail / beforeMount ... ")
    this.contentFields = this.routeConfig.contents_fields

  },

  mounted(){
    // hack to scroll top because vue-router scrollBehavior thing doesn't seem to work on Firefox on Linux at least
    // console.log(" - - DynamicDetail / mounted... ")
    const int = setInterval(() => {
      if(window.pageYOffset < 50){
        clearInterval(int)
      }
      else{
        window.scrollTo(0, 0)
      }
    }, 100);

    getItemById(this.$route.query.id,this.$store.state.search.endpoint)
    .then(item => {
      // this.$store.commit('setDisplayedProject', {item})
      // console.log(" - - DynamicDetail / item : \n ", item)
      this.displayableItem = item
    })
    .catch(function(err) { this.isError = true ; console.error('item route error', err) })
  },

  computed: {
    // ...mapState({
    //   project: 'displayedProject',
    // }),
    ...mapState({
        user: 'user'
    }),

    // default texts
    backToResults() {
      return this.$store.getters.defaultText({txt:'back_to_results'})
    },

    noData() {
      return this.$store.getters.defaultText({txt:'no_data'})
    },

    seeWebsite() {
      return this.$store.getters.defaultText({txt:'see_website'})
    },
    seeContact() {
      return this.$store.getters.defaultText({txt:'see_contact'})
    },
    shareLink() {
      return this.$store.getters.defaultText({txt:'share_link'})
    },
    sourceData() {
      return this.$store.getters.defaultText({txt:'source'})
    },
    infosData() {
      return this.$store.getters.defaultText({txt:'infos'})
    },
    infosTel() {
      return this.$store.getters.defaultText({txt:'tel'})
    },
    infosOpen() {
      return this.$store.getters.defaultText({txt:'open_infos'})
    },
    infosMore() {
      return this.$store.getters.defaultText({txt:'more_infos'})
    },
    servicesData() {
      return this.$store.getters.defaultText({txt:'services'})
    },
    noAbstractText() {
      return this.$store.getters.defaultText({txt:'no_abstract'})
    },
    noInfos() {
      return this.$store.getters.defaultText({txt:'no_info'})
    },
    noAddress() {
      return this.$store.getters.defaultText({txt:'no_address'})
    },
    // projectFormatted(){
    //   if (!this.project) {
    //     return {
    //       tags: [],
    //       image: '',
    //       logo_url: '',
    //       title: '',
    //       address: '',
    //       description: '',
    //       projectPartners: '',
    //       website: '',
    //       pageAtSourcer: ''
    //     }
    //   } else {
    //     // return this.$store.getters.getProjectConfigUniform(this.project)
    //     return this.project
    //   }
    // },



  },

  methods : {

    itemImage(fieldBlock){
      return this.$store.getters.getImageUrl({item: this.displayableItem, position: fieldBlock})
      // return this.item
    },
    matchProjectWithConfig(fieldBlock) {
      const contentField = this.contentFields.find(f=> f.position == fieldBlock)
      // console.log("contentField : ", contentField)
      if (contentField){
        const field = contentField.field
        let content = this.displayableItem[field]
        // console.log("content : ", content)
        if ( content && content !== "None" && content !== "" ){
          return content
        } else {
          // console.log("content is None | null ...")
          // console.log("this.noData : ", this.noData)
          return this.noData
        }
      } else {
        return undefined
      }

    },

    projectId() {
      return this.matchProjectWithConfig('block_id')
    },

    projectAbstract() {
      let fullAbstract = this.matchProjectWithConfig('block_abstract')
      fullAbstract = ( fullAbstract == null ) ? this.noAbstractText : fullAbstract
      const tail = fullAbstract.length > MAX_SUMMARY_LENGTH ? '...' : '';
      return fullAbstract.slice(0, MAX_SUMMARY_LENGTH) + tail
    },
    projectInfo(field) {
      let fullInfo = this.matchProjectWithConfig(field)
      fullInfo = ( fullInfo == null ) ? this.noInfos : fullInfo
      return fullInfo
    },
    projectAddress() {
      let fullAddress = this.matchProjectWithConfig('block_address')
      // console.log('fullAddress : ', fullAddress)
      let address = ( fullAddress || fullAddress !== 'None' ) ?  fullAddress : this.noAddress
      return address
    },


    goBack(e){
        e.preventDefault()
        this.$router.back()
    }
  },

}
</script>


<style lang="scss" scoped>
  @import '../../styles/apiviz-colors.scss';
  @import '../../styles/apiviz-misc.scss';

  main{
    // background-color: $apiviz-blue-deep;
    background-color: $apiviz-grey-background;
    margin-top: $apiviz-navbar-height;
    height: 100%;
    padding-bottom: 3em;
    

  }

  a.disabled {
    pointer-events: none;
    border-bottom: none !important ;
    cursor: default;
  }

  a.back{
    padding: 1em 0;
    display: block;

    color: $apiviz-text-color;
    // color: white ;

    img, .icon{
      height: 1.5em;
      transform: translateY(0.6em);
    }

    span{
      margin-left: 1em;
      // color: white ;
    }
  }

  .columns{
      margin-top: 0;
  }

  .illustration{
    width: 100%;
    margin-bottom: 1em;
  }

  .description, .added{
    // background-color: $apiviz-blue-deep;
    background-color: white;
    // color: white;
    padding: 1em;
    margin-bottom: 1em;
  }

  .description{
    h1{
        font-weight: bold;
    }

    p{
        margin-bottom: 1em;
    }

    a{
        color: $apiviz-primary;
        border-bottom: 1px solid $apiviz-primary;
    }
  }


  .added {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: left;

    .link-at-sourcer img{
        max-height: 1.1em;
        transform: translateY(0.2em);
    }

    img{
        height:auto;
    }

    .no-left-padding {
        padding-left: 0em;
    }
    .is-vertical-centered {
        // padding-left: 1em;
        display: flex;
        align-items: center;
    }

    .logo {
        // max-width: 175px;
        height: auto;
        width:100%;
    }

    a{
        color: $apiviz-primary;
        font-weight: bold;
    }
  }

  .content{
    h2{
        font-weight: bold;
    }

    .tag{
        background-color: #767676;
        color: white;
        margin-right: 1em;
        margin-bottom: 0.5em;
    }
  }
</style>
