
import '@/styles/reset.css'
import '@/styles/app.scss'
import '@/styles/scss/flex.scss'
import '@/styles/scss/global.scss'
import '@/styles/scss/margin.scss'
import '@/styles/scss/padding.scss'
import 'element-plus/dist/index.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import routers from './routers'

// Vuetify
import vuetify from './plugins/vuetify'



const app = createApp(App)

app.use(vuetify)
app.use(createPinia())
app.use(routers)

app.mount('#app')
