<template>
  <div
    v-if="message"
    :class="[
      'rounded-md px-4 py-3 text-sm flex items-start gap-2 border-l-4',
      typeClass
    ]"
  >
    <span class="text-lg">{{ icon }}</span>
    <div class="flex-1">
      <p class="font-semibold">{{ title }}</p>
      <p class="text-sm">{{ message }}</p>
    </div>
    <button @click="$emit('close')" class="ml-4 text-lg text-gray-500 hover:text-red-500">×</button>
  </div>
</template>

<script setup>
const props = defineProps({
  title: String,
  message: String,
  type: {
    type: String,
    default: 'info' // success, warning, error, info
  }
})

const typeMap = {
  success: {
    icon: '✅',
    class: 'bg-green-50 border-green-500 text-green-800 dark:bg-green-900 dark:text-green-100'
  },
  warning: {
    icon: '⚠️',
    class: 'bg-yellow-50 border-yellow-500 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-100'
  },
  error: {
    icon: '❌',
    class: 'bg-red-50 border-red-500 text-red-800 dark:bg-red-900 dark:text-red-100'
  },
  info: {
    icon: 'ℹ️',
    class: 'bg-blue-50 border-blue-500 text-blue-800 dark:bg-blue-900 dark:text-blue-100'
  }
}

const icon = typeMap[props.type]?.icon || 'ℹ️'
const typeClass = typeMap[props.type]?.class || typeMap.info.class
</script>
