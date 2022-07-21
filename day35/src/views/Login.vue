<template>
    <div>

<div class="p-3">
<form class="topic2" v-if="conn">
<h2>Profiles</h2>
<h6>About Profile You can Edit and put Data you for show in Profile</h6>

<div class="container">
<div class="row p-3">
    <div class="col">
        <div class="row " >
            <div class="col" style=" text-align: right;">User :</div>
            <div class="col " style=" text-align: left;">{{this.$cookies.get('profiles').user}}</div>
</div>

        <div class="row " >
            <div class="col" style=" text-align: right;">Email :</div>
            <div class="col " style=" text-align: left;">{{this.$cookies.get('profiles').email}}</div>
        </div>
</div>

<div class="col">
<div style="text-align:left;font-size: 20px;">Friend</div>
<table class="table border">
  <caption class="text-center " style="margin:auto;padding-bottom: 0px;">
    <b-button variant="outline-primary" style="font-size:12px">Add Friend</b-button>    
    </caption>
  <thead>
    <tr>
      <td class="col">Friend</td>
      <td scope="col">Email</td>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>bam</td>
      <td>bam@email</td>
    </tr>
    </tbody>

  </table>

</div>

</div>
</div>

<div class="p-3">
<b-button variant="outline-success" @click="logout()">logout</b-button>    
</div></form>

<form class="topic1" v-else>
<h1>Please Sign In</h1>
<input type="text" class="form-control" id="user" placeholder="User">
<input type="password" class="form-control" id="password" placeholder="Passwold">
<div class="p-3">
    <router-link to="/register">Register</router-link>
<b-button variant="outline-success" @click="login()">Sign In</b-button>    
</div></form>

</div>


    </div>

</template>
<style>
.col{
    margin: auto;
    font-family: Verdana;
}
.topic1{
    border: 1px solid;
    max-width:400px;
    max-height: 600px;
    padding: 20px;
    margin: auto;
    border-radius: 20px;
}
.topic2{
    max-width:1200px;
    max-height: 2800px;
    padding: 20px;
    border-radius: 20px;
    margin: auto;
    border:1px solid
}

input[type="text"]{
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
}
input[type="password"]{
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
}

</style>
<script>
export default{
    data(){
        return{conn:false}
    },
    mounted(){  
        this.connectAuto()
    },
    methods: {
        logout(){
            this.$cookies.remove('profiles')
            this.conn = false
        },

        connectAuto(){
        if (this.$cookies.get('profiles')){

        let user = this.$cookies.get('profiles').user
        let email = this.$cookies.get('profiles').email
        console.log(user,email)
                this.conn = true

        }else{
            console.log('null')
                this.conn = false

        }
        },

        connect(data){
            if (data){
                var id = data["id"]
                var user = data["user"]
                var email = data["email"]
                let profiles = {"id":id,"user":user,"email":email}
                this.$cookies.set('profiles',profiles)
                console.log('hello')
                this.conn = true
            }else{
                console.log('error')
                this.conn = false
            }
        }
        ,
        login(){
            let user = document.getElementById('user').value
            let password = document.getElementById('password').value
            let url = 'http://localhost:3000/login?user='+user+'&password='+password
            fetch(url)
            .then(response => response.json())
            .then(data => this.connect(data))
        }
    },
}
</script>
