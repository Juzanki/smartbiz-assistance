<template>
  <div class="space-y-4">
    <!-- Search -->
    <input
      v-model="searchQuery"
      type="text"
      placeholder="Search..."
      class="w-full px-4 py-2 border rounded-md text-sm focus:outline-none dark:bg-[#1e293b] dark:text-white"
    />

    <!-- Table -->
    <table class="min-w-full text-sm border rounded overflow-hidden">
      <thead class="bg-gray-100 dark:bg-gray-700 text-left">
        <tr>
          <th v-for="header in headers" :key="header" class="px-4 py-2 font-semibold text-gray-700 dark:text-gray-200">
            {{ header }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in filteredRows" :key="index" class="odd:bg-white even:bg-gray-50 dark:odd:bg-[#1e1e2e] dark:even:bg-[#1a1a27]">
          <td v-for="cell in row" :key="cell" class="px-4 py-2 text-gray-800 dark:text-gray-100">
            {{ cell }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  headers: Array,
  rows: Array
})

const searchQuery = ref('')

const filteredRows = computed(() => {
  if (!searchQuery.value) return props.rows
  return props.rows.filter(row =>
    row.some(cell => String(cell).toLowerCase().includes(searchQuery.value.toLowerCase()))
  )
})
</script>

<style scoped>
/* Scrollbar and table styling if needed */
</style>
