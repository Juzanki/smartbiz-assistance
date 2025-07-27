<template>
  <div v-if="filterVisible" class="absolute inset-0 z-10 pointer-events-none">
    <img
      :src="filterSrc"
      alt="Face Filter"
      class="w-32 h-32 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 opacity-90 animate-pulse"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'

const filterVisible = ref(true)
const filterSrc = ref('/filters/crown.png') // Customize path or make dynamic
</script>
