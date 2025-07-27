<template>
  <div class="absolute top-20 left-0 right-0 z-20 flex flex-col items-center space-y-2 pointer-events-none">
    <transition-group name="float-comment" tag="div">
      <div
        v-for="(comment, index) in comments"
        :key="comment.id"
        class="bg-black/70 text-white px-4 py-2 rounded-full shadow text-sm animate-float"
      >
        💬 {{ comment.text }}
      </div>
    </transition-group>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { nanoid } from 'nanoid'

const comments = ref([])

function addFloatingComment(text) {
  const id = nanoid()
  comments.value.push({ id, text })

  setTimeout(() => {
    comments.value = comments.value.filter(c => c.id !== id)
  }, 4000)
}

// 👇 Expose to parent if needed
defineExpose({
  addFloatingComment
})
</script>

<style scoped>
.float-comment-enter-active,
.float-comment-leave-active {
  transition: all 0.8s ease;
}
.float-comment-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.float-comment-enter-to {
  opacity: 1;
  transform: translateY(0);
}
.float-comment-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
</style>
