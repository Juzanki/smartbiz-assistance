<template>
  <div class="min-h-screen bg-white text-dark dark:bg-dark dark:text-white">
    <!-- 🌐 Navbar -->
    <nav class="flex items-center justify-between px-4 py-3 bg-primary shadow-sm">
      <!-- 📛 Logo + Brand -->
      <router-link to="/" class="flex items-center gap-2">
        <img
          src="/icons/logo.png"
          alt="SmartBiz Logo"
          class="rounded-full"
          style="width: 36px; height: 36px; object-fit: cover; background: #fff; border: 2px solid #FFD700;"
        />
        <span class="text-white font-bold text-base hidden sm:inline">SmartBiz</span>
      </router-link>

      <!-- 🔐 Auth Buttons -->
      <div class="flex gap-2">
        <router-link to="/login" class="btn btn-sm btn-outline-light">Login</router-link>
        <router-link to="/signup" class="btn btn-sm btn-warning text-primary fw-bold">Sign Up</router-link>
      </div>
    </nav>

    <!-- 🎯 Hero Section -->
    <section class="text-center px-4 py-6 bg-light dark:bg-dark">
      <h1 class="text-xl sm:text-2xl font-bold mb-2 leading-snug text-primary dark:text-yellow-400">
        Automate Messaging Across All Platforms
      </h1>
      <p class="text-sm text-gray-700 dark:text-gray-300 mb-4">
        Connect WhatsApp, Telegram, SMS & Email in one smart dashboard.
      </p>
      <router-link to="/signup" class="btn btn-warning btn-glow text-primary fw-bold">
        Get Started Free (1 Month)
      </router-link>
    </section>

    <!-- 🛠️ Features -->
    <section id="features" class="py-5 bg-white dark:bg-dark px-4">
      <div class="container">
        <h2 class="text-center text-lg font-bold text-primary dark:text-yellow-400 mb-4">Platform Features</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <div
            v-for="feature in features"
            :key="feature.id"
            class="bg-white dark:bg-gray-800 rounded-lg p-4 shadow-sm text-center hover:shadow-md transition"
          >
            <div class="text-3xl mb-2 text-warning">{{ feature.icon }}</div>
            <h3 class="font-bold text-lg mb-1">{{ feature.title }}</h3>
            <p class="text-sm text-gray-600 dark:text-gray-300">{{ feature.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 🌟 Testimonials -->
    <section class="py-6 bg-light dark:bg-secondary text-center px-4">
      <h2 class="text-lg font-bold text-primary dark:text-yellow-400 mb-4">What Our Users Say</h2>
      <div class="max-w-md mx-auto bg-white dark:bg-gray-800 rounded shadow p-4">
        <p class="italic">“SmartBiz helped me automate WhatsApp replies while I sleep. I’ve tripled my customer response rate!”</p>
        <p class="font-bold mt-2">— Asha, Business Owner</p>
      </div>
    </section>

    <!-- 🔻 Footer Slot -->
    <slot />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

/* ✅ 1. Platform Features (Smart Cards) */
const features = ref([
  { id: 1, icon: '📱', title: 'WhatsApp Automation', desc: 'Auto-reply and broadcast to clients on WhatsApp.' },
  { id: 2, icon: '🤖', title: 'Telegram Bots', desc: 'Engage users with customizable Telegram bots.' },
  { id: 3, icon: '✉️', title: 'SMS Campaigns', desc: 'Send bulk promotions and OTPs via SMS.' },
  { id: 4, icon: '📧', title: 'Email Sequences', desc: 'Automate marketing emails with rich templates.' },
  { id: 5, icon: '📊', title: 'Unified Analytics', desc: 'Get insights across all messaging channels.' },
  { id: 6, icon: '🔌', title: 'API & Webhooks', desc: 'Easily connect with your CRM or ERP.' },
])

/* ✅ 2. Dark Mode (Mobile Friendly Theme Toggle) */
const isDark = ref(false)

const applyTheme = () => {
  document.documentElement.classList.toggle('dark', isDark.value)
  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
}

const detectTheme = () => {
  const saved = localStorage.getItem('theme')
  if (saved) {
    isDark.value = saved === 'dark'
  } else {
    isDark.value = window.matchMedia('(prefers-color-scheme: dark)').matches
  }
  applyTheme()
}

onMounted(() => {
  detectTheme()
})

const toggleTheme = () => {
  isDark.value = !isDark.value
  applyTheme()
}

/* ✅ 3. Scroll to Demo Section (Removed Video, but keep logic optional) */
const scrollToDemo = () => {
  const section = document.querySelector('#features')
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' })
  } else {
    console.warn('📌 Feature section not found')
  }
}
</script>
<style scoped>
/* 🎬 Smooth Entrance Animation */
@keyframes fadeInSlide {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
.animate-fade-in {
  animation: fadeInSlide 0.7s ease-out both;
}

/* 🎨 Brand Colors */
.bg-primary {
  background-color: #1E40AF !important;
}
.text-primary {
  color: #1E40AF !important;
}
.text-warning {
  color: #FFA500 !important;
}
.bg-warning {
  background-color: #FFD600 !important;
}

/* 🌙 Dark Mode Styling */
.dark .bg-dark {
  background-color: #0b1120 !important;
}
.dark .text-warning {
  color: #FFD600 !important;
}
.dark .bg-light {
  background-color: #1a1a2e !important;
}
.dark .text-secondary {
  color: #cbd5e1 !important;
}

/* ✨ Buttons & Hover */
.btn-glow {
  transition: box-shadow 0.3s ease-in-out;
}
.btn-glow:hover {
  box-shadow: 0 0 16px rgba(255, 214, 0, 0.6);
}
.hover-shadow-sm:hover {
  box-shadow: 0 0.5rem 1.2rem rgba(30, 64, 175, 0.15) !important;
}

/* 🧊 Card Interaction */
.card-hover {
  transition: all 0.3s ease;
}
.card-hover:hover {
  transform: translateY(-6px);
  box-shadow: 0 0.75rem 1.5rem rgba(0, 0, 0, 0.08);
}

/* 📱 Mobile Responsiveness */
@media (max-width: 768px) {
  h1, .display-4, .display-6 {
    font-size: 1.5rem !important;
    line-height: 1.3;
  }
  .btn-lg {
    font-size: 1rem !important;
    padding: 0.5rem 1rem;
  }
  .navbar-brand span {
    font-size: 1rem !important;
  }
  .navbar .btn {
    padding: 0.3rem 0.7rem !important;
    font-size: 0.9rem;
  }
  .container {
    padding-left: 1rem !important;
    padding-right: 1rem !important;
  }
  video {
    max-width: 100%;
    height: auto;
    border-radius: 0.75rem;
  }
}
</style>
