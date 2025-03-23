import { createRouter, createWebHistory } from 'vue-router'
import Main from '../views/Main.vue'
import UserPage from '../views/UserPage.vue'

const routes = [
  { path: '/', name: 'Main', component: Main },
  { path: '/users/:id?', name: 'UserPage', component: UserPage }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
