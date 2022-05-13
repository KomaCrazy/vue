<template>
  <div id="app">
    <div id="nav">
      <h2>
      <router-link to="/">HOME</router-link>   |
      <router-link to="/about">ABOUT</router-link>  |
      <router-link to="/user">USER</router-link> |
      <router-link to="/register">REGISTER</router-link>  |
      <router-link to="/Test">Test</router-link>
      </h2>
    </div>
    <router-view />
  </div>
</template>

<script>

</script>

<style>
*{
  background-color:#1a1a1a;
  color:white;
  font-family: inherit;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}
#nav a:hover{
    color: #42b983;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
