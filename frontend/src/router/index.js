import { createRouter, createWebHistory } from "vue-router"
import ReportDetail from "../views/ReportDetail.vue"

import Login from "../views/Login.vue"
import Register from "../views/Register.vue"
import Dashboard from "../views/Dashboard.vue"


const router = createRouter({
  history: createWebHistory(),

 routes:[
    {
    path:"/",
    redirect:"/dashboard"
    },

    {
    path:"/login",
    component:Login
    },

    {
    path:"/register",
    component:Register
    },

    {
    path:"/dashboard",
    component:Dashboard
    },

    {
    path:"/report/:id",
    component:ReportDetail
    }

]
})


export default router