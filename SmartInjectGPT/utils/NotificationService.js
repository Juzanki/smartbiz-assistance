// src/utils/NotificationService.js
import { useToast } from 'vue-toastification'

const toast = useToast()

export const notify = {
  success(message, options = {}) {
    toast.success(message, {
      timeout: 3000,
      position: 'top-right',
      ...options
    })
  },

  error(message, options = {}) {
    toast.error(message, {
      timeout: 4000,
      position: 'top-right',
      ...options
    })
  },

  info(message, options = {}) {
    toast.info(message, {
      timeout: 3000,
      position: 'top-right',
      ...options
    })
  },

  warning(message, options = {}) {
    toast.warning(message, {
      timeout: 3500,
      position: 'top-right',
      ...options
    })
  }
}

export default notify
