<template>
  <div class="smart-cam-wrapper relative overflow-hidden rounded-3xl shadow-2xl border border-white/10">
    <!-- Live Video Feed -->
    <video ref="video" autoplay muted playsinline class="smart-video" />

    <!-- Controls Top Left -->
    <div class="absolute top-3 left-3 flex flex-col gap-2 z-20">
      <button @click="flipCamera" class="control-button" title="Flip Camera">🔄 Flip</button>
      <button @click="toggleBackground" class="control-button" title="Change Background">🎬 BG</button>
      <button @click="applyBeautyFilter" class="control-button" title="Apply Filter">✨ Filter</button>
      <button @click="takeSnapshot" class="control-button" title="Take Snapshot">📸 Snap</button>
      <button @click="toggleMic" class="control-button" :title="micOn ? 'Mute Mic' : 'Unmute Mic'">
        {{ micOn ? '🎙️ Mic On' : '🔇 Mic Off' }}
      </button>
    </div>

    <!-- Emoji Reactions (Top Right) -->
    <div class="absolute top-3 right-3 z-20 flex gap-2">
      <button
        v-for="emoji in emojis"
        :key="emoji"
        @click="triggerReaction(emoji)"
        class="emoji-button"
        :title="`React with ${emoji}`"
      >
        {{ emoji }}
      </button>
    </div>

    <!-- Floating Emoji Reactions -->
    <div class="absolute inset-0 pointer-events-none z-40 overflow-hidden">
      <div
        v-for="(item, index) in floatingReactions"
        :key="item.id"
        class="absolute text-4xl animate-reaction pointer-events-none"
        :style="{
          left: item.x + '%',
          bottom: '0%',
          animationDelay: item.delay + 'ms'
        }"
      >
        {{ item.emoji }}
      </div>
    </div>

    <!-- Sticker Picker -->
    <div class="absolute bottom-24 right-3 z-30">
      <select v-model="selectedSticker" class="sticker-select">
        <option disabled value="">🎭 Sticker Overlay</option>
        <option value="boom">💥 Boom</option>
        <option value="like">👍 Like</option>
        <option value="star">🌟 Star</option>
        <option value="fire">🔥 Fire</option>
      </select>
    </div>

    <!-- Floating Sticker -->
    <transition name="bounce">
      <div v-if="selectedSticker" class="absolute bottom-32 right-6 text-6xl z-30 animate-bounce">
        {{ stickerMap[selectedSticker] }}
      </div>
    </transition>

    <!-- Custom Background Popover -->
    <transition name="fade">
      <div
        v-if="showBackgroundSelector"
        class="absolute top-24 left-3 bg-white text-sm shadow-xl rounded-lg border border-gray-300 z-50 p-3 space-y-2 w-40"
      >
        <div
          v-for="option in backgroundOptions"
          :key="option.value"
          @click="selectBackground(option.value)"
          class="cursor-pointer hover:bg-gray-100 px-3 py-1 rounded transition"
          :class="{ 'bg-indigo-100 font-semibold': selectedBackground === option.value }"
        >
          {{ option.label }}
        </div>
      </div>
    </transition>

    <!-- Share Snapshot -->
    <div
      v-if="snapshots.length"
      class="absolute bottom-3 left-1/2 -translate-x-1/2 bg-black/50 px-4 py-2 rounded-full z-20 text-white text-sm shadow-lg cursor-pointer hover:bg-black/70"
      @click="shareLastSnapshot"
    >
      📤 Share Last Snapshot
    </div>

    <!-- Spotlight -->
    <div v-if="showSpotlight" class="absolute inset-0 bg-gradient-to-br from-indigo-500/10 to-purple-500/10 pointer-events-none animate-pulse" />

    <!-- Flash Effect -->
    <transition name="fade">
      <div v-if="flash" class="absolute inset-0 bg-white/40 backdrop-blur-[1px] animate-flash z-30"></div>
    </transition>

    <!-- Snapshot Thumbnails -->
    <div
      v-if="snapshots.length"
      class="absolute bottom-3 right-3 bg-black/50 p-2 rounded-xl max-w-xs overflow-x-auto z-20 flex gap-2"
    >
      <img
        v-for="(snap, index) in snapshots"
        :key="index"
        :src="snap"
        alt="Snapshot"
        class="w-14 h-10 object-cover rounded border border-white/20"
      />
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, watch } from 'vue'
import { io } from 'socket.io-client'

// Core refs
const video = ref(null)
const flash = ref(false)
const micOn = ref(false)
const useFrontCam = ref(true)
const showSpotlight = ref(true)
const showBackgroundSelector = ref(false)
const selectedBackground = ref('none')
const selectedSticker = ref('')
const snapshots = ref([])
const floatingReactions = ref([])
const currentStream = ref(null)

// Emoji & Sticker data
const emojis = ['🔥', '🎉', '😂', '😍', '💯']
const stickerMap = {
  boom: '💥',
  like: '👍',
  star: '🌟',
  fire: '🔥'
}
const backgroundOptions = [
  { label: 'None', value: 'none' },
  { label: 'Blur', value: 'blur' },
  { label: 'Star Field', value: 'stars' },
  { label: 'City View', value: 'city' }
]

// Fallback UUID
const uuidv4 = () =>
  crypto?.randomUUID?.() ?? Math.random().toString(36).substring(2) + Date.now().toString(36)

// SOCKET.IO connection for real-time emoji sync
const socket = io('http://localhost:5000') // Adjust to your backend URL
socket.on('reaction-broadcast', data => {
  const { emoji } = data
  triggerReaction(emoji, false)
})

// Stop camera stream safely
const stopCurrentStream = () => {
  currentStream.value?.getTracks()?.forEach(track => track.stop())
  currentStream.value = null
}

// Start camera with proper permissions and AI filter support
const startCamera = async () => {
  try {
    stopCurrentStream()
    const constraints = {
      video: {
        facingMode: useFrontCam.value ? 'user' : 'environment',
        width: { ideal: 1280 },
        height: { ideal: 720 },
        frameRate: { ideal: 30 }
      },
      audio: micOn.value
    }
    const stream = await navigator.mediaDevices.getUserMedia(constraints)
    currentStream.value = stream
    if (video.value) {
      video.value.srcObject = stream

      // 🧠 Integrate AI Filter SDK (e.g., TensorFlow.js or Mediapipe)
      applyAIFilter(stream)
    }
  } catch (error) {
    console.warn('🚫 Camera/Microphone access was denied.', error)
    alert('📷 Camera or microphone access was denied.\nPlease allow access from your browser and reload.')
  }
}

// Dummy AI filter application placeholder
const applyAIFilter = (stream) => {
  // In a real-world app, you could load TF.js or MediaPipe here
  // e.g., apply beautification, background removal, face smoothing
  console.log('🧠 AI Filter applied to stream (stub)')
}

const flipCamera = async () => {
  useFrontCam.value = !useFrontCam.value
  await startCamera()
}

const toggleMic = async () => {
  micOn.value = !micOn.value
  await startCamera()
}

const toggleBackground = () => {
  showBackgroundSelector.value = !showBackgroundSelector.value
}

const selectBackground = (val) => {
  selectedBackground.value = val
  updateBackground()
  showBackgroundSelector.value = false
}

const updateBackground = () => {
  const wrapper = video.value?.parentElement
  if (!wrapper) return
  wrapper.classList.remove('bg-blur', 'bg-stars', 'bg-city')
  if (selectedBackground.value !== 'none') {
    wrapper.classList.add(`bg-${selectedBackground.value}`)
  }
}

const applyBeautyFilter = () => {
  if (!video.value) return
  video.value.style.filter = video.value.style.filter
    ? ''
    : 'brightness(1.05) contrast(1.1) saturate(1.2)'
}

const takeSnapshot = () => {
  if (!video.value) return
  flash.value = true
  setTimeout(() => (flash.value = false), 250)

  const canvas = document.createElement('canvas')
  canvas.width = video.value.videoWidth || 1280
  canvas.height = video.value.videoHeight || 720
  const ctx = canvas.getContext('2d')
  ctx.drawImage(video.value, 0, 0, canvas.width, canvas.height)

  const dataUrl = canvas.toDataURL('image/png')
  snapshots.value.push(dataUrl)
  if (snapshots.value.length > 12) snapshots.value.shift()
}

const shareLastSnapshot = () => {
  const last = snapshots.value.at(-1)
  if (!last) return
  const link = document.createElement('a')
  link.href = last
  link.download = 'snapshot.png'
  link.click()
}

const triggerReaction = (emoji, emit = true) => {
  const id = uuidv4()
  const x = Math.random() * 80 + 10
  const delay = Math.random() * 200
  floatingReactions.value.push({ id, emoji, x, delay })

  const audio = new Audio('/sounds/reaction.mp3')
  audio.play().catch(() => {})

  if (emit) {
    socket.emit('send-reaction', { emoji })
  }

  setTimeout(() => {
    floatingReactions.value = floatingReactions.value.filter(r => r.id !== id)
  }, 3000)
}

// Optional voice/gesture stub
const setupVoiceCommand = () => {
  if (!('webkitSpeechRecognition' in window)) return
  const recognition = new webkitSpeechRecognition()
  recognition.continuous = true
  recognition.interimResults = false
  recognition.lang = 'en-US'

  recognition.onresult = (event) => {
    const transcript = event.results[event.results.length - 1][0].transcript.trim()
    console.log('🎤 Voice Command:', transcript)
    if (transcript.toLowerCase().includes('snap')) takeSnapshot()
    if (transcript.toLowerCase().includes('flip')) flipCamera()
  }

  recognition.onerror = (err) => console.warn('Voice error:', err)
  recognition.start()
}

onMounted(() => {
  startCamera()
  setupVoiceCommand()
})
</script>
<style scoped>
.smart-cam-wrapper {
  @apply w-full aspect-video relative overflow-hidden rounded-3xl shadow-2xl border border-white/10 bg-black;
  will-change: transform, opacity;
}

/* Video Area */
.smart-video {
  @apply w-full h-full object-cover rounded-inherit transition-all duration-300 ease-in-out;
  transform-origin: center center;
  backface-visibility: hidden;
}

/* Overlay Control Buttons */
.control-button {
  @apply text-white bg-black/50 hover:bg-black/70 px-3 py-1 rounded-full backdrop-blur-sm text-sm font-semibold shadow-lg transition duration-200 ease-in-out;
  min-width: 42px;
  text-align: center;
}

/* Flash on Snapshot */
.animate-flash {
  animation: flash-glow 0.45s ease-in-out;
}
@keyframes flash-glow {
  0% {
    opacity: 0.95;
  }
  100% {
    opacity: 0;
  }
}

/* Floating Emoji Animation */
.animate-reaction {
  animation: float-up 2.8s ease-out forwards;
  pointer-events: none;
  user-select: none;
  position: absolute;
}
@keyframes float-up {
  0% {
    transform: translateY(0px) scale(1);
    opacity: 1;
  }
  50% {
    transform: translateY(-60px) scale(1.3);
    opacity: 0.9;
  }
  100% {
    transform: translateY(-180px) scale(1.6);
    opacity: 0;
  }
}

/* Fade Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Spotlight Pulse Glow */
.animate-pulse {
  animation: pulse-glow 3.5s ease-in-out infinite;
}
@keyframes pulse-glow {
  0%, 100% {
    opacity: 0.12;
  }
  50% {
    opacity: 0.25;
  }
}

/* Background Effects */
.bg-blur::before,
.bg-stars::before,
.bg-city::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  pointer-events: none;
}

.bg-blur::before {
  backdrop-filter: blur(14px);
}

.bg-stars::before {
  background: url('/assets/bg-stars.gif') center/cover no-repeat;
  opacity: 0.5;
}

.bg-city::before {
  background: url('/assets/bg-city.jpg') center/cover no-repeat;
  opacity: 0.4;
}

/* Snapshot Thumbnail Preview */
.snapshot-thumbnail {
  @apply w-14 h-10 object-cover rounded border border-white/20 shadow;
  transition: transform 0.3s ease;
}
.snapshot-thumbnail:hover {
  transform: scale(1.05);
}

/* Bounce Sticker Animation */
.bounce-enter-active {
  animation: sticker-bounce 0.6s ease;
}
@keyframes sticker-bounce {
  0% {
    transform: scale(0.7);
    opacity: 0;
  }
  50% {
    transform: scale(1.25);
    opacity: 1;
  }
  100% {
    transform: scale(1);
  }
}
</style>
