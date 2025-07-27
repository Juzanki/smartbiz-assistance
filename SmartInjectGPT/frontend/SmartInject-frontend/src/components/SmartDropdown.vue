<template>
  <div class="space-y-1">
    <label v-if="label" :for="name" class="block text-sm font-medium text-gray-700 dark:text-gray-200">
      {{ label }}
    </label>
    <select
      :id="name"
      :name="name"
      v-model="selectedValue"
      :class="[
        'w-full px-4 py-2 border rounded-md bg-white dark:bg-[#1e293b] dark:text-white focus:outline-none shadow-sm text-sm transition',
        error ? 'border-red-500 bg-red-50 text-red-800' : 'border-gray-300 text-black'
      ]"
    >
      <option disabled value="">-- Select --</option>
      <option v-for="option in options" :key="option.value" :value="option.value">
        {{ option.label }}
      </option>
    </select>
    <p v-if="error" class="text-xs text-red-600">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  modelValue: [String, Number],
  name: String,
  label: String,
  options: Array,
  error: String
})

const emit = defineEmits(['update:modelValue'])
const selectedValue = ref(props.modelValue)

watch(() => props.modelValue, val => selectedValue.value = val)
watch(selectedValue, val => emit('update:modelValue', val))
</script>

<style scoped>
/* optional enhancements */
</style>
