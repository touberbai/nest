<script setup lang="ts">
import { onMounted } from 'vue'
import { post } from '@/utils/request'
onMounted(() => {
  post({
    url: '/api/future/all_boll',
  })
})
</script>

<template>

</template>

<style scoped>

</style>
