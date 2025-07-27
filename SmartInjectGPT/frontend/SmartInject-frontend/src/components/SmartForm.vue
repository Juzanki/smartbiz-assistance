<template>
  <div class="space-y-4">
    <label :for="name" class="block text-sm font-medium mb-1">{{ label }}</label>
    <input
      :id="name"
      :name="name"
      :type="type"
      v-model="modelValue"
      :placeholder="placeholder"
      :class="[
        'w-full px-4 py-2 border rounded-md shadow-sm focus:outline-none transition',
        error ? 'border-red-500 bg-red-50 text-red-800' : 'border-gray-300 bg-white text-black'
      ]"
    />
    <p v-if="error" class="text-sm text-red-600 mt-1">{{ error }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  modelValue: [String, Number],
  label: String,
  name: String,
  type: {
    type: String,
    default: 'text'
  },
  placeholder: {
    type: String,
    default: ''
  },
  error: {
    type: String,
    default: ''
  }
})

const emit = defineEmits(['update:modelValue'])

watch(
  () => props.modelValue,
  (val) => emit('update:modelValue', val)
)
</script>

<style scoped>
/* Optional focus or transition styles */
</style>
