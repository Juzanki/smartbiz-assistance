// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// === Styles ===
import 'uno.css'
import './style.css'

// === Optional Plugins (tayari kwa matumizi ya baadaye) ===
import { createPinia } from 'pinia'
import { createI18n } from 'vue-i18n'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'

// === Initialize App ===
const app = createApp(App)

// === Global Plugins ===
app.use(router)
app.use(createPinia())

// === I18n (Multilingual Ready)
const i18n = createI18n({
  locale: 'en',
  fallbackLocale: 'en',
  messages: {} // utaweka lugha baadaye
})
app.use(i18n)

// === Toast Notification Options
const toastOptions = {
  timeout: 3500,
  position: 'top-right',
  closeOnClick: true,
  pauseOnFocusLoss: true,
  pauseOnHover: true
}
app.use(Toast, toastOptions)

// === Mount App ===
app.mount('#app')
