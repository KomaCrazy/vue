<template>
  <div class="user">
	<table>
        <tr>
            <h1>Table</h1>
        </tr>
        <th>Id</th>
        <th>user</th>
        <th>password</th>
        <th>age</th>
        <th>contact</th>
            <tr v-for="item in list" :key="item.id">
            <th>{{item.id}}</th>
            <th>{{item.user}}</th>
            <th>{{item.password}}</th>
            <th>{{item.age}}</th>
            <th>{{item.contact}}</th>
            </tr>
            
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
table{
  margin-left: auto;
  margin-right: auto
}

.cen{
  text-align: center;
  margin: auto;
  
}
th,tr,td{  
  border: 1px solid #b9b9b9;
  padding: 6px;

}
</style>
