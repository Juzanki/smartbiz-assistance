<template>
  <div class="space-y-4">
    <!-- Layout Selector -->
    <div class="flex justify-between items-center">
      <h3 class="text-white text-lg font-semibold">🧩 Grid Layout</h3>
      <select v-model="selectedLayout" class="bg-white/10 text-white rounded-lg px-3 py-1 text-sm">
        <option v-for="layout in layouts" :key="layout" :value="layout">
          {{ layout }} Layout
        </option>
      </select>
    </div>

    <!-- Grid Area -->
    <div :class="gridClass" class="gap-4 grid w-full bg-white/5 p-4 rounded-2xl border border-white/10">
      <div
        v-for="slot in gridSlots"
        :key="slot.id"
        class="relative flex items-center justify-center rounded-xl aspect-video border border-white/10 bg-black/20 text-white/70 hover:scale-105 transition group overflow-hidden">

        <template v-if="slot.host">
          <img :src="slot.host.avatar" class="w-16 h-16 rounded-full border border-white shadow-lg" />
          <div class="absolute bottom-2 left-2 text-xs bg-white/10 px-2 py-1 rounded-full">
            {{ slot.host.name }}
          </div>
          <!-- Mic & Cam Status -->
          <div class="absolute top-2 right-2 flex gap-2">
            <i :class="slot.host.mic ? 'i-tabler-microphone text-green-400' : 'i-tabler-microphone-off text-red-400'" />
            <i :class="slot.host.cam ? 'i-tabler-camera text-green-400' : 'i-tabler-camera-off text-red-400'" />
          </div>
          <!-- Expand Button -->
          <button
            class="absolute bottom-2 right-2 text-xs text-white/80 bg-pink-600 hover:bg-pink-700 px-2 py-1 rounded-full"
            @click="$emit('expand', slot.host)"
          >
            ⬆ Expand
          </button>
        </template>

        <template v-else>
          <div class="text-3xl opacity-40">👑</div>
          <button
            class="absolute bottom-2 right-2 text-xs text-white/70 bg-white/10 px-2 py-1 rounded-full hover:bg-white/20"
            @click="$emit('assign', slot.id)"
          >
            + Assign
          </button>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, reactive, ref, watch } from 'vue'

const props = defineProps({
  hosts: Array
})
const emit = defineEmits(['assign', 'expand'])

const selectedLayout = ref('2x2')
const layouts = ['1x1', '2x2', '3x3', '4x4', '6x6', 'Dynamic']

const layoutToSlots = {
  '1x1': 1,
  '2x2': 4,
  '3x3': 9,
  '4x4': 16,
  '6x6': 36,
  'Dynamic': 12
}

const gridSlots = ref([])

const gridClass = computed(() => {
  const base = 'grid'
  const size = layoutToSlots[selectedLayout.value] || 12
  const cols = Math.ceil(Math.sqrt(size))
  return `${base} grid-cols-${cols}`
})

watch(() => [props.hosts, selectedLayout.value], () => {
  const total = layoutToSlots[selectedLayout.value] || 12
  const slots = []
  for (let i = 0; i < total; i++) {
    slots.push({ id: i, host: props.hosts[i] || null })
  }
  gridSlots.value = slots
}, { immediate: true })
</script>

<style scoped>
.grid > div {
  transition: all 0.3s ease;
  background-image: linear-gradient(145deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
  box-shadow: inset 0 0 5px rgba(255,255,255,0.05);
}
</style>
