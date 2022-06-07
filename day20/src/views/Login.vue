<template>
  <div>

      <h3>Login</h3>
    <form>
{{name}}
        <input type="text" placeholder="user"><br><br>
        <input type="text" placeholder="password"><br><br>

    <button>Login</button>
    </form>


</div>
</template>
<script>
export default{ 
    data(){
        return{
            name:''
        }
    },
    created() {
        this.checklogin()
    },

    methods:{
        checklogin(){
            var user = localStorage.getItem("user")
            if(!user){
                 console.log("Error")
            }else{
                this.name = user
            }
        }
    }

}

</script>
