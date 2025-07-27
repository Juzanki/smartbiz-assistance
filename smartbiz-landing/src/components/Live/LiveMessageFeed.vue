<template>
  <div
    class="live-message-feed fixed bottom-[100px] left-4 z-40 flex flex-col-reverse gap-1 max-h-[35vh] overflow-y-auto pr-1"
  >
    <transition-group name="fade" tag="div">
      <div
        v-for="(msg, index) in messages"
        :key="msg.id + '-' + index"
        :class="msg.type === 'gift' ? 'gift-message' : 'chat-message'"
        class="flex items-center gap-2 px-4 py-2 rounded-2xl max-w-[90vw] shadow-md backdrop-blur-sm bg-white/5 text-white text-sm"
      >
        <!-- 🧑 Sender -->
        <span class="font-semibold truncate text-white/80 max-w-[30%]">
          {{ msg.sender }}:
        </span>

        <!-- 💬 Normal Chat Message -->
        <template v-if="msg.type === 'chat'">
          <span class="truncate text-white/95 text-sm max-w-[60%]">
            {{ msg.text.slice(0, 120) }}
          </span>
        </template>

        <!-- 🎁 Gift Message -->
        <template v-else-if="msg.type === 'gift'">
          <img
            :src="msg.icon"
            alt="gift icon"
            class="w-6 h-6 animate-bounce drop-shadow-md"
          />
          <span class="text-sm font-semibold text-yellow-300">
            sent <span class="text-blue-300">{{ msg.name }}</span> 🎁
          </span>
        </template>
      </div>
    </transition-group>
  </div>
</template>
<script setup>
import { ref, watch, onMounted, onBeforeUnmount } from 'vue'

// 🎯 Props kutoka kwa mzazi
const props = defineProps({
  messages: {
    type: Array,
    required: true,
  }
})

// 💬 Orodha ya ujumbe unaoonekana sasa
const displayedMessages = ref([])

// 🧠 Timer wa kusafisha ujumbe wa zamani
let cleanupTimer = null

// ➕ Ongeza ujumbe mmoja kwa wakati
function addMessage(msg) {
  const exists = displayedMessages.value.find(
    m => m.id === msg.id && m.timestamp === msg.timestamp
  )
  if (exists) return

  displayedMessages.value.push(msg)

  // ⏳ Auto-remove zawadi baada ya sekunde 10
  if (msg.type === 'gift') {
    setTimeout(() => {
      displayedMessages.value = displayedMessages.value.filter(
        m => !(m.id === msg.id && m.timestamp === msg.timestamp)
      )
    }, 10000)
  }
}

// 🧼 Ondoa chat messages zilizopitwa na muda (dakika 5)
function cleanOldMessages() {
  const now = Date.now()
  const maxAge = 5 * 60 * 1000 // 5 dakika
  displayedMessages.value = displayedMessages.value.filter(
    m => now - m.timestamp < maxAge
  )
}

// 👂 Watch kwa messages mpya kutoka kwa mzazi
watch(
  () => props.messages,
  (newMessages) => {
    newMessages.forEach(addMessage)
  },
  { immediate: true, deep: true }
)

// ⏱️ Anzisha timer ya kusafisha messages
onMounted(() => {
  cleanupTimer = setInterval(cleanOldMessages, 60000)
})

// 🛑 Sitisha timer ukiondoka kwenye page
onBeforeUnmount(() => {
  if (cleanupTimer) clearInterval(cleanupTimer)
})
</script>
<style scoped>
/* 📦 Message Feed Container - Fixed Bottom Left */
.live-message-feed {
  position: fixed;
  bottom: 100px;
  left: 1rem;
  z-index: 40;
  width: 90vw;
  max-width: 24rem;
  display: flex;
  flex-direction: column-reverse;
  gap: 0.25rem;
  pointer-events: none;
  max-height: 35vh;
  overflow-y: auto;
  padding-right: 4px;
  scrollbar-width: thin;
}
.live-message-feed::-webkit-scrollbar {
  width: 6px;
}
.live-message-feed::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.12);
  border-radius: 4px;
}

/* 💬 Normal Chat Message */
.chat-message {
  background: rgba(255, 255, 255, 0.05);
  color: white;
  font-size: 0.875rem;
  padding: 0.25rem 1rem;
  border-radius: 9999px;
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
  font-weight: 400;
  letter-spacing: 0.3px;
  animation: fadeInChat 0.3s ease-out;
}

/* 🎁 Gift Message */
.gift-message {
  background: linear-gradient(to right, rgba(0, 102, 204, 0.2), rgba(255, 215, 0, 0.25));
  color: white;
  font-size: 0.875rem;
  font-weight: 600;
  padding: 0.25rem 1rem;
  border-radius: 0.75rem;
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow:
    0 0 10px rgba(255, 215, 0, 0.15),
    0 0 15px rgba(0, 102, 204, 0.2);
  animation:
    fadeOut10s 10s ease-out forwards,
    pulseGift 4s ease-in-out infinite;
}

/* 🖼 Gift Icon Inside Message */
.gift-message img {
  animation: bounceGift 0.8s infinite alternate;
  filter: drop-shadow(0 0 4px rgba(255, 255, 255, 0.4));
  margin-right: 6px;
  vertical-align: middle;
  height: 20px;
}

/* 💫 Gift Icon Floating Bounce */
@keyframes bounceGift {
  0%   { transform: translateY(0); }
  100% { transform: translateY(-5px); }
}

/* 💨 Fade Out After 10 Seconds */
@keyframes fadeOut10s {
  0%   { opacity: 1; }
  100% { opacity: 0; transform: translateY(-10px); }
}

/* 🌟 Glowing Gift Pulse */
@keyframes pulseGift {
  0%, 100% {
    box-shadow:
      0 0 10px rgba(255, 215, 0, 0.2),
      0 0 14px rgba(0, 102, 204, 0.2);
  }
  50% {
    box-shadow:
      0 0 16px rgba(255, 215, 0, 0.35),
      0 0 20px rgba(0, 102, 204, 0.35);
  }
}

/* ✨ Message Entry Animation */
@keyframes fadeInChat {
  0%   { opacity: 0; transform: translateY(14px) scale(0.96); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}

/* 🎭 Vue Transition Effects */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(10px);
}
</style>
