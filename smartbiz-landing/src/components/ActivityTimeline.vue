<template>
  <div class="bg-[#0f172a] p-6 rounded-xl border border-cyan-700">
    <h2 class="text-xl font-bold text-cyan-200 mb-4">🔄 Recent Activity Timeline</h2>

    <ul class="timeline space-y-4">
      <li
        v-for="(activity, index) in timeline"
        :key="index"
        class="timeline-item"
      >
        <div class="timeline-marker"></div>
        <div class="timeline-content">
          <p class="text-sm text-gray-200">
            <span class="text-cyan-400 font-medium">{{ activity.user }}</span>
            {{ activity.action }}
            <span class="font-semibold text-white">{{ activity.target }}</span>
          </p>
          <p class="text-xs text-gray-400 mt-1">{{ activity.timeAgo }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
const timeline = [
  {
    user: 'Julius Zakayo',
    action: 'liked',
    target: '"Business Growth Tips" post',
    timeAgo: 'Just now'
  },
  {
    user: 'Julius Zakayo',
    action: 'followed',
    target: '@linda_ai',
    timeAgo: '3h ago'
  },
  {
    user: 'Julius Zakayo',
    action: 'received gift',
    target: '"Galaxy Orbit" 🎁',
    timeAgo: '1d ago'
  },
  {
    user: 'Julius Zakayo',
    action: 'commented on',
    target: 'AI Discussion video',
    timeAgo: '2d ago'
  }
]
</script>

<style scoped>
.timeline-item {
  @apply flex items-start gap-4;
}

.timeline-marker {
  @apply w-3 h-3 mt-1 rounded-full bg-cyan-400 shadow-lg;
  flex-shrink: 0;
}

.timeline-content {
  @apply flex-1;
  border-left: 2px solid #334155;
  padding-left: 0.75rem;
}
</style>
