<script setup lang="ts">
import { EditorContent, Editor } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import Highlight from '@tiptap/extension-highlight'
// import Code from '@tiptap/extension-code'
// import Document from '@tiptap/extension-document'
// import Paragraph from '@tiptap/extension-paragraph'
// import Text from '@tiptap/extension-text'
import Typography from '@tiptap/extension-typography'
import { ref, onBeforeUnmount, onMounted } from 'vue'
import { ColorHighlighter } from '@/plugins/tiptap/ColorHighlighter.ts'
import { SmilieReplacer } from '@/plugins/tiptap/SmilieReplacer.ts'
import EditorHeaderMenu from '@/views/blog/modules/header_menu.vue'
import { useEditorStore } from '@/stores/editor.ts'
const editorStore = useEditorStore()

const editor = ref<Editor>()

// const editor = useEditor({
//   extensions: [
//     StarterKit,
//     Highlight,
//     Typography,
//   ],
//   content: `
//         <p>
//           Markdown shortcuts make it easy to format the text while typing.
//         </p>
//         <p>
//           To test that, start a new line and type <code>#</code> followed by a space to get a heading. Try <code>#</code>, <code>##</code>, <code>###</code>, <code>####</code>, <code>#####</code>, <code>######</code> for different levels.
//         </p>
//         <p>
//           Those conventions are called input rules in Tiptap. Some of them are enabled by default. Try <code>></code> for blockquotes, <code>*</code>, <code>-</code> or <code>+</code> for bullet lists, or <code>\`foobar\`</code> to highlight code, <code>~~tildes~~</code> to strike text, or <code>==equal signs==</code> to highlight text.
//         </p>
//         <p>
//           You can overwrite existing input rules or add your own to nodes, marks and extensions.
//         </p>
//         <p>
//           For example, we added the <code>Typography</code> extension here. Try typing <code>(c)</code> to see how it’s converted to a proper © character. You can also try <code>-></code>, <code>>></code>, <code>1/2</code>, <code>!=</code>, or <code>--</code>.
//         </p>
//       `,
// })

onMounted(() => {
  editor.value = (new Editor({
    extensions: [
      StarterKit,
      Highlight,
      Typography,
      // Code,
      // Document,
      // Paragraph,
      // Text,
      ColorHighlighter,
      SmilieReplacer,
    ],
    // editable: false,
    content: `
      <p>
        → With the Typography extension, Tiptap understands »what you mean« and adds correct characters to your text — it’s like a “typography nerd” on your side.
      </p>
      <p>
        Try it out and type <code>(c)</code>, <code>-></code>, <code>>></code>, <code>1/2</code>, <code>!=</code>, <code>--</code> or <code>1x1</code> here:
      </p>
      <p></p>
      <p>
        Or add completely custom input rules. We added a custom extension here that replaces smilies like <code>:-)</code>, <code><3</code> or <code>>:P</code> with emojis. Try it out:
      </p>
      <p></p>
      <p>
        You can also teach the editor new things. For example to recognize hex colors and add a color swatch on the fly: #FFF, #0D0D0D, #616161, #A975FF, #FB5151, #FD9170, #FFCB6B, #68CEF8, #80cbc4, #9DEF8F
      </p>
      <p>
        Markdown shortcuts make it easy to format the text while typing.
      </p>
      <p>
        To test that, start a new line and type <code>#</code> followed by a space to get a heading. Try <code>#</code>, <code>##</code>, <code>###</code>, <code>####</code>, <code>#####</code>, <code>######</code> for different levels.
      </p>
      <p>
        Those conventions are called input rules in Tiptap. Some of them are enabled by default. Try <code>></code> for blockquotes, <code>*</code>, <code>-</code> or <code>+</code> for bullet lists, or <code>\`foobar\`</code> to highlight code, <code>~~tildes~~</code> to strike text, or <code>==equal signs==</code> to highlight text.
      </p>
      <p>
        You can overwrite existing input rules or add your own to nodes, marks and extensions.
      </p>
      <p>
        For example, we added the <code>Typography</code> extension here. Try typing <code>(c)</code> to see how it’s converted to a proper © character. You can also try <code>-></code>, <code>>></code>, <code>1/2</code>, <code>!=</code>, or <code>--</code>.
      </p>
    `,
  }))

  editorStore.setEditor(editor.value)

})

onBeforeUnmount(() => {
  if (editor.value) {
    editor.value.destroy()
  }
})
</script>

<template>
<div
  class="blog_editor"
>
  <EditorHeaderMenu
    v-if="editor"
    class="editor_header_menu"
    :editor="editor"
  ></EditorHeaderMenu>
  <editor-content
    :editor="editor"
    class="ProseMirror-focused"
  />
</div>
</template>

<style scoped lang="scss">
.blog_editor {
  .editor_header_menu {
    width: 100%;
    padding: 0 20px;
  }
}

</style>

<style lang="scss">
.tiptap {
  outline: none;

  :first-child {
    margin-top: 0;
  }
  /* Code and preformatted text styles */
  code {
    background-color: var(--purple-light);
    border-radius: 0.4rem;
    color: var(--black);
    font-size: 0.85rem;
    padding: 0.25em 0.3em;
  }

  /* Color swatches */
  .color {
    white-space: nowrap;

    &::before {
      background-color: var(--color);
      border: 1px solid rgba(128, 128, 128, 0.3);
      border-radius: 2px;
      content: ' ';
      display: inline-block;
      height: 1em;
      margin-bottom: 0.15em;
      margin-right: 0.1em;
      vertical-align: middle;
      width: 1em;
    }
  }
  /* List styles */
  ul,
  ol {
    padding: 0 1rem;
    margin: 1.25rem 1rem 1.25rem 0.4rem;

    li p {
      margin-top: 0.25em;
      margin-bottom: 0.25em;
    }
  }

  /* Heading styles */
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    line-height: 1.1;
    margin-top: 2.5rem;
    text-wrap: pretty;
  }

  h1,
  h2 {
    margin-top: 3.5rem;
    margin-bottom: 1.5rem;
  }

  h1 {
    font-size: 1.4rem;
  }

  h2 {
    font-size: 1.2rem;
  }

  h3 {
    font-size: 1.1rem;
  }

  h4,
  h5,
  h6 {
    font-size: 1rem;
  }

  /* Code and preformatted text styles */
  code {
    background-color: var(--purple-light);
    border-radius: 0.4rem;
    color: var(--black);
    font-size: 0.85rem;
    padding: 0.25em 0.3em;
  }

  pre {
    background: var(--black);
    border-radius: 0.5rem;
    color: var(--white);
    font-family: 'JetBrainsMono', monospace;
    margin: 1.5rem 0;
    padding: 0.75rem 1rem;

    code {
      background: none;
      color: inherit;
      font-size: 0.8rem;
      padding: 0;
    }
  }

  mark {
    background-color: #FAF594;
    border-radius: 0.4rem;
    box-decoration-break: clone;
    padding: 0.1rem 0.3rem;
  }

  blockquote {
    border-left: 3px solid var(--gray-3);
    margin: 1.5rem 0;
    padding-left: 1rem;
  }

  hr {
    border: none;
    border-top: 1px solid var(--gray-2);
    margin: 2rem 0;
  }
}

</style>
