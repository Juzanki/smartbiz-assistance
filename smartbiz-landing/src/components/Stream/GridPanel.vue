<!-- GridPanel.vue -->
<template>
  <div class="relative w-full h-full overflow-hidden rounded-2xl border border-white/10 bg-black">
    <!-- Overlay ya Controls -->
    <div class="absolute top-0 left-0 right-0 z-10 p-4 flex justify-between items-center bg-gradient-to-b from-black/60 to-transparent">
      <h3 class="text-white font-semibold text-lg">🎥 Unified Guest View</h3>
      <select v-model="selectedLayout" class="bg-white/10 text-white rounded-lg px-3 py-1 text-sm">
        <option v-for="layout in layouts" :key="layout" :value="layout">
          {{ layout }} Layout
        </option>
      </select>
    </div>

    <!-- Eneo la Video zote -->
    <div :class="mergedLayoutClass" class="absolute inset-0 z-0 flex flex-wrap items-center justify-center">
      <SmartCam
        v-for="(guest, index) in limitedGuests"
        :key="index"
        :user="guest"
        :style="guestStyle(index)"
      />
    </div>
  </div>
</template>
<script setup>
import { ref, computed } from 'vue'
import SmartCam from '@/components/Common/SmartCam.vue' // ✅ Corrected path

const props = defineProps({
  guests: {
    type: Array,
    default: () => []
  }
})

const selectedLayout = ref('dynamic')
const layouts = ['1x1', '2x2', '3x3', 'Full', 'dynamic']

const layoutSlotsMap = {
  '1x1': 1,
  '2x2': 4,
  '3x3': 9,
  'Full': Infinity,
  'dynamic': 6
}

const limitedGuests = computed(() => {
  const limit = layoutSlotsMap[selectedLayout.value] || 6
  return props.guests.slice(0, limit)
})

// Dynamic layout classes
const mergedLayoutClass = computed(() => {
  if (selectedLayout.value === 'Full') return 'flex flex-wrap items-center justify-center'
  const cols = Math.ceil(Math.sqrt(layoutSlotsMap[selectedLayout.value]))
  return `grid grid-cols-${cols} gap-2 p-4`
})

// Optional: style customization per guest
const guestStyle = (index) => {
  if (selectedLayout.value === 'Full') {
    return {
      width: '100%',
      height: '100%',
      objectFit: 'cover'
    }
  }
  return {}
}
</script>

<style scoped>
/* Ensure video screens merge well visually */
</style>
