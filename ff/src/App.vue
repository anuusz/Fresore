<script setup lang="ts">
import { onMounted } from 'vue'
// import { RouterLink, RouterView } from 'vue-router'
// import Listitem from './components/Listitem.vue';
// import Navbar from './components/Navbar.vue';
// import Footer from './components/Footer.vue'
// import AboutView from './views/AboutView.vue'
// import HomeView from './views/HomeView.vue'
// import Footer from './components/Footer.vue'
// import Banner from './components/Banner.vue';
// import Banner from './components/Home.vue';

// Auto-clear localStorage untuk testing - hapus di production
onMounted(() => {
  localStorage.clear() // Uncomment untuk auto-logout setiap refresh
  console.log('localStorage cleared - user logged out for testing')
})
</script>

<template>
  <!-- <HomeView /> -->
  <!-- <AboutView /> -->
  <!-- <Topbar /> -->
  <!-- <Navbar /> -->
  <!-- <Listitem /> -->
  <!-- <Home></Home> -->
  <!-- <Banner></Banner> -->
  <!-- <Footer /> -->
  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
