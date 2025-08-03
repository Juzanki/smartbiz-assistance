<template>
  <div class="d-flex flex-column flex-md-row min-vh-100 bg-light">
    <!-- Sidebar (Collapsible on mobile) -->
    <aside
      class="d-flex flex-column p-3 bg-primary text-white w-100 w-md-25"
      style="max-width: 260px"
    >
      <!-- Brand Name -->
      <div class="d-flex align-items-center justify-content-between mb-3">
        <span class="fs-4 fw-bold">SmartBiz</span>
      </div>
      <hr class="border-light" />
      <ul class="nav flex-column mb-auto">
        <li v-for="link in navLinks" :key="link.name" class="nav-item">
          <router-link
            :to="link.path"
            class="nav-link text-white d-flex align-items-center gap-2"
            active-class="active"
          >
            <span>{{ link.icon }}</span>
            <span class="d-none d-md-inline">{{ $t(link.name) }}</span>
          </router-link>
        </li>
      </ul>
      <hr class="border-light" />
      <div class="text-center small">
        &copy; {{ new Date().getFullYear() }} SmartBiz
      </div>
    </aside>

    <!-- Main Content -->
    <div class="flex-grow-1 p-3 p-md-4">
      <!-- Top Header -->
      <div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <h2 class="text-primary fw-bold text-center text-md-start w-100 w-md-auto">
          👤 {{ $t('dashboard') }} – {{ user.value?.name || $t('user') }}
        </h2>
        <div class="d-flex align-items-center gap-2">
          <span class="text-muted small">{{ user.value?.name || $t('user') }}</span>
          <div
            class="rounded-circle bg-secondary text-white d-flex align-items-center justify-content-center"
            style="width: 36px; height: 36px"
          >
            {{ user.value?.name?.charAt(0)?.toUpperCase() || 'U' }}
          </div>
        </div>
      </div>

      <!-- Quick Stats -->
      <div class="row g-3 mb-4">
        <div class="col-6 col-md-4" v-for="stat in stats" :key="stat.title">
          <div class="card shadow-sm text-center p-3">
            <div class="fs-2">{{ stat.icon }}</div>
            <h6 class="fw-bold my-2">{{ $t(stat.title) }}</h6>
            <p class="fs-5 text-primary">{{ stat.value }}</p>
          </div>
        </div>
      </div>

      <!-- Platform Connections -->
      <div class="card shadow-sm p-4 mb-4">
        <h5 class="text-primary fw-bold mb-3">🔗 {{ $t('platform_connections') }}</h5>
        <div class="row g-2 g-md-3">
          <div class="col-6 col-md-3" v-for="platform in platforms" :key="platform.name">
            <div class="card text-center p-2 p-md-3 h-100">
              <div class="fs-4">{{ platform.icon }}</div>
              <h6 class="my-1">{{ $t(platform.name) }}</h6>
              <small :class="platform.connected ? 'text-success' : 'text-danger'">
                {{ platform.connected ? 'Connected' : 'Disconnected' }}
              </small>
            </div>
          </div>
        </div>
      </div>

      <!-- Recent Messages -->
      <div class="card shadow-sm p-4 mb-4">
        <h5 class="text-primary fw-bold mb-3">💬 {{ $t('recent_messages') }}</h5>
        <div class="table-responsive">
          <table class="table table-striped align-middle text-sm">
            <thead class="table-light">
              <tr>
                <th>{{ $t('platform') }}</th>
                <th>{{ $t('sender') }}</th>
                <th>{{ $t('message') }}</th>
                <th>{{ $t('timestamp') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="message in recentMessages" :key="message.id">
                <td>{{ message.platform.icon }} {{ $t(message.platform.name) }}</td>
                <td>{{ message.sender }}</td>
                <td>{{ message.text }}</td>
                <td class="text-muted">{{ message.timestamp }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// 🔐 Redirect if not authenticated
onMounted(() => {
  const token = localStorage.getItem('access_token')
  if (!token) router.replace('/login')
})

// 👤 User data from localStorage
const user = ref({
  name: localStorage.getItem('user_name') || 'User'
})

// 📚 Navigation Links
const navLinks = [
  { name: 'dashboard', path: '/dashboard/user', icon: '🏠' },
  { name: 'customers', path: '/customers', icon: '👥' },
  { name: 'products', path: '/products', icon: '🛒' },
  { name: 'orders', path: '/orders', icon: '📦' },
  { name: 'messaging_center', path: '/messaging-center', icon: '✉️' },
  { name: 'scheduled_promotions', path: '/scheduled-promotions', icon: '📅' },
  { name: 'support', path: '/support', icon: '🆘' },
  { name: 'affiliate_dashboard', path: '/affiliate', icon: '🤝' },
  { name: 'live_stream', path: '/live-stream', icon: '📺' },
  { name: 'drone_tracking', path: '/drones/missions', icon: '🚁' },
  { name: 'analytics', path: '/analytics', icon: '📊' },
  { name: 'settings', path: '/settings', icon: '⚙️' },
  { name: 'profile', path: '/profile', icon: '👤' },
  { name: 'notifications', path: '/notifications', icon: '🔔' },
  { name: 'loyalty_rewards', path: '/loyalty', icon: '🎁' },
  { name: 'help', path: '/help', icon: '❓' },
  { name: 'billing', path: '/billing', icon: '💳' },
  { name: 'activity_log', path: '/my-logs', icon: '📜' },
  { name: 'smart_assistant', path: '/assistant', icon: '🤖' }
]

// 📊 Dashboard Stats
const stats = [
  { title: 'messages_sent', value: '2,543', icon: '📨' },
  { title: 'active_platforms', value: '3/5', icon: '🔌' },
  { title: 'response_rate', value: '89%', icon: '🚀' }
]

// 🔗 Platforms Connection Status
const platforms = [
  { name: 'whatsapp', icon: '📱', connected: true },
  { name: 'telegram', icon: '✈️', connected: true },
  { name: 'sms', icon: '📲', connected: false },
  { name: 'email', icon: '📧', connected: true }
]

// 💬 Recent Messages
const recentMessages = [
  {
    id: 1,
    platform: { name: 'whatsapp', icon: '📱' },
    sender: '+255 712 345 678',
    text: 'Hello, I need support!',
    timestamp: '2 min ago'
  },
  {
    id: 2,
    platform: { name: 'email', icon: '📧' },
    sender: 'john@company.com',
    text: 'Order confirmation',
    timestamp: '1 hour ago'
  },
  {
    id: 3,
    platform: { name: 'telegram', icon: '✈️' },
    sender: '@johndoe',
    text: 'Bot not working',
    timestamp: '3 hours ago'
  }
]
</script>
<style scoped>
/* 🔆 Active Nav Highlight */
.active {
  background-color: #FFD600;
  color: #181829 !important;
  font-weight: 600;
  border-radius: 6px;
  padding: 0.4rem 0.75rem;
  transition: background-color 0.3s ease;
}

/* 📱 Mobile Friendly Adjustments */
@media (max-width: 768px) {
  .active {
    font-size: 0.95rem;
    padding: 0.5rem 1rem;
  }
}
</style>
