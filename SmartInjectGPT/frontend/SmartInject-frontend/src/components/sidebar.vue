<template>
  <aside class="w-full md:w-64 bg-[#0e1a2b] text-white min-h-screen shadow-lg p-4 space-y-4">
    <h2 class="text-lg font-bold text-yellow-400 mb-2">🧠 SmartInjectGPT</h2>

    <ul class="space-y-2 text-sm">
      <li v-for="link in links" :key="link.name">
        <router-link
          :to="link.path"
          class="block px-3 py-2 rounded hover:bg-blue-600"
          :class="{ 'bg-blue-700 font-bold': $route.path === link.path }"
        >
          {{ link.icon }} {{ link.name }}
        </router-link>
      </li>
    </ul>
  </aside>
</template>

<script setup>
const links = [
  { name: 'Dashboard', path: '/dashboardOwner', icon: '🏠' },
  { name: 'Vision Console', path: '/vision-console', icon: '🔭' },
  { name: 'AI Chatbot', path: '/ai-chatbot', icon: '🤖' },
  { name: 'Dream Trigger', path: '/dream-trigger', icon: '🌌' },
  { name: 'Kernel Monitor', path: '/kernel-monitor', icon: '🧬' },
  { name: 'Prompt History', path: '/prompt-history', icon: '📜' },
  { name: 'Inject Page', path: '/inject-page', icon: '💉' },
  { name: 'Logs', path: '/logs', icon: '📄' },
  { name: 'Shield Page', path: '/shield-page', icon: '🛡️' },
  { name: 'System Settings', path: '/settings', icon: '⚙️' },
  { name: 'Logout', path: '/logout', icon: '🚪' }
  { name: 'Admin Dashboard', path: '/admin', icon: '🛠' }

]
</script>

<style scoped>
.router-link-exact-active {
  font-weight: bold;
  background-color: #1b3a57;
}
</style>
