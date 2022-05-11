<template>
  <div class="user">
    <h1>table</h1>
  <table class="cen">
    <th>id</th>
    <th>user</th>
    <th>password</th>
    <th>age</th>
    <th>contact</th>
    <a v-for="item in list" :key="item.id">  
  
     </a>
</table>
   
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "App",
  data(){
    return {
      list:[]
    }
  },

  async mounted() {
    let result = await axios.get("http://192.168.1.24:5000/1");
    console.log(result.data)
    this.list=result.data
  },
} 
</script>

<style>
.cen{
  text-align: center;
  display: block;
  margin: auto;
  
}
th,tr{  
  display:contents;
  margin: auto;
  border: 2px solid #000000;
}
</style>
