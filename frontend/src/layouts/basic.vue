<script setup lang="ts">
import LayoutNavigation from '@/layouts/modules/navigation.vue'

</script>

<template>
<div
  class="layouts_basic"
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
.layouts_basic {
  position: relative;
}
</style>
