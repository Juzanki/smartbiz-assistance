// src/services/api.js
import axios from 'axios'

const api = axios.create({
  baseURL: '/api', // Proxy to http://127.0.0.1:8010 from vite.config.js
  timeout: 10000,  // Add timeout to avoid hanging requests
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json'
  },
  withCredentials: true
})

// Optional: Response logging and error catching globally
api.interceptors.response.use(
  response => response,
  error => {
    console.error('[API Error]', error.response?.data || error.message)
    return Promise.reject(error)
  }
)

export default api
