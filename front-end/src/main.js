/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

const app = createApp(App)
import Vue3DraggableResizable from 'vue3-draggable-resizable'
app.use(Vue3DraggableResizable)
registerPlugins(app)
app.mount('#app')
