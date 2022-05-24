<template>
  <div>
      <Datalist></Datalist>
    <b-table striped hover :items="items"></b-table>
  </div>
</template>

<script>
import Datalist from "@/components/datalist.vue";

export default {
    data(){
        return{

        }
    },
    name:"listuser",
    components:{ 
        Datalist,
    },
    

}


</script>
