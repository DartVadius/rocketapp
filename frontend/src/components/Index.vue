<template>
  <!-- MAIN -->
  <div role="main" id="main" class="cf">

    <!-- posts list -->
    <div id="posts-list" class="cf" v-for="(item, key) in posts" v-bind:key="key">
      <article class="cf">

        <div class="entry-right-data">
          <a href="#" class="post-heading">{{ item.title }}</a>
          <div class="meta">
          <div class="excerpt">
            {{ item.body }}
          </div>
            <router-link :to="'/post/' + item.id" class="link-button"><span>Читать дальше</span></router-link>
        </div>
        </div>
      </article>
    </div>
    <!-- ENDS posts list -->
  </div>
</template>
<script>

export default {
  name: 'Index',
  data () {
    return {
      posts: []
    }
  },
  methods: {
    getItems () {
      return this.$store.getters.all_posts
    }
  },
  computed: {
    postsAll () {
      return this.$store.getters.all_posts
    }
  },
  mounted () {
    this.$store.dispatch('getAllPosts').then(() => {
      this.posts = this.$store.getters.all_posts
      console.log(this.$store.getters.all_posts)
    })
  }
}
</script>
