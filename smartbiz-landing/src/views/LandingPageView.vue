<template>
  <div class="min-vh-100 bg-white text-dark dark:bg-dark dark:text-white">
    <!-- 🌐 Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm py-2 px-3">
      <div class="container-fluid justify-content-between">
        <!-- 📛 Logo + Brand -->
        <router-link to="/" class="navbar-brand d-flex align-items-center gap-2">
          <img
            src="@/assets/logo-circle.png"
            alt="SmartBiz Logo"
            class="rounded-circle shadow-sm"
            style="width: 34px; height: 34px; object-fit: cover; background: #fff; border: 2px solid #FFD700;"
          />
          <span class="fw-bold fs-5 d-none d-md-inline" style="letter-spacing: -0.5px;">SmartBiz</span>
        </router-link>

        <!-- ☀️🌙 Theme & Auth -->
        <div class="d-flex align-items-center gap-2">
          <button @click="toggleTheme" class="btn btn-sm btn-light">
            {{ isDark ? '☀️ Light' : '🌙 Dark' }}
          </button>
          <router-link to="/login" class="btn btn-sm btn-outline-light fw-semibold">
            Login
          </router-link>
          <router-link to="/signup" class="btn btn-sm btn-warning fw-bold text-primary">
            Sign Up
          </router-link>
        </div>
      </div>
    </nav>

    <!-- 🎯 Hero Section -->
    <section class="bg-gradient-to-r from-primary to-info text-white py-5 text-center px-3">
      <div class="container">
        <img
          src="@/assets/logo-circle.png"
          alt="SmartBiz Logo"
          class="mx-auto mb-4"
          style="width: 90px; height: 90px; background: #fff; border-radius: 50%; border: 3px solid #FFD700;"
        />
        <h1 class="display-6 fw-bold mb-3">Automate Messaging Across All Platforms</h1>
        <p class="lead mb-4">Connect WhatsApp, Telegram, SMS, and Email in one powerful dashboard.</p>
        <div class="d-flex flex-column flex-md-row justify-content-center gap-3">
          <router-link to="/signup" class="btn btn-warning btn-lg fw-bold text-primary">
            Get Started Free (1 Month)
          </router-link>
          <button class="btn btn-outline-light btn-lg" @click="scrollToDemo">Watch Demo</button>
        </div>
      </div>
    </section>

    <!-- 🎥 Demo Video -->
    <section class="py-5 bg-light dark:bg-dark px-3">
      <div class="container text-center">
        <h2 class="fs-4 fw-bold mb-3">See How It Works</h2>
        <video
          class="w-100 rounded shadow mb-3"
          controls
          src="https://www.w3schools.com/html/mov_bbb.mp4"
        ></video>
        <p class="text-secondary">A quick tour on how SmartBiz automates your messaging workflow in real time.</p>
      </div>
    </section>

    <!-- 🛠️ Features -->
    <section id="features" class="py-5 bg-white dark:bg-dark">
      <div class="container">
        <h2 class="fs-4 fw-bold text-center mb-4 text-primary dark:text-warning">Platform Features</h2>
        <div class="row g-4">
          <div v-for="feature in features" :key="feature.id" class="col-12 col-md-6 col-lg-4">
            <div class="card h-100 border-0 shadow-sm">
              <div class="card-body text-center">
                <div class="fs-1 mb-3 text-warning">{{ feature.icon }}</div>
                <h5 class="card-title fw-bold mb-2">{{ feature.title }}</h5>
                <p class="card-text">{{ feature.desc }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 🌟 Testimonials -->
    <section class="py-5 bg-light dark:bg-secondary text-center px-3">
      <div class="container">
        <h2 class="fs-4 fw-bold mb-4 text-primary dark:text-warning">What Our Users Say</h2>
        <div class="card border-0 shadow-lg mx-auto" style="max-width: 480px;">
          <div class="card-body">
            <p class="fs-5 fst-italic mb-2">“SmartBiz helped me automate WhatsApp replies while I sleep. I’ve tripled my customer response rate!”</p>
            <p class="fw-bold mb-0">— Asha, Business Owner</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 🔻 Footer slot -->
    <slot />
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'

// 🌟 Feature List
const features = ref([
  { id: 1, icon: "📱", title: "WhatsApp Automation", desc: "Auto-reply and broadcast to clients on WhatsApp." },
  { id: 2, icon: "🤖", title: "Telegram Bots", desc: "Engage users with customizable Telegram bots." },
  { id: 3, icon: "✉️", title: "SMS Campaigns", desc: "Send bulk promotions and OTPs via SMS." },
  { id: 4, icon: "📧", title: "Email Sequences", desc: "Automate marketing emails with rich templates." },
  { id: 5, icon: "📊", title: "Unified Analytics", desc: "Get insights across all messaging channels." },
  { id: 6, icon: "🔌", title: "API & Webhooks", desc: "Easily connect with your CRM or ERP." }
])

// 🌗 Dark Mode State
const isDark = ref(false)

onMounted(() => {
  isDark.value = document.documentElement.classList.contains("dark")
})

// 🌗 Toggle Theme
function toggleTheme() {
  isDark.value = !isDark.value
  document.documentElement.classList.toggle("dark", isDark.value)
}

// 🎬 Scroll to Demo Video
function scrollToDemo() {
  const videoSection = document.querySelector("video")
  if (videoSection) {
    videoSection.scrollIntoView({ behavior: "smooth" })
  }
}
</script>
<style scoped>
/* ✨ Fade In Animation */
.animate-fade-in {
  animation: fadeIn 1s ease-in-out both;
}
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(12px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 🎨 Brand Colors */
.bg-primary {
  background-color: #1E40AF !important;
}
.bg-info {
  background-color: #0B89B1 !important;
}
.text-primary {
  color: #1E40AF !important;
}
.text-warning {
  color: #FF9E0B !important;
}

/* 🌗 Dark Mode Enhancements */
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

/* 🧊 Utility Enhancements */
.hover-shadow-sm:hover {
  box-shadow: 0 0.5rem 1rem rgba(30, 64, 175, 0.15) !important;
}
.transition {
  transition: all 0.3s ease-in-out;
}
.btn-glow {
  transition: box-shadow 0.3s ease-in-out;
}
.btn-glow:hover {
  box-shadow: 0 0 12px rgba(255, 214, 0, 0.6);
}

/* 📱 Responsive Enhancements */
@media (max-width: 768px) {
  h1, .display-4 {
    font-size: 1.75rem;
  }
  .btn-lg {
    font-size: 1rem;
    padding: 0.75rem 1.25rem;
  }
  .navbar-brand span {
    font-size: 1.1rem;
  }
}

/* 🧊 Elegant Card Hover */
.card-hover:hover {
  transform: translateY(-6px);
  box-shadow: 0 0.75rem 1.5rem rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

/* 👇 Smooth Slide Effect */
.fade-slide {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeSlideIn 0.8s ease forwards;
}
@keyframes fadeSlideIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
