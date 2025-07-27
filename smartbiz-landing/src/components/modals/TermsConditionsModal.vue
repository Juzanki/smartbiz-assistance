<template>
  <div class="fixed inset-0 flex items-center justify-center bg-black/60 backdrop-blur-sm z-50">
    <div class="bg-white rounded-xl shadow-2xl p-6 max-w-2xl w-full animate-fade-in">
      <h2 class="text-xl font-bold text-gray-800 flex items-center gap-2 mb-4">
        📜 Live Stream Terms & Conditions
      </h2>

      <div class="overflow-y-auto max-h-[60vh] space-y-4 mb-4 text-sm text-gray-700">
        <p>By proceeding to stream live, you agree to adhere to the following:</p>

        <ul class="list-disc pl-5 space-y-2">
          <li><strong>Respect & Safety:</strong> No harassment, hate speech, bullying, or inappropriate language.</li>
          <li><strong>No Nudity or Inappropriate Content:</strong> Strictly prohibited; violations will lead to suspension.</li>
          <li><strong>No Illegal Activities:</strong> Do not show or promote illegal or harmful actions.</li>
          <li><strong>Privacy & Consent:</strong> Ensure consent before featuring anyone in your stream.</li>
          <li><strong>Commercial Conduct:</strong> Honest and transparent business practices are required.</li>
          <li><strong>Moderation Policy:</strong> Your stream may be monitored, paused, or stopped if rules are violated.</li>
        </ul>

        <p class="mt-4">Read our full <a href="#" class="text-indigo-500 underline">Community Guidelines</a> and <a href="#" class="text-indigo-500 underline">Privacy Policy</a>.</p>
      </div>

      <div class="flex items-center gap-3 justify-end">
        <button
          @click="$emit('decline')"
          class="px-4 py-2 text-sm font-semibold text-red-600 hover:text-red-700"
        >Decline</button>
        <button
          @click="$emit('accept')"
          class="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-2 rounded-lg shadow-md font-semibold"
        >
          Accept & Go Live
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineEmits(['accept', 'decline'])
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.4s ease-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
