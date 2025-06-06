<script setup lang="ts">
import { useUserStore } from '@/stores/user.ts'
const userStore = useUserStore()
import { storeToRefs } from 'pinia'
const {
  user,
} = storeToRefs(userStore)
</script>

<template>
<div
  class="layouts_modules_navigation user-select-none"
>
  <div
    class="container d-flex align-center justify-space-between"
  >
    <div
      class="logo_wrapper"
    >
      <div
        class="logo_group"
      >
        <div
          class="name"
        >
          NEST
        </div>
      </div>
    </div>
  <!--  登录用户信息 -->
    <div
      class="user_info_group d-flex align-center"
    >
      <div
        class="name"
      >
        {{ user.email }}
      </div>
      <div
        class="logout"
      >
        logout
      </div>
    </div>
  </div>
</div>
</template>

<style scoped>
.layouts_modules_navigation {
  background-color: rgba(250, 250, 250, 0.7);
  height: 60px;
  color: #333;
  .container {
    width: 100%;
    padding: 0 40px;
    height: 100%;
    .logo_wrapper {
      .logo_group {
        .name {
          font-weight: bold;
          font-size: 20px;
        }
      }
    }
    .user_info_group {
      .name {
        margin-right: 10px;
      }
      .logout {
        font-size: 13px;

      }
    }
  }
}
</style>
