<template>
<div class="datalist">
  <div class="container border">
    <b-table striped hover :items="items" :fields="fields"></b-table>
  </div>
</div>
</template>

<script >

export default{ 
    name:"Datalist",
    components:{
    },
    data() {
        return{
        fields:['id','user','password','gmail','contact'],
        items:[]
        }
    },
    mounted(){
      this.getdata();
    },
    methods:{ 
        getdata(){
            fetch('http://localhost:5000/find')
                .then(response => response.json())
                .then(data => this.items=data);
        }
    }
}


</script>
