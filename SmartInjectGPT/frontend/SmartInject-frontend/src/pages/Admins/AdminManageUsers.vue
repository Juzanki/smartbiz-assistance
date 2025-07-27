<template>
  <SmartCard title="👥 Manage Users">
    <div class="flex justify-end mb-3">
      <SmartButton @click="addUser" icon="➕">Add User</SmartButton>
    </div>

    <SmartTable :headers="headers" :rows="users" />
  </SmartCard>
</template>

<script setup>
import SmartCard from '@/components/SmartCard.vue'
import SmartButton from '@/components/SmartButton.vue'
import SmartTable from '@/components/SmartTable.vue'
import { ref, onMounted } from 'vue'

const headers = [
  { text: 'ID', value: 'id' },
  { text: 'Name', value: 'name' },
  { text: 'Email', value: 'email' },
  { text: 'Role', value: 'role' }
]

const users = ref([])

const fetchUsers = async () => {
  // Placeholder for future API
  users.value = [
    { id: 1, name: 'Jane Doe', email: 'jane@smartinject.ai', role: 'admin' },
    { id: 2, name: 'John Smith', email: 'john@smartinject.ai', role: 'user' }
  ]
}

const addUser = () => {
  alert('🔧 User creation form coming soon!')
}

onMounted(() => {
  fetchUsers()
})
</script>

<style scoped>
</style>
