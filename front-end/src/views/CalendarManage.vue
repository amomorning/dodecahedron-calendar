<script setup>
import Viewer from "@inst-aaa/archiweb-core/src/components/Viewer.vue";
import SideDrawer from "@inst-aaa/archiweb-core/src/components/SideDrawer.vue"
import index from '../index'
import {onMounted, reactive, watch} from "vue";
onMounted(()=>{
  index.main();
})

const state = reactive({ drawer: false })
watch(state, () => { setTimeout(() => { window.resizeFunc() }, 200) }, {deep: true})

import {useDisplay} from 'vuetify'
const {mdAndUp} = useDisplay()

const authors = ['amomorning'];
const items = [{
  icon: 'mdi-help-box',
  title: 'About',
  content: 'ArchiWeb is a front-end web application using Vuetify and three.js. ArchiWeb provides a template to create a\n' +
    '            web application from scratch, you can easily use Vuetify UI components to generate a material design web,\n' +
    '            also with 3d rendering.'
},
  {
    icon: 'mdi-blur',
    title: 'Item Example',
    content: '<p class="text-h4 ma-4">Content can be <code>html</code> <span class="mdi mdi-flag"></span></p>'
  }
]

</script>

<template>
  <v-app>
    <SideDrawer v-model="state.drawer" :githubID="authors" :items="items"></SideDrawer>
    <v-btn icon="mdi-menu" variant="outlined" v-if="!mdAndUp"
           style="position: absolute; bottom: 20px; left: 50%; translate:-50%; z-index: 2;"
           @click="state.drawer = !state.drawer">
    </v-btn>
    <v-app-bar app color="transparent" flat>
      <v-app-bar-nav-icon
        v-if="mdAndUp"
        @click="state.drawer = !state.drawer"
      ></v-app-bar-nav-icon>
      <h2 v-if="mdAndUp">ArchiWeb Geometries</h2>
      <h2 v-else class="ml-5">ArchiWeb Geometries</h2>
    </v-app-bar>
    <v-main class="pt-0">
      <Viewer :gui="false" container="container"></Viewer>
      <section style="position: relative;">
        <Toolbox v-if="mdAndUp" id="toolbox"></Toolbox>
      </section>

    </v-main>
  </v-app>
</template>

<style scoped>

</style>
