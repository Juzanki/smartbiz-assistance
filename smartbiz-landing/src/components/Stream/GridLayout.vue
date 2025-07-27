<template>
  <div class="grid-layout-wrapper">
    <div :class="gridClass" class="grid gap-3 p-2">
      <div
        v-for="(guest, index) in visibleGuests"
        :key="guest.id"
        class="rounded-xl overflow-hidden bg-black/80 relative border border-white/10 shadow-md guest-tile"
      >
        <!-- Placeholder for Guest Video -->
        <div class="w-full h-40 sm:h-48 md:h-56 lg:h-64 bg-gradient-to-br from-gray-800 to-gray-700 flex items-center justify-center text-white text-xl">
          🎥 {{ guest.name }}
        </div>
        <!-- Controls (Optional) -->
        <div class="absolute top-2 right-2 flex gap-2 z-10">
          <button
            @click="$emit('remove', guest.id)"
            class="bg-red-600 hover:bg-red-700 text-white text-xs px-2 py-1 rounded shadow">
            ✖ Remove
          </button>
          <button
            @click="$emit('expand', guest.id)"
            class="bg-indigo-600 hover:bg-indigo-700 text-white text-xs px-2 py-1 rounded shadow">
            ⛶ Expand
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  guests: Array,
  layout: {
    type: String,
    default: '2x2' // Options: 1x1, 2x2, 3x3, dynamic
  }
})

const layoutMap = {
  '1x1': 1,
  '2x2': 4,
  '3x3': 9,
  dynamic: 6
}

const visibleGuests = computed(() => {
  const limit = layoutMap[props.layout] || 6
  return props.guests.slice(0, limit)
})

const gridClass = computed(() => {
  const count = layoutMap[props.layout] || 2
  const cols = Math.ceil(Math.sqrt(count))
  return `grid-cols-${cols}`
})
</script>

<style scoped>
.grid-layout-wrapper {
  @apply w-full;
}

.guest-tile {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.guest-tile:hover {
  transform: scale(1.02);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}
</style>
