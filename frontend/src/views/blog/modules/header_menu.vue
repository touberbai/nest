<script setup lang="ts">
import Heading from '@/views/blog/modules/header/heading.vue'
import HeadingGroup from '@/views/blog/modules/header/heading_group.vue'
import { useEditorStore } from '@/stores/editor.ts'

const editorStore = useEditorStore()
// 获取editorStore中的editor实例
const editor = editorStore.editor

// const props = defineProps({
//   editor: {
//     type: Object,
//     required: true
//   },
// })

const touchSave = () => {
  console.log(editor, editor.getJSON)
  if (!editor) {
    return
  }
  try {
    const json = editor.getJSON()
    console.log(json)
    console.log(JSON.stringify(json))
  } catch (error) {
    console.log(error)
  }
}
</script>

<template>
<div
  v-if="editor"
  class="blog_modules_header d-flex align-center justify-space-between user-select-none"
>
  <div
    class="operation_wrapper d-flex align-center"
  >
    <Heading
      :editor="editor"
      :level="1"
    ></Heading>
    1
    <HeadingGroup
      :editor="editor"
    ></HeadingGroup>
  </div>
  <div
    class="function_wrapper d-flex align-center"
  >
    <div
      class="btn"
      @click="touchSave"
    >
      Save
    </div>
  </div>



</div>
</template>

<style lang="scss">
.blog_modules_header {
  button {
    padding: 2px 5px;
    background-color: #ccc;
    border-radius: 4px;
    color: #333;
    margin-right: 5px;
    &.is-active {
      background-color: #6a00f5;
      color: #fff;
    }
  }
  .function_wrapper {
    .btn {
      margin-left: 5px;
      cursor: pointer;
      height: 28px;
      line-height: 28px;
      font-size: 14px;
      background-color: #ccc;
      border-radius: 4px;
      padding: 0 5px;
    }
  }
}
</style>
