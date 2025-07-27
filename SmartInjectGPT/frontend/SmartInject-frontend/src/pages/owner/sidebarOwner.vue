<template>
  <aside class="h-screen w-64 bg-dark-800 text-light flex flex-col border-r border-yellow-400">
    <!-- Logo -->
    <div class="flex items-center justify-center py-6 border-b border-gray-700">
      <img src="/logo.png" alt="Logo" class="w-10 h-10 rounded-full mr-2" />
      <span class="text-yellow-400 font-bold text-xl">SmartInjectGPT</span>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 overflow-y-auto">
      <ul class="list-unstyled px-4 py-4 space-y-2">
        <li>
          <router-link to="/dashboardOwner" class="nav-link" active-class="text-yellow-400 font-bold">
            🧭 Dashboard
          </router-link>
        </li>
        <li>
          <router-link to="/manage-admins" class="nav-link" active-class="text-yellow-400 font-bold">
            👥 Manage Admins
          </router-link>
        </li>
        <li>
          <router-link to="/otp-logs" class="nav-link" active-class="text-yellow-400 font-bold">
            🔐 OTP Logs
          </router-link>
        </li>
        <li>
          <router-link to="/activity-logs" class="nav-link" active-class="text-yellow-400 font-bold">
            📜 Activity Logs
          </router-link>
        </li>
        <li>
          <router-link to="/security-panel" class="nav-link" active-class="text-yellow-400 font-bold">
            🛡 Security Panel
          </router-link>
        </li>
        <li>
          <router-link to="/settings" class="nav-link" active-class="text-yellow-400 font-bold">
            ⚙️ System Settings
          </router-link>
        </li>
        <li>
          <router-link to="/logout" class="nav-link text-red-500 hover:text-red-400">
            🚪 Logout
          </router-link>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script setup>
// Sidebar simple static navigation for owner
</script>

<style scoped>
.nav-link {
  display: block;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  transition: background 0.2s;
  color: #e0e0e0;
}

.nav-link:hover {
  background-color: #2c3e50;
  color: #f1c40f;
}
</style>
