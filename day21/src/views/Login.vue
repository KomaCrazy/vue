<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-sm"></div>
        <div class="col-sm border border-dark">
          <div v-if="login">
            <h3 class="p-2">Login</h3>
            <h4>
              {{ user }}
            </h4>
            <div class="row" id="page1">
              <div class="col-sm">User</div>
              <div class="col-sm"><input type="text" v-model="user" /></div>
            </div>
            <div class="row">
              <div class="col-sm">Password</div>
              <div class="col-sm"><input type="text" v-model="password" /></div>
            </div>
            <p></p>
            <b-button variant="outline-success" v-on:click="clickLogin()"
              >Login</b-button
            >
          </div>
          <!-- End page login-->

          <div v-else>
            <h3 class="p-2">Profile</h3>

            <div class="row">
              <div class="col-sm-4"></div>
              <div class="col-sm-1">Id</div>
              <div class="col-sm-3">{{ id }}</div>
            </div>

            <div class="row">
              <div class="col-sm-4"></div>
              <div class="col-sm-1">user</div>
              <div class="col-sm-4">{{ user }}</div>
            </div>

            <div class="row">
              <div class="col-sm-4"></div>
              <div class="col-sm-2">Email</div>
              <div class="col-sm-4">{{ email }}</div>
            </div>

            <p></p>
            <b-button variant="outline-success" v-on:click="clickLogout()"
              >logout</b-button
            >
          </div>
          <!-- End page login-->

          <p></p>
        </div>
        <div class="col-sm"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: "",
      password: "",
      email: "",
      id: "",
      age: "",
      login: true,
    };
  },
  mounted() {
    this.recon();
    console.log(this.$cookies.get("user"));
  },
  methods: {
    recon() {
      var check = this.$cookies.get("user");
      var re_user = this.$cookies.get("user");
      var re_password = this.$cookies.get("password");
      console.log(check);
      if (check != null) {
        console.log("not null");
        this.login = false;
        var url =
          "http://localhost:5000/login?user=" +
          re_user +
          "&password=" +
          re_password;
        fetch(url)
          .then((response) => response.json())
          .then((data) => this.share(data));
      } else {
        console.log("null");
      }
    },
    share(data) {
      this.id = data[0];
      this.user = data[1];
      this.password = data[2];
      this.email = data[3];
      this.age = data[4];
      this.login = false;
    },

    clickLogin() {
      this.$cookies.set("user", this.user);
      this.$cookies.set("password", this.password);
      this.$cookies.set("login", this.login);

      var url =
        "http://localhost:5000/login?user=" +
        this.user +
        "&password=" +
        this.password;
      fetch(url)
        .then((response) => response.json())
        .then((data) => this.share(data));
    },
    clickLogout() {
      console.log("logout!");
      this.$cookies.keys().forEach((cookie) => this.$cookies.remove(cookie));
      this.login = true;
    },
  },
};
</script>
