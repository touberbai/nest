<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps(
  {
    editor: {
      type: Object,
      required: true
    },
  }
)
const HeaderNumber = computed(() => {
  if (props.editor) {
    for(let i = 1; i <= 6; i++) {
      if (props.editor.isActive('heading', { level: i })) {
        return i
      }
    }
  }
  return ''
})
const headingItems = [
  {
    title: 'H1 Heading1',
    value: 1,
  },
  {
    title: 'H2 Heading2',
    value: 2,
  },
  {
    title: 'H3 Heading3',
    value: 3,
  },
  {
    title: 'H4 Heading4',
    value: 4,
  },
  {
    title: 'H5 Heading5',
    value: 5,
  },
  {
    title: 'H6 Heading6',
    value: 6,
  }
]
const selectHeading = (params: any) => {
  const {
    id,
  } = params
  props.editor.chain().focus().toggleHeading({ level: id }).run()
}
</script>

<template>
  <div
    class="heading_group d-flex align-center justify-center"
    :class="{
      on: props.editor.isActive('heading')
    }"
  >
    <div
      class="text"
    >
      H
    </div>
    <div
      v-if="HeaderNumber"
      class="number"
    >
      {{ HeaderNumber }}
    </div>
    <v-icon
      v-if="0"
      icon="mdi-menu-down"
    ></v-icon>
    <v-menu activator="parent">
      <v-list
        @click:select="selectHeading"
      >
        <v-list-item
          v-for="(item, index) in headingItems"
          :key="index"
          :title="item.title"
          :height="24"
          :min-height="24"
          class="list_item"
          color="purple"
          :value="item.value"
          :active="HeaderNumber === item.value"
        >
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<style scoped>
.heading_group {
  padding: 2px 0;
  width: 25px;
  background-color: #ccc;
  border-radius: 4px;
  color: #333;
  margin-right: 5px;
  .text {
    line-height: 24px;
  }
  .number {
    font-size: 10px;
    line-height: 16px;
    width: 5px;
    align-self: end;
  }
  &.on {
    background-color: #6a00f5;
    color: #fff;
  }
  .list_item {
    background-color: rgba(106, 0, 245, 0.3);
    &:hover {
      background-color: rgba(106, 0, 245, 0.3);
    }
  }
}
</style>
