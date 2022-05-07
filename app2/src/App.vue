<template>
1
</template>
<script>
export default {
  name: "App",

  data() {
    return {
      picture:"https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
      user: "001",
      nick: "kaw",

    };
  },

  methods: {
    togglevisible() {
      this.isvisible = !this.isvisible;
    },
  },
};
</script>

<style>
* {
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}
</style>
