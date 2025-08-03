<template>
  <div
    class="relative w-full h-screen overflow-hidden font-sans text-white"
    :style="backgroundStyle"
    @click="tapLikeAnywhere"
  >
    <!-- 🔴 TOP BAR (Mobile-first optimized) -->
    <div class="absolute top-0 inset-x-0 z-50 flex flex-wrap justify-between items-center px-3 py-2 bg-black/60 backdrop-blur border-b border-white/10">
      <div class="flex items-center gap-2 overflow-x-auto w-full sm:w-auto">
        <div class="relative shrink-0">
          <img
            :src="hostAvatar"
            alt="Host Avatar"
            class="w-9 h-9 rounded-full object-cover border-2 border-white"
          />
          <span class="absolute -top-0.5 -right-0.5 w-2 h-2 bg-red-500 rounded-full border border-white animate-ping"></span>
        </div>
        <div class="text-xs leading-tight">
          <div class="flex items-center gap-1 font-bold">
            {{ hostUsername }}
            <span v-if="isVerified" class="text-yellow-400">✔</span>
            <span class="bg-white/10 text-pink-400 px-1 ml-1 rounded-full text-[10px]">LIVE Host</span>
          </div>
          <div class="text-pink-400 text-[11px]">{{ viewerCount }} Watching</div>
        </div>
        <div class="flex items-center gap-1 px-2 py-0.5 bg-white/10 rounded-full text-pink-300 text-xs font-bold">
          <i class="i-tabler-heart-filled text-pink-400 text-sm"></i>
          <span>{{ likeCount }}</span>
        </div>
        <span class="px-2 py-0.5 bg-yellow-500/20 text-yellow-300 rounded-full text-[10px]">🔥 Daily Ranking</span>
        <button
          @click="showAddGoal = true"
          class="px-2 py-0.5 bg-pink-500 text-white rounded-full text-[10px] hover:bg-pink-600"
        >
          ➕ Goal
        </button>
      </div>
    </div>

    <!-- 🎯 Topic & Ticker (mobile stack) -->
    <div class="absolute top-14 inset-x-0 px-4 z-40 text-center">
      <marquee behavior="scroll" direction="left" scrollamount="3" class="bg-black/70 text-xs text-white py-1 rounded">
        🚀 Boost visibility & earn coins | 🌐 Invite & get rewards
      </marquee>
      <div class="mt-2">
        <div class="bg-white/10 text-xs px-3 py-1 rounded-full border border-white/20 inline-block">
          🎯 Topic: Boosting Business Engagement 🔥
        </div>
        <div
          v-if="currentGoal"
          class="mt-1 bg-gradient-to-r from-yellow-400 to-pink-500 text-white text-xs px-3 py-1 rounded-full border border-white/20 animate-pulse inline-block"
        >
          🎯 Goal: {{ currentGoal }}
        </div>
      </div>
    </div>

    <!-- 📹 Video Background -->
    <video
      ref="videoFeed"
      autoplay
      playsinline
      muted
      class="absolute inset-0 w-full h-full object-cover z-0"
    />

    <!-- 🎭 Effects & Visuals -->
    <FaceFilterLayer :filter="selectedFilter" />
    <FloatingParticles />
    <AnimatedGiftEffect />
    <StageLighting />

    <LiveGiftAnimation
      v-if="currentGiftAnimation"
      :gift="currentGiftAnimation"
      class="absolute bottom-[120px] top-[40%] left-0 right-0 z-50 pointer-events-none"
    />

    <transition-group
      name="fly"
      tag="div"
      class="absolute inset-x-0 bottom-[120px] top-[40%] z-50 pointer-events-none"
    >
      <GiftFly
        v-for="(gift, index) in flyingGifts"
        :key="gift.id || index"
        :gift="gift"
      />
    </transition-group>

    <!-- 💬 Chat Feed & Input -->
    <LiveMessageFeed
      :messages="liveMessages"
      class="fixed bottom-[115px] left-3 z-40 w-[92vw] max-w-md"
    />
    <ChatInput
      v-model="chatMessage"
      @send="handleSendMessage"
      class="fixed bottom-3 left-3 z-50 w-[92vw] max-w-md"
    />

    <!-- ❤️ Likes Button -->
    <div class="absolute bottom-44 right-3 z-50 flex flex-col items-center">
      <button
        @click="tapLikeAnywhere"
        class="w-9 h-9 bg-pink-500 hover:bg-pink-600 rounded-full flex items-center justify-center"
      >
        <i class="i-tabler-heart-filled text-white text-xl"></i>
      </button>
      <span class="text-sm text-pink-300 font-bold mt-1">{{ likeCount }}</span>
    </div>

    <!-- 🧭 Bottom Actions Row -->
    <div class="absolute bottom-16 left-0 right-0 px-4 z-40">
      <div class="flex justify-between items-center">
        <template v-for="action in bottomActions" :key="action.label">
          <button
            @click="action.onClick"
            :class="[
              'w-12 h-12 flex flex-col items-center justify-center rounded-full text-xs shadow border border-white/10 backdrop-blur-lg transition',
              action.label === 'Gifts' ? 'bg-pink-600'
                : action.label === 'Share' ? 'bg-red-600'
                : action.label === '+Guests' ? 'bg-indigo-700'
                : action.label === '+Hosts' ? 'bg-blue-600'
                : 'bg-gray-700',
              'hover:scale-105'
            ]"
          >
            <i :class="action.icon + ' text-base'" />
            <span class="text-[10px] mt-0.5">{{ action.label }}</span>
          </button>
        </template>
      </div>
    </div>

    <!-- 💡 Smart Tips -->
    <transition name="fade">
      <div
        v-if="aiSuggestions.length"
        class="fixed bottom-[180px] left-3 z-40 bg-white/10 backdrop-blur p-2 rounded-xl text-xs w-[92vw] max-w-md"
      >
        <div class="font-bold mb-1">🧠 Smart Tips:</div>
        <ul class="list-disc list-inside">
          <li v-for="(suggestion, i) in aiSuggestions" :key="i">{{ suggestion }}</li>
        </ul>
      </div>
    </transition>

    <!-- 📢 Announcement -->
    <transition name="fade">
      <div
        v-if="streamAnnouncement"
        class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50 bg-black/80 px-4 py-2 rounded-xl text-sm font-bold text-white shadow"
      >
        {{ streamAnnouncement }}
      </div>
    </transition>

    <!-- 📦 Panels -->
    <GiftDrawer v-if="showGiftDrawer" @close="showGiftDrawer = false" @send="handleGiftSend" @recharge="goToRecharge" />
    <GiftsPanel v-if="showGiftDrawer" :gifts="giftList" @close="showGiftDrawer = false" @send="handleGiftSend" />
    <SuperChatModal v-if="showSuperChatModal" @close="showSuperChatModal = false" @send="handleSuperChat" />
    <SettingsModal v-if="showSettings" @close="showSettings = false" />
    <WalletTopupModal v-if="showWalletTopup" @close="showWalletTopup = false" />
    <HostsPanel v-if="showHostsPanel" @close="closeHostsPanel" />
    <GuestsPanel v-if="showGuestPanel" @close="closeGuestsPanel" />
    <EffectsPanel v-if="showEffectsPanel" @close="showEffectsPanel = false" />
    <AddGoal v-if="showAddGoal" @close="showAddGoal = false" @set-goal="goal => currentGoal = goal" />
  </div>
</template>
<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import { nanoid } from 'nanoid'

// 🎯 User
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()
const router = useRouter()

// 👤 Host Info
const username = computed(() => userStore.username || 'Host')
const hostAvatar = computed(() => userStore.profileImage || '/avatars/default.png')
const isVerified = computed(() => userStore.is_verified === true)

// 📦 UI States
const showSettings = ref(false)
const showWalletTopup = ref(false)
const showMoreOptions = ref(false)
const showGiftDrawer = ref(false)
const showSuperChatModal = ref(false)
const showHostsPanel = ref(false)
const showGuestPanel = ref(false)
const showEffectsPanel = ref(false)
const showAddGoal = ref(false)

// 🎁 Gift System
import { giftList } from '@/data/giftList.js'
const currentGiftAnimation = ref(null)
const flyingGifts = ref([])

// 💬 Messaging
const liveMessages = ref([])
const chatMessage = ref('')

// 🔗 Sharing
const streamLink = window.location.href
const copyLink = () => {
  navigator.clipboard.writeText(streamLink)
  alert('🔗 Link copied!')
  showMoreOptions.value = false
}
const shareStream = () => copyLink()

// 🔊 Likes
const likeCount = ref(0)
const likeTapCount = ref(0)
const floatingLikes = ref([])
const tapLikeAnywhere = (event) => {
  likeCount.value++
  likeTapCount.value++
  floatingLikes.value.push({
    id: nanoid(),
    x: event?.clientX || window.innerWidth / 2,
    y: event?.clientY || window.innerHeight - 120,
    createdAt: Date.now()
  })
  setTimeout(() => floatingLikes.value.shift(), 1200)
}

// 📢 SuperChat
const sendSuperChat = () => showSuperChatModal.value = true
const handleSuperChat = ({ amount, message }) => {
  liveMessages.value.push({
    id: nanoid(),
    sender: username.value,
    type: 'chat',
    text: `🌟 SuperChat (${amount}💰): ${message}`
  })
}

// 🧠 AI Suggestions
const aiSuggestions = ref([])
const streamAnnouncement = ref('')
const currentGoal = ref('')

// ✨ Send Gift
const sendGift = (gift) => {
  liveMessages.value.push({
    id: nanoid(),
    sender: username.value,
    type: 'gift',
    icon: gift.icon,
    name: gift.name
  })
  flyingGifts.value.push(gift)
  setTimeout(() => flyingGifts.value.shift(), 3000)
  currentGiftAnimation.value = gift
  setTimeout(() => currentGiftAnimation.value = null, 4000)
}
const handleGiftSend = (gift) => sendGift(gift)

// 📲 Send Chat Message
const handleSendMessage = () => {
  if (!chatMessage.value.trim()) return
  sendMessage(chatMessage.value)
  chatMessage.value = ''
}
const sendMessage = (msg) => {
  liveMessages.value.push({ id: nanoid(), sender: 'You', type: 'chat', text: msg })
}

// 👥 Guests
const guestRequests = ref([
  { id: 'guest_1', name: 'Monarutta ❤', avatar: '/avatars/user1.png' },
  { id: 'guest_2', name: 'Besasha 💖', avatar: '/avatars/user2.png' }
])
const joinRequests = ref([])
const incomingRequest = ref(null)
const activeGuest = ref(null)
const approveRequest = (guest) => joinRequests.value = joinRequests.value.filter(r => r.timestamp !== guest.timestamp)
const rejectRequest = (index) => joinRequests.value.splice(index, 1)
const handleGuestRequest = ({ accepted, guest }) => {
  if (accepted) activeGuest.value = guest
  incomingRequest.value = null
}
const handleApproveGuest = (guestId) => guestRequests.value = guestRequests.value.filter(g => g.id !== guestId)
const handleRejectGuest = (guestId) => guestRequests.value = guestRequests.value.filter(g => g.id !== guestId)

// 🔧 Misc Controls
const viewerCount = ref(0)
const selectedFilter = ref('none')

// 🎯 Goals
const setGoal = (goal) => {
  currentGoal.value = goal
  showAddGoal.value = false
}

// ⛔ End Stream
const confirmEndStream = () => {
  if (confirm('Are you sure you want to end the live?')) router.push('/dashboard')
}

// 🎮 Bottom Actions
const bottomActions = [
  { label: '+Hosts', icon: 'i-tabler-user-plus', onClick: () => showHostsPanel.value = true },
  { label: '+Guests', icon: 'i-tabler-users', onClick: () => showGuestPanel.value = true },
  { label: 'Share', icon: 'i-tabler-share', onClick: shareStream },
  { label: 'Gifts', icon: 'i-tabler-gift', onClick: () => showGiftDrawer.value = true },
  { label: 'SuperChat', icon: 'i-tabler-message-star', onClick: sendSuperChat },
  { label: 'More', icon: 'i-tabler-dots', onClick: () => showMoreOptions.value = !showMoreOptions.value }
]

// 🧠 Background Styling
const backgroundStyle = `
  background: radial-gradient(circle at top left, #111827, #1e3a8a, #7c3aed);
  background-size: cover;
  background-repeat: no-repeat;
`

// 🔁 Lifecycle
onMounted(() => {
  setInterval(() => viewerCount.value += Math.floor(Math.random() * 2) + 1, 3000)
  window.addEventListener('click', tapLikeAnywhere)
  window.addEventListener('touchstart', tapLikeAnywhere)
  setInterval(() => {
    const now = Date.now()
    floatingLikes.value = floatingLikes.value.filter(like => now - like.createdAt < 1200)
  }, 500)
})
onBeforeUnmount(() => {
  window.removeEventListener('click', tapLikeAnywhere)
  window.removeEventListener('touchstart', tapLikeAnywhere)
})
</script>
<style scoped>
/* 🎥 Video Feed Background */
video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
  filter: brightness(0.95) contrast(1.1);
}

/* 🌐 Universal Icon Button */
.icon-btn {
  color: white;
  font-size: 1.25rem;
  padding: 0.5rem;
  border-radius: 9999px;
  transition: all 0.3s ease-in-out;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.35);
}
.icon-btn:hover {
  color: #67e8f9;
  transform: scale(1.1);
  filter: drop-shadow(0 0 6px rgba(0, 255, 255, 0.3));
}

/* 🔘 Bottom Action Buttons */
.btn-action {
  color: white;
  font-size: 1.125rem;
  padding: 0.75rem;
  border-radius: 9999px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(255, 255, 255, 0.07);
  backdrop-filter: blur(22px);
  box-shadow: 0 8px 26px rgba(0, 0, 0, 0.45);
  transition: transform 0.3s ease-in-out;
}
.btn-action:hover {
  transform: scale(1.25);
  color: #a5b4fc;
}
.btn-action::after {
  content: attr(data-label);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  margin-bottom: 0.5rem;
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.7);
  font-weight: 600;
}

/* 💬 Chat Container */
.chat-box {
  background: linear-gradient(to bottom right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.3));
  color: white;
  border-radius: 0.75rem;
  padding: 0.75rem;
  box-shadow: inset 0 0 8px rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  max-height: 40vh;
  overflow-y: auto;
  animation: fadeInUp 0.5s ease-out both;
}
@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(16px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 🌌 Floating Particles */
.particle {
  position: absolute;
  width: 0.5rem;
  height: 0.5rem;
  background-color: white;
  border-radius: 9999px;
  opacity: 0.1;
  pointer-events: none;
  animation: float 6s ease-in-out infinite;
}
@keyframes float {
  0%, 100% {
    transform: translateY(0) scale(1);
  }
  50% {
    transform: translateY(-180px) scale(1.25);
  }
}

/* 💖 Floating Likes */
.floating-like {
  position: absolute;
  color: #f472b6;
  font-size: 1.25rem;
  pointer-events: none;
  user-select: none;
  animation: floatUp 1.1s ease-out forwards;
}
@keyframes floatUp {
  0% {
    transform: translate(-50%, 0) scale(1);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -100px) scale(1.4);
    opacity: 0;
  }
}

/* ✨ Fly Transition */
.float-enter-active,
.float-leave-active {
  transition: all 1.2s ease-out;
}
.float-enter-from,
.float-leave-to {
  opacity: 0;
  transform: translateY(0);
}

/* 💠 Scrollbar for chat */
.chat-box::-webkit-scrollbar {
  width: 6px;
}
.chat-box::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.15);
  border-radius: 6px;
}

/* 🎇 Gift Splash Animation */
.gift-splash {
  position: absolute;
  width: 4rem;
  height: 4rem;
  pointer-events: none;
  user-select: none;
  animation: giftBoom 0.8s ease-out forwards;
}
@keyframes giftBoom {
  0% {
    opacity: 0;
    transform: scale(0.5) rotate(0deg);
  }
  50% {
    opacity: 1;
    transform: scale(1.3) rotate(180deg);
  }
  100% {
    opacity: 0;
    transform: scale(0.8) rotate(360deg);
  }
}

/* 😍 Emoji Reaction Fly */
.emoji-fly {
  position: absolute;
  font-size: 1.875rem;
  pointer-events: none;
  animation: emojiFloat 1.5s ease-in-out forwards;
}
@keyframes emojiFloat {
  0% {
    opacity: 0;
    transform: translateY(40px) scale(0.7);
  }
  50% {
    opacity: 1;
    transform: translateY(-10px) scale(1.2);
  }
  100% {
    opacity: 0;
    transform: translateY(-100px) scale(0.8);
  }
}

/* 📱 Mobile Responsiveness */
@media (max-width: 768px) {
  .btn-action {
    padding: 0.5rem;
    width: 2.75rem;
    height: 2.75rem;
    font-size: 0.875rem;
  }
  .chat-box {
    padding: 0.5rem;
    font-size: 0.85rem;
  }
  .icon-btn {
    padding: 0.4rem;
    font-size: 1rem;
  }
}
</style>
