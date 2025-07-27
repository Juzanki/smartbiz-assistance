<template>
  <div class="fixed inset-0 bg-black/60 flex items-center justify-center z-50">
    <div class="bg-white p-6 rounded-xl shadow-lg w-full max-w-md">
      <h2 class="text-lg font-bold mb-4">🏆 Leaderboard ya Washiriki</h2>

      <ul class="divide-y divide-gray-200">
        <li v-for="(user, index) in leaderboard" :key="user.id" class="py-2 flex justify-between">
          <span class="font-medium">{{ index + 1 }}. {{ user.name }}</span>
          <span class="text-indigo-600 font-bold">{{ user.score }} pts</span>
        </li>
      </ul>

      <div class="mt-6 text-right">
        <button @click="$emit('close')" class="text-sm text-gray-600 hover:text-black">✖️ Funga</button>
      </div>
    </div>
  </div>
</template>

<script setup>
const leaderboard = [
  { id: 1, name: 'Janet', score: 120 },
  { id: 2, name: 'Moses', score: 105 },
  { id: 3, name: 'Lilian', score: 97 },
  { id: 4, name: 'Alex', score: 91 }
]
</script>
