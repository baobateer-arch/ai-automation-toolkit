<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import request from "../api/request"


const router = useRouter()


const email = ref("")
const password = ref("")
const error = ref("")


async function login(){

  error.value=""

  try {

    const res = await request.post(
      "/api/auth/login",
      {
        email: email.value,
        password: password.value
      }
    )


    localStorage.setItem(
      "token",
      res.data.access_token
    )


    router.push("/dashboard")


  } catch(e){

    error.value =
      e.response?.data?.detail ||
      "登录失败"

  }

}

</script>


<template>

<div class="login">

<h1>AI Automation Toolkit</h1>

<h2>登录</h2>


<input
v-model="email"
placeholder="邮箱"
/>


<input
v-model="password"
type="password"
placeholder="密码"
/>


<button @click="login">
登录
</button>


<p v-if="error">
{{error}}
</p>


</div>

</template>