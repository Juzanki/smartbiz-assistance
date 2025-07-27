<template>
  <div class="relative">
    <!-- 🔗 Share Button -->
    <button
      @click="showPanel = !showPanel"
      class="px-4 py-2 bg-pink-600 hover:bg-pink-700 text-white rounded-full text-sm font-semibold shadow"
    >
      🔗 Share
    </button>

    <!-- 📤 Share Panel -->
    <transition name="fade">
      <div
        v-if="showPanel"
        class="absolute bottom-full mb-3 right-0 w-72 bg-white rounded-2xl shadow-xl p-4 z-50 text-sm"
      >
        <h3 class="font-bold text-gray-800 mb-3">Share this Stream</h3>

        <!-- 🔗 Social Share Options -->
        <div class="grid grid-cols-4 gap-4">
          <button @click="copyLink" class="flex flex-col items-center hover:text-yellow-600">
            <i class="i-tabler-link text-xl"></i>
            <span class="text-xs mt-1">Copy</span>
          </button>

          <button @click="shareTo('whatsapp')" class="flex flex-col items-center hover:text-green-600">
            <i class="i-fa6-brands-whatsapp text-xl"></i>
            <span class="text-xs mt-1">WhatsApp</span>
          </button>

          <button @click="shareTo('facebook')" class="flex flex-col items-center hover:text-blue-600">
            <i class="i-fa6-brands-facebook text-xl"></i>
            <span class="text-xs mt-1">Facebook</span>
          </button>

          <button @click="shareTo('messenger')" class="flex flex-col items-center hover:text-indigo-600">
            <i class="i-fa6-brands-facebook-messenger text-xl"></i>
            <span class="text-xs mt-1">Messenger</span>
          </button>
        </div>

        <!-- 👥 Internal Invite -->
        <div class="mt-4 border-t pt-3">
          <button @click="openInternalInvite" class="flex items-center gap-2 text-indigo-600 hover:underline">
            <i class="i-tabler-users"></i> Invite Friends in App
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const showPanel = ref(false)
const streamLink = window.location.href

function shareTo(platform) {
  const encoded = encodeURIComponent(streamLink)
  if (platform === 'whatsapp') {
    window.open(`https://wa.me/?text=${encoded}`, '_blank')
  } else if (platform === 'facebook') {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encoded}`, '_blank')
  } else if (platform === 'messenger') {
    window.open(`fb-messenger://share/?link=${encoded}`, '_blank')
  }
}

function copyLink() {
  navigator.clipboard.writeText(streamLink)
  alert('🔗 Link copied to clipboard!')
}

function openInternalInvite() {
  alert('📨 Invite inside SmartBiz webapp triggered.')
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
