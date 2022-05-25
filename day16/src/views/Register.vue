<template>
    <div>
        <form class="border container">
        <h1>Basic Login</h1>

    <label for="" class="">
    <h5 class="text-left">User</h5>
    <input type="text" v-model="user"></label><br>

    <label for="" class="">
    <h5 class="text-left">Password</h5>
    <input type="password" v-model="password"></label><br>

    <label for="" class="">
    <h5 class="text-left">Email</h5>
    <input type="email" v-model="email" id="email" name="email"></label><br>
    
    <label for="" class="">
    <h5 class="text-left">contact</h5>
    <input type="text" v-model="contact"></label><br>

    <label for="" class="p-3">
    <input type="button" class="button button1" @click="addregis()" value="Register"></label><br>
</form>
    </div>
</template>



<script>


export default{ 
    components:{ 

    },
    data(){
        return{ 
            user:"",
            password:"", 
            email:"", 
            contact:"",
        }
    },

    mounted(){ 

    },

    methods:{ 
        addregis(){
            console.log("user : " + this.user)
            console.log("password : " + this.password)
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function(){
                if (this.readyState == 4 && this.status == 200){
                    console.log(xhttp.responseText);
                }
            };
            xhttp.open("GET", "http://localhost:5000/register?user="+this.user+"&password="+this.password+"&gmail="+this.email+"&contact="+this.contact,true);
            xhttp.send();
        },
        apiReturn(){ 
            fetch('http://localhost:5000/find')
                .then(response => response.json())
                .then(data => console.log(data))
        }


    },
}



</script>
<style>
.button1 {
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 4px;
    padding-bottom: 4px;
  background-color: white; 
  color: black; 
  border: 2px solid #4CAF50;
  transition-duration: 0.4s;
}
.button1:hover{ 
    background-color:#4CAF50;
}
</style>