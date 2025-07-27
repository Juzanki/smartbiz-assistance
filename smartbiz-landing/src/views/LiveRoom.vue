<template>
  <div
    class="relative w-full h-screen overflow-hidden font-sans text-white"
    :style="backgroundStyle"
    @click="tapLikeAnywhere"
  >
    <!-- 🔴 TOP BAR - Host Info -->
    <div
      class="absolute top-0 inset-x-0 z-50 flex flex-wrap justify-between items-center px-3 py-2 bg-black/60 backdrop-blur border-b border-white/10"
    >
      <div class="flex items-center gap-2 overflow-x-auto max-w-[70vw]">
        <div class="relative shrink-0">
          <img
            :src="hostAvatar"
            alt="Host Avatar"
            class="w-8 h-8 rounded-full object-cover border-2 border-white"
          />
          <span
            class="absolute -top-0.5 -right-0.5 w-2 h-2 bg-red-500 rounded-full border border-white animate-ping"
          ></span>
        </div>
        <div class="text-xs leading-tight">
          <div class="flex items-center gap-1 font-bold">
            {{ hostUsername }}
            <span v-if="isVerified" class="text-yellow-400">✔</span>
            <span
              class="bg-white/10 text-pink-400 px-1 ml-1 rounded-full text-[10px]"
              >LIVE Host</span
            >
          </div>
          <div class="text-pink-400 text-[11px]">{{ viewerCount }} Watching</div>
        </div>
        <div
          class="flex items-center gap-1 px-2 py-0.5 bg-white/10 rounded-full text-pink-300 text-xs font-bold"
        >
          <i class="i-tabler-heart-filled text-pink-400 text-sm"></i>
          <span>{{ likeCount }}</span>
        </div>
        <span
          class="px-2 py-0.5 bg-yellow-500/20 text-yellow-300 rounded-full text-[10px]"
          >🔥 Daily Ranking</span
        >
        <button
          @click="showAddGoal = true"
          class="px-2 py-0.5 bg-pink-500 text-white rounded-full text-[10px] hover:bg-pink-600"
        >
          ➕ Goal
        </button>
      </div>

      <div class="flex gap-1 items-center text-[10px] mt-2 sm:mt-0">
        <button
          class="px-2 py-1 rounded-full bg-blue-500 hover:brightness-110"
        >
          ⭐ Featured
        </button>
        <button
          class="px-2 py-1 rounded-full bg-orange-500 hover:brightness-110"
        >
          🌍 Explore
        </button>
        <span class="px-2 py-1 rounded-full bg-white/10 text-blue-200"
          >👑 TopFan</span
        >
        <span class="text-white/70 hidden sm:inline">{{ viewerCount }}</span>
        <span class="text-red-500 animate-pulse">● LIVE</span>
        <button
          @click="confirmEndStream"
          class="ml-1 px-2 py-1 bg-red-600 hover:bg-red-700 rounded-full"
        >
          ✖ End
        </button>
      </div>
    </div>

    <!-- 💬 Ticker -->
    <div
      class="absolute top-12 left-0 right-0 z-40 text-xs px-3 py-1 bg-black/70 text-white"
    >
      <marquee behavior="scroll" direction="left" scrollamount="4">
        🚀 Boost visibility & earn coins | 🌐 Invite & get rewards
      </marquee>
    </div>

    <!-- 🎯 Topic -->
    <div
      class="absolute top-20 left-1/2 -translate-x-1/2 z-40 text-center w-full max-w-[85vw]"
    >
      <div
        class="bg-white/10 text-xs px-3 py-1 rounded-full border border-white/20"
      >
        🎯 Topic: Boosting Business Engagement 🔥
      </div>
      <div
        v-if="currentGoal"
        class="mt-1 bg-gradient-to-r from-yellow-400 to-pink-500 text-white text-xs px-3 py-1 rounded-full border border-white/20 animate-pulse"
      >
        🎯 Goal: {{ currentGoal }}
      </div>
    </div>

    <!-- 📹 Video -->
    <video
      ref="videoFeed"
      autoplay
      playsinline
      muted
      class="absolute inset-0 w-full h-full object-cover z-0"
    />

    <!-- 🎭 Effects -->
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

    <!-- 💬 Chat & Input -->
    <LiveMessageFeed
      :messages="liveMessages"
      class="fixed bottom-[115px] left-3 z-40 w-[92vw] max-w-md"
    />
    <ChatInput
      v-model="chatMessage"
      @send="handleSendMessage"
      class="fixed bottom-3 left-3 z-50 w-[92vw] max-w-md"
    />

    <!-- ❤️ Likes -->
    <div class="absolute bottom-44 right-3 z-50 flex flex-col items-center">
      <button
        @click="tapLikeAnywhere"
        class="w-9 h-9 bg-pink-500 hover:bg-pink-600 rounded-full flex items-center justify-center"
      >
        <i class="i-tabler-heart-filled text-white text-xl"></i>
      </button>
      <span class="text-sm text-pink-300 font-bold mt-1">{{ likeCount }}</span>
    </div>

    <!-- 🧭 Bottom Actions -->
    <div class="absolute bottom-16 left-0 right-0 px-4 z-40">
      <div class="flex justify-between items-center">
        <template v-for="action in bottomActions" :key="action.label">
          <button
            @click="action.onClick"
            :class="[
              'w-12 h-12 flex flex-col items-center justify-center rounded-full text-xs shadow border border-white/10 backdrop-blur-lg transition',
              action.label === 'Gifts'
                ? 'bg-pink-600'
                : action.label === 'Share'
                ? 'bg-red-600'
                : action.label === '+Guests'
                ? 'bg-indigo-700'
                : action.label === '+Hosts'
                ? 'bg-blue-600'
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

    <!-- 🧠 AI Tips -->
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

    <!-- 🔔 Announcement -->
    <transition name="fade">
      <div
        v-if="streamAnnouncement"
        class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 z-50 bg-black/80 px-4 py-2 rounded-xl text-sm font-bold text-white shadow"
      >
        {{ streamAnnouncement }}
      </div>
    </transition>

    <!-- Panels -->
    <GiftDrawer
      v-if="showGiftDrawer"
      @close="showGiftDrawer = false"
      @send="handleGiftSend"
      @recharge="goToRecharge"
    />
    <GiftsPanel
      v-if="showGiftDrawer"
      :gifts="giftList"
      @close="showGiftDrawer = false"
      @send="handleGiftSend"
    />
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

// 🧠 === Store & Router ===
import { useUserStore } from '@/stores/user'
const router = useRouter()
const userStore = useUserStore()

// 👤 === User Info ===
const username = computed(() => userStore.username || 'Host')
const hostAvatar = computed(() => userStore.profileImage || '/avatars/default.png')
const isVerified = computed(() => userStore.is_verified === true)

// 🧩 === Components ===
import LiveMessageFeed from '@/components/Live/LiveMessageFeed.vue'
import ChatInput from '@/components/ChatInput.vue'
import SettingsModal from '@/components/modals/SettingsModal.vue'
import WalletTopupModal from '@/components/modals/WalletTopupModal.vue'
import GiftDrawer from '@/components/modals/GiftDrawer.vue'
import GiftsPanel from '@/components/modals/GiftsPanel.vue'
import SuperChatModal from '@/components/modals/SuperChatModal.vue'
import AddGoal from '@/components/Goals/AddGoal.vue'
import EffectsPanel from '@/components/modals/EffectsPanel.vue'
import HostsPanel from '@/components/modals/HostsPanel.vue'
import GuestsPanel from '@/components/modals/GuestsPanel.vue'
import FloatingParticles from '@/components/effects/FloatingParticles.vue'
import AnimatedGiftEffect from '@/components/effects/AnimatedGiftEffect.vue'
import StageLighting from '@/components/effects/StageLighting.vue'
import FaceFilterLayer from '@/components/effects/FaceFilterLayer.vue'
import FaceFilterSelector from '@/components/FaceFilterSelector.vue'
import LiveGiftAnimation from '@/components/LiveGiftAnimation.vue'
import GiftFly from '@/components/GiftFly.vue'

// 📊 === State Management ===
import { giftList } from '@/data/giftList.js'
const viewerCount = ref(0)
const likeCount = ref(0)
const likeTapCount = ref(0)
const currentGoal = ref('')
const chatMessage = ref('')
const liveMessages = ref([])
const currentGiftAnimation = ref(null)
const flyingGifts = ref([])
const floatingLikes = ref([])
const aiSuggestions = ref([])
const streamAnnouncement = ref('')
const aiHostAvatar = '/avatars/aihost.png'
const showAiHostAvatar = ref(true)

// 🎛️ === UI States ===
const showSettings = ref(false)
const showWalletTopup = ref(false)
const showMoreOptions = ref(false)
const showGiftDrawer = ref(false)
const showSuperChatModal = ref(false)
const showHostsPanel = ref(false)
const showGuestPanel = ref(false)
const showReplay = ref(false)
const showEffects = ref(false)
const showSummary = ref(false)
const showVoiceChat = ref(false)
const showAddGoal = ref(false)
const showFaceFilterSelector = ref(false)
const selectedFilter = ref('none')

// 🧑‍🤝‍🧑 === Guest Management ===
const guestRequests = ref([
  { id: 'guest_1', name: 'Monarutta ❤', avatar: '/avatars/user1.png' },
  { id: 'guest_2', name: 'Besasha 💖', avatar: '/avatars/user2.png' }
])
const joinRequests = ref([])
const incomingRequest = ref(null)
const activeGuest = ref(null)

// 🌌 === Background Styling ===
const backgroundStyle = `
  background: radial-gradient(circle at top left, #111827, #1e3a8a, #7c3aed);
  background-size: cover;
  background-repeat: no-repeat;
`

// 💬 === Messaging ===
const handleSendMessage = () => {
  if (!chatMessage.value.trim()) return
  sendMessage(chatMessage.value)
  chatMessage.value = ''
}
const sendMessage = (msg) => {
  liveMessages.value.push({ id: nanoid(), sender: 'You', type: 'chat', text: msg })
}

// ❤️ === Likes ===
const tapLikeAnywhere = (event) => {
  likeCount.value++
  likeTapCount.value++
  const like = {
    id: nanoid(),
    x: event?.clientX || window.innerWidth / 2,
    y: event?.clientY || window.innerHeight - 120,
    createdAt: Date.now()
  }
  floatingLikes.value.push(like)
  setTimeout(() => floatingLikes.value.shift(), 1200)
}

// 💰 === SuperChat ===
const sendSuperChat = () => showSuperChatModal.value = true
const handleSuperChat = ({ amount, message }) => {
  liveMessages.value.push({
    id: nanoid(),
    sender: username.value,
    type: 'chat',
    text: `🌟 SuperChat (${amount}💰): ${message}`
  })
}

// 🎁 === Gift System ===
const sendGift = (gift) => {
  liveMessages.value.push({ id: nanoid(), sender: username.value, type: 'gift', icon: gift.icon, name: gift.name })
  flyingGifts.value.push(gift)
  setTimeout(() => flyingGifts.value.shift(), 3000)
  currentGiftAnimation.value = gift
  setTimeout(() => currentGiftAnimation.value = null, 4000)
}
const handleGiftSend = (gift) => sendGift(gift)

// 🧑‍💻 === Guest Requests ===
const handleGuestRequest = ({ accepted, guest }) => {
  if (accepted) activeGuest.value = guest
  incomingRequest.value = null
}
const approveRequest = (guest) => joinRequests.value = joinRequests.value.filter(r => r.timestamp !== guest.timestamp)
const rejectRequest = (index) => joinRequests.value.splice(index, 1)
const handleApproveGuest = (guestId) => guestRequests.value = guestRequests.value.filter(g => g.id !== guestId)
const handleRejectGuest = (guestId) => guestRequests.value = guestRequests.value.filter(g => g.id !== guestId)

// 🛠️ === UI Actions ===
const toggleSettings = () => showSettings.value = !showSettings.value
const toggleMoreOptions = () => showMoreOptions.value = !showMoreOptions.value
const toggleReplay = () => showReplay.value = !showReplay.value
const openEffects = () => showEffects.value = true
const openSummary = () => showSummary.value = true
const startVoiceChat = () => showVoiceChat.value = true
const openHostsPanel = () => showHostsPanel.value = true
const openGuestsPanel = () => showGuestPanel.value = true
const closeHostsPanel = () => showHostsPanel.value = false
const closeGuestsPanel = () => showGuestPanel.value = false
const setGoal = (goal) => {
  currentGoal.value = goal
  showAddGoal.value = false
}
const confirmEndStream = () => {
  if (confirm('Are you sure you want to end the live?')) {
    router.push('/dashboard')
  }
}

// 🔗 === Sharing Features ===
const streamLink = window.location.href
const copyLink = () => {
  navigator.clipboard.writeText(streamLink)
  alert('🔗 Link copied!')
  showMoreOptions.value = false
}
const shareStream = () => copyLink()

// 🎮 === Bottom Bar Actions ===
const bottomActions = [
  { label: '+Hosts', icon: 'i-tabler-user-plus', onClick: openHostsPanel },
  { label: '+Guests', icon: 'i-tabler-users', onClick: openGuestsPanel, hasNotification: ref(false) },
  { label: 'Share', icon: 'i-tabler-share', onClick: shareStream },
  { label: 'Gifts', icon: 'i-tabler-gift', onClick: () => showGiftDrawer.value = true },
  { label: 'SuperChat', icon: 'i-tabler-message-star', onClick: sendSuperChat },
  { label: 'More', icon: 'i-tabler-dots', onClick: toggleMoreOptions }
]

// 🔁 === Lifecycle Hooks ===
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
/* 🎥 VIDEO BACKDROP - Hugs screen with elegance */
video {
  @apply absolute inset-0 w-full h-full object-cover z-[-1];
  filter: brightness(0.95) contrast(1.1);
}

/* ✨ UNIVERSAL GLASS ICON BUTTONS */
.icon-btn {
  @apply text-white text-xl p-2 rounded-full transition-all duration-300 ease-in-out;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.35);
}
.icon-btn:hover {
  @apply text-cyan-300 scale-110;
  filter: drop-shadow(0 0 6px rgba(0, 255, 255, 0.3));
}

/* 🔘 BOTTOM ACTION CONTROLS */
.btn-action {
  @apply text-white text-lg p-3 rounded-full relative border border-white/10 transition-transform duration-300 ease-in-out;
  background: rgba(255, 255, 255, 0.07);
  backdrop-filter: blur(22px);
  box-shadow: 0 8px 26px rgba(0, 0, 0, 0.45);
}
.btn-action:hover {
  @apply scale-125 text-indigo-300;
}
.btn-action::after {
  content: attr(data-label);
  @apply absolute bottom-full left-1/2 -translate-x-1/2 mb-2 text-xs text-white/70 font-semibold tracking-wide;
}

/* 💬 LIVE CHAT CONTAINER */
.chat-box {
  @apply bg-gradient-to-br from-black/70 to-black/30 text-white rounded-xl p-3 shadow-inner border border-white/10 backdrop-blur-lg max-h-[40vh] overflow-y-auto;
  animation: fadeInUp 0.5s ease-out both;
}

/* 💬 CHAT ANIMATION ENTRANCE */
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

/* 🌌 PARTICLES FLOATING DECORATION */
.particle {
  @apply absolute w-2 h-2 bg-white rounded-full opacity-10 pointer-events-none;
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

/* 💖 FLOATING HEART ANIMATION (Likes) */
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

.floating-like {
  @apply absolute text-pink-400 text-lg pointer-events-none select-none;
  animation: floatUp 1.1s ease-out forwards;
}

/* 🎈 FLOATING CHAT ENTRANCE */
.float-enter-active,
.float-leave-active {
  @apply transition-all duration-[1200ms] ease-out;
}
.float-enter-from,
.float-leave-to {
  @apply opacity-0 translate-y-0;
}

/* 💠 Custom Scrollbar for Chat */
.chat-box::-webkit-scrollbar {
  width: 6px;
}
.chat-box::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.15);
  border-radius: 6px;
}

/* 🎆 GIFTS & EMOJI PARTICLES */
.gift-splash {
  @apply absolute w-16 h-16 pointer-events-none select-none;
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

/* 🌠 EMOJI REACTIONS (LIKE TIKTOK) */
.emoji-fly {
  @apply absolute text-3xl pointer-events-none;
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
</style>
