// 📁 src/utils/axiosInstance.js
import axios from 'axios'
import router from '@/router'

// ✅ Use only environment variable for backend URL (no localhost fallback)
const API_BASE = import.meta.env.VITE_API_BASE

// 🌐 Create Axios instance with defaults
const axiosInstance = axios.create({
  baseURL: API_BASE,
  timeout: 15000, // ⏱️ 15s timeout
  headers: {
    Accept: 'application/json',
  },
})

// 🔐 Attach token to every request if available
axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// 🚨 Handle global response errors
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      // ⛔ Token expired or unauthorized
      localStorage.removeItem('access_token')
      localStorage.removeItem('user_role')
      localStorage.removeItem('user_name')
      localStorage.removeItem('user_lang')

      // 🔁 Redirect to login page
      router.push('/login')
    }

    // ⚠️ Optionally: Handle other errors like 403, 500, etc.
    return Promise.reject(error)
  }
)

export default axiosInstance
