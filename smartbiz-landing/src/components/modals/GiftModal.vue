<!-- src/components/modals/GiftModal.vue -->
<template>
  <div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
    <div class="bg-white rounded-2xl p-6 w-[320px] shadow-lg">
      <!-- 🧾 Title -->
      <h2 class="text-center text-pink-600 text-lg font-bold mb-4">
        🎁 Choose a Gift
      </h2>

      <!-- 🎁 Gift List -->
      <div class="grid grid-cols-3 gap-4">
        <GiftItem
          v-for="(gift, index) in gifts"
          :key="index"
          :src="gift.image"
          :name="gift.name"
          @click="selectGift(gift)"
        />
      </div>

      <!-- ❌ Cancel Button -->
      <div class="mt-6 text-center">
        <button
          @click="$emit('close')"
          class="text-gray-600 hover:text-red-500 text-sm mt-2 underline"
        >
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import GiftItem from '../shared/GiftItem.vue'

// 🎁 Sample gifts
const gifts = [
  { name: 'Rose', image: new URL('@/assets/gifts/rose.png', import.meta.url).href },
  { name: 'Diamond', image: new URL('@/assets/gifts/diamond.png', import.meta.url).href },
  { name: 'Trophy', image: new URL('@/assets/gifts/trophy.png', import.meta.url).href },
  { name: 'Rocket', image: new URL('@/assets/gifts/rocket.png', import.meta.url).href },
  { name: 'Crown', image: new URL('@/assets/gifts/crown.png', import.meta.url).href },
  { name: 'Heart', image: new URL('@/assets/gifts/heart.png', import.meta.url).href },
]

const emit = defineEmits(['close', 'send'])
const selectGift = (gift) => {
  emit('send', gift)
  emit('close')
}
</script>
