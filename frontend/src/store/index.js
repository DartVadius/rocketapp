import Vue from 'vue'
import Vuex from 'vuex'
import { Posts } from '../api/api'

import {
  GET_POSTS,
  GET_POST
} from './mutation-types'

Vue.use(Vuex)

const state = {
  all_posts: [],
  post: {}
}

const getters = {
  all_posts: state => state.all_posts,
  post: state => state.post
}

const mutations = {
  [GET_POSTS] (state, posts) {
    state.all_posts = posts
  },
  [GET_POST] (state, post) {
    state.post = post
  }
}

const actions = {
  getAllPosts ({ commit }) {
    return new Promise(resolve => {
      Posts.getPosts().then(posts => {
        commit('GET_POSTS', posts)
        resolve(posts)
      })
    })
  },
  getPost ({ commit }, id) {
    return new Promise(resolve => {
      Posts.getPost(id).then(post => {
        commit('GET_POST', post)
        resolve(post)
      })
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
