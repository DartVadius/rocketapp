<template>
  <div class="wrapper cf">
  <div id="app">
    <header class="cf">
      <div id="logo" class="cf">
        <a href="#"><img src="assets/img/logo.png" alt=""/></a>
      </div>

      <!-- nav -->
      <nav class="cf">
        <ul id="nav" class="sf-menu">
          <li>
            <router-link to="/" class="current-menu-item"><span>ГЛАВНАЯ</span></router-link>
          </li>
          <li>
            <router-link to="/foo"><span>ФОТО</span></router-link>
          </li>
          <li>
            <router-link to="/bar"><span>КОНТАКТЫ</span></router-link>
          </li>
        </ul>
        <div id="combo-holder"></div>
      </nav>
      <!-- ends nav -->
    </header>
    <router-view></router-view>
  </div>
  </div>
</template>

<script>
import hljs from 'highlight.js'

export default {
  name: 'App',
  beforeCreate () {
    hljs.initHighlightingOnLoad()
  }
}
</script>

<style>
  @import 'assets/css/superfish.css';
  @import 'assets/css/nivo-slider.css';
  @import 'assets/css/tweet.css';
  @import 'assets/css/style.css';
  @import 'assets/css/lessframework.css';
  @import 'assets/fluent_comments/css/ajaxcomments.css';
  @import '//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/default.min.css';
</style>
