import Vue from "vue";
import App from "./App.vue";
import router from "./router";

Vue.config.productionTip = false;


import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueCookies from 'vue-cookies'

Vue.use(VueCookies, { expire: '7d'})
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
