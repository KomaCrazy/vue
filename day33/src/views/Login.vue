<template>
    <div class="Login">

<div class="container">
<div class="row">
</div>
</div>


    </div>
</template>
<style>
*{
    
}

</style>

<script>

export default{
    name:"Login",
    components:{
    },
    
    mounted(){

    },
    methods:{
        login(){
            var user = document.getElementById('user')
            var password = document.getElementById('password')
            console.log(user,password)
        }
    }
}

</script>