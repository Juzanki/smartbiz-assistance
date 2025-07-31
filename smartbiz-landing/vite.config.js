import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import UnoCSS from 'unocss/vite'
import path from 'node:path'

export default defineConfig(({ mode }) => {
  // Load .env files
  const env = loadEnv(mode, process.cwd(), '')

  return {
    plugins: [
      vue(),
      UnoCSS(),
    ],
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'),
      },
    },
    define: {
      // Inject VITE_ variables as global constants
      __APP_ENV__: env.VITE_ENVIRONMENT,
      __APP_NAME__: JSON.stringify(env.VITE_APP_NAME || 'SmartBiz Assistance'),
      __API_URL__: JSON.stringify(env.VITE_API_URL),
    },
    server: {
      host: '0.0.0.0',
      port: 5173,
      hmr: {
        overlay: false,
      },
      strictPort: true,
      cors: {
        origin: [
          env.RAILWAY_PUBLIC_URL || '',
          env.NETLIFY_PUBLIC_URL || '',
        ],
        credentials: true,
      },
    },
    preview: {
      port: 4173,
      strictPort: true,
    },
  }
})
