<template>
  <div>
    <!-- Floating Trigger Button -->
    <button
      class="icon-btn flex items-center gap-2 px-4 py-2 rounded-full shadow-lg bg-white/10 text-white hover:bg-white/20 backdrop-blur-sm transition"
      @click="toggleMorePanel"
    >
      <i class="i-tabler-settings"></i>
      <span class="font-semibold">More</span>
    </button>

    <!-- More Control Panel -->
    <transition name="fade">
      <div
        v-if="isOpen"
        class="absolute bottom-24 left-1/2 -translate-x-1/2 z-50 p-5 w-[92vw] max-w-3xl bg-black/70 backdrop-blur-xl rounded-2xl text-white shadow-xl space-y-6"
      >
        <!-- 🎯 Engagement & Tools -->
        <Section title="🎯 Engagement & Tools">
          <button @click="openModal('poll')" class="option-btn">🗳️ Poll</button>
          <button @click="openModal('goals')" class="option-btn">🎯 Goals</button>
          <button @click="openModal('summary')" class="option-btn">📊 Summary</button>
          <button @click="$emit('toggle-voice')" class="option-btn">🔈 Voice Chat</button>
        </Section>

        <!-- 🎨 Visual Controls -->
        <Section title="🎨 Visual Controls">
          <button @click="$emit('open-effects')" class="option-btn">✨ Effects</button>
          <button @click="openModal('background')" class="option-btn">🌅 Background</button>
          <button @click="$emit('toggle-grid')" class="option-btn">📺 Layout/Grid</button>
          <button @click="$emit('toggle-filters')" class="option-btn">🎭 Filters</button>
        </Section>

        <!-- 🛡️ Admin Controls -->
        <Section title="🛡️ Admin Controls" titleClass="text-red-300">
          <button @click="openModal('settings')" class="option-btn">⚙️ Stream Settings</button>
          <button @click="$emit('toggle-replay')" class="option-btn">📼 Replay</button>
          <button @click="openModal('moderation')" class="option-btn">🛡️ Moderation</button>
          <button @click="$emit('block-user')" class="option-btn">🚫 Block Viewer</button>
        </Section>

        <!-- 💰 Monetization Tools -->
        <Section title="💰 Business Tools" titleClass="text-yellow-300">
          <button @click="$emit('promote-product')" class="option-btn">🛒 Promote Product</button>
          <button @click="$emit('flash-gift')" class="option-btn">🎁 Flash Gift</button>
          <button @click="$emit('live-auction')" class="option-btn">🔨 Live Auction</button>
          <button @click="$emit('show-analytics')" class="option-btn">📈 Analytics</button>
        </Section>

        <!-- Close Button -->
        <div class="text-center pt-3">
          <button @click="isOpen = false" class="text-xs text-gray-300 hover:underline">✖ Close</button>
        </div>
      </div>
    </transition>

    <!-- 🔍 MoreModal for Fullscreen Items -->
    <MoreModal v-if="showModal" :type="modalType" @close="showModal = false" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import MoreModal from './MoreModal.vue'

const isOpen = ref(false)
const showModal = ref(false)
const modalType = ref('settings')

function toggleMorePanel() {
  isOpen.value = !isOpen.value
}

function openModal(type) {
  modalType.value = type
  showModal.value = true
}

defineEmits([
  'toggle-voice', 'open-effects', 'toggle-grid', 'toggle-filters',
  'toggle-replay', 'block-user', 'promote-product', 'flash-gift',
  'live-auction', 'show-analytics'
])
</script>

<!-- Reusable Section Wrapper -->
<script>
export default {
  components: {
    Section: {
      props: ['title', 'titleClass'],
      template: `
        <div>
          <h3 :class="'text-sm font-bold mb-2 ' + (titleClass || 'text-indigo-300')">{{ title }}</h3>
          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3">
            <slot />
          </div>
        </div>
      `
    }
  }
}
</script>

<style scoped>
.icon-btn {
  @apply text-white bg-black/30 px-3 py-2 rounded-full font-medium backdrop-blur-sm hover:bg-black/40 transition;
}
.option-btn {
  @apply bg-white/10 hover:bg-white/20 text-white text-xs md:text-sm px-4 py-2 rounded-xl font-semibold transition text-center;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
