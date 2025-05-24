<script setup lang="ts">
import { ref } from 'vue'
// import { post } from '@/utils/request'
import { useUserStore } from '@/stores/user';

const userStore = useUserStore()

const username = ref('')
const email = ref('')
const password = ref('')
// 重复输入的密码
const password2 = ref('')

const pageMode = ref('login') // register 注册 forget 忘记密码


// 登录
const login = async () => {
  const res = await userStore.login(
    email.value,
    password.value
  )
  console.log(res)
  return
  // console.log('username', username.value)
  // console.log('pwd', password.value)
  // const res = await post({
  //   url: '/api/login',
  //   data: {
  //     username: "string",
  //     email: "u1ser@example.com",
  //     password: "string"
  //   }
  // })
}

const changePageMode = (mode: string) => {
  pageMode.value = mode
}
</script>

<template>
<div
  class="v_login_index d-flex align-center justify-center"
>
  <v-card
    loading
    class="login_wrapper"
    color="blue-grey"
  >
    <v-card-title
      class="text-center"
    >
      LOGIN
    </v-card-title>
    <v-card-text>
      <v-text-field
        v-model="email"
        label="Email"
        outlined
      />
      <v-text-field
        v-model="password"
        label="Password"
        outlined
        type="password"
      />
      <v-text-field
        v-show="pageMode === 'register'"
        v-model="password2"
        label="Password again"
        outlined
        type="password"
      />
    </v-card-text>
    <v-card-actions
      class="d-flex justify-space-between align-center"
    >
      <div
        class="d-flex"
      >
        <v-btn
          v-if="pageMode !== 'register'"
          variant="text"
          @click="changePageMode('register')"
        >Register</v-btn>
        <v-btn
          v-if="pageMode !== 'login'"
          variant="text"
          @click="changePageMode('login')"
        >Login</v-btn>
        <v-btn
          v-if="pageMode !== 'forget'"
          variant="text"
          @click="changePageMode('forget')"
        >Forget</v-btn>
      </div>

      <v-btn
        @click="login"
      >Submit</v-btn>
    </v-card-actions>
  </v-card>
  <el-card
    v-if="0"
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
  .login_wrapper {
    width: 420px;
  }
}
</style>
