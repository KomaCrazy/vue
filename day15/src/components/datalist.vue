<template>
<div class="datalist">
 <template>
  <div class="container border">
    <b-table striped hover :items="items" :fields="fields" ></b-table>
  </div>
</template>
</div>
</template>
<script >

export default{ 
    name:"Datalist",
    components:{

    },
    data() {
        return {
        fields: ['id','user','password','gmail','contact'],
         items: []
        }
    },
    mounted(){
      this.getdata();
    },
    methods:{ 
        getdata(){
            fetch('http://192.168.1.40:5000/find')
                .then(response => response.json())
                .then(data => this.items=data);
        }
    }
}


</script>
