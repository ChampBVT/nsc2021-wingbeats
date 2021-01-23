<template>
  <div id="app">
    <div id="nav">
      <div class="d-flex">
        <b-navbar-brand class="mr-auto p-2" href="#">
          <img src="./assets/wingbeats.png" class="d-inline-block align-center" id="navbar-logo" alt="WingBeats ICON" />WingBeats
        </b-navbar-brand>
        <div class="p-2">Home</div>
        <!-- <div class="p-2"><router-link to="/">Home</router-link></div> -->
        <!-- <div class="p-2"><router-link to="/about">About</router-link></div> -->
      </div>
    </div>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
  font-weight: bold;
  margin-left: 100px;
  margin-right: 100px;
}

#navbar-logo {
  width: 50px;
  margin-right: 10px;
}

#nav a {
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #458ff6;
}
</style>
