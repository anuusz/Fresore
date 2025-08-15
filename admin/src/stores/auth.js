import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  // State
  const user = ref(null)
  const token = ref(localStorage.getItem('auth_token') || null)
  const isLoading = ref(false)

  // Getters
  const isAuthenticated = computed(() => !!token.value && !!user.value)
  const isGuest = computed(() => !isAuthenticated.value)

  // Actions
  const login = async (credentials) => {
    isLoading.value = true
    try {
      // Simulate API call - ganti dengan API endpoint Anda
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials),
      })

      if (!response.ok) {
        throw new Error('Login failed')
      }

      const data = await response.json()

      // Set user and token
      user.value = data.user
      token.value = data.token

      // Save to localStorage
      localStorage.setItem('auth_token', data.token)
      localStorage.setItem('user_data', JSON.stringify(data.user))

      return { success: true, user: data.user }
    } catch (error) {
      console.error('Login error:', error)
      return { success: false, error: error.message }
    } finally {
      isLoading.value = false
    }
  }

  const logout = () => {
    user.value = null
    token.value = null
    localStorage.removeItem('auth_token')
    localStorage.removeItem('user_data')
  }

  const initAuth = () => {
    const savedToken = localStorage.getItem('auth_token')
    const savedUser = localStorage.getItem('user_data')

    if (savedToken && savedUser) {
      token.value = savedToken
      user.value = JSON.parse(savedUser)
    }
  }

  const checkTokenValidity = async () => {
    if (!token.value) return false

    try {
      const response = await fetch('/api/verify-token', {
        headers: {
          'Authorization': `Bearer ${token.value}`
        }
      })

      if (!response.ok) {
        logout()
        return false
      }

      return true
    } catch (error) {
      logout()
      return false
    }
  }

  return {
    user,
    token,
    isLoading,
    isAuthenticated,
    isGuest,
    login,
    logout,
    initAuth,
    checkTokenValidity
  }
})
