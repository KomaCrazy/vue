<template>
    <div>


<div class="text-center mt-5 topic1 p-3" v-if="box">
    <form style="max-width:300px;margin: auto;">
        {{this.$cookies.get('profile').id}}
        {{this.$cookies.get('profile').user}}
        {{this.$cookies.get('profile').email}}
    </form>
</div>

<div class="text-center mt-5 topic1 p-3" v-else>
    <form style="max-width:300px;margin: auto;">
        <h1>Please Sign in</h1>
        <input type="text" class="form-control" placeholder="User" id="user">
        <input type="password" class="form-control" placeholder="Password" id="password">
        <div class="p-3">
            <b-button variant="outline-success" @click="login()">Sign In</b-button>

        </div>
    </form>
</div>


    </div>
</template>
<style>
.topic1{
    border:1px solid;
    max-width: 400px;
    max-height: 600px;
    border-radius: 10px;
    margin: auto;
}
input[type="email"]{
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
        return {box:false}
    },

    mounted(){
        this.connection()
        console.log(this.box)
    },
    methods:{
        cookie(data){
            var status = data["status"]
            var id = data["id"]
            var user = data["user"]
            var password = data["password"]
            var email = data["email"]
            if (status == "1"){
                this.$alert("Please Sign In Again");
            }else {
                 this.$alert("Hello "+user+" welcome To web");
                 let profile = {"id":id,"user":user,"email":email}
                 this.$cookies.set('profile',profile)
                console.log(id,user,password,email)
            }
        },

        login(){
            let user = document.getElementById('user').value
            let password = document.getElementById('password').value
            var url = 'http://192.168.1.110:5000/login?user='+user+'&password='+password
            console.log(url)
            fetch(url)
            .then(response => response.json())
            .then(data => this.cookie(data))
        },
        connection(){
            if (this.$cookies.get('profile') == this.$cookies.get('profile') ){
                this.box = false
            }else{
                this.box = true
                console.log(this.box)
            }
        }

    }
}

</script>