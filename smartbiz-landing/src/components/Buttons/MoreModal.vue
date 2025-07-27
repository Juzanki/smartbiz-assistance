<template>
  <transition name="fade">
    <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm px-4 py-6">
      <div class="w-full max-w-4xl bg-white rounded-3xl shadow-2xl p-6 relative animate-fade-in space-y-4">
        <!-- Header -->
        <div class="flex items-center justify-between border-b pb-3">
          <h2 class="text-xl font-bold text-indigo-700 capitalize flex items-center gap-2">
            <span>{{ modalIcon }}</span> {{ titleMap[type] || 'Panel' }}
          </h2>
          <button @click="$emit('close')" class="text-red-500 text-2xl hover:text-red-700">✖</button>
        </div>

        <!-- Dynamic Content -->
        <component :is="componentMap[type]" />

        <!-- Close Button -->
        <div class="text-right pt-3">
          <button @click="$emit('close')" class="bg-gray-200 hover:bg-gray-300 px-5 py-2 rounded-full text-sm font-semibold text-gray-700">
            Close
          </button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { computed } from 'vue'
import StreamSettings from './LiveSettingsPanel.vue'
import SummaryPanel from './LiveSummary.vue'
import PollPanel from './PollPanel.vue'
import ModerationPanel from './ModerationPanel.vue'
import BackgroundPanel from './BackgroundPanel.vue'
import GoalPanel from './AddGoal.vue'

const props = defineProps({
  type: {
    type: String,
    required: true,
  }
})

const titleMap = {
  settings: 'Stream Settings',
  summary: 'Live Summary',
  poll: 'Live Polls',
  moderation: 'Moderation Tools',
  background: 'Background Selector',
  goals: 'Live Goals',
}

const iconMap = {
  settings: '⚙️',
  summary: '📊',
  poll: '🗳️',
  moderation: '🛡️',
  background: '🌅',
  goals: '🎯',
}

const modalIcon = computed(() => iconMap[props.type] || '🔧')

const componentMap = {
  settings: StreamSettings,
  summary: SummaryPanel,
  poll: PollPanel,
  moderation: ModerationPanel,
  background: BackgroundPanel,
  goals: GoalPanel,
}
</script>

<style scoped>
.animate-fade-in {
  animation: fadeInUp 0.35s ease-out both;
}
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
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
