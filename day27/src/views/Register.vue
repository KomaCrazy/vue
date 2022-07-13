<template>
    <div></div>
</template>

<script>

export default {

    mounted(){
        this.api()
    },
    methods:{
        share(val){
            console.log(val)
        }
        ,
        api(){
            fetch('http://192.168.129.216:5000/')
            .then(response => share(response))
        }
    }
}

</script>