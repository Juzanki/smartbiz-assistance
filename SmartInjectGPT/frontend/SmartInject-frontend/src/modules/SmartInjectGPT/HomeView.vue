<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-800 text-white px-6 py-4 relative">

    <!-- LOGO TOP-LEFT -->
    <div class="absolute top-4 left-4">
      <img
        src="@/assets/logo.png"
        alt="SmartInjectGPT Logo"
        class="w-12 h-12 rounded-full border border-yellow-400 shadow bg-white object-contain"
      />
    </div>

    <!-- CENTERED CONTENT -->
    <div class="flex flex-col items-center justify-center text-center min-h-[calc(100vh-80px)]">
      <h1 class="text-4xl font-extrabold text-yellow-400 drop-shadow-lg tracking-wide">
        Welcome to SmartInjectGPT
      </h1>

      <p class="text-gray-300 mt-3 text-lg max-w-md leading-relaxed">
        Build, Train, and Deploy <span class="text-teal-400 font-medium">Enterprise AI Tools</span>
        with confidence and speed.
      </p>

      <footer class="text-xs text-gray-500 mt-6">
        © 2025 SmartInjectGPT — All rights reserved.
      </footer>
    </div>
  </div>
</template>

<script setup>
// Optional enhancements here
</script>
