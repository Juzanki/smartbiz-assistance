<template>
  <div v-if="show" class="fixed inset-0 z-50 flex items-center justify-center bg-black/60">
    <div class="bg-white dark:bg-[#111827] rounded-xl shadow-xl w-full max-w-md p-6 relative">
      <h2 v-if="title" class="text-lg font-semibold mb-4 text-gray-800 dark:text-gray-200">{{ title }}</h2>

      <slot />

      <div class="mt-6 flex justify-end gap-3">
        <button
          class="px-4 py-2 rounded bg-gray-300 hover:bg-gray-400 text-gray-900"
          @click="$emit('cancel')"
        >
          Cancel
        </button>
        <button
          class="px-4 py-2 rounded bg-blue-600 hover:bg-blue-700 text-white"
          @click="$emit('confirm')"
        >
          Confirm
        </button>
      </div>

      <button
        class="absolute top-2 right-3 text-gray-500 hover:text-red-500"
        @click="$emit('close')"
      >
        ✖
      </button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  show: Boolean,
  title: String
})
</script>

<style scoped>
/* Optional: add modal animations later */
</style>
