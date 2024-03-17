// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {path: '/manage', component: () => import('@/views/CalendarManage.vue')},
  {path: '/', component: () => import('@/views/CalendarCanvas.vue')}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
