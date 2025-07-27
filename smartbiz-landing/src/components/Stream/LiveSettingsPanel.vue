<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
    <div class="w-full max-w-3xl bg-white rounded-3xl shadow-2xl p-6 relative animate-fade-in space-y-6">
      <!-- Header -->
      <div class="flex items-center justify-between">
        <h2 class="text-2xl font-bold text-indigo-700 flex items-center gap-2">
          ⚙️ Live Stream Settings
        </h2>
        <button @click="$emit('close')" class="text-red-500 text-2xl hover:text-red-700">✖</button>
      </div>

      <!-- Terms Acknowledgment -->
      <div class="bg-indigo-50 border border-indigo-200 rounded-xl p-4">
        <h3 class="text-lg font-semibold text-indigo-700 mb-2">📜 Terms & Community Guidelines</h3>
        <ul class="text-sm text-gray-700 list-disc pl-5 space-y-1">
          <li>No nudity or sexually explicit content</li>
          <li>No hate speech, bullying, or harassment</li>
          <li>Respect all users regardless of race, religion, or identity</li>
          <li>No illegal activity or promotions</li>
          <li>Follow all applicable national laws and digital ethics</li>
        </ul>
        <div class="mt-4 flex items-center gap-3">
          <input type="checkbox" id="agree" v-model="agreed" />
          <label for="agree" class="text-sm text-gray-800">
            I have read and agree to the <a href="#" class="text-indigo-600 underline">Terms and Community Policy</a>.
          </label>
        </div>
      </div>

      <!-- Camera & Audio Options -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-gray-50 rounded-xl border p-4">
          <label class="block text-sm font-semibold text-gray-700 mb-2">🎥 Choose Camera</label>
          <select v-model="camera" class="w-full rounded-lg border px-3 py-2">
            <option value="front">Front Camera</option>
            <option value="back">Back Camera</option>
            <option value="external">External Device</option>
          </select>
        </div>

        <div class="bg-gray-50 rounded-xl border p-4">
          <label class="block text-sm font-semibold text-gray-700 mb-2">🎤 Microphone</label>
          <select v-model="mic" class="w-full rounded-lg border px-3 py-2">
            <option value="default">Default</option>
            <option value="mute">Mute</option>
            <option value="external">External Mic</option>
          </select>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex justify-end gap-4">
        <button @click="$emit('close')" class="bg-gray-300 hover:bg-gray-400 text-gray-800 px-6 py-2 rounded-full font-semibold">
          Cancel
        </button>
        <button
          :disabled="!agreed"
          @click="startLive"
          class="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-2 rounded-full font-bold disabled:opacity-50 disabled:cursor-not-allowed"
        >
          🚀 Go Live
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const agreed = ref(false)
const camera = ref('front')
const mic = ref('default')

const startLive = () => {
  // Optional: emit selected settings to parent
  console.log('Live starting with', camera.value, mic.value)
  // Trigger actual live logic from parent component
  // Could emit to parent like: emit('start', { camera: camera.value, mic: mic.value })
  alert('Live started ✅')
}
</script>

<style scoped>
.animate-fade-in {
  animation: fadeInUp 0.35s ease-out both;
}
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
