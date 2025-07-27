<template>
  <div class="fixed inset-0 bg-black/70 flex items-center justify-center z-50">
    <div class="bg-white rounded-xl shadow-lg p-6 max-w-md w-full">
      <h2 class="text-lg font-bold mb-4">🎨 Chagua Mandhari</h2>
      <div class="flex justify-between gap-3">
        <button @click="applyTheme('light')" class="px-4 py-2 bg-yellow-200 text-black rounded">☀️ Light</button>
        <button @click="applyTheme('dark')" class="px-4 py-2 bg-gray-800 text-white rounded">🌙 Dark</button>
        <button @click="applyTheme('colorful')" class="px-4 py-2 bg-gradient-to-r from-pink-500 to-blue-500 text-white rounded">🌈 Fun</button>
      </div>
      <div class="mt-4 text-right">
        <button @click="$emit('close')" class="text-sm text-gray-600 hover:text-black">✖️ Funga</button>
      </div>
    </div>
  </div>
</template>

<script setup>
function applyTheme(theme) {
  // Placeholder: You can save this in localStorage or a global state
  console.log("Theme selected:", theme)
}
</script>
