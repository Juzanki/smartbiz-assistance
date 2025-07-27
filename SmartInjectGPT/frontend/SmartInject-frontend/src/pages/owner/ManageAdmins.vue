<template>
  <div class="min-h-screen bg-[#0d1b2a] text-white p-6">
    <h2 class="text-2xl font-bold text-yellow-400 mb-4">Manage Admins</h2>

    <!-- Create Magic Link -->
    <div class="bg-[#1b263b] p-4 rounded-xl shadow mb-6">
      <h3 class="text-lg font-semibold text-yellow-400 mb-2">Create Admin Invite Link</h3>
      <div class="flex gap-3 items-center">
        <input
          v-model="newAdminEmail"
          type="email"
          placeholder="Enter admin email"
          class="p-2 rounded bg-[#0d1b2a] border border-yellow-500 text-white w-full"
        />
        <button
          @click="generateMagicLink"
          class="bg-yellow-500 hover:bg-yellow-600 text-[#0d1b2a] font-bold px-4 py-2 rounded"
        >
          Generate Link
        </button>
      </div>
      <p v-if="generatedLink" class="mt-2 text-sm text-green-400">
        Invite Link: <a :href="generatedLink" class="underline">{{ generatedLink }}</a>
      </p>
    </div>

    <!-- Admins List -->
    <div class="bg-[#1b263b] p-4 rounded-xl shadow">
      <h3 class="text-lg font-semibold text-yellow-400 mb-4">Current Admins</h3>
      <table class="w-full text-sm">
        <thead>
          <tr class="text-left text-yellow-300">
            <th>Email</th>
            <th>Status</th>
            <th>Last Active</th>
            <th>IP Address</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="admin in admins" :key="admin.id" class="border-t border-gray-700">
            <td>{{ admin.email }}</td>
            <td>
              <span
                :class="admin.active ? 'text-green-400' : 'text-red-400'"
              >
                {{ admin.active ? 'Active' : 'Suspended' }}
              </span>
            </td>
            <td>{{ admin.last_active || 'Never' }}</td>
            <td>{{ admin.last_ip || 'N/A' }}</td>
            <td class="space-x-2">
              <button
                class="text-yellow-400 hover:underline"
                @click="toggleStatus(admin.id)"
              >
                {{ admin.active ? 'Suspend' : 'Activate' }}
              </button>
              <button
                class="text-red-400 hover:underline"
                @click="deleteAdmin(admin.id)"
              >
                Remove
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const admins = ref([])
const newAdminEmail = ref('')
const generatedLink = ref('')

const fetchAdmins = async () => {
  const res = await axios.get('/api/admins')
  admins.value = res.data
}

const generateMagicLink = async () => {
  try {
    const res = await axios.post('/api/admins/invite', { email: newAdminEmail.value })
    generatedLink.value = res.data.link
    newAdminEmail.value = ''
    fetchAdmins()
  } catch (err) {
    alert('Failed to generate link.')
  }
}

const toggleStatus = async (adminId) => {
  try {
    await axios.post(`/api/admins/${adminId}/toggle`)
    fetchAdmins()
  } catch (err) {
    alert('Failed to update status.')
  }
}

const deleteAdmin = async (adminId) => {
  if (!confirm('Are you sure you want to remove this admin?')) return
  try {
    await axios.delete(`/api/admins/${adminId}`)
    fetchAdmins()
  } catch (err) {
    alert('Failed to delete admin.')
  }
}

onMounted(fetchAdmins)
</script>

<style scoped>
table th,
table td {
  padding: 0.5rem;
}
</style>
