<template>
  <span
    class="inline-block px-3 py-1 rounded-full text-xs font-semibold capitalize"
    :class="badgeClass"
  >
    {{ label }}
  </span>
</template>

<script setup>
const props = defineProps({
  label: String,
  type: {
    type: String,
    default: 'info' // info, success, warning, danger
  }
})

const badgeClassMap = {
  info: 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200',
  success: 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200',
  warning: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200',
  danger: 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200'
}

const badgeClass = computed(() => badgeClassMap[props.type] || badgeClassMap.info)
</script>
