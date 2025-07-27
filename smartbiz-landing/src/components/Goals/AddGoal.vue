<template>
  <div class="backdrop-blur-md bg-white/10 border border-white/20 rounded-2xl p-6 w-full max-w-md mx-auto shadow-xl text-white space-y-5 animate-fade-in">
    <!-- Title -->
    <h2 class="text-lg font-bold flex items-center gap-2 text-pink-200">
      🎯 Add Live Goal
    </h2>

    <!-- Goal Type -->
    <div>
      <label class="block text-sm text-white/80 mb-1">Goal Type</label>
      <select v-model="goal.type" class="w-full bg-white/10 border border-white/20 rounded-lg px-3 py-2 text-white">
        <option value="coins">🏅 Coin Target</option>
        <option value="sales">🛍 Product Sales</option>
        <option value="likes">❤️ Viewer Likes</option>
        <option value="comments">💬 Comment Milestone</option>
        <option value="gifts">🎁 Gift Quantity</option>
      </select>
    </div>

    <!-- Target -->
    <div>
      <label class="block text-sm text-white/80 mb-1">Target Amount</label>
      <input
        type="number"
        v-model.number="goal.target"
        min="1"
        placeholder="Enter target value..."
        class="w-full bg-white/10 border border-white/20 rounded-lg px-3 py-2 text-white placeholder-white/60"
      />
    </div>

    <!-- Description -->
    <div>
      <label class="block text-sm text-white/80 mb-1">Short Description (Optional)</label>
      <input
        v-model="goal.description"
        placeholder="E.g. Let's reach 1000 coins together!"
        class="w-full bg-white/10 border border-white/20 rounded-lg px-3 py-2 text-white placeholder-white/60"
      />
    </div>

    <!-- Set Goal Button -->
    <div class="text-center">
      <button
        @click="submitGoal"
        class="bg-gradient-to-r from-purple-500 via-pink-500 to-indigo-500 px-6 py-2 rounded-full font-semibold hover:scale-105 transition duration-200"
      >
        ✅ Set Goal
      </button>
    </div>

    <!-- 🎉 Preview -->
    <transition name="fade">
      <div v-if="goalSet" class="space-y-4">
        <div class="bg-green-100/10 border border-green-400 text-green-300 p-3 rounded-xl">
          🎉 Goal Set: <strong>{{ previewText }}</strong>
        </div>

        <!-- 📊 Progress Bar -->
        <div class="w-full bg-white/10 rounded-full h-4 overflow-hidden">
          <div :style="{ width: progressPercent + '%' }" class="bg-green-400 h-full transition-all duration-500"></div>
        </div>

        <!-- 💖 Contributors -->
        <div>
          <p class="text-sm font-semibold mb-1">🌟 Top Supporters</p>
          <ul class="text-xs space-y-1">
            <li v-for="user in supporters" :key="user.name">- {{ user.name }} ({{ user.amount }})</li>
          </ul>
        </div>

        <!-- 🏆 Leaderboard -->
        <div>
          <p class="text-sm font-semibold mb-1">🏆 Leaderboard</p>
          <ol class="text-xs list-decimal pl-4">
            <li v-for="(user, index) in leaderboard" :key="index">
              {{ user.name }} — {{ user.amount }} {{ goal.type }}
            </li>
          </ol>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'

const emit = defineEmits(['close'])

const goal = reactive({
  type: 'coins',
  target: 0,
  description: ''
})

const goalSet = ref(false)
const progress = ref(0)
const supporters = ref([
  { name: 'Alice', amount: 250 },
  { name: 'Bob', amount: 120 },
  { name: 'Zaki', amount: 80 }
])
const leaderboard = computed(() => supporters.value.sort((a, b) => b.amount - a.amount))

const submitGoal = () => {
  if (!goal.target || goal.target <= 0) {
    alert('⚠️ Please set a valid target!')
    return
  }
  goalSet.value = true
  progress.value = Math.floor(Math.random() * goal.target) // simulate

  setTimeout(() => {
    emit('close')
  }, 2000)
}

const previewText = computed(() => {
  const desc = goal.description ? ` (${goal.description})` : ''
  switch (goal.type) {
    case 'coins': return `Get ${goal.target} coins${desc}`
    case 'sales': return `Sell ${goal.target} products${desc}`
    case 'likes': return `Get ${goal.target} likes${desc}`
    case 'comments': return `Reach ${goal.target} comments${desc}`
    case 'gifts': return `Receive ${goal.target} gifts${desc}`
    default: return `Set target: ${goal.target}${desc}`
  }
})

const progressPercent = computed(() => {
  return Math.min((progress.value / goal.target) * 100, 100).toFixed(1)
})
</script>

<style scoped>
.animate-fade-in {
  animation: fadeInUp 0.6s ease-out;
}
@keyframes fadeInUp {
  0% {
    transform: translateY(12px);
    opacity: 0;
  }
  100% {
    transform: translateY(0px);
    opacity: 1;
  }
}
</style>
