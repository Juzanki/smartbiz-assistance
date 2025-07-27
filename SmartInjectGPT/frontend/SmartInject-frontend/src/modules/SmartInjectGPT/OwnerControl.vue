<template>
  <div class="bg-white dark:bg-[#0f1e2f] rounded-xl p-6 shadow-lg mt-6 border-2 border-red-500 dark:border-yellow-400">
    <h3 class="text-xl font-bold mb-4 text-red-600 dark:text-yellow-300">🛡️ Owner Control Panel (Secret)</h3>

    <div class="space-y-4 text-sm">
      <div>
        <label class="block font-semibold">🔐 Spiritual Key (Owner only)</label>
        <input
          v-model="key"
          type="password"
          class="w-full mt-1 p-2 rounded bg-gray-100 dark:bg-[#1e2e3e] focus:outline-none focus:ring-2 focus:ring-blue-400"
          placeholder="Ingiza spiritual key yako hapa..."
        />
      </div>

      <button
        @click="verifyKey"
        class="bg-blue-700 text-white px-6 py-2 rounded hover:bg-blue-800 transition"
      >
        ✅ Thibitisha
      </button>

      <div v-if="accessGranted" class="mt-6 space-y-4">
        <!-- ACTION BUTTONS -->
        <button @click="lockKernel" class="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 w-full">
          🔒 Funga Kernel
        </button>
        <button @click="unlockKernel" class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 w-full">
          🔓 Fungua Kernel
        </button>
        <button @click="enableStealth" class="bg-purple-600 text-white px-4 py-2 rounded hover:bg-purple-700 w-full">
          👻 Weka Stealth Mode
        </button>
        <button @click="logoutOwner" class="bg-gray-700 text-white px-4 py-2 rounded hover:bg-gray-800 w-full">
          🚪 Toka kama Owner
        </button>

        <!-- ⏱️ COUNTDOWN -->
        <div v-if="countdown" class="text-xs text-yellow-400 mt-1">
          ⏳ Muda wa ruhusa uliobaki: {{ countdown }}
        </div>

        <!-- 🧠 KERNEL STATUS -->
        <div class="text-xs text-blue-400 mt-2">
          <div>
            🧠 Kernel Status:
            <span :class="{
              'text-green-400': !kernelStatus.locked && !kernelStatus.stealth,
              'text-yellow-400': kernelStatus.stealth,
              'text-red-400': kernelStatus.locked
            }">
              {{ kernelStatus.locked ? '🔒 Locked' : kernelStatus.stealth ? '👻 Stealth Mode' : '✅ Active & Open' }}
            </span>
          </div>
          <div v-if="kernelStatus.last_action" class="mt-1 text-gray-400 dark:text-gray-300">
            📅 Last: {{ kernelStatus.last_action }}
          </div>
        </div>
      </div>

      <div v-if="message" :class="accessGranted ? 'text-green-400' : 'text-red-400'" class="mt-4">
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { setOwnerKey, removeOwnerKey } from '@/utils/auth'

const key = ref('')
const accessGranted = ref(false)
const message = ref('')
const countdown = ref('')
let countdownInterval = null

const kernelStatus = ref({
  locked: false,
  stealth: false,
  last_action: null
})

const verifyKey = async () => {
  try {
    const res = await axios.post('/api/smartinject/verify-owner', { key: key.value })

    if (res.data?.access === 'granted') {
      setOwnerKey(key.value)
      accessGranted.value = true
      message.value = '✅ Umefanikiwa kufungua milango ya kernel.'
      startCountdown()
      await fetchKernelStatus()
    } else {
      message.value = '❌ Ufunguo si sahihi.'
    }
  } catch {
    message.value = '⚠️ Hitilafu ya mawasiliano na kernel.'
  }
}

const lockKernel = async () => {
  const res = await axios.post('/api/smartinject/lock')
  message.value = res.data?.message || '🔒 Kernel imefungwa.'
  await fetchKernelStatus()
}

const unlockKernel = async () => {
  const res = await axios.post('/api/smartinject/unlock')
  message.value = res.data?.message || '🔓 Kernel imefunguliwa.'
  await fetchKernelStatus()
}

const enableStealth = async () => {
  const res = await axios.post('/api/smartinject/stealth')
  message.value = res.data?.message || '👻 Stealth mode imewashwa.'
  await fetchKernelStatus()
}

const logoutOwner = () => {
  removeOwnerKey()
  clearInterval(countdownInterval)
  accessGranted.value = false
  key.value = ''
  countdown.value = ''
  message.value = '🚪 Umetoka kama Owner. Ruhusa imeondolewa.'
}

const fetchKernelStatus = async () => {
  try {
    const res = await axios.get('/api/smartinject/status')
    kernelStatus.value = res.data
  } catch {
    kernelStatus.value = {
      locked: null,
      stealth: null,
      last_action: '⚠️ Imeshindwa kuwasiliana na kernel.'
    }
  }
}

function startCountdown() {
  const data = JSON.parse(localStorage.getItem('owner_token') || '{}')
  const expiry = 15 * 60 * 1000
  if (!data.timestamp) return

  const targetTime = data.timestamp + expiry

  countdownInterval = setInterval(() => {
    const now = Date.now()
    const remaining = targetTime - now

    if (remaining <= 0) {
      clearInterval(countdownInterval)
      removeOwnerKey()
      accessGranted.value = false
      countdown.value = '⏳ Imeisha'
      message.value = '🚪 Ruhusa imeondolewa kiotomatiki.'
    } else {
      const minutes = Math.floor(remaining / 60000)
      const seconds = Math.floor((remaining % 60000) / 1000)
      countdown.value = `${minutes}m ${seconds}s`
    }
  }, 1000)
}

onMounted(() => {
  const token = localStorage.getItem('owner_token')
  if (token) {
    accessGranted.value = true
    startCountdown()
    fetchKernelStatus()
  }
})
</script>
