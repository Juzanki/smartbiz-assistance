<template>
  <div>
    <LiveGiftAnimations
      v-if="currentGift"
      :gift="currentGift"
      :combo-count="comboCount"
      @animation-end="handleAnimationEnd"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import LiveGiftAnimations from './LiveGiftAnimations.vue'

// 📦 State ya zawadi
const giftQueue = ref([])
const currentGift = ref(null)
const lastGiftId = ref(null)
const comboCount = ref(1)
let comboTimer = null

// 🟢 Ongeza zawadi mpya kwenye queue
function enqueueGift(gift) {
  giftQueue.value.push(gift)
  if (!currentGift.value) {
    showNextGift()
  }
}

// 🎁 Onyesha zawadi inayofuata kutoka kwenye queue
function showNextGift() {
  if (giftQueue.value.length === 0) return

  const nextGift = giftQueue.value.shift()

  // 🔁 Angalia kama ni combo (zawadi ile ile mfululizo)
  if (nextGift.id === lastGiftId.value) {
    comboCount.value += 1
  } else {
    comboCount.value = 1
    lastGiftId.value = nextGift.id
  }

  currentGift.value = nextGift

  // ⏱️ Reset combo baada ya sekunde 3
  if (comboTimer) clearTimeout(comboTimer)
  comboTimer = setTimeout(() => {
    comboCount.value = 1
    lastGiftId.value = null
  }, 3000)
}

// 🔚 Inapoisha kuonyesha zawadi
function handleAnimationEnd() {
  currentGift.value = null
  showNextGift()
}

// 🌐 Ruhusu wazazi kuitumia
defineExpose({ enqueueGift })
</script>
