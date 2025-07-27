<template>
  <div class="space-y-2">
    <label :for="name" class="block text-sm font-medium text-gray-700 dark:text-gray-200">
      {{ label }}
    </label>
    <textarea
      ref="textareaRef"
      :id="name"
      :name="name"
      v-model="inputValue"
      :rows="minRows"
      :placeholder="placeholder"
      :class="[
        'w-full px-4 py-2 border rounded-md resize-none focus:outline-none text-sm shadow-sm transition',
        error ? 'border-red-500 bg-red-50 text-red-800' : 'border-gray-300 bg-white text-black dark:bg-[#1e293b] dark:text-white'
      ]"
      @input="autoResize"
    ></textarea>
    <p v-if="error" class="text-xs text-red-600">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, nextTick } from 'vue'

const props = defineProps({
  modelValue: String,
  name: String,
  label: String,
  placeholder: String,
  error: String,
  minRows: {
    type: Number,
    default: 3
  },
  maxHeight: {
    type: String,
    default: '300px'
  }
})

const emit = defineEmits(['update:modelValue'])
const textareaRef = ref(null)
const inputValue = ref(props.modelValue)

watch(() => props.modelValue, val => {
  inputValue.value = val
  nextTick(autoResize)
})

watch(inputValue, val => emit('update:modelValue', val))

function autoResize() {
  const el = textareaRef.value
  if (!el) return
  el.style.height = 'auto'
  el.style.height = Math.min(el.scrollHeight, parseInt(props.maxHeight)) + 'px'
}

onMounted(() => {
  nextTick(autoResize)
})
</script>

<style scoped>
textarea {
  line-height: 1.4;
  max-height: 300px;
  overflow-y: auto;
}
</style>
