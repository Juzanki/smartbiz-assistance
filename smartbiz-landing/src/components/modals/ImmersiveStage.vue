<template>
  <div class="relative w-full h-full overflow-hidden">
    <!-- Background Layer -->
    <div :style="backgroundStyle" class="absolute inset-0 transition-all duration-500 bg-cover bg-center z-0"></div>

    <!-- Draggable Guests -->
    <VueDraggableResizable
      v-for="guest in guests"
      :key="guest.id"
      :x="guest.x"
      :y="guest.y"
      :w="guest.width"
      :h="guest.height"
      :active="guest.active"
      @dragstop="updatePosition(guest, $event)"
      :parent="true"
      class="absolute z-10 cursor-move guest-item">
      <div class="relative w-full h-full rounded-2xl overflow-hidden shadow-xl border border-white/20">
        <img :src="guest.avatar" class="object-cover w-full h-full" />
        <div v-if="guest.spotlight" class="absolute inset-0 bg-black/40 flex items-center justify-center text-white text-xl font-bold">
          🎤 Spotlight
        </div>
      </div>
    </VueDraggableResizable>

    <!-- Effects Layer -->
    <transition name="fade">
      <div v-if="effect === 'confetti'" class="absolute inset-0 z-20 pointer-events-none">
        <ConfettiEffect />
      </div>
    </transition>

    <!-- Control Panel -->
    <div class="absolute top-4 right-4 z-30 bg-white/80 backdrop-blur p-4 rounded-xl shadow-xl flex flex-col gap-4 w-72">
      <h2 class="text-lg font-semibold text-gray-800">🎛 Stage Controls</h2>

      <!-- Background Selector -->
      <div>
        <label class="block mb-1 text-sm font-medium">🎨 Background</label>
        <select v-model="selectedBackground" class="w-full p-2 rounded-lg border">
          <option v-for="bg in backgrounds" :value="bg.url" :key="bg.label">
            {{ bg.label }}
          </option>
        </select>
      </div>

      <!-- Effect Selector -->
      <div>
        <label class="block mb-1 text-sm font-medium">✨ Effects</label>
        <select v-model="effect" class="w-full p-2 rounded-lg border">
          <option value="">None</option>
          <option value="confetti">🎉 Confetti</option>
        </select>
      </div>

      <!-- Toggle Guest Glow -->
      <div>
        <label class="block mb-1 text-sm font-medium">🔦 Spotlight</label>
        <div class="grid grid-cols-2 gap-2">
          <button
            v-for="guest in guests"
            :key="guest.id"
            @click="toggleSpotlight(guest)"
            class="px-2 py-1 rounded bg-indigo-500 text-white text-sm hover:bg-indigo-600">
            {{ guest.name }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import VueDraggableResizable from 'vue3-draggable-resizable'
import 'vue3-draggable-resizable/dist/Vue3DraggableResizable.css'
import ConfettiEffect from '@/components/effects/ConfettiEffect.vue'

const guests = ref([
  { id: 1, name: 'Diana', avatar: '/avatars/guest1.png', x: 50, y: 100, width: 150, height: 200, active: true, spotlight: false },
  { id: 2, name: 'Jay', avatar: '/avatars/guest2.png', x: 300, y: 200, width: 150, height: 200, active: false, spotlight: false },
])

const updatePosition = (guest, event) => {
  guest.x = event.x
  guest.y = event.y
}

const toggleSpotlight = (guest) => {
  guest.spotlight = !guest.spotlight
}

const selectedBackground = ref('/backgrounds/studio.jpg')
const effect = ref('')

const backgrounds = [
  { label: '🎬 Studio', url: '/backgrounds/studio.jpg' },
  { label: '🪐 Galaxy', url: '/backgrounds/galaxy.jpg' },
  { label: '🌆 City Night', url: '/backgrounds/city.jpg' },
  { label: '🎨 Custom Art', url: '/backgrounds/artistic.jpg' }
]

const backgroundStyle = computed(() => `background-image: url(${selectedBackground.value});`)
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

<script setup>
import { ref, computed, onMounted } from 'vue'

const backgroundOptions = [
  { id: 'bg1', label: 'Office', url: '/backgrounds/office.jpg' },
  { id: 'bg2', label: 'Lounge', url: '/backgrounds/lounge.jpg' },
  { id: 'bg3', label: 'Stage Lights', url: '/backgrounds/stage.jpg' },
  { id: 'bg4', label: 'Custom Color', url: '' } // Custom background color
]

const selectedBackground = ref(backgroundOptions[0].url)
const customBackground = ref('#ffffff')

const guests = ref([
  {
    id: 1,
    name: 'Tracy',
    avatar: '/avatars/guest1.png',
    mic: true,
    cam: true,
    x: 100,
    y: 100,
    spotlight: false
  },
  {
    id: 2,
    name: 'Jay Smart',
    avatar: '/avatars/guest2.png',
    mic: false,
    cam: true,
    x: 250,
    y: 180,
    spotlight: false
  }
])

const selectedGuestId = ref(null)
const confettiActive = ref(false)

const stageStyle = computed(() => {
  if (selectedBackground.value === '') {
    return {
      backgroundColor: customBackground.value
    }
  }
  return {
    backgroundImage: `url(${selectedBackground.value})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center'
  }
})

function setBackground(url) {
  selectedBackground.value = url
}

function toggleSpotlight(id) {
  guests.value = guests.value.map(g =>
    g.id === id ? { ...g, spotlight: !g.spotlight } : g
  )
}

function toggleMic(id) {
  const guest = guests.value.find(g => g.id === id)
  if (guest) guest.mic = !guest.mic
}

function toggleCam(id) {
  const guest = guests.value.find(g => g.id === id)
  if (guest) guest.cam = !guest.cam
}

function triggerConfetti() {
  confettiActive.value = true
  setTimeout(() => (confettiActive.value = false), 3000)
}

// Drag support
let dragGuest = null
let offsetX = 0
let offsetY = 0

function startDrag(event, guest) {
  dragGuest = guest
  offsetX = event.clientX - guest.x
  offsetY = event.clientY - guest.y
  document.addEventListener('mousemove', onDrag)
  document.addEventListener('mouseup', stopDrag)
}

function onDrag(event) {
  if (dragGuest) {
    dragGuest.x = event.clientX - offsetX
    dragGuest.y = event.clientY - offsetY
  }
}

function stopDrag() {
  document.removeEventListener('mousemove', onDrag)
  document.removeEventListener('mouseup', stopDrag)
  dragGuest = null
}

onMounted(() => {
  console.log('ImmersiveStage mounted with', guests.value.length, 'guests.')
})
</script>

<style scoped>
.immersive-stage {
  min-height: 600px;
  border-radius: 1.5rem;
  overflow: hidden;
  position: relative;
  transition: background 0.5s ease-in-out;
  box-shadow: 0 0 40px rgba(0, 0, 0, 0.15);
  background-blend-mode: overlay;
  backdrop-filter: blur(4px);
}

.control-panel {
  background: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 1rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  animation: fadeSlideUp 0.6s ease-out;
}

.control-panel button {
  transition: all 0.3s ease;
}
.control-panel button:hover {
  transform: scale(1.05);
}

.avatar-draggable {
  transition: all 0.2s ease-in-out;
  animation: fadeZoomIn 0.5s ease-in-out;
  cursor: grab;
  z-index: 10;
}
.avatar-draggable:active {
  cursor: grabbing;
}

.avatar-draggable:hover {
  transform: scale(1.05);
  box-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
}

.spotlight {
  box-shadow: 0 0 30px 8px rgba(255, 255, 0, 0.5);
  animation: pulse 1.5s infinite ease-in-out;
}

.glow {
  box-shadow: 0 0 15px 4px rgba(255, 255, 255, 0.3);
}

@keyframes fadeZoomIn {
  from {
    opacity: 0;
    transform: scale(0.95) translateY(20px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

@keyframes fadeSlideUp {
  0% {
    opacity: 0;
    transform: translateY(40px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% {
    box-shadow: 0 0 20px 5px rgba(255, 255, 0, 0.3);
  }
  50% {
    box-shadow: 0 0 35px 10px rgba(255, 255, 0, 0.6);
  }
}
</style>
