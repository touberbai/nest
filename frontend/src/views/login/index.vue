<script setup lang="ts">
import { ref } from 'vue'
import { post } from '@/utils/request'

const username = ref('')
const pwd = ref('')

// 登录
const login = async () => {
  console.log('username', username.value)
  console.log('pwd', pwd.value)
  const res = await post({
    url: '/api/login',
    data: {
      username: "string",
      email: "u1ser@example.com",
      password: "string"
    }
  })
}
</script>

<template>
<div
  class="v_login_index d-flex align-center justify-center"
>
  <v-card
    loading
    color="blue-grey"
  >
    <v-card-title
      class="text-center"
    >
      LOGIN
    </v-card-title>
    <v-card-actions>
      <v-btn>Click me</v-btn>
    </v-card-actions>
  </v-card>
  <el-card
    style="max-width: 480px"
    shadow="hover"
  >
    <template #header>
      <div class="card-header">
        <span>Login</span>
      </div>
    </template>
    <el-input
      class="mb-5 input"
      v-model="username"
      style="width: 240px"
      placeholder="Please input"
    />
    <el-input
      class="mb-5 input"
      v-model="pwd"
      style="width: 240px"
      placeholder="Please input"
      type="password"
    />
    <template #footer>
      <div class="footer_wrapper d-flex justify-end">
        <el-button>
          Cancel
        </el-button>
        <el-button
          type="primary"
          @click="login"
        >
          Enter
        </el-button>
      </div>
    </template>
  </el-card>
</div>
</template>

<style scoped>
.v_login_index {
  width: 100%;
  height: 100%;
  .input {
    width: 100%!important;
  }
}
</style>
