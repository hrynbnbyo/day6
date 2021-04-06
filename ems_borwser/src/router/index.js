import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login";
import Register from "../components/Register";
import Index from "../components/Index";
import Update from "../components/Update";
import Add from "../components/Add";

Vue.use(Router)

export default new Router({
    routes: [
        {path: "/", component: Login},
        {path: "/login", component: Login},
        {path: "/register", component: Register},
        {path: "/index", component: Index},
        {path: "/update/:id", component: Update},
        {path: "/add", component: Add},
        {path: "/*", redirect: "/login"},
    ]
})
