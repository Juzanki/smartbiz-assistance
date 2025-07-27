<!-- 📁 src/components/MobileBottomBar.vue -->
<template>
  <div class="fixed bottom-0 inset-x-0 z-40 bg-black/40 backdrop-blur-sm px-2 py-2 flex flex-col gap-2">
    <!-- Smart Replies Toggle -->
    <div>
      <button @click="showSmartReplies = !showSmartReplies" class="text-white text-xs bg-yellow-500/80 px-3 py-1 rounded-full shadow hover:bg-yellow-500">
        💬 Smart Replies
      </button>
      <transition name="fade">
        <div v-if="showSmartReplies" class="mt-2 flex gap-2 overflow-x-auto whitespace-nowrap">
          <button v-for="(reply, i) in replies" :key="i" @click="send(reply)"
            class="bg-white/20 text-white px-3 py-1 rounded-full text-xs shadow hover:bg-white/30">
            {{ reply }}
          </button>
        </div>
      </transition>
    </div>

    <!-- Chat Input Row -->
    <div class="flex items-center gap-2">
      <input
        v-model="message"
        placeholder="Type a short message..."
        class="flex-1 bg-black/50 text-white text-sm px-3 py-2 rounded-full focus:outline-none"
      />
      <button @click="send(message)" class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 text-sm rounded-full shadow">
        Send
      </button>
    </div>

    <!-- Bottom Action Bar -->
    <div class="flex items-center gap-4 overflow-x-auto">
      <button v-for="(btn, index) in actions" :key="index" @click="btn.onClick" class="flex flex-col items-center text-white text-xs">
        <i :class="btn.icon + ' text-lg'"></i>
        <span>{{ btn.label }}</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const showSmartReplies = ref(false)
const message = ref('')
const replies = [
  'Welcome to the stream!',
  'Thanks for your support ❤️',
  'We love your energy!',
  '🔥🔥🔥'
]

const send = (msg) => {
  if (!msg.trim()) return
  console.log("Send message:", msg)
  message.value = ''
}

const actions = [
  { label: '+Hosts', icon: 'i-tabler-user-plus', onClick: () => console.log('+Hosts') },
  { label: '+Guests', icon: 'i-tabler-users-group', onClick: () => console.log('+Guests') },
  { label: 'Share', icon: 'i-tabler-share', onClick: () => console.log('Share') },
  { label: 'Gifts', icon: 'i-tabler-gift', onClick: () => console.log('Gifts') },
  { label: 'SuperChat', icon: 'i-tabler-message-2-star', onClick: () => console.log('SuperChat') },
  { label: 'More', icon: 'i-tabler-dots-circle-horizontal', onClick: () => console.log('More') },
]
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
