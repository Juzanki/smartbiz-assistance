<template>
  <div class="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-black text-white p-6">
    <div class="max-w-2xl mx-auto bg-white/10 backdrop-blur-md p-8 rounded-3xl shadow-2xl border border-white/20">

      <!-- Header -->
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-yellow-400">Recharge Your Wallet</h1>
        <p class="text-sm text-white/80 mt-2">
          Top up your SmartCoins and enjoy premium features, send gifts, and more.
        </p>
      </div>

      <!-- Balance Display -->
      <div class="bg-black/30 border border-white/20 p-4 rounded-xl text-center mb-6">
        <p class="text-sm text-white/70">Current Balance</p>
        <div class="flex justify-center items-center gap-2 text-2xl font-bold text-yellow-300 animate-bounce-slow">
          <img src="/icons/smartbiz-coin.png" alt="Coin" class="w-6 h-6 sparkle-glow" />
          {{ formattedBalance }} Coins
        </div>
      </div>

      <!-- Recharge Options -->
      <div class="space-y-4">
        <div class="grid grid-cols-2 gap-4">
          <button @click="selectAmount(5000)" class="recharge-btn coin-btn">
            <img src="/icons/smartbiz-coin.png" alt="Coin" class="w-5 h-5" />
            5,000
          </button>
          <button @click="selectAmount(10000)" class="recharge-btn coin-btn">
            <img src="/icons/smartbiz-coin.png" alt="Coin" class="w-5 h-5" />
            10,000
          </button>
          <button @click="selectAmount(20000)" class="recharge-btn coin-btn">
            <img src="/icons/smartbiz-coin.png" alt="Coin" class="w-5 h-5" />
            20,000
          </button>
          <button @click="selectAmount(50000)" class="recharge-btn coin-btn">
            <img src="/icons/smartbiz-coin.png" alt="Coin" class="w-5 h-5" />
            50,000
          </button>
        </div>

        <!-- Manual Entry -->
        <div>
          <label class="block mb-1 text-sm text-white/70">Or enter custom amount</label>
          <input
            v-model.number="customAmount"
            type="number"
            min="100"
            placeholder="Enter amount..."
            class="w-full rounded-lg px-4 py-2 bg-black/20 border border-white/30 placeholder-white/50 text-white"
          />
          <p v-if="customAmount" class="text-sm text-white/60 mt-1 italic">
            {{ customAmount.toLocaleString() }} coins ≈ 
            <span class="text-yellow-300 font-semibold">TSH {{ coinToTsh }}</span>
          </p>
        </div>

        <!-- Payment Method -->
        <div>
          <label class="block mb-1 text-sm text-white/70">Select Payment Method</label>
          <select
            v-model="paymentMethod"
            class="w-full rounded-lg px-4 py-2 bg-black/20 border border-white/30 text-white"
          >
            <option value="mpesa">📱 M-Pesa</option>
            <option value="card">💳 Debit/Credit Card</option>
            <option value="paypal">🅿 PayPal</option>
            <option value="crypto">₿ Crypto (USDT/BTC)</option>
          </select>
        </div>
      </div>

      <!-- Recharge Button -->
      <div class="text-center mt-6">
        <button
          @click="openRechargePage"
          class="bg-yellow-400 hover:bg-yellow-500 text-black font-bold px-8 py-3 rounded-full shadow-lg transition"
        >
          🚀 Recharge Now
        </button>
      </div>
    </div>

    <!-- RechargePage Modal -->
    <RechargePage
      v-if="showRechargeModal"
      :amount="customAmount"
      :method="paymentMethod"
      @close="showRechargeModal = false"
      @confirmed="handleRechargeSuccess"
    />
  </div>
</template>
<script setup>
import { ref, computed, nextTick } from 'vue'
import RechargePage from '@/components/modals/RechargePage.vue'

// 📌 Exchange rate (1 coin = 1.5 TSH)
const COIN_TO_TSH = 1.5

// 💰 User coin balance (replace with real user store in future)
const userBalance = ref(1_000_000)
const balanceFlash = ref(false)

// 📦 Form state
const customAmount = ref(0)
const paymentMethod = ref('mpesa')
const showRechargeModal = ref(false)
const toastVisible = ref(false)

// 📊 Formatted coin balance
const formattedBalance = computed(() => {
  const val = userBalance.value
  if (val >= 1_000_000) return (val / 1_000_000).toFixed(1) + 'M'
  if (val >= 1_000) return (val / 1000).toFixed(1) + 'K'
  return val.toLocaleString()
})

// 🧮 Convert coin to TSH in real-time
const coinToTsh = computed(() => {
  return (customAmount.value * COIN_TO_TSH).toLocaleString()
})

// 📥 Preset amount button
function selectAmount(amount) {
  customAmount.value = amount
}

// 🚀 Open recharge confirmation modal
function openRechargePage() {
  if (customAmount.value < 100) {
    alert('Please enter a valid amount of at least 100 coins.')
    return
  }
  showRechargeModal.value = true
}

// ✅ After recharge success
async function handleRechargeSuccess() {
  showRechargeModal.value = false

  // Add to user's coin balance
  userBalance.value += customAmount.value

  // Flash animation on balance
  balanceFlash.value = true
  await nextTick()
  setTimeout(() => {
    balanceFlash.value = false
  }, 800)

  // Show success toast
  toastVisible.value = true
  setTimeout(() => {
    toastVisible.value = false
  }, 4000)

  // Clear form
  customAmount.value = 0
}
</script>
<style scoped>
/* 🌊 Wavy Gradient Background */
.bg-wave {
  background: linear-gradient(135deg, #1e3a8a, #6d28d9, #000);
  background-size: 400% 400%;
  animation: gradient-wave 12s ease infinite;
}
@keyframes gradient-wave {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

/* 🌟 Coin Icon Glow */
.sparkle-glow {
  filter: drop-shadow(0 0 4px #facc15);
  animation: coin-glow 3s ease-in-out infinite;
}
@keyframes coin-glow {
  0%, 100% { filter: drop-shadow(0 0 4px #facc15); }
  50% { filter: drop-shadow(0 0 10px #fde047) brightness(1.15); }
}

/* 🪙 Recharge Buttons */
.recharge-btn {
  @apply text-yellow-300 font-semibold py-3 px-4 rounded-xl border shadow transition-all duration-300 ease-in-out flex items-center justify-center gap-2;
  background: linear-gradient(to right, rgba(255,255,255,0.06), rgba(255,255,255,0.12));
  border: 1px solid rgba(253, 224, 71, 0.2);
}
.recharge-btn:hover {
  background: linear-gradient(to right, #fde047, #facc15);
  color: black;
  transform: scale(1.05);
  box-shadow:
    0 0 15px rgba(253, 224, 71, 0.4),
    0 0 25px rgba(253, 224, 71, 0.2);
}

/* 🐢 Bounce Animation for Balance */
@keyframes bounce-slow {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
.animate-bounce-slow {
  animation: bounce-slow 3s infinite ease-in-out;
}

/* 🟡 Coin Pill Button (for other areas) */
.coin-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(253, 224, 71, 0.3);
  border-radius: 9999px;
  font-weight: 600;
  color: #fff;
  transition: all 0.3s ease;
}
.coin-btn:hover {
  background: linear-gradient(to right, #fde047, #facc15);
  color: #000;
  transform: scale(1.05);
  box-shadow:
    0 0 12px rgba(253, 224, 71, 0.3),
    0 0 24px rgba(253, 224, 71, 0.15);
}

/* 🚀 Recharge Now Button */
button.bg-yellow-400:hover {
  box-shadow:
    0 0 16px rgba(253, 224, 71, 0.35),
    0 0 28px rgba(253, 224, 71, 0.2);
  transform: scale(1.04);
}

/* 💬 TSH Equivalent Hint */
.coin-hint {
  font-size: 0.85rem;
  color: #e5e7eb;
  margin-top: 0.4rem;
}
.coin-hint span {
  color: #facc15;
  font-weight: 600;
}

/* 🎉 Toast Notification */
.toast-success {
  @apply fixed bottom-6 left-1/2 transform -translate-x-1/2 bg-green-500 text-white font-semibold px-6 py-3 rounded-full shadow-lg z-50;
  animation: toast-slide-in 0.4s ease-out, toast-fade-out 0.4s ease-in 3.6s forwards;
}
@keyframes toast-slide-in {
  from {
    opacity: 0;
    transform: translateX(-50%) translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
  }
}
@keyframes toast-fade-out {
  to {
    opacity: 0;
    transform: translateX(-50%) translateY(40px);
  }
}

/* 💡 Flash Coin Balance on Recharge */
.balance-flash {
  animation: flash-scale 0.6s ease-out;
}
@keyframes flash-scale {
  0% { transform: scale(1); color: #facc15; }
  50% { transform: scale(1.3); color: #fff176; }
  100% { transform: scale(1); color: #facc15; }
}
</style>
