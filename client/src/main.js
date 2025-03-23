import '@mdi/font/css/materialdesignicons.css'
import '@mdi/font/css/materialdesignicons.min.css'
import { createApp } from 'vue'
import { createVuetify } from 'vuetify'
import * as mdi from 'vuetify/lib/iconsets/mdi'
import 'vuetify/styles'
import App from './App.vue'
import router from './router'


const vuetify = createVuetify({
  icons: {
    defaultSet: 'mdi', // Use the mdi icon set
    sets: {
      mdi,
    },
  },
})

const app = createApp(App)

app.use(router)
app.use(vuetify)

app.mount('#app')
