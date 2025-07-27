<template>
  <div class="min-h-screen bg-gradient-to-tr from-gray-900 via-slate-800 to-gray-900 p-6 text-white font-sans">

    <!-- 🧾 Header -->
    <div class="flex justify-between items-center mb-8">
      <div>
        <h1 class="text-3xl font-bold text-pink-400 flex items-center gap-2">🏦 Withdraw Request</h1>
        <p class="text-xs text-gray-400">Securely request to withdraw your SmartCoins.</p>
      </div>
      <div class="text-sm text-right text-gray-300">
        Balance: <span class="text-green-400 font-semibold">{{ walletBalance }} SC</span>
      </div>
    </div>

    <!-- 💸 Withdraw Form -->
    <div class="bg-white/5 border border-white/10 rounded-xl p-6 shadow-lg mb-12">
      <h3 class="text-lg font-semibold text-white mb-4">📝 Create New Request</h3>

      <div class="grid md:grid-cols-3 gap-4">
        <div>
          <label class="block text-sm text-gray-300 mb-1">Amount (SC)</label>
          <input v-model.number="amount" type="number" min="1" placeholder="e.g. 250"
            class="w-full px-4 py-2 rounded-lg bg-white/10 border border-white/20 text-white focus:outline-none focus:ring focus:ring-pink-400" />
        </div>

        <div>
          <label class="block text-sm text-gray-300 mb-1">Method</label>
          <select v-model="method"
            class="w-full px-4 py-2 rounded-lg bg-white/10 border border-white/20 text-white">
            <option disabled value="">Select Method</option>
            <option value="mpesa">📱 Mobile Money (Mpesa/TigoPesa)</option>
            <option value="bank">🏦 Bank Transfer</option>
            <option value="paypal">💻 PayPal</option>
            <option value="crypto">🪙 Crypto Wallet (USDT)</option>
          </select>
        </div>

        <div>
          <label class="block text-sm text-gray-300 mb-1">Destination (Phone/Account/Wallet)</label>
          <input v-model="account" type="text" placeholder="e.g. 07XXXXXXXX"
            class="w-full px-4 py-2 rounded-lg bg-white/10 border border-white/20 text-white" />
        </div>
      </div>

      <div class="mt-6 flex justify-end">
        <button :disabled="loading" @click="submitWithdraw"
          class="bg-pink-500 hover:bg-pink-600 disabled:opacity-50 px-6 py-2 rounded-lg font-semibold shadow transition">
          🚀 Submit Request
        </button>
      </div>

      <!-- Alert -->
      <div v-if="message" class="mt-4 p-3 rounded text-sm font-medium"
        :class="messageType === 'success' ? 'bg-green-600' : 'bg-red-600'">
        {{ message }}
      </div>
    </div>

    <!-- 📜 Request History -->
    <div class="bg-white/5 border border-white/10 rounded-xl p-6 shadow-lg">
      <h3 class="text-lg font-semibold text-white mb-4">📂 Withdrawal History</h3>

      <div v-if="withdrawals.length === 0" class="text-sm text-gray-400 italic">
        😴 No withdrawal requests yet.
      </div>

      <ul v-else class="divide-y divide-white/10 text-sm">
        <li v-for="w in withdrawals" :key="w.id" class="py-3">
          <div class="flex justify-between items-center">
            <div>
              <p class="text-pink-300 font-bold">{{ w.amount }} SC</p>
              <p class="text-gray-400 text-xs">{{ formatDate(w.date) }} — {{ w.method }} — {{ w.account }}</p>
            </div>
            <span :class="statusColor(w.status)" class="text-xs font-semibold uppercase">
              {{ w.status }}
            </span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import axios from '@/utils/axios'
import { useAuthStore } from '@/stores/auth'

// ✅ Auth Store
const auth = useAuthStore()

// 🧾 Form Data
const amount = ref('')
const method = ref('mpesa')
const account = ref('')
const walletBalance = ref(0)
const loading = ref(false)
const message = ref('')
const messageType = ref('')

// 📜 History List
const withdrawals = ref([])

// 🔄 Fetch Wallet Balance
const fetchWallet = async () => {
  try {
    const res = await axios.get('/wallet/smartcoin-log')
    walletBalance.value = res.data.balance || 0
  } catch (err) {
    console.warn('⚠️ Wallet fetch failed', err)
  }
}

// 📥 Fetch My Withdraw Requests
const fetchWithdrawals = async () => {
  try {
    const res = await axios.get('/wallet/withdrawals')
    withdrawals.value = res.data || []
  } catch (err) {
    console.warn('⚠️ Withdrawals fetch failed', err)
  }
}

// 🚀 Submit Withdraw Request
const submitWithdraw = async () => {
  // Validation
  if (!amount.value || !method.value || !account.value) {
    message.value = '⚠️ Please complete all fields before submitting.'
    messageType.value = 'error'
    return
  }

  loading.value = true
  message.value = ''
  try {
    const userId = localStorage.getItem('user_id') || 'unknown'

    await axios.post('/wallet/request-withdraw', {
      user_id: userId,
      amount: Number(amount.value),
      method: method.value,
      account: account.value
    })

    message.value = '✅ Your request has been submitted successfully.'
    messageType.value = 'success'

    // Reset
    amount.value = ''
    method.value = 'mpesa'
    account.value = ''

    // Refresh history
    await fetchWithdrawals()
    await fetchWallet()
  } catch (err) {
    console.error('❌ Submit failed:', err)
    message.value = '❌ Failed to submit request. Please try again later.'
    messageType.value = 'error'
  } finally {
    loading.value = false
  }
}

// 📅 Format date
const formatDate = (timestamp) => new Date(timestamp).toLocaleString()

// 🎨 Status color
const statusColor = (status) => {
  switch (status.toLowerCase()) {
    case 'approved': return 'text-green-500'
    case 'pending': return 'text-yellow-500'
    case 'rejected': return 'text-red-500'
    default: return 'text-gray-400'
  }
}

// ▶️ Run on load
onMounted(() => {
  fetchWallet()
  fetchWithdrawals()
})
</script>
