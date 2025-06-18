<script setup lang="ts">
const props = defineProps<{
  switchDialog: {
    type: Boolean,
    default: false,
  }
}>()
</script>

<template>
<v-dialog
  v-model="props.switchDialog"
  width="auto"
>
  <v-date-picker
    header="h"
    title="t"
    elevation="24"
  ></v-date-picker>
</v-dialog>
</template>

<style scoped>

</style>
