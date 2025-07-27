<template>
  <div class="absolute inset-0 z-0 pointer-events-none">
    <div class="absolute w-full h-full bg-gradient-to-br from-purple-800/30 via-transparent to-pink-700/30 animate-pulse"></div>
    <div class="absolute w-1/2 h-1/2 bg-indigo-600/20 rounded-full blur-2xl top-1/4 left-1/4 animate-fade"></div>
    <div class="absolute w-1/3 h-1/3 bg-pink-500/20 rounded-full blur-2xl top-1/2 left-2/3 animate-fade delay-1000"></div>
  </div>
</template>

<style scoped>
@keyframes fade {
  0%, 100% { opacity: 0.4; }
  50% { opacity: 0.9; }
}
.animate-fade {
  animation: fade 4s ease-in-out infinite;
}
</style>
