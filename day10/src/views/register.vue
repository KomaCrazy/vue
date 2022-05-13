<template>
<div>
<form action="">
<h1>Register</h1>


<br>
<input v-model="user" placeholder=""><br>
<input v-model="message" placeholder=""><br>
<input type="submit" value="Register">
</form>    

</div>
</template>



<style>
input ,select{
    width: 10%;
    padding: 8px 0;
    margin: 8px;
    display: inline-block;
}
input[type="sumbmit"]{
    color: #42b983;
}

</style>