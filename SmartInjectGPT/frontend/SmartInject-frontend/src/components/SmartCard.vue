<template>
  <div class="rounded-xl shadow-md p-5 border bg-white dark:bg-[#1e1e2e] dark:border-gray-700">
    <div v-if="title" class="mb-3 text-lg font-semibold text-gray-800 dark:text-gray-200">
      {{ title }}
    </div>
    <slot />
  </div>
</template>

<script setup>
const props = defineProps({
  title: String
})
</script>

<style scoped>
/* Optional transitions */
</style>
