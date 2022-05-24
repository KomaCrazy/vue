<template>
    <div class="border container" style="padding-right:27%;padding-left:27%">
    <div class="">
    <form class="">
  <div class="form-group p-3">
    <label for="user">user
    <input type="text" class="form-control" v-model="username"  placeholder="Username">
    </label>
  </div>

    <div class="form-group p-3">
    <label for="lastname">lastname
    <input type="text" class="form-control" v-model="lastname" placeholder="Lastname">
    </label>
  </div>

    <div class="form-group p-3">
    <label for="age">Age
    <input type="text" class="form-control" v-model="age" placeholder="Age">
    </label>
  </div>

  <div class="form-group p-3">
    <label for="passworld">password
    <input type="text" class="form-control" v-model="password" placeholder="password">
    </label>
  </div>

    <div class="form-group p-3">
    <label for="exampleInputEmail1">Email address
    <input type="email" class="form-control" v-model="email" placeholder="Enter email">
    </label>
  </div>
<br>
  <input type="button"  class="btn btn-primary" @click="addsummit()" value="Submit">
  <p></p>
</form>

</div>
    </div>
</template>
<script>

export default {
    components:{

    },
  data() {
    return {
      username:"",
      lastname:"",
      password:"",
      email:"",
      age:""
    }
  },methods:{
     addsummit(){
       console.log("username:"+this.username)  
       console.log("lastname:"+this.lastname)  
       var xhttp = new XMLHttpRequest();
       xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
       console.log(xhttp.responseText);
       }
       };   
       xhttp.open("GET", "http://localhost:5000/register?username="+this.username+"&lastname="+this.lastname, true);
       xhttp.send();
     }
  }
}
</script>
<style>
</style>