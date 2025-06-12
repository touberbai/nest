<script setup lang="ts">
import LayoutNavigation from '@/layouts/modules/navigation.vue'
import { useRoute } from 'vue-router'
import { ref } from 'vue'

const route = useRoute()
const hideNavigation = ref(false)
// 路由元信息中如果hideNavigation为true则不显示导航栏
if (route.meta.hideNavigation) {
  hideNavigation.value = true
}
</script>

<template>
<div
  class="layouts_blog"
>
  <LayoutNavigation
    v-if="hideNavigation === false"
  ></LayoutNavigation>
  <div
    class="container"
  >
    <RouterView></RouterView>
  </div>
</div>
</template>

<style scoped>

</style>
