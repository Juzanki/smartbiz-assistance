<template>
  <button
    :type="type"
    :class="[
      'inline-flex items-center justify-center gap-2 rounded-md font-semibold transition duration-200 ease-in-out',
      themeClass,
      sizeClass,
      { 'opacity-50 cursor-not-allowed': disabled || loading }
    ]"
    :disabled="disabled || loading"
    @click="onClick"
  >
    <span v-if="loading" class="animate-spin">🔄</span>
    <span v-else-if="icon">{{ icon }}</span>
    <slot />
  </button>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  type: { type: String, default: 'button' },
  theme: { type: String, default: 'primary' }, // primary, danger, success, ghost
  size: { type: String, default: 'md' },       // sm, md, lg
  icon: { type: String, default: '' },
  loading: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false }
})

const emit = defineEmits(['click'])

const onClick = (event) => {
  emit('click', event)
}

const themeClassMap = {
  primary: 'bg-blue-600 text-white hover:bg-blue-700',
  danger: 'bg-red-600 text-white hover:bg-red-700',
  success: 'bg-green-600 text-white hover:bg-green-700',
  ghost: 'bg-transparent border border-gray-500 text-gray-300 hover:bg-gray-700'
}

const sizeClassMap = {
  sm: 'text-sm py-1 px-3',
  md: 'text-base py-2 px-4',
  lg: 'text-lg py-3 px-5'
}

const themeClass = computed(() => themeClassMap[props.theme] || themeClassMap.primary)
const sizeClass = computed(() => sizeClassMap[props.size] || sizeClassMap.md)
</script>

<style scoped>
/* Optional additional styling */
</style>
