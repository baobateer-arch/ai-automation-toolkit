<template>
  <div class="auth-page">
    <div class="auth-card">
      <router-link to="/" class="auth-logo">Contract Risk AI</router-link>
      <h1>Create Account</h1>
      <form @submit.prevent="handleRegister">
        <div class="form-group"><label>Email</label><input v-model="email" type="email" required placeholder="you@example.com" /></div>
        <div class="form-group"><label>Password</label><input v-model="password" type="password" required minlength="6" placeholder="At least 6 characters" /></div>
        <div class="form-group"><label>Confirm</label><input v-model="confirm" type="password" required placeholder="Confirm password" /></div>
        <p v-if="error" class="auth-error">{{ error }}</p>
        <button type="submit" class="btn btn-primary btn-full" :disabled="loading"><span v-if="loading" class="spinner"></span><span v-else>Create Account</span></button>
      </form>
      <p class="auth-link">Already have an account? <router-link to="/login">Sign in</router-link></p>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import request from '../api/request.js'
const router = useRouter()
const email = ref(''); const password = ref(''); const confirm = ref(''); const error = ref(''); const loading = ref(false)
async function handleRegister() {
  if (!email.value || !password.value) { error.value = 'Email and password are required'; return }
  if (password.value.length < 6) { error.value = 'Password must be at least 6 characters'; return }
  if (password.value !== confirm.value) { error.value = 'Passwords do not match'; return }
  loading.value = true; error.value = ''
  try {
    const res = await request.post('/auth/register', { email: email.value, password: password.value })
    localStorage.setItem('token', res.data.access_token)
    localStorage.setItem('user_email', email.value)
    router.push('/dashboard')
  } catch (err) { error.value = err.response?.data?.detail || 'Registration failed' }
  finally { loading.value = false }
}
</script>
<style scoped>
.auth-page{min-height:100vh;display:flex;align-items:center;justify-content:center;background:#f8fafc;padding:20px}
.auth-card{background:#fff;border-radius:16px;padding:40px;width:100%;max-width:400px;box-shadow:0 1px 3px rgba(0,0,0,.06);border:1px solid #e2e8f0}
.auth-logo{display:block;text-align:center;font-weight:700;font-size:18px;color:#0f172a;text-decoration:none;margin-bottom:24px}
.auth-card h1{font-size:24px;font-weight:700;text-align:center;margin-bottom:24px}
.form-group{margin-bottom:16px}
.form-group label{display:block;font-size:14px;font-weight:500;margin-bottom:6px;color:#0f172a}
.form-group input{width:100%;padding:10px 14px;border:1px solid #e2e8f0;border-radius:8px;font-size:14px;outline:none;transition:border-color .15s;box-sizing:border-box}
.form-group input:focus{border-color:#2563eb}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:10px 24px;border-radius:8px;font-size:14px;font-weight:600;border:none;cursor:pointer;transition:all .15s;line-height:1;text-decoration:none}
.btn-primary{background:#2563eb;color:#fff}
.btn-primary:hover{background:#1d4ed8}
.btn:disabled{opacity:.5;cursor:not-allowed}
.btn-full{width:100%}
.auth-error{color:#dc2626;font-size:14px;margin-bottom:12px;text-align:center}
.auth-link{text-align:center;margin-top:20px;font-size:14px;color:#64748b}
.auth-link a{color:#2563eb;text-decoration:none;font-weight:500}
.spinner{display:inline-block;width:16px;height:16px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:spin .6s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
