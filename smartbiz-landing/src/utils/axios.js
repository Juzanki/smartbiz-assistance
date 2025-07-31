// src/utils/axios.js
import axios from 'axios'

const baseURL = import.meta.env.VITE_API_BASE_URL

if (!baseURL) {
  throw new Error("❌ VITE_API_BASE_URL haijatajwa kwenye environment. Tafadhali iweke kwenye .env au Netlify Environment Variables.")
}

const instance = axios.create({
  baseURL: baseURL, // Hakikisha imetoka kwenye env
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
})

export default instance
