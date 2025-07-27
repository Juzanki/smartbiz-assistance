<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
    <div class="bg-white rounded-xl shadow-lg p-6 w-full max-w-sm text-center">
      <h2 class="text-lg font-bold mb-4 text-black">🛑 End Stream?</h2>
      <p class="text-gray-700 mb-6">Are you sure you want to end your live stream?</p>
      <div class="flex justify-center gap-4">
        <button @click="cancel" class="px-4 py-2 bg-gray-300 hover:bg-gray-400 rounded text-sm">
          Cancel
        </button>
        <button @click="confirm" class="px-4 py-2 bg-red-600 hover:bg-red-500 text-white rounded text-sm">
          End Stream
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const emit = defineEmits(['confirm', 'cancel'])

function confirm() {
  emit('confirm')
}

function cancel() {
  emit('cancel')
}
</script>

<style scoped>
/* Optional: You can add transitions or animations */
</style>
