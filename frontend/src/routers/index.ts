import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/components/HelloWorld.vue'
import FullPageRouter from '@/routers/modules/full_page.ts'
import BlogRouter from '@/routers/modules/blog.ts'
import BasicRouter from '@/routers/basic.ts'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    ...FullPageRouter,
    ...BlogRouter,
    ...BasicRouter,

    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // },
    // {
    //   path: '/test',
    //   name: 'Test',
    //   component: () => import('@/views/test.vue')
    // },
    // ...YiRouter,
    // ...StockRouter,
    // ...LoginRouter,
    // ...FuturesOptionRouter,
    // ...FutureRouter,
  ]
})

export default router
