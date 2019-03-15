<template>
  <div class="map">
    <div class="count-and-tabs-container">
      <div class="container">

        <CISSearchResultsCountAndTabs 
          :view="VIEW_MAP" 
          :open="!!highlightedItem"
          >
          
          <!-- HIGHLIGHTED ITEM  -->
          <div class="highlighted-project" v-if="highlightedItem" slot="project">
            
            <!-- BUTTON TO CLOSE PREVIEW -->
            <button class="button close" @click="highlightProject(undefined)">
              <span class="icon is-small">
                <i class="fas fa-times"></i>
              </span>
            </button>
            
            <!-- PROJECT CARD -->
            <div class="card">

              <!-- BLOCK IMAGE -->
              <router-link 
                :to="`/project/${highlightedItem.id}`" 
                class="card-image"
              >
                <img 
                  :src="highlightedItem.image" 
                  :alt="highlightedItem.title">
              </router-link>
              
              <!-- BLOCK ADDRESS -->
              <div class="card-content" v-if="highlightedItem.address.trim().length > 1">
                <!-- 
                <span class="icon has-text-light">
                  <i class="fas fa-location-arrow"></i>
                </span> -->
                <span class="icon">
                  <img class="image is-16x16" src="/static/icons/icon_pin.svg">
                </span>
                <span class="subtitle is-6">
                  {{ highlightedItem.address.slice(0, 100) }}
                </span>
              </div>

              <!-- BLOCK LINK -->
              <router-link 
                :to="`/project/${highlightedItem.id}`" 
                class="card-content"
                >
                <h1>{{highlightedItem.title}}</h1>
              </router-link>

              <!-- BLOCK TAGS -->
              <div class="card-content" 
                v-if="Array.isArray(highlightedItem.tags) && highlightedItem.tags.length >=1">
                <span 
                  v-for="tag in highlightedItem.tags" 
                  :key="tag"
                  class="tag"
                > 
                  {{tag}}
                </span>
              </div>

              </div>

          </div>

        </CISSearchResultsCountAndTabs>

      </div>
  </div>

  <l-map
    :zoom="zoom"
    :options="{zoomControl: false}"
    :center="center"
    @update:center="centerUpdate"
    @update:zoom="zoomUpdate"
    >

    <!-- :bounds="bounds" -->
    <l-control-zoom position="bottomright"/>

    <l-tile-layer
      :url="url"
      :attribution="attribution"/>

      <!-- MARKER CLUSTER -->
      <v-marker-cluster 
        :options="{showCoverageOnHover: false, iconCreateFunction: iconCreateFunction}"
        >
        <!-- <l-marker 
          v-for="p in displayedProjects"
          :key="p.sd_id"
          :lat-lng="itemToMarker(p)"
          @click="highlightProject(p)"
          >
          <l-icon
            iconUrl="/static/icons/icon_pin_plein_violet.svg"
            :iconSize="p === highlightedItem ? [46, 46] : [29, 29]"
          />
        </l-marker> -->


        <l-marker 
          v-for="(p, i) in projects"
          :key="i"
          :lat-lng="{lng: parseFloat(p.lon), lat: parseFloat(p.lat)}"
          @click="highlightProject(p)"
          >
          <!-- :lat-lng="{lng: parseFloat(p.lon), lat: parseFloat(p.lat)}" -->
          <!-- :lat-lng="{lng: geolocByProjectId.get(p.id).lon, lat: geolocByProjectId.get(p.id).lat}" -->
          <l-icon
            iconUrl="/static/icons/icon_pin_plein_violet.svg"
            :iconSize="p === highlightedItem ? [46, 46] : [29, 29]"
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

import CISSearchResultsCountAndTabs from './CISSearchResultsCountAndTabs.vue'

import {VIEW_MAP} from '../constants.js'

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
    CISSearchResultsCountAndTabs
  },

  props: [
    'routeConfig', 
    'endPointConfig'
  ],

  data() {
    return {

      // LOCAL DATA
      VIEW_MAP,

      // ITEMS
      highlightedItem: undefined,
      itemsOnMap : [
        {sd_id : 'A', lat : '47.412', lon : '-1.218' },
        {sd_id : 'B', lat : '47.4234', lon : '-1.248' },

      ],

      // LEAFLET SETUP
      zoom: 6,
      maxZoom: 19,
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

    console.log("test marker / L.latLng(47.412, -1.218)", L.latLng(47.412, -1.218))
    // set up leaflet options
    const mapOptions = this.endPointConfig.map_options

    this.zoom = mapOptions.zoom
    this.maxZoom = mapOptions.maxZoom
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
    this.itemsOnMap = projects

  },

  computed: {

    ...mapState({
      projects({search}){ return search.answer.result && search.answer.result.projects },
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
      // bounds(){
      //   return this.displayedProjects && new L.LatLngBounds(this.displayedProjects.map(p => ({
      //     // lng: this.geolocByProjectId.get(p.id).lon, 
      //     // lat: this.geolocByProjectId.get(p.id).lat
      //     lng: parseFloat(p.lon), 
      //     lat: parseFloat(p.lat),
      //   })));
      // },
      // geolocByProjectId({geolocByProjectId}){return geolocByProjectId}
    }),
    // displayedProjects(){
    //   let items = this.$store.getters.getGeoResults
    //   console.log("displayedProjects / items : ", items)
    //   if (typeof items !== 'undefined') {
    //     return items
    //   }
    // },
  },




  methods: {


    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    highlightProject(p) {
      this.highlightedItem = p;
    },
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