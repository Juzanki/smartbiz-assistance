// src/services/api.js
import axios from 'axios'

const api = axios.create({
  baseURL: '/api', // it goes through Vite proxy
  withCredentials: true
})

export default api
