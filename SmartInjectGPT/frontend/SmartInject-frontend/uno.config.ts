// uno.config.ts
import { defineConfig, presetUno, presetAttributify, presetIcons } from 'unocss'

export default defineConfig({
  shortcuts: [
    ['btn', 'px-4 py-2 rounded-md font-semibold text-white bg-yellow-400 hover:bg-yellow-500 transition duration-200'],
    ['btn-outline', 'px-4 py-2 rounded-md border border-yellow-400 text-yellow-400 hover:bg-yellow-500 hover:text-black transition duration-200'],
    ['card', 'bg-dark-800 text-light p-5 rounded-xl shadow-lg'],
    ['input', 'px-3 py-2 rounded-md border border-gray-400 bg-dark-700 text-light placeholder-gray-400'],
    ['section-title', 'text-2xl font-bold text-yellow-400 mb-4'],
    ['flex-center', 'flex items-center justify-center'],
  ],
  theme: {
    colors: {
      dark: {
        DEFAULT: '#0a0a1a',
        700: '#1e293b',
        800: '#0f172a',
        900: '#020617',
      },
      light: '#f3f4f6',
      yellow: {
        400: '#facc15',
        500: '#fde047',
      },
      teal: {
        400: '#2dd4bf',
        500: '#14b8a6',
      },
      gray: {
        300: '#d1d5db',
        400: '#9ca3af',
      }
    },
  },
  presets: [
    presetUno(),
    presetAttributify(),
    presetIcons()
  ],
})
