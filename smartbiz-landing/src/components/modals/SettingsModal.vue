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

      <!-- 🛡️ Terms Acknowledgment -->
      <div class="bg-indigo-50 border border-indigo-200 rounded-xl p-4">
        <h3 class="text-lg font-semibold text-indigo-700 mb-2">📜 Terms & Community Guidelines</h3>
        <ul class="text-sm text-gray-700 list-disc pl-5 space-y-1">
          <li>No nudity or sexually explicit content</li>
          <li>No hate speech, bullying, or harassment</li>
          <li>Respect all users regardless of race, religion, or identity</li>
          <li>No illegal activity or promotions</li>
          <li>Follow national laws and digital ethics</li>
        </ul>
        <div class="mt-4 flex items-center gap-3">
          <input type="checkbox" id="agree" v-model="agreed" />
          <label for="agree" class="text-sm text-gray-800">
            I agree to the <a href="#" class="text-indigo-600 underline">Terms & Community Policy</a>.
          </label>
        </div>
      </div>

      <!-- 📷 Camera & Mic Settings -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-gray-50 border rounded-xl p-4">
          <label class="block text-sm font-semibold text-gray-700 mb-2">🎥 Choose Camera</label>
          <select v-model="camera" class="w-full border px-3 py-2 rounded-lg">
            <option value="front">Front Camera</option>
            <option value="back">Back Camera</option>
            <option value="external">External Device</option>
          </select>
        </div>
        <div class="bg-gray-50 border rounded-xl p-4">
          <label class="block text-sm font-semibold text-gray-700 mb-2">🎤 Microphone</label>
          <select v-model="mic" class="w-full border px-3 py-2 rounded-lg">
            <option value="default">Default</option>
            <option value="mute">Mute</option>
            <option value="external">External Mic</option>
          </select>
        </div>
      </div>

      <!-- 🌐 Visibility & Comments -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="bg-gray-50 border rounded-xl p-4">
          <label class="block text-sm font-semibold text-gray-700 mb-2">💬 Enable Comments</label>
          <select v-model="commentsEnabled" class="w-full border px-3 py-2 rounded-lg">
            <option value="true">Yes</option>
            <option value="false">No</option>
          </select>
        </div>
        <div class="bg-gray-50 border rounded-xl p-4">
          <label class="block text-sm font-semibold text-gray-700 mb-2">🌍 Stream Visibility</label>
          <select v-model="visibility" class="w-full border px-3 py-2 rounded-lg">
            <option value="public">Public</option>
            <option value="private">Private</option>
          </select>
        </div>
      </div>

      <!-- 🔘 Actions -->
      <div class="flex justify-end gap-4">
        <button @click="$emit('close')" class="bg-gray-300 hover:bg-gray-400 text-gray-800 px-6 py-2 rounded-full font-semibold">
          Cancel
        </button>
        <button
          :disabled="!agreed"
          @click="startLive"
          class="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-2 rounded-full font-bold disabled:opacity-40"
        >
          🚀 Go Live
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const emit = defineEmits(['close'])

const agreed = ref(false)
const camera = ref('front')
const mic = ref('default')
const commentsEnabled = ref('true')
const visibility = ref('public')

const startLive = () => {
  console.log('Starting live with:', {
    camera: camera.value,
    mic: mic.value,
    comments: commentsEnabled.value,
    visibility: visibility.value
  })
  emit('close')
  // Optional: emit('start', { camera: camera.value, mic: mic.value, comments: commentsEnabled.value, visibility: visibility.value })
}
</script>

<style scoped>
.animate-fade-in {
  animation: fadeInUp 0.4s ease-out;
}
@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
