<template>
    <div>

<div class="text-center mt-5 topic1 p-3">
    <form style="max-width:300px;margin: auto;">
        <h1>Please Sign in</h1>
        <input type="email" class="form-control" placeholder="Email" id="email">
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
    mounted(){
    },
    methods:{
        login(){
            var email = document.getElementById('email').value
            console.log(email)
        }
    }
}

</script>