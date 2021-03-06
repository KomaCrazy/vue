import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import("../views/About.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () =>
      import("../views/login.vue"),
  },
  {
    path: "/user",
    name: "user",
    component: () =>
      import("../views/user.vue"),
  },

  {
    path: "/register",
    name: "register",
    component: () =>
      import("../views/resgister.vue"),
  },

];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
