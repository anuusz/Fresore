// src/composables/useAuth.js

import { ref, computed } from 'vue'
import api from '@/axios'

const user = ref(null)
const token = ref(null)

export const useAuth = () => {
  const isAuthenticated = computed(() => !!token.value && !!user.value)

  const login = async (email, password) => {
    try {
      const response = await api.post('/api/auth/login/', {
        username: email,
        password: password,
      })
      token.value = response.data.access
      // Ambil profile user
      const profileRes = await api.get('/api/shop/profile/', {
        headers: { Authorization: `Bearer ${token.value}` },
      })
      user.value = profileRes.data
      return true
    } catch (error) {
      console.error('Login error:', error)
      return false
    }
  }

  const logout = () => {
    user.value = null
    token.value = null
  }

  const checkAuth = async () => {
    if (!token.value) return false
    try {
      const profileRes = await api.get('/api/shop/profile/', {
        headers: { Authorization: `Bearer ${token.value}` },
      })
      user.value = profileRes.data
      return true
    } catch (error) {
      user.value = null
      token.value = null
      return false
    }
  }

  return {
    user: computed(() => user.value),
    token: computed(() => token.value),
    isAuthenticated,
    login,
    logout,
    checkAuth,
  }
}
