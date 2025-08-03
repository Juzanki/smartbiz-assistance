<template>
  <div class="relative w-screen h-screen bg-black overflow-hidden text-white font-sans">
    <!-- 🎥 Camera Feed -->
    <video ref="videoRef" autoplay playsinline muted class="absolute inset-0 w-full h-full object-cover z-0" />

    <!-- 🔝 Top Overlay Controls -->
    <div class="absolute top-0 inset-x-0 px-4 pt-3 z-10 flex justify-between items-center bg-black/40">
      <div class="flex items-center gap-2">
        <span class="bg-green-500 text-white text-xs px-2 py-1 rounded-full font-semibold">LIVE</span>
        <button @click="leaveStream" class="bg-red-600 hover:bg-red-700 text-xs px-3 py-1 rounded-full">Leave</button>
      </div>
      <button @click="switchCamera" class="bg-gray-800 text-xs px-2 py-1 rounded-full">Switch Cam</button>
    </div>

    <!-- 💎 Flying Gift Animations -->
    <transition-group name="gift-fly" tag="div" class="absolute inset-0 pointer-events-none z-40">
      <div
        v-for="g in animatedGifts"
        :key="g.uid"
        class="absolute"
        :style="g.style"
      >
        <img :src="g.image" alt="" class="w-16 h-16 object-contain animate-bounce" />
        <div class="text-center text-xs font-bold bg-black/60 text-white mt-1 px-2 py-1 rounded-full">
          {{ g.name }}
        </div>
      </div>
    </transition-group>

    <!-- 🛍️ Floating Product -->
    <transition name="fade">
      <div v-if="currentProduct" :class="['absolute z-30', positionClass]">
        <div class="bg-white/90 text-black rounded-lg shadow p-3 animate-pulse text-center w-36">
          <img :src="currentProduct.image" class="w-16 h-16 object-cover rounded mb-1 mx-auto" />
          <div class="text-sm font-semibold">{{ currentProduct.name }}</div>
          <div class="text-green-600 font-bold text-sm">TZS {{ currentProduct.price }}</div>
          <button @click="placeOrder(currentProduct)" class="mt-1 text-xs text-white bg-green-500 px-2 py-1 rounded-full">
            Buy Now
          </button>
        </div>
      </div>
    </transition>

    <!-- 🔘 Bottom Controls -->
    <div class="absolute bottom-0 inset-x-0 px-4 pb-4 z-10 flex flex-col gap-3 items-center">
      <div class="flex gap-3 justify-center w-full">
        <button @click="startStream" class="bg-pink-600 hover:bg-pink-700 text-sm font-bold px-4 py-2 rounded-full w-full">
          Go Live
        </button>
        <button @click="openProductModal" class="bg-blue-600 hover:bg-blue-700 text-sm px-4 py-2 rounded-full w-full">
          Product
        </button>
        <button @click="sendGift" class="bg-yellow-400 hover:bg-yellow-500 text-sm text-black px-4 py-2 rounded-full w-full">
          Gift
        </button>
      </div>
    </div>

    <!-- 💬 Chat Messages -->
    <div class="absolute bottom-28 right-3 w-[85vw] max-w-xs h-48 overflow-y-auto bg-black/40 rounded-lg text-xs px-3 py-2 z-10 backdrop-blur">
      <div v-for="msg in chatMessages" :key="msg.id" class="mb-1 text-white">
        <span class="font-semibold text-pink-300">{{ msg.user }}</span>: {{ msg.text }}
      </div>
    </div>

    <!-- 🛒 Product Modal -->
    <div v-if="showProductModal" class="fixed inset-0 z-50 bg-black/60 flex items-center justify-center px-4">
      <div class="bg-white w-full max-w-sm p-5 rounded-xl shadow-lg text-black">
        <h3 class="text-lg font-bold mb-4">Set Product</h3>
        <input v-model="product.name" type="text" placeholder="Product Name" class="w-full mb-2 p-2 border rounded" />
        <input v-model="product.price" type="number" placeholder="Price (TZS)" class="w-full mb-2 p-2 border rounded" />
        <input type="file" @change="handleImageUpload" class="mb-2 w-full" />
        <select v-model="product.position" class="w-full mb-4 p-2 border rounded">
          <option value="top">Top</option>
          <option value="center">Center</option>
          <option value="bottom">Bottom</option>
        </select>
        <div class="flex justify-between">
          <button @click="showProductModal = false" class="text-sm bg-gray-300 px-3 py-1 rounded">Cancel</button>
          <button @click="setProduct" class="text-sm bg-blue-600 text-white px-3 py-1 rounded">Set</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

// 🎥 Video reference
const videoRef = ref(null)

// 💬 Live chat messages
const chatMessages = ref([
  { id: 1, user: 'Alice', text: 'How much is it?' },
  { id: 2, user: 'Bob', text: 'I want that bag!' }
])

// 🛒 Product modal + data
const showProductModal = ref(false)
const product = ref({ name: '', price: '', image: '', position: 'bottom' })
const currentProduct = ref(null)

// 🎁 Gift animation management
const animatedGifts = ref([])
let counter = 0

// 🔧 Compute product position on screen
const positionClass = computed(() => {
  switch (product.value.position) {
    case 'top': return 'top-10 left-1/2 transform -translate-x-1/2'
    case 'center': return 'top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2'
    case 'bottom': return 'bottom-10 left-1/2 transform -translate-x-1/2'
    default: return ''
  }
})

// 🚀 Start Live Stream
function startStream() {
  navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(stream => {
      if (videoRef.value) videoRef.value.srcObject = stream
    })
    .catch(err => alert('Camera access denied'))
}

// 🔴 Stop Live Stream
function leaveStream() {
  const tracks = videoRef.value?.srcObject?.getTracks()
  tracks?.forEach(track => track.stop())
  videoRef.value.srcObject = null
}

// 🔄 Simulate camera switch
function switchCamera() {
  alert("🔄 Switching between front/back camera not implemented yet.")
}

// 🧾 Open Product Setting Modal
function openProductModal() {
  showProductModal.value = true
}

// 🖼️ Handle Image Upload
function handleImageUpload(e) {
  const file = e.target.files[0]
  if (file) {
    product.value.image = URL.createObjectURL(file)
  }
}

// ✅ Confirm Product Set
function setProduct() {
  currentProduct.value = { ...product.value }
  showProductModal.value = false
}

// 💰 Purchase Product
function placeOrder(product) {
  alert(`🛍️ Order placed for: ${product.name}`)
}

// 🎁 Send a Gift
function sendGift() {
  const gift = {
    name: 'Phoenix Spirit',
    image: '/assets/gifts/phoenix.png'
  }
  launchGiftAnimation(gift)
}

// 🎇 Animate Gift on Screen
function launchGiftAnimation(gift) {
  const uid = counter++
  const style = {
    top: `${Math.random() * 70 + 10}%`,
    left: `${Math.random() * 70 + 10}%`,
    transition: 'transform 3s ease-in-out',
    animation: 'flyGift 3s ease-in-out forwards'
  }
  animatedGifts.value.push({ ...gift, uid, style })
  setTimeout(() => {
    animatedGifts.value = animatedGifts.value.filter(g => g.uid !== uid)
  }, 3000)
}

// ⚡ Cleanup if user exits page
onBeforeUnmount(() => {
  leaveStream()
})
</script>
<style scoped>
/* 🧠 Input Fields - Clean, Mobile-Ready */
.input {
  width: 100%;
  padding: 0.6rem 1rem;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 0.95rem;
  transition: border 0.2s ease-in-out;
}
.input:focus {
  border-color: #2563eb;
  outline: none;
  box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
}

/* 🎯 Buttons */
.btn {
  padding: 0.6rem 1.2rem;
  border-radius: 9999px;
  font-weight: 600;
  font-size: 0.9rem;
  transition: all 0.25s ease-in-out;
}
.btn-primary {
  background-color: #2563eb;
  color: #fff;
}
.btn-primary:hover {
  background-color: #1e40af;
}
.btn-secondary {
  background-color: #6b7280;
  color: #fff;
}
.btn-secondary:hover {
  background-color: #4b5563;
}

/* 🟡 Gift Animation */
@keyframes flyGift {
  0% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
  50% {
    transform: translateY(-120px) scale(1.2) rotate(15deg);
    opacity: 0.85;
  }
  100% {
    transform: translateY(-280px) scale(1.4) rotate(360deg);
    opacity: 0;
  }
}

/* 🛫 Gift Fly Transition Group */
.gift-fly-enter-active,
.gift-fly-leave-active {
  transition: all 0.6s ease-in-out;
}
.gift-fly-enter-from,
.gift-fly-leave-to {
  opacity: 0;
  transform: scale(0.8);
}

/* 🎬 Fade Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* 📱 Responsive Tweaks */
@media (max-width: 768px) {
  .btn {
    font-size: 0.85rem;
    padding: 0.5rem 1rem;
  }
  .input {
    font-size: 0.85rem;
    padding: 0.5rem 0.9rem;
  }
}
</style>
