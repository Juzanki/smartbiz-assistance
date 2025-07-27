<template>
  <div class="min-h-screen bg-[#0d1b2a] text-white p-6">
    <h1 class="text-2xl font-bold text-yellow-400 mb-6">Security Panel</h1>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- MFA Setting -->
      <div class="bg-[#1b263b] p-4 rounded-xl shadow">
        <h2 class="text-lg font-semibold text-yellow-300 mb-2">Multi-Factor Authentication (MFA)</h2>
        <label class="flex items-center gap-3">
          <input type="checkbox" v-model="settings.mfa_enabled" class="accent-yellow-400 scale-125" />
          <span class="text-sm">Enable MFA for all admin logins</span>
        </label>
      </div>

      <!-- IP Whitelist -->
      <div class="bg-[#1b263b] p-4 rounded-xl shadow">
        <h2 class="text-lg font-semibold text-yellow-300 mb-2">Allowed IP Addresses</h2>
        <textarea
          v-model="settings.allowed_ips"
          placeholder="One IP per line"
          class="w-full h-24 p-2 rounded bg-[#0d1b2a] border border-yellow-500 text-sm"
        ></textarea>
      </div>

      <!-- Login Fail Limit -->
      <div class="bg-[#1b263b] p-4 rounded-xl shadow">
        <h2 class="text-lg font-semibold text-yellow-300 mb-2">Max Failed Login Attempts</h2>
        <input
          v-model="settings.max_login_failures"
          type="number"
          min="1"
          class="w-full p-2 rounded bg-[#0d1b2a] border border-yellow-500"
        />
      </div>

      <!-- Session Timeout -->
      <div class="bg-[#1b263b] p-4 rounded-xl shadow">
        <h2 class="text-lg font-semibold text-yellow-300 mb-2">Session Timeout (minutes)</h2>
        <input
          v-model="settings.session_timeout"
          type="number"
          min="1"
          class="w-full p-2 rounded bg-[#0d1b2a] border border-yellow-500"
        />
      </div>

      <!-- Auto Lock -->
      <div class="bg-[#1b263b] p-4 rounded-xl shadow">
        <h2 class="text-lg font-semibold text-yellow-300 mb-2">Auto Lock Inactivity</h2>
        <label class="flex items-center gap-3">
          <input type="checkbox" v-model="settings.auto_lock_enabled" class="accent-yellow-400 scale-125" />
          <span class="text-sm">Lock system after inactivity period</span>
        </label>
      </div>

      <!-- System Lockdown -->
      <div class="bg-red-900 p-4 rounded-xl shadow border border-red-400">
        <h2 class="text-lg font-bold text-red-300 mb-2">Emergency Lockdown Mode</h2>
        <p class="text-sm mb-2">Disable all logins and actions except for owner emergency access.</p>
        <button
          @click="toggleLockdown"
          class="bg-red-600 hover:bg-red-700 px-4 py-2 rounded font-bold text-white"
        >
          {{ settings.lockdown_mode ? 'Deactivate Lockdown' : 'Activate Lockdown' }}
        </button>
      </div>
    </div>

    <!-- Save Button -->
    <div class="mt-8">
      <button
        @click="saveSettings"
        class="bg-yellow-500 hover:bg-yellow-600 text-[#0d1b2a] px-6 py-2 rounded font-bold"
      >
        Save Changes
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const settings = ref({
  mfa_enabled: false,
  allowed_ips: '',
  max_login_failures: 5,
  session_timeout: 30,
  auto_lock_enabled: true,
  lockdown_mode: false,
})

const fetchSettings = async () => {
  try {
    const res = await axios.get('/api/security/settings')
    settings.value = res.data
  } catch (err) {
    console.error('Failed to fetch settings', err)
  }
}

const saveSettings = async () => {
  try {
    await axios.post('/api/security/settings', settings.value)
    alert('Settings saved successfully!')
  } catch (err) {
    alert('Failed to save settings.')
  }
}

const toggleLockdown = () => {
  settings.value.lockdown_mode = !settings.value.lockdown_mode
}

onMounted(fetchSettings)
</script>

<style scoped>
input[type='checkbox'] {
  cursor: pointer;
}
</style>
