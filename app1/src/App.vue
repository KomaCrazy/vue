<template>
 <section>
   <img :src="picture" :width="size" :height="size" ref="imageEl">
   <form @submit.prevent="submitform">
     <label>ป้อนชื่อเล่น</label>
     <input type="text" ref="nicknameEl">
     <button type="submit">save</button>
   </form>

    <h4>Name : {{getFullName()}}</h4>
    <h4>nick : {{nickname}}</h4>
    <h4>age : {{age}}</h4>
    <h4>address : <span v-html="address"></span></h4>
    <h4>Social : <a :href="social" target="_blank">facebook</a></h4>
    hobby
    <ul>
        <li>{{hobby[0]}}</li>
        <li>{{hobby[1]}}</li>
        <li>{{hobby[2]}}</li>
    </ul>
    gerneral
    <ul>
        <li>เพศ : {{gerneral.gender}}</li>
        <li>น้ำหนัก : {{gerneral.wegiht}}</li>
        <li>ส่วนสูง : {{gerneral.height}}</li>
         <li>โรคประจำตัว : {{gerneral.wegiht}}</li>
    </ul>
    
  <button v-on:click="showdata">Click</button>
  <button v-on:click="incremnet(10)">เพิ่ม</button>
  <button v-on:click="decrement(10)">ลด</button>
 </section>
</template>



<script>
export default {
  name: 'App',
  data(){
    return{
      fristname:"เก้า",
      lastname:"แสนสวย",
      nickname:"",
      address:"<i>กรุงพนบเปน</i>",
      picture:"https://scontent.fbkk23-1.fna.fbcdn.net/v/t1.6435-9/91399490_2308760639417050_2714482849343340544_n.jpg?_nc_cat=101&ccb=1-5&_nc_sid=09cbfe&_nc_eui2=AeHfo4EBE6dLiEYNDUYdZF5TPdKR2P083xI90pHY_TzfEhXXI7vLu29wh4a11hObKhyfN8vX9H4J54yrwh5Unnr_&_nc_ohc=KfiBG4JF0LIAX9jc4gz&_nc_oc=AQmUR9gj5QwQ-91Vkm7GhRKXUscNZKBBrrtQWbsmMYFxcp3Y8A30vV_prbtHPL7WArA&_nc_ht=scontent.fbkk23-1.fna&oh=00_AT_90JtZmbJSrY9C8ri0mrV16zJiTP6rbgMLRbh3IMTlyw&oe=625C7501",
      social:"https://www.facebook.com/profile.php?id=100008494095921",
      hobby:["ตบเด็ก","เตะหมา","หาเรื่องคนแก่"],
      gerneral:{gender:"ชาย",wegiht:76.5,height:171,status:false},
      age:20,
      size:120
    }
  },
  methods:{
    getFullName(){
      return this.fristname +"  "+  this.lastname
    },

    showdata(){
      alert(this.fristname)
    },

    incremnet(value){
      this.age+=value
    },
    decrement(value){
      this.age-=value
    },


    submitform(){
      alert("บันทึกเรียบร้อย")
      this.nickname = this.$refs.nicknameEl.value

    }

  }
}
</script>

<style>
*{
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  background: rgba(147, 197, 160, 0.24);
}
</style>