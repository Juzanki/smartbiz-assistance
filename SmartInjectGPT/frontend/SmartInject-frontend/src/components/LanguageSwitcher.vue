<!-- src/components/LanguageSwitcher.vue -->
<template>
  <select v-model="lang" @change="switchLang" class="px-2 py-1 border rounded text-sm bg-dark-600 text-white">
    <option value="en">🇬🇧 English</option>
    <option value="sw">🇰🇪 Swahili</option>
    <option value="fr">🇫🇷 French</option>
    <option value="tr">🇹🇷 Turkish</option>
  </select>
</template>

<script setup>
import { ref } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const lang = ref(locale.value)

const switchLang = () => {
  locale.value = lang.value
  localStorage.setItem('lang', lang.value)
}
</script>
