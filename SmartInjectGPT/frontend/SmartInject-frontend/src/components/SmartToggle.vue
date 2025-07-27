<template>
  <label class="flex items-center cursor-pointer select-none gap-3">
    <span class="text-sm font-medium text-gray-700 dark:text-gray-200">{{ label }}</span>
    <div class="relative">
      <input
        type="checkbox"
        class="sr-only"
        :checked="modelValue"
        @change="$emit('update:modelValue', $event.target.checked)"
      />
      <div
        class="block w-11 h-6 rounded-full"
        :class="modelValue ? 'bg-blue-600' : 'bg-gray-400 dark:bg-gray-600'"
      ></div>
      <div
        class="dot absolute left-1 top-1 w-4 h-4 bg-white rounded-full transition"
        :class="modelValue ? 'translate-x-5' : ''"
      ></div>
    </div>
  </label>
</template>

<script setup>
const props = defineProps({
  modelValue: Boolean,
  label: {
    type: String,
    default: 'Enable'
  }
})
</script>

<style scoped>
.dot {
  transition: transform 0.2s ease-in-out;
}
</style>
