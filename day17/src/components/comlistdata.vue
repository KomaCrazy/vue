<template>
<div>
        <div class="container">
            <b-table striped hover :items="items" :fields="fields"></b-table>
        </div>
</div>
</template>

<script>
export default {
    name:"comlistdata",
    components:{ 

    },
    data(){ 
        return{ 
            fields:['id','user','password','email','contact'],
            items:[],
        }
    },
    mounted(){ 
        this.apiData()
    },
    methods:{ 
        apiData(){
            fetch('http://localhost:5000/api')
            .then(response => response.json())
            .then(data => { this.items=data})
        }
    }
}

</script>