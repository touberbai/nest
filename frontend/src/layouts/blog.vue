<script setup lang="ts">
import LayoutNavigation from '@/layouts/modules/navigation.vue'

</script>

<template>
<div
  class="layouts_blog"
>
  <LayoutNavigation></LayoutNavigation>
  <div
    class="container"
  >
    <RouterView></RouterView>
  </div>
</div>
</template>

<style scoped>

</style>
