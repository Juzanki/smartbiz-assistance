<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm">
    <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md p-6 relative animate-fade-in space-y-6 text-black">

      <!-- Close Button -->
      <button
        @click="$emit('close')"
        :disabled="loading"
        class="absolute top-3 right-4 text-gray-400 hover:text-red-500 text-xl"
      >
        ✖
      </button>

      <!-- Header -->
      <div class="text-center space-y-2">
        <h1 class="text-2xl font-bold text-indigo-700">Confirm Recharge</h1>
        <p class="text-sm text-gray-600">You're about to recharge your SmartWallet</p>
      </div>

      <!-- Recharge Summary -->
      <div class="bg-indigo-50 p-4 rounded-xl shadow-inner text-center space-y-2">
        <p class="text-sm text-gray-500">Recharge Amount</p>
        <div class="flex justify-center items-center gap-2">
          <img src="/icons/smartbiz-coin.png" alt="SmartBiz Coin" class="w-6 h-6" />
          <h2 class="text-3xl font-bold text-indigo-600">
            {{ amount.toLocaleString() }} Coins
          </h2>
        </div>
        <p class="text-sm text-gray-500 mt-2">
          Payment via <strong class="capitalize">{{ methodName }}</strong>
        </p>
      </div>

      <!-- Action Buttons -->
      <div class="flex justify-center items-center gap-4 mt-4">
        <!-- Confirm Button -->
        <button
          @click="confirmRecharge"
          :disabled="loading"
          class="bg-yellow-400 hover:bg-yellow-500 disabled:opacity-60 disabled:cursor-wait text-black font-bold px-6 py-3 rounded-full shadow-md transition flex items-center gap-2"
        >
          <span v-if="!loading">🚀 Confirm Recharge</span>
          <span v-else class="flex items-center gap-2">
            <svg class="animate-spin h-5 w-5 text-black" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
              <path class="opacity-75" fill="currentColor"
                d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
            </svg>
            Processing...
          </span>
        </button>

        <!-- Cancel Button -->
        <button
          @click="$emit('close')"
          :disabled="loading"
          class="text-sm text-gray-500 hover:text-red-500 transition"
        >
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

// Props from parent component
const props = defineProps({
  amount: {
    type: Number,
    required: true,
    default: 0,
  },
  method: {
    type: String,
    required: true,
    default: 'mpesa',
  },
})

// Emit events to parent (confirmed, close)
const emit = defineEmits(['confirmed', 'close'])

// Local UI state
const loading = ref(false)

// Display-friendly method name
const methodName = computed(() => {
  const labels = {
    mpesa: 'M-Pesa',
    card: 'Visa / Mastercard',
    paypal: 'PayPal',
    crypto: 'Crypto (BTC/USDT)',
  }
  return labels[props.method] || props.method
})

// Main recharge confirmation flow
function confirmRecharge() {
  if (loading.value) return

  const ask = window.confirm(
    `You're about to recharge ${props.amount.toLocaleString()} SmartCoins via ${methodName.value}.\nPress OK to confirm or Cancel to abort.`
  )

  if (!ask) return
  loading.value = true

  switch (props.method) {
    case 'mpesa':
      simulateMpesa()
      break
    case 'card':
      simulateCard()
      break
    case 'paypal':
      simulatePaypal()
      break
    case 'crypto':
      simulateCrypto()
      break
    default:
      fallbackProcess()
  }
}

// -----------------------------
// Simulated Payments (for demo)
// -----------------------------
function simulateMpesa() {
  setTimeout(() => {
    alert(`✅ M-Pesa payment successful.\n${props.amount.toLocaleString()} SmartCoins have been added.`)
    finishRecharge()
  }, 1500)
}

function simulateCard() {
  setTimeout(() => {
    alert(`✅ Card payment processed.\n${props.amount.toLocaleString()} SmartCoins have been credited.`)
    finishRecharge()
  }, 1500)
}

function simulatePaypal() {
  setTimeout(() => {
    alert(`✅ PayPal transaction complete.\n${props.amount.toLocaleString()} SmartCoins received.`)
    finishRecharge()
  }, 1500)
}

function simulateCrypto() {
  setTimeout(() => {
    alert(`✅ Blockchain confirmed.\n${props.amount.toLocaleString()} SmartCoins now available.`)
    finishRecharge()
  }, 1500)
}

function fallbackProcess() {
  setTimeout(() => {
    alert(`✅ Recharge successful via ${methodName.value}.`)
    finishRecharge()
  }, 1500)
}

// Finalize recharge and reset state
function finishRecharge() {
  emit('confirmed')
  loading.value = false
}
</script>
<style scoped>
/* 🌀 Entry Animation: Smooth glow, lift and blur */
.animate-fade-in {
  animation: fadeInUpGlow 0.5s ease-out both;
  will-change: opacity, transform, filter;
  transform-origin: center;
  backdrop-filter: blur(16px) saturate(160%);
  background: rgba(255, 255, 255, 0.05);
  border-radius: 1.5rem;
  box-shadow:
    0 8px 24px rgba(0, 0, 0, 0.2),
    0 0 8px rgba(255, 255, 255, 0.05);
}

/* 🌠 Entry Keyframes */
@keyframes fadeInUpGlow {
  0% {
    opacity: 0;
    transform: translateY(60px) scale(0.94);
    filter: blur(4px) brightness(0.85);
  }
  60% {
    transform: translateY(12px) scale(1.02);
    filter: blur(1px) brightness(1.08);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0) brightness(1);
  }
}

/* 🚪 Exit Animation: graceful fade down */
.animate-fade-out {
  animation: fadeOutDownBlur 0.45s ease-in both;
}

/* ❄️ Exit Keyframes */
@keyframes fadeOutDownBlur {
  0% {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0) brightness(1);
  }
  100% {
    opacity: 0;
    transform: translateY(70px) scale(0.9);
    filter: blur(6px) brightness(0.7);
  }
}
</style>
