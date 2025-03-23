import { createApp } from 'vue'
import { createVuetify } from 'vuetify'
import 'vuetify/styles'
import App from './App.vue'
import router from './router'

const vuetify = createVuetify()

const app = createApp(App)

app.use(router)
app.use(vuetify)

app.mount('#app')
