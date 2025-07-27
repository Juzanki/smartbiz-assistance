<template>
  <div class="p-6">
    <h2 class="text-xl font-bold mb-4">🏆 Top Gift Earners</h2>

    <div class="mb-4">
      <label class="mr-2 font-medium">Select Range:</label>
      <select v-model="days" @change="fetchLeaderboard" class="border rounded px-3 py-1">
        <option value="7">Last 7 Days</option>
        <option value="30">Last 30 Days</option>
        <option value="90">Last 90 Days</option>
      </select>
    </div>

    <div class="overflow-x-auto">
      <table class="w-full border shadow-sm bg-white rounded">
        <thead class="bg-gray-100 text-left">
          <tr>
            <th class="py-2 px-4">#</th>
            <th class="py-2 px-4">Name</th>
            <th class="py-2 px-4">Username</th>
            <th class="py-2 px-4 text-right">SmartCoins Earned</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user, index) in leaderboard" :key="user.user_id" class="border-t">
            <td class="py-2 px-4 font-bold">{{ index + 1 }}</td>
            <td class="py-2 px-4">{{ user.full_name }}</td>
            <td class="py-2 px-4 text-gray-600">@{{ user.username }}</td>
            <td class="py-2 px-4 text-right text-green-600 font-semibold">{{ user.total_earned }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/utils/axios'

const leaderboard = ref([])
const days = ref(7)

const fetchLeaderboard = async () => {
  const res = await axios.get(`/leaderboard/gifts?days=${days.value}`)
  leaderboard.value = res.data
}

onMounted(fetchLeaderboard)
</script>
