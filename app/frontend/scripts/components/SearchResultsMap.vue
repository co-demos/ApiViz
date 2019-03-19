<template>
  <div class="map">
    <div class="count-and-tabs-container">
      <div class="container">

        <CISSearchResultsCountAndTabs 
          :view="VIEW_MAP" 
          :open="!!highlightedItem"
          >
          
          <!-- HIGHLIGHTED ITEM  -->
          <div 
            class="highlighted-project" 
            v-if="showCard" 
            slot="project"
            >
            
            <!-- BUTTON TO CLOSE PREVIEW -->
            <button 
              v-show="itemLoaded"
              class="button close" 
              @click="showCard = false"
              >
              <!-- @click="highlightItem(undefined)" -->
              <span class="icon is-small">
                <i class="fas fa-times"></i>
              </span>
            </button>
            
            <!-- PROJECT CARD -->
            <div class="card">

              <div 
                class="columns is-mobile is-vcentered"
                v-show="!itemLoaded"
                >
                <div class="column is-12 has-text-centered has-text-primary"
                  >
                  <span class="icon app-loader">
                    <i class="fas fa-spinner fa-pulse fa-3x"></i>
                  </span>
                </div>
              </div>

              <ProjectCard 
                v-if="itemLoaded"
                :item="highlightedItem"
                :contentFields="contentFields"
                >
              </ProjectCard>


              <!-- BLOCK IMAGE -->
              <!-- <router-link 
                :to="`/project/${highlightedItem.id}`" 
                class="card-image"
              >
                <img 
                  :src="highlightedItem.image" 
                  :alt="highlightedItem.title">
              </router-link> -->
              
              <!-- BLOCK ADDRESS -->
              <!-- <div class="card-content" v-if="highlightedItem.address.trim().length > 1"> -->
                <!-- 
                <span class="icon has-text-light">
                  <i class="fas fa-location-arrow"></i>
                </span> -->
                <!-- <span class="icon">
                  <img class="image is-16x16" src="/static/icons/icon_pin.svg">
                </span>
                <span class="subtitle is-6">
                  {{ highlightedItem.address.slice(0, 100) }}
                </span>
              </div> -->

              <!-- BLOCK LINK -->
              <!-- <router-link 
                :to="`/project/${highlightedItem.id}`" 
                class="card-content"
                >
                <h1>{{highlightedItem.title}}</h1>
              </router-link> -->

              <!-- BLOCK TAGS -->
              <!-- <div class="card-content" 
                v-if="Array.isArray(highlightedItem.tags) && highlightedItem.tags.length >=1">
                <span 
                  v-for="tag in highlightedItem.tags" 
                  :key="tag"
                  class="tag"
                > 
                  {{tag}}
                </span>
              </div> -->

            </div>

          </div>

        </CISSearchResultsCountAndTabs>

      </div>
  </div>

  <l-map
    :zoom="zoom"
    :bounds="bounds"
    :preferCanvas="preferCanvas"
    :min-zoom="minZoom"
    :max-zoom="maxZoom"
    :options="{ zoomControl: false }"
    :center="center"
    @update:center="centerUpdate"
    @update:zoom="zoomUpdate"
    >

    <l-control-zoom position="bottomright"/>

    <l-tile-layer
      :url="url"
      :attribution="attribution"/>

      <!-- MARKER CLUSTER -->
      <v-marker-cluster 
        v-if="projects"
        :options="{showCoverageOnHover: false, iconCreateFunction: iconCreateFunction}"
        >
        <!-- <l-marker 
          v-for="p in displayedProjects"
          :key="p.sd_id"
          :lat-lng="itemToMarker(p)"
          @click="highlightItem(p)"
          >
          <l-icon
            iconUrl="/static/icons/icon_pin_plein_violet.svg"
            :iconSize="p === highlightedItem ? [46, 46] : [29, 29]"
          />
        </l-marker> -->


          <!-- v-for="(item, i) in projects" -->
        <l-marker 
          v-for="(item, i) in itemsForMap()"
          :key="i"
          :lat-lng="{lng: parseFloat(item.lon), lat: parseFloat(item.lat)}"
          @click="showCard=true; highlightItem(item)"
          >
          <!-- :lat-lng="{lng: parseFloat(p.lon), lat: parseFloat(p.lat)}" -->
          <!-- :lat-lng="{lng: parseFloat(p.lon), lat: parseFloat(p.lat)}" -->
          <!-- :lat-lng="{lng: geolocByProjectId.get(p.id).lon, lat: geolocByProjectId.get(p.id).lat}" -->
          <l-icon
            v-if="checkIfItemHasLatLng(item)"
            iconUrl="/static/icons/icon_pin_plein_violet.svg"
            :iconSize="item === highlightedItem ? [46, 46] : [29, 29]"
          />
        </l-marker>


      </v-marker-cluster>

    </l-map>

  </div>
</template>



<script>
import { mapState, mapActions } from 'vuex'

import { L, LMap, LControlZoom, LTileLayer, LMarker, LIcon } from 'vue2-leaflet';
import Vue2LeafletMarkerCluster from 'vue2-leaflet-markercluster'
// import { PruneCluster, PruneClusterForLeaflet } from 'exports-loader?PruneCluster,PruneClusterForLeaflet!prunecluster/dist/PruneCluster.js'
// import { PruneCluster, PruneClusterForLeaflet } from 'PruneCluster'

import ProjectCard from './ProjectCard.vue'
import CISSearchResultsCountAndTabs from './CISSearchResultsCountAndTabs.vue'

import {VIEW_MAP} from '../constants.js'
import {getItemById} from '../utils.js';

const FRANCE_CENTER = [46.2276, 2.2137];


export default {
  name: "SearchResultsMap",

  components: {
    LMap,
    LControlZoom,
    LTileLayer,
    LMarker,
    LIcon,
    'v-marker-cluster': Vue2LeafletMarkerCluster,

    // PruneCluster,
    // PruneClusterForLeaflet,

    ProjectCard,
    CISSearchResultsCountAndTabs,

  },

  props: [
    'routeConfig', 
    'endPointConfig'
  ],

  data() {
    return {

      // LOCAL DATA
      VIEW_MAP,

      // FIELDS MAPPER
      contentFields : undefined,

      // ITEMS
      highlightedItem: undefined,
      itemLoaded: false,
      showCard:false,
      itemsOnMap : [
        // {sd_id : 'A', lat : '47.412', lon : '-1.218' },
        // {sd_id : 'B', lat : '47.4234', lon : '-1.248' },
      ],

      // LEAFLET SETUP
      preferCanvas: true,
      zoom: 6,
      maxZoom: 19,
      minZoom: 2,
      currentZoom: 6,
      center: FRANCE_CENTER,
      currentCenter: FRANCE_CENTER,

      // url: 'https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png',
      // attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contibutors',
      
      url: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
      subdomains: 'abcd',
      
    };
  },

  beforeMount: function () {
    console.log("- - - - - MAP TIME !!!! - - - - - -")
    console.log("\n - - SearchResultsMap / beforeMount ... ")
    console.log(" - - SearchResultsMap / routeConfig : \n", this.routeConfig)
    console.log(" - - SearchResultsMap / endPointConfig : \n", this.endPointConfig)

    // let pruneCluster = new PruneClusterForLeaflet();

    // set up fields mapper
    this.contentFields = this.routeConfig.contents_fields
    console.log(" - - SearchResultsMap / contentFields : \n", this.contentFields)

    // console.log("test marker / L.latLng(47.412, -1.218)", L.latLng(47.412, -1.218))
    // set up leaflet options
    const mapOptions = this.endPointConfig.map_options

    this.zoom = mapOptions.zoom
    this.maxZoom = mapOptions.maxZoom
    this.minZoom = mapOptions.minZoom
    this.currentZoom = mapOptions.currentZoom
    this.center = mapOptions.center
    this.currentCenter = mapOptions.currentCenter
    this.url = mapOptions.url
    this.attribution = mapOptions.attribution
    this.subdomains = mapOptions.subdomains

  },

  mounted(){

    console.log(" - - SearchResultsMap / mounted... ")
    // if(this.projects){
    //   const projectsWithMissingAddress = this.projects.filter(p => !p.lat)
    //   // if(projectsWithMissingAddress.length >= 1)
    //   //   this.findProjectsGeolocs(projectsWithMissingAddress)
    //   }
    this.itemsOnMap = this.projects

  },

  computed: {

    ...mapState({
      projects({search}){ return search.answer.result && search.answer.result.projects },
      items({search}){ return search.answer.resultMap && search.answer.result.projects },
      // displayedProjects(){
      //   return this.projects && this.projects.filter(p => this.geolocByProjectId.get(p.id))
      // },
      // displayedProjects(){
      //   console.log("displayedProjects : ", this.projects)
      //   if(this.projects){
      //     let itemsWithLatLng = this.projects.filter(i => !i.lat && !i.lon)
      //     return itemsWithLatLng
      //   }
      // },
      // geolocByProjectId({geolocByProjectId}){return geolocByProjectId}
    }),
    bounds(){
      let displayedItems = this.itemsForMap()
      return displayedItems && new L.LatLngBounds(displayedItems.map(p => ({
        lng: parseFloat(p.lon), 
        lat: parseFloat(p.lat),
      })));
    },
  },




  methods: {

    itemsForMap(){
      if (this.projects){
        return this.projects.filter(item => this.checkIfItemHasLatLng(item) )
      }
    },


    checkIfStringFloat(value){
      let val = parseFloat(value)
      if(!isNaN(val)){
        return val
      } else {
        return false
      }
    },
    getLatLng(item){
      return { lat : this.checkIfStringFloat(item.lat) , lng : checkIfStringFloat(item.lon) }
    },
    getLatLngDense(item){
      return { lat : this.checkIfStringFloat(item.latlng[0]) , lng : checkIfStringFloat(item.latlng[1]) }
    },
    checkIfItemHasLatLng(item){
      return this.checkIfStringFloat(item.lat) && this.checkIfStringFloat(item.lon)
    },

    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },



    highlightItem(i) {
      // console.log("highlightItem / p : \n", p)
      // show loader 
      this.showCard = true
      this.itemLoaded = false
      // get item info
      getItemById(i.sd_id,this.$store.state.search.endpoint.root_url)
      .then(item => {
        // this.$store.commit('setDisplayedProject', {item})
        // console.log(" - - DynamicDetail / item : \n ", item)
        this.highlightedItem = item;
        this.itemLoaded = true
      })
      .catch(function(err) { this.isError = true ; console.error('item route error', err) })

    },



    // itemImage(fieldBlock){
    //   return this.$store.getters.getImageUrl({item: this.displayableItem, position: fieldBlock})
    //   // return this.item
    // },
    // matchProjectWithConfig(fieldBlock) {
    //   const contentField = this.contentFields.find(f=> f.position == fieldBlock)
    //   const field = contentField.field
    //   return this.displayableItem[field]
    // },
    // projectId() {
    //   return this.matchProjectWithConfig('block_id')
    // },
    // projectAbstract() {
    //   let fullAbstract = this.matchProjectWithConfig('block_abstract')
    //   fullAbstract = ( fullAbstract == null ) ? this.noAbstractText : fullAbstract
    //   const tail = fullAbstract.length > MAX_SUMMARY_LENGTH ? '...' : '';
    //   return fullAbstract.slice(0, MAX_SUMMARY_LENGTH) + tail
    // },
    // projectInfo(field) {
    //   let fullInfo = this.matchProjectWithConfig(field)
    //   fullInfo = ( fullInfo == null ) ? this.noInfos : fullInfo
    //   return fullInfo
    // },
    // projectAddress() {
    //   let fullAddress = this.matchProjectWithConfig('block_address')
    //   console.log('fullAddress : ', fullAddress)
    //   let address = ( fullAddress || fullAddress !== 'None' ) ?  fullAddress : this.noAddress
    //   return address
    // },











    iconCreateFunction(cluster){
      const markerCount = cluster.getChildCount();

      return new L.DivIcon({
        html: `<span>${markerCount}</span>`, 
        className: 'cis-marker-cluster',
        iconSize: new L.Point(40, 40)
      });
    },
    // ...mapActions([
    //   'findProjectsGeolocs'
    // ])
  },

  // beforeUpdate(){
  //   console.log(" - - SearchResultsMap / beforeUpdate... ")
  //   if(this.projects){
  //     const projectsWithMissingAddress = this.projects.filter(p => !this.geolocByProjectId.has(p.lat))
  //   //   if(projectsWithMissingAddress.length >= 1)
  //   //       this.findProjectsGeolocs(projectsWithMissingAddress)
  //   }
  // },

};
</script>

<style>
  .app-loader {
    margin: 1.5em;
    padding: 1.5em
  }
  .map { 
    height: calc(100vh - 120px); 
    width: 100%;
  }

  /*
      Leaflet adds its own z-index to a bunch of elements which makes the map appear on top of 
      other elements with no good reason
      This line allows for the map to be usable without known limit yet while leaving the map below
      other elements
  */
  .map .leaflet-container *{
    z-index: 1;
  }


  .map{
    position: relative;
  }
  .map .count-and-tabs-container{
    position: absolute;
    top: 1rem;
    width: 100%;
  }

  .map .count-and-tabs-container .result-count-parent,
  .map .count-and-tabs-container .buttons{
    z-index: 2;
  }

  .map .cis-marker-cluster{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;

    background-color: #80C2BD;
    color: white;

    font-size: 16px;
    font-weight: bold;

    border-radius: 50%;
  }

  .highlighted-project{
    display: flex;
    flex-direction: column;
    margin-bottom: 1em;
  }

  .highlighted-project button.close{
    margin: 0.5em 0;
    background-color: transparent;
    border: 0;

    align-self: flex-end;
  }

  .highlighted-project .card{
    font-size: 0.9em;
      
    box-shadow: none;
  }

  .highlighted-project .card .card-content{
    padding: 0.2em 0.5em;   
  }

  .highlighted-project .card .card-content:first-of-type{
    padding-top: 0.5em;
  }
  .highlighted-project .card .card-content:last-of-type{
    padding-bottom: 0.5em;
  }

  .highlighted-project .card .card-content h1{
    font-size: 1.1em;
    font-weight: bold;
  }

  /* TODO SASS : share this style with search result project card tag style */
  .highlighted-project .tag{
    margin-right: 0.5em;
    margin-bottom: 0.5em;
    padding: 0.2em 1em;
    background-color: #767676;
    color: white;
  }

</style>