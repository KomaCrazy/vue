<template>
  <div id="app">
    <p><img :src="picture" :width="picturesize" alt=""></p>
    <p>user : {{getFull()}}</p>
    <p>Name : {{ name }}</p>
    <p>age : {{ age }}</p>
    
      <ul>Hobby :
        <li>{{hobby[0]}}</li>
      </ul>

    

    <p><a :href="linkfacbook" target="_blank"> 
      <img :src="facbookicon" :width="sizefacbook" alt="" ></a>
    <a><img :src="instagicon" :width="sizeinstag"  alt=""></a></p>

  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {

      name: "kaw",
      user: "koma",
      last: "crazy",
      age: 18,
      address: "70 / 10 Thai",
      linkfacbook:'https://www.facebook.com/profile.php?id=100008494095921',
      facbookicon:"https://cdn-icons-png.flaticon.com/512/1051/1051309.png",
      picture:
        "https://t4.ftcdn.net/jpg/00/73/69/47/240_F_73694724_7n3f29wiCflslPQiVFKWOVlMCh76wkHu.jpg",    
      instagicon:"https://cdn-icons-png.flaticon.com/128/1384/1384015.png",
      sizefacbook:50,
      picturesize:120,
      sizeinstag:50,
      hobby:["Playgame","cooking","runing"],
    }
  },
  methods: {
    //This part controller Fuction
    getFull() {
      return this.user + this.last;
    },
  },
};
</script>

<style scoped>
*{
  padding-left: 10px;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
