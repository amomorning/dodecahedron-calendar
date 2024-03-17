<script setup>
import index from '../index'
import {onMounted, reactive, watch} from "vue";
import Notification from '@inst-aaa/archiweb-core/src/components/Notification.vue';
import GUICard from '@inst-aaa/archiweb-core/src/components/GUICard.vue';
import InfoCard from '@inst-aaa/archiweb-core/src/components/InfoCard.vue';
import ControlPane from '@inst-aaa/archiweb-core/src/components/ControlPane.vue';

onMounted(()=>{
  index.main();
})
</script>
<template>
    <v-app>
        <Notification></Notification>
        <ControlPane></ControlPane>
        <InfoCard></InfoCard>
        <GUICard style="position: absolute; top: 50px; right: 50px; z-index: 10"></GUICard>
                <div id="container"></div>
    </v-app>
    
    
</template>
