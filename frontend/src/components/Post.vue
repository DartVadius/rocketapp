<template>
  <!-- MAIN -->
  <div role="main" id="main" class="cf">

    <!-- posts list -->
    <div id="posts-list" class="cf">

      <article class="cf">
        <div class="entry-left-data">

        <div class="entry-right-data">
          <a href="#" class="post-heading">{{ post.title }}</a>
          <div class="excerpt">
            {{ post.body }}
          </div>

        </div>
        </div>
      </article>

    </div>
    <!-- ENDS posts list -->

    <!-- sidebar -->
    <aside id="sidebar">

      <ul>

        <li class="block">
          <div class="sidebar-top"></div>
          <div class="sidebar-content">
            <h4 class="heading">Text Widget</h4>
            Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
            Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero
            sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.
            Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed,
            commodo vitae, ornare sit amet, wisi.
          </div>
          <div class="sidebar-bottom"></div>
        </li>

      </ul>

    </aside>
    <!-- ENDS sidebar -->

  </div>
  <!-- ENDS MAIN -->
</template>

<script>
export default {
  name: 'Post',
  data () {
    return {
      post: {}
    }
  },
  mounted () {
    this.$store.dispatch('getPost', this.$route.params['id']).then(() => {
      this.post = this.$store.getters.post
    })
  }
}
</script>
