<script setup>
import Viewer from "@inst-aaa/archiweb-core/src/components/Viewer.vue";
import index from '../index'
import {onMounted} from "vue";
onMounted(()=>{
  index.main();
})

</script>

<template>
  <Viewer :gui="false" container="container"></Viewer>
</template>

<style scoped>

</style>
