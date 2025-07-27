<template>
  <div class="min-h-screen bg-gray-100 dark:bg-[#0c1a2e] p-6 text-gray-900 dark:text-white">
    <h1 class="text-3xl font-bold mb-6 text-blue-600 dark:text-yellow-400">
      🧠 SmartInjectGPT Control Panel
    </h1>

    <div class="space-y-8">
      <!-- 🔁 Prompt Input -->
      <section>
        <FrontendPromptInjector />
      </section>

      <!-- 🔊 Kernel Voice Feedback -->
      <section>
        <AIVoiceOverlay />
      </section>

      <!-- 📡 Live Tracking & Analysis -->
      <section class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        <LivePromptTracker />
        <AutoDeployConsole />
        <KernelMonitor />
        <AutoFeedback />
        <PromptHistory />
        <GenerationPreview />
        <DreamTrigger />
        <AIChatBot />
      </section>
    </div>
  </div>
</template>

<script setup>
import FrontendPromptInjector from './FrontendPromptInjector.vue'
import AIVoiceOverlay from './AIVoiceOverlay.vue'
import LivePromptTracker from './LivePromptTracker.vue'
import AutoDeployConsole from './AutoDeployConsole.vue'
import KernelMonitor from './KernelMonitor.vue'
import PromptHistory from './PromptHistory.vue'
import GenerationPreview from './GenerationPreview.vue'
import DreamTrigger from './DreamTrigger.vue'
import AutoFeedback from './AutoFeedback.vue'
import AIChatBot from './AIChatBot.vue'
</script>
