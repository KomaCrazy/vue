<template>
    <div>
      <div class="container">
         <div class="row">
            <div class="col-lg-3 col-md-5 col-sm-8 mx-auto">
                  <form class="form-group border"> 
                      <div class="p-3 ">
                      <h2 class="">Regsiter</h2>
                      <a class="">User</a>
                      <input type="text" class="form-control p">
                      <a class="">Password</a>
                      <input type="password" class="form-control p">
                     <a class="">email</a>
                      <input type="email" class="form-control p">
                     <a class="">contact</a>
                      <input type="text" class="form-control p">
                     <a class="">contact</a>
                      <input type="text" class="form-control p">
                      <div class="btn">
                    <input type="button" class="button button1 p" @click="addregis()"  value="Register">
                          
                      </div>

                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default{ 
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
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function(){
                if (this.readyState == 4 && this.status == 200){
                    console.log(xhttp.responseText);
                }
            };
            xhttp.open("GET", "http://localhost:5000/register?user="+this.user+"&password="+this.password+"&gmail="+this.email+"&contact="+this.contact,true);
            xhttp.send();
        }
    }
}



</script>

<style>

h2{ 
    padding-bottom:10px
}

.button {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding-bottom: 8px;
  padding-top: 8px;
  padding-left: 10px;
  padding-right: 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}
.button1 {
  background-color: white; 
  color: black; 
  border: 2px solid #4CAF50;
}
.button1:hover {
  background-color: #4CAF50;
  color: white;
}
</style>