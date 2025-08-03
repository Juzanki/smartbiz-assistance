<template>
  <nav class="bg-blue-800 text-white p-4 flex items-center justify-between shadow-md">
    <!-- 🔰 Logo & App Name -->
    <div class="flex items-center space-x-2">
      <span class="text-xl font-bold tracking-wide">SmartBiz</span>
    </div>

    <!-- 🧭 Navigation Links -->
    <div class="flex items-center space-x-4">
      <a href="#features" class="hover:text-yellow-400 transition">Features</a>
      <a href="#pricing" class="hover:text-yellow-400 transition">Pricing</a>
      <a href="#contact" class="hover:text-yellow-400 transition">Contact</a>

      <!-- 👤 Auth Buttons -->
      <router-link to="/login" class="px-4 py-1 border border-white rounded hover:bg-white hover:text-blue-800 transition">
        Login
      </router-link>
      <router-link to="/signup" class="bg-yellow-400 text-black font-bold px-4 py-1 rounded hover:bg-yellow-300 transition">
        Sign Up
      </router-link>
    </div>
  </nav>
</template>

<script setup>
// No logic needed for static navbar
</script>

<style scoped>
/* Hakuna extra CSS inahitajika hapa */
</style>
