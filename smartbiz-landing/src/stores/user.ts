import { defineStore } from 'pinia'

// Define the structure of user data
interface UserData {
  username: string
  profile_image: string
  is_verified: boolean
}

export const useUserStore = defineStore('user', {
  state: () => ({
    username: '',
    profileImage: '',
    is_verified: false
  }),

  getters: {
    displayName: (state) => state.username || 'Host',
    avatar: (state) => state.profileImage || '/avatars/default.png',
    isVerified: (state) => state.is_verified === true
  },

  actions: {
    setUser(data: UserData) {
      this.username = data.username
      this.profileImage = data.profile_image
      this.is_verified = data.is_verified
      // Save to localStorage
      localStorage.setItem('user', JSON.stringify(data))
    },

    loadUser() {
      const saved = localStorage.getItem('user')
      if (saved) {
        const data = JSON.parse(saved)
        this.username = data.username
        this.profileImage = data.profile_image
        this.is_verified = data.is_verified
      }
    },

    clearUser() {
      this.username = ''
      this.profileImage = ''
      this.is_verified = false
      localStorage.removeItem('user')
    }
  }
})
