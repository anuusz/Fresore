// src/composables/useLoginModal.js
import { ref } from 'vue'

console.log('useLoginModal.js loaded') // Debug

const showLoginModal = ref(false)
const pendingAction = ref(null)

export const useLoginModal = () => {
  console.log('useLoginModal function called') // Debug

  const openLoginModal = (callback = null) => {
    console.log('openLoginModal called with callback:', typeof callback) // Debug
    showLoginModal.value = true
    pendingAction.value = callback

    // Prevent body scroll
    document.body.style.overflow = 'hidden'
    document.body.style.height = '100vh'
  }

  const closeLoginModal = () => {
    console.log('closeLoginModal called') // Debug
    showLoginModal.value = false
    pendingAction.value = null

    // Restore body scroll
    document.body.style.overflow = 'auto'
    document.body.style.height = 'auto'
  }

  const executePendingAction = () => {
    console.log('executePendingAction called, pending:', typeof pendingAction.value) // Debug
    if (pendingAction.value && typeof pendingAction.value === 'function') {
      pendingAction.value()
    }
    pendingAction.value = null
  }

  console.log('Returning functions:', {
    showLoginModal: showLoginModal.value,
    openLoginModal: typeof openLoginModal,
    closeLoginModal: typeof closeLoginModal,
  }) // Debug

  return {
    showLoginModal,
    pendingAction,
    openLoginModal,
    closeLoginModal,
    executePendingAction,
  }
}
