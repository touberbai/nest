/** ts-ignore */
import { defineStore } from 'pinia';
import { Editor } from '@tiptap/vue-3'
import { ref } from 'vue'
// 忽略下面一行的ts检查

export const useEditorStore = defineStore('editor', () => {
  const editor = ref<Editor | null>(null)

  const setEditor = (newEditor: Editor | null) => {
    editor.value = newEditor
  }

  return {
    editor,
    setEditor,
  }
})
