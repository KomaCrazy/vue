<template>
    <div>
      <h3 class="">Table</h3>
<div class="container mt-5 ">
  <div class="row">
    <div v-for="item in list" :key="item.id" class="col-sm-2 p1">
      <a class="topic_1">Profile {{item.id}}</a><br>
      <a>user : {{item.user}}</a><br>
      <a>password : {{item.password}}</a><br>
      <a>age : {{item.age}}</a>
    </div>

  </div>
  </div>
</div>


</template>

<script>

import axios from "axios";
export default{
  name: "App",
  data(){
    return{
    list:[]
  }
},

async mounted(){
  let result = await axios.get("http://192.168.1.50:5000/1");
  console.log(result.data)
  this.list = result.data
},
}
</script>

<style>
.p1{
  padding-bottom: 48px;
  text-align: left;
}
.topic_1{
  color:black;
  font-size: 20px;
  text-decoration: none;
}
.topic_1:hover{
  color: #42b983;
}

*{
   cursor:context-menu;
}
</style>