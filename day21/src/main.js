import Vue from "vue";
import App from "./App.vue";
import router from "./router";
Vue.use(require("vue-cookies"));

// es2015 module
import VueCookies from "vue-cookies";

Vue.use(VueCookies, { expire: "7d" });

import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
