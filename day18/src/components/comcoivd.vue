<template>
    <div></div>
</template>

<script> 
export default { 
    name: "comcovid",
    Data(){
        return{ 
            items:[],
        }
    },

    mounted(){
        this.covid()
    },
    methods:{ 
        covid(){
            fetch('https://covid19.ddc.moph.go.th/api/Cases/today-cases-all')
            .then(respose => respose.json())
            .then(data => {this.items=data;console.log(this.items)})
        }
    }

}
</script>
