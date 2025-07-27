<template>
  <div :class="themeClass" class="d-flex min-vh-100">

    <!-- Sidebar Navigation -->
    <transition name="slide">
      <aside v-if="sidebarOpen" class="sidebar shadow-lg p-4 bg-dark border-end border-warning">
        <h5 class="text-warning fw-bold mb-4">☰ Owner Controls</h5>
        <ul class="nav flex-column gap-2">
          <li
            v-for="page in pages"
            :key="page.name"
            class="nav-item"
          >
            <a
              @click="navigate(page.route)"
              class="nav-link cursor-pointer"
              :class="{
                'text-warning fw-bold': page.route === $route.path,
                'text-light': page.route !== $route.path
              }"
            >
              {{ page.name }}
            </a>
          </li>
        </ul>
      </aside>
    </transition>

    <!-- Main Content -->
    <div class="flex-grow-1 d-flex flex-column p-4">

      <!-- Header -->
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div class="d-flex align-items-center gap-3">
          <button @click="sidebarOpen = !sidebarOpen" class="btn btn-outline-warning btn-sm">☰</button>
          <div>
            <h3 class="text-warning fw-bold m-0">SmartInjectGPT Owner</h3>
            <small class="text-muted">Secure Control Panel</small>
          </div>
        </div>
        <div class="d-flex align-items-center gap-2">
          <select v-model="theme" @change="switchTheme" class="form-select form-select-sm bg-dark text-light border-secondary">
            <option value="light">☀️ Light</option>
            <option value="dark">🌙 Dark</option>
          </select>
          <button class="btn btn-outline-danger btn-sm" @click="logout">Logout</button>
        </div>
      </header>

      <!-- AI Command Interface -->
      <main class="flex-grow-1">
        <div class="bg-black bg-opacity-50 rounded-4 p-4 shadow border border-warning">
          <h5 class="text-warning mb-3">🧠 AI Assistant</h5>
          <div class="chat-interface mb-3">
            <textarea
              v-model="ownerCommand"
              class="form-control bg-dark text-light border border-warning rounded"
              rows="3"
              placeholder="Give commands like 'List active admins' or 'Generate user report'..."
            ></textarea>
          </div>
          <div class="text-end">
            <button class="btn btn-warning px-4 fw-bold" @click="sendCommand">Send</button>
          </div>
          <div v-if="aiResponse" class="mt-3 alert alert-info">{{ aiResponse }}</div>
        </div>
      </main>

      <!-- Footer -->
      <footer class="text-center text-muted mt-4 small">
        © {{ year }} SmartInjectGPT — All rights reserved.
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const $route = useRoute()
const year = new Date().getFullYear()

const ownerCommand = ref('')
const aiResponse = ref('')
const theme = ref(localStorage.getItem('theme') || 'dark')
const themeClass = computed(() => theme.value === 'dark' ? 'theme-dark text-light bg-dark' : 'theme-light text-dark bg-light')
const sidebarOpen = ref(true)

const pages = [
  { name: 'Dashboard', route: '/dashboard-owner' },
  { name: 'Manage Admins', route: '/manage-admins' },
  { name: 'System Settings', route: '/settings' },
  { name: 'Activity Logs', route: '/activity-logs' },
  { name: 'API Usage Logs', route: '/logs' },
  { name: 'AI Bot Settings', route: '/ai-chatbot' }
]

const switchTheme = () => {
  localStorage.setItem('theme', theme.value)
  document.body.className = themeClass.value
}

const logout = () => {
  localStorage.clear()
  router.replace('/login')
}

const sendCommand = () => {
  if (!ownerCommand.value.trim()) {
    return alert('⚠️ Please enter a command')
  }
  aiResponse.value = `Processing your command: "${ownerCommand.value}"`
  ownerCommand.value = ''
}

const navigate = (route) => {
  if ($route.path !== route) {
    router.push(route)
  }
}

onMounted(() => {
  document.body.className = themeClass.value
})
</script>

<style scoped>
body {
  font-family: 'Fira Code', monospace;
  transition: all 0.3s ease-in-out;
}

.theme-dark {
  background-color: #0a0f1a;
}

.theme-light {
  background-color: #ffffff;
}

.sidebar {
  width: 260px;
  min-height: 100vh;
}

.chat-interface textarea::placeholder {
  color: #ccc;
  font-style: italic;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}
.slide-enter-from,
.slide-leave-to {
  transform: translateX(-100%);
  opacity: 0;
}
</style>
