<script setup lang="ts">
const props = defineProps(
  {
    editor: {
      type: Object,
      required: true
    },
    level: {
      type: Number,
      default: 1,
      required: true
    }
  }
)


</script>

<template>
  <button
    @click="props.editor.chain().focus().toggleHeading({ level: props.level }).run()"
    :class="{ 'is-active': props.editor.isActive('heading', { level: props.level }) }"
  >
    H{{ props.level }}
  </button>
</template>

<style scoped>

</style>
