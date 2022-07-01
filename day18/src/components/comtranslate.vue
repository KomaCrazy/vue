<template>
  <div>
    <div class="container">
      <h3>Translate for bot</h3>

    <textarea id="input1" rows="10" cols="50" v-model="text1" v-on:input="convert()" style="font-size:18px"></textarea>
    <textarea id="output1" rows="10" cols="50" style="font-size:18px"></textarea>
    </div>

</div>
</template>
<script>
export default {
  name: "comtranslate",
  components: {},
  data() {
    return {
      text: "",
      text1: "",
      box1: "",
      items: [],
    };
  },
  mounted() {},
  methods: {
    translate(sentences, targetDiv, from_lang = this.l1, to_lang = this.l2) {
      sentences = sentences.replace(/\n/g, "<br>");
      let endPoint = `https://translate.googleapis.com/translate_a/single?client=gtx&sl=${from_lang}&tl=${to_lang}&dt=t&ie=UTF-8&oe=UTF-8&q=${encodeURIComponent(
        sentences
      )}`;

      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
          var jsonText = JSON.parse(this.responseText);
          this.text = jsonText[0][0][0];
          this.text = this.text.replace(/<br>/g, "\n");
          targetDiv.innerHTML = "&nbsp;" + this.text;
        }
      };
      xhttp.open("GET", endPoint, true);
      xhttp.send();
    },
    convert() {
    console.log(this.text1);

    if(this.text1.match(/^([a-z0-9])+$/i)){
        this.l1 = 'en'
        this.l2 = 'th'
    }
    if(this.text1.match(/^([ก-ฮ๐-๙])+$/i)){
        this.l1 = 'th'
        this.l2 = 'en'
    }   

    if (this.text1 != ""){
      this.translate(this.text1, this.box1 = document.getElementById("output1"), this.from_lang =this.l1, this.to_lang=this.l2)
    }
    else{
      this.translate("-", this.box1 = document.getElementById("output1"), this.from_lang =this.l1, this.to_lang=this.l2)
    }

    },
  },
};
</script>

