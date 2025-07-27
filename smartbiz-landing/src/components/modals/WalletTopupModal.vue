<template>
  <div class="fixed inset-0 bg-black/50 backdrop-blur flex justify-center items-center z-50">
    <div class="bg-white text-black p-6 rounded-xl w-[90vw] max-w-md shadow-lg">
      <h2 class="text-lg font-bold mb-4">💰 Wallet Topup</h2>
      <p>Enter amount and method</p>
      <button class="mt-4 px-4 py-2 bg-red-600 text-white rounded" @click="$emit('close')">Close</button>
    </div>
  </div>
</template>

<script setup>
</script>
