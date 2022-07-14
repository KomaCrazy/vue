<template>
    <div>

    <div class="container p-3 bg-dark text-success">
        <div class bg-warnning>
    
        </div>            
    </div>


    </div>
</template>
<style>


</style>
<script>

var user = 'kaasdw'
var password = '1234'
var url = 'http://192.168.1.110:5000/login?user='+user+'&password='+password

fetch(url)
.then(response => response.json())
.then(data => console.log(data))
</script>