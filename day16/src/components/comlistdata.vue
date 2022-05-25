<template>
    <div>
        <div class="container border">
            <h1>Basic Table</h1>
            <h3>This web use for build web site</h3>
            <div>
                <b-table striped hover :items="items" :fields="fields"></b-table>
            </div>
        </div>
    </div>
</template>
<script>

export default{ 
    name:"comlistdata",
    components:{ 
    },
    data(){
        return{ 
            fields:['id','user','password','gmail','contact'],
            items:[],
            
        }
    },  

    mounted(){
        this.apiData();

    },

    methods:{ 
        apiData(){ 
            fetch('http://localhost:5000/find')
                .then(response => response.json())
                .then(data => {this.items=data})
        }
    }
}
</script>