<template>
    <div>
<div>
    <h1>Covid19 To Day</h1>
    <a v-for="(item,idx) in items" :key="idx">
    <p> Updata last : {{ item.txn_date }}</p>
    <p> New case : {{ item.new_case }}</p>
    <p> Death : {{item.new_death}}</p>
    
    </a>
        
</div>



    </div>
</template>
<script>
export default{ 
    name:"comcovid",
    components:{ 
    },
    data(){ 
        return{ 
            items:[
            ],
        }
    },

    mounted(){ 
        this.apicovid();
    },
    methods:{ 
        apicovid(){
        fetch('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all')
            .then(response => response.json())
            .then(data => {this.items=data})
        }
    }
}




</script>