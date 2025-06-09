// src/plugins/vuetify.js
import '@mdi/font/css/materialdesignicons.css'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components' // 无需手动导入具体组件
import * as directives from 'vuetify/directives' // 无需手动导入具体指令
import 'vuetify/_styles.scss' // 引入核心样式

export default createVuetify({
  components, // 自动导入使用到的组件
  directives, // 自动导入使用到的指令
  icons: {
    defaultSet: 'mdi',
  }
})
