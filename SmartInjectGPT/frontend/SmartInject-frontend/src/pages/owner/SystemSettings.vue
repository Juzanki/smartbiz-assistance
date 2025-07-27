<template>
  <div class="min-h-screen p-6 bg-[#0f172a] text-white">
    <div class="max-w-2xl mx-auto bg-dark-800 rounded-2xl p-6 border border-yellow-500 shadow-xl">
      <h2 class="text-2xl font-bold text-yellow-400 mb-6">⚙️ System Settings</h2>

      <!-- Logo Upload -->
      <div class="mb-6">
        <label class="block text-sm mb-2">System Logo</label>
        <div class="flex items-center gap-4">
          <input type="file" accept="image/*" @change="onLogoChange" class="block w-full text-sm" />
          <img v-if="logoUrl" :src="logoUrl" class="w-16 h-16 object-cover rounded border border-yellow-400" />
        </div>
      </div>

      <!-- App Title -->
      <div class="mb-6">
        <label class="block text-sm mb-2">App Title</label>
        <input
          v-model="title"
          type="text"
          class="w-full p-2 bg-dark-700 text-white rounded border border-gray-600 focus:ring focus:ring-yellow-400"
          placeholder="SmartInjectGPT"
        />
      </div>

      <!-- Theme -->
      <div class="mb-6">
        <label class="block text-sm mb-2">Default Theme</label>
        <select
          v-model="theme"
          class="w-full p-2 bg-dark-700 text-white rounded border border-gray-600 focus:ring focus:ring-yellow-400"
        >
          <option value="auto">🌗 Auto</option>
          <option value="light">☀️ Light</option>
          <option value="dark">🌙 Dark</option>
        </select>
      </div>

      <button
        @click="saveSettings"
        class="bg-yellow-400 hover:bg-yellow-300 text-dark font-bold px-6 py-2 rounded transition w-full"
      >
        💾 Save Settings
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const title = ref('SmartInjectGPT')
const theme = ref('auto')
const logoUrl = ref('')

onMounted(() => {
  title.value = localStorage.getItem('app_title') || title.value
  theme.value = localStorage.getItem('app_theme') || 'auto'
  logoUrl.value = localStorage.getItem('app_logo') || '/logo.svg'
})

const onLogoChange = (e) => {
  const file = e.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (event) => {
      logoUrl.value = event.target.result
    }
    reader.readAsDataURL(file)
  }
}

const saveSettings = () => {
  localStorage.setItem('app_title', title.value)
  localStorage.setItem('app_theme', theme.value)
  localStorage.setItem('app_logo', logoUrl.value)
  alert('✅ Settings saved successfully!')
  location.reload()
}
</script>

<style scoped>
body {
  font-family: 'Fira Code', monospace;
}
</style>
