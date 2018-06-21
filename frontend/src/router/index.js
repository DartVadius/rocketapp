import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Post from '@/components/Post'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/post/:id',
      name: 'Post',
      component: Post
    }
  ]
})
