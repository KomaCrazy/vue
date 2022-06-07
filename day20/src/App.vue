<template class="">
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>  | 
      <router-link to="/login">Login</router-link>  |
      <div class="nav1 text-right" id="user">1</div>

    </div>
    <router-view />
  </div>
</template>
<script>
export default{ 
  name:"App",
  components:{
  },
  data(){
    return{ 
      user:"",
    }
  }, 
  mounted(){ 
    this.test()
  },

  methods:{
    test(){ 
      var box = document.getElementById("user").innerHTML = this.user
      console.log(box)
    }
  }


}

</script>

<style>
.nav1{
  padding-right: 20px;
  float:right;
  display: inline;
  font-weight: bold;
  color: #2c3e50;
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
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
