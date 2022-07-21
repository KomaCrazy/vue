<template>
    <div>
        <form class="topic1">
    <h1>Register Form</h1>
<input type="text" class="form-control" id="user" placeholder="User">
<input type="password" class="form-control" id="password" placeholder="Passwold">
<input type="password" class="form-control" id="password_c" @change="check()" placeholder="Confirm Password">
<input type="email" class="form-control" id="email" placeholder="Email">

<div class="p-3">
<b-button type="submit" variant="outline-success">Register</b-button>    
</div></form>
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
    border-radius: 0;
}
input[type="email"]{
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;

}


</style>

<script>
export default{
    
    mounted(){
    },
    
    methods:{
        check(){
            var box1=  document.getElementById('password').value 
            var box2 = document.getElementById('password_c').value
            if (box1 == box2){
                console.log('easd')
            }else{
                alert("Password Do Not Match")
                document.getElementById('password_c').value = ""
            }
        },
        register(){
            let user = document.getElementById('user').value
            let password = document.getElementById('password').value
            let email = document.getElementById('email').value
            var url = 'http://localhost:3000/register?user='+user+'&password='+password+'&email='+email
            fetch(url)
            .then(response => response.json())
            .then(data => console.log(data))
        }


    }


}


</script>


