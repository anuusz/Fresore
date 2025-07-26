<!-- src/components/LoginModal.vue -->
<template>
  <!-- Modal Overlay -->
  <Transition name="modal">
    <div v-if="showLoginModal" class="modal-overlay" @click="handleCloseModal">
      <!-- Animated Background Particles -->
      <div class="background-particles">
        <div
          v-for="(particle, index) in particles"
          :key="index"
          class="particle"
          :style="particle.style"
        >
          {{ particle.emoji }}
        </div>
      </div>

      <div class="modal-container" @click.stop>
        <!-- Close Button -->
        <button class="close-btn" @click="handleCloseModal">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>

        <!-- Header Section with Glassmorphism -->
        <div class="modal-header">
          <div class="header-bg"></div>
          <div class="header-content">
            <div class="cart-icon-container">
              <div class="cart-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="8" cy="21" r="1"></circle>
                  <circle cx="19" cy="21" r="1"></circle>
                  <path
                    d="m2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"
                  ></path>
                </svg>
              </div>
              <div class="pulse-ring"></div>
              <div class="pulse-ring-2"></div>
            </div>
            <h2 class="modal-title">Welcome Back!</h2>
            <p class="modal-subtitle">Continue your fresh shopping journey 🌿</p>
          </div>
        </div>

        <!-- Content Area -->
        <div class="modal-content">
          <!-- Login Options -->
          <div class="login-options">
            <!-- Existing User Card -->
            <div class="option-card primary-card" @click="goToLogin">
              <div class="card-bg"></div>
              <div class="card-content">
                <div class="card-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
                    <polyline points="10,17 15,12 10,7"></polyline>
                    <line x1="15" y1="12" x2="3" y2="12"></line>
                  </svg>
                </div>
                <div class="card-text">
                  <h3>I Have Account</h3>
                  <p>Sign in to continue</p>
                </div>
                <div class="card-arrow">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="9,18 15,12 9,6"></polyline>
                  </svg>
                </div>
              </div>
            </div>

            <!-- New User Card -->
            <div class="option-card secondary-card" @click="goToRegister">
              <div class="card-bg"></div>
              <div class="card-content">
                <div class="card-icon">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                    <circle cx="9" cy="7" r="4"></circle>
                    <line x1="19" y1="8" x2="19" y2="14"></line>
                    <line x1="22" y1="11" x2="16" y2="11"></line>
                  </svg>
                </div>
                <div class="card-text">
                  <h3>New Here?</h3>
                  <p>Create free account</p>
                </div>
                <div class="card-arrow">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="9,18 15,12 9,6"></polyline>
                  </svg>
                </div>
              </div>
            </div>

            <!-- Guest Option -->
            <div class="guest-section">
              <button @click="continueAsGuest" class="guest-btn">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                  <circle cx="9" cy="7" r="4"></circle>
                  <path d="m22 9-10.5 3L7 12"></path>
                </svg>
                Continue as Guest
                <span class="guest-note">Limited features</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script>
import { ref, watch, onMounted, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '@/composables/useAuth.js'

export default {
  name: 'LoginModal',
  setup() {
    const router = useRouter()
    const { login } = useAuth()

    const particles = ref([])
    const isLoggingIn = ref(false)
    const showLoginModal = ref(false)
    const showOptions = ref(true) // Toggle between options and login form
    const showPassword = ref(false)

    const loginData = reactive({
      email: '',
      password: '',
      rememberMe: false,
    })

    const vegetables = ['🥬', '🥕', '🍅', '🥒', '🌽', '🥦', '🍆', '🥔', '🧅', '🥑']
    const fruits = ['🍎', '🍊', '🍌', '🍇', '🍓', '🥝', '🍑', '🍒']
    const allItems = [...vegetables, ...fruits]

    const createParticles = () => {
      particles.value = []
      for (let i = 0; i < 12; i++) {
        particles.value.push({
          emoji: allItems[Math.floor(Math.random() * allItems.length)],
          style: {
            left: Math.random() * 100 + '%',
            top: Math.random() * 100 + '%',
            animationDelay: Math.random() * 10 + 's',
            animationDuration: Math.random() * 10 + 15 + 's',
            fontSize: Math.random() * 20 + 20 + 'px',
            opacity: Math.random() * 0.7 + 0.3,
          },
        })
      }
    }

    const handleCloseModal = () => {
      console.log('Closing modal')
      showLoginModal.value = false
      showOptions.value = true // Reset to options view
      document.body.style.overflow = 'auto'
      document.body.style.height = 'auto'

      // Clear form
      loginData.email = ''
      loginData.password = ''
      loginData.rememberMe = false
    }

    const goToLogin = () => {
      localStorage.setItem('redirectAfterLogin', router.currentRoute.value.fullPath)
      router.push('/login')
      handleCloseModal()
    }

    const backToOptions = () => {
      showOptions.value = true
      // Clear form when going back
      loginData.email = ''
      loginData.password = ''
    }

    const goToRegister = () => {
      localStorage.setItem('redirectAfterLogin', router.currentRoute.value.fullPath)
      router.push('/register')
      handleCloseModal()
    }

    const continueAsGuest = () => {
      console.log('Continue as guest')
      handleCloseModal()

      const notification = document.createElement('div')
      notification.innerHTML = '👤 Continuing as guest. Cart will be temporary.'
      notification.className = 'info-notification'
      notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3);
        z-index: 100001;
        font-weight: 600;
        animation: slideInRight 0.5s ease;
      `
      document.body.appendChild(notification)

      setTimeout(() => {
        if (document.body.contains(notification)) {
          document.body.removeChild(notification)
        }
      }, 3000)
    }

    const handleLogin = async () => {
      // Basic validation
      if (!loginData.email || !loginData.password) {
        alert('Mohon isi email dan password!')
        return
      }

      isLoggingIn.value = true

      try {
        console.log('Starting login...')

        // Simulate API call
        await new Promise((resolve) => setTimeout(resolve, 1500))

        // Mock login validation - ganti dengan API call yang real
        if (loginData.email === 'test@email.com' && loginData.password === 'password') {
          // Mock successful login
          const userData = {
            id: Date.now(),
            name: 'Ahmad Wijaya',
            email: loginData.email,
            totalOrders: 15,
            favoriteProducts: 8,
            points: 2450,
          }

          const authToken =
            'jwt-token-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9)

          // Use useAuth login
          login(userData, authToken)

          console.log('Login successful:', userData)

          // Show success notification
          const notification = document.createElement('div')
          notification.innerHTML = '✅ Login berhasil! Selamat datang kembali!'
          notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #2ed573, #26af5f);
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(46, 213, 115, 0.3);
            z-index: 100001;
            font-weight: 600;
            animation: slideInRight 0.5s ease;
          `
          document.body.appendChild(notification)

          setTimeout(() => {
            if (document.body.contains(notification)) {
              document.body.removeChild(notification)
            }
          }, 3000)

          // Close modal
          handleCloseModal()
        } else {
          // Mock failed login
          alert(
            'Email atau password salah!\n\nUntuk testing, gunakan:\nEmail: test@email.com\nPassword: password',
          )
        }
      } catch (error) {
        console.error('Login failed:', error)
        alert('Login gagal! Silakan coba lagi.')
      } finally {
        isLoggingIn.value = false
      }
    }

    // Global modal control
    window.showLoginModal = () => {
      console.log('Global showLoginModal called')
      showLoginModal.value = true
      document.body.style.overflow = 'hidden'
      document.body.style.height = '100vh'
      createParticles()
    }

    onMounted(() => {
      window.addEventListener('show-login-modal', () => {
        console.log('Global event received: show-login-modal')
        showLoginModal.value = true
        document.body.style.overflow = 'hidden'
        document.body.style.height = '100vh'
        createParticles()
      })

      createParticles()
    })

    watch(
      () => showLoginModal.value,
      (newVal) => {
        if (newVal) {
          createParticles()
        }
      },
    )

    return {
      showLoginModal,
      showOptions,
      showPassword,
      particles,
      loginData,
      isLoggingIn,
      handleCloseModal,
      goToLogin,
      backToOptions,
      goToRegister,
      continueAsGuest,
      handleLogin,
    }
  },
}
</script>

<style scoped>
.modal-overlay {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.9));
  backdrop-filter: blur(10px);
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  z-index: 99999 !important;
  padding: 1rem;
  opacity: 1 !important;
  visibility: visible !important;
}

.background-particles {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none;
}

.particle {
  position: absolute;
  animation: particleFloat 20s ease-in-out infinite;
  pointer-events: none;
  z-index: 1;
}

@keyframes particleFloat {
  0%,
  100% {
    transform: translateY(0px) rotateZ(0deg);
    opacity: 0.3;
  }
  25% {
    transform: translateY(-30px) rotateZ(90deg);
    opacity: 1;
  }
  50% {
    transform: translateY(-15px) rotateZ(180deg);
    opacity: 0.8;
  }
  75% {
    transform: translateY(-25px) rotateZ(270deg);
    opacity: 0.6;
  }
}

.modal-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  width: 100%;
  max-width: 420px;
  max-height: 85vh;
  overflow: hidden;
  position: relative;
  box-shadow:
    0 32px 64px rgba(0, 0, 0, 0.2),
    0 16px 32px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  animation: modalSlideIn 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
  z-index: 100000 !important;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

@keyframes modalSlideIn {
  from {
    transform: translateY(50px) scale(0.9);
    opacity: 0;
  }
  to {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
}

.close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  width: 44px;
  height: 44px;
  border: none;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.close-btn svg {
  width: 20px;
  height: 20px;
  color: #666;
  transition: all 0.3s ease;
}

.close-btn:hover {
  background: rgba(255, 255, 255, 1);
  transform: scale(1.1) rotate(90deg);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
}

.close-btn:hover svg {
  color: #ff6b6b;
}

.modal-header {
  position: relative;
  height: 180px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.header-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #2ed573 0%, #26af5f 100%);
  opacity: 0.95;
}

.header-content {
  position: relative;
  z-index: 5;
  text-align: center;
  color: white;
}

.cart-icon-container {
  position: relative;
  display: inline-block;
  margin-bottom: 1rem;
}

.cart-icon {
  width: 64px;
  height: 64px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border-top: 2px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.test-credentials {
  background: #f8fafc;
  padding: 15px;
  border-radius: 8px;
  font-size: 12px;
  color: #64748b;
  text-align: center;
  margin-top: 15px;
  border: 1px solid #e2e8f0;
}

/* Options View Styles */
.login-options {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
  animation: slideInFromLeft 0.4s ease;
}

@keyframes slideInFromLeft {
  from {
    transform: translateX(-20px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.option-card {
  position: relative;
  cursor: pointer;
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.card-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transition: all 0.4s ease;
}

.primary-card .card-bg {
  background: linear-gradient(135deg, #2ed573 0%, #26af5f 100%);
}

.secondary-card .card-bg {
  background: linear-gradient(135deg, #26af5f 0%, #1e7e34 100%);
}

.card-content {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  padding: 1.5rem;
  color: white;
}

.card-icon {
  width: 48px;
  height: 48px;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.card-icon svg {
  width: 24px;
  height: 24px;
}

.card-text {
  flex: 1;
}

.card-text h3 {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.card-text p {
  font-size: 0.9rem;
  opacity: 0.9;
}

.card-arrow {
  width: 24px;
  height: 24px;
  opacity: 0.7;
  transition: all 0.3s ease;
}

.card-arrow svg {
  width: 100%;
  height: 100%;
}

.option-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.option-card:hover .card-bg {
  transform: scale(1.05);
}

.option-card:hover .card-arrow {
  opacity: 1;
  transform: translateX(4px);
}

.guest-section {
  margin-top: 1rem;
  text-align: center;
}

.guest-btn {
  background: none;
  border: 2px solid #e2e8f0;
  color: #64748b;
  padding: 1rem;
  border-radius: 12px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  width: 100%;
  flex-direction: column;
}

.guest-btn svg {
  width: 20px;
  height: 20px;
}

.guest-note {
  font-size: 0.75rem;
  opacity: 0.7;
  margin-top: 0.25rem;
}

.guest-btn:hover {
  border-color: #cbd5e1;
  background: rgba(248, 250, 252, 0.5);
  transform: translateY(-1px);
}

.modal-enter-active,
.modal-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;
  backdrop-filter: blur(0px);
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  transform: translateY(50px) scale(0.9);
}

/* Success/Info Notifications */
@keyframes slideInRight {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* Responsive */
@media (max-width: 768px) {
  .modal-container {
    margin: 1rem;
    max-width: 380px;
  }

  .modal-content {
    padding: 1.5rem;
  }

  .modal-title {
    font-size: 1.6rem;
  }

  .login-options {
    gap: 0.8rem;
  }

  .card-content {
    padding: 1.2rem;
  }
}

@media (max-width: 480px) {
  .modal-container {
    margin: 0.5rem;
    max-width: 360px;
  }

  .modal-content {
    padding: 1rem;
  }

  .modal-title {
    font-size: 1.4rem;
  }

  .form-input {
    padding: 10px 10px 10px 40px;
    font-size: 13px;
  }

  .input-icon {
    left: 10px;
    width: 14px;
    height: 14px;
  }

  .password-toggle svg {
    width: 14px;
    height: 14px;
  }

  .card-content {
    padding: 1rem;
  }

  .card-text h3 {
    font-size: 1rem;
  }

  .card-text p {
    font-size: 0.8rem;
  }
}

/* animation: iconBounce 2s ease-in-out infinite;
} */

.cart-icon svg {
  width: 28px;
  height: 28px;
  color: white;
}

@keyframes iconBounce {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

.pulse-ring,
.pulse-ring-2 {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: 2px solid rgba(255, 255, 255, 0.6);
  border-radius: 50%;
  animation: pulseRing 2s ease-out infinite;
}

.pulse-ring-2 {
  animation-delay: 1s;
}

@keyframes pulseRing {
  0% {
    width: 64px;
    height: 64px;
    opacity: 1;
  }
  100% {
    width: 120px;
    height: 120px;
    opacity: 0;
  }
}

.modal-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  background: linear-gradient(45deg, #ffffff, #f0f9ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.modal-subtitle {
  font-size: 1rem;
  opacity: 0.9;
  font-weight: 400;
}

.modal-content {
  padding: 1.5rem 2rem 2rem 2rem;
}

/* Login Form Styles */
.login-form-container {
  animation: slideInFromRight 0.4s ease;
  min-height: 300px;
}

.login-form-header {
  text-align: center;
  margin-bottom: 25px;
}

.login-form-header h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 5px;
}

.login-form-header p {
  color: #64748b;
  font-size: 0.9rem;
}

@keyframes slideInFromRight {
  from {
    transform: translateX(20px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

.back-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background: none;
  border: none;
  color: #64748b;
  cursor: pointer;
  padding: 8px 0;
  margin-bottom: 20px;
  font-size: 14px;
  transition: color 0.3s ease;
}

.back-btn:hover {
  color: #2ed573;
}

.back-btn svg {
  width: 16px;
  height: 16px;
}

.quick-form {
  space-y: 1rem;
}

.input-group {
  margin-bottom: 20px;
}

.input-container {
  position: relative;
}

.input-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 16px;
  height: 16px;
  color: #64748b;
  z-index: 2;
}

.form-input {
  width: 100%;
  padding: 12px 12px 12px 44px;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  font-size: 14px;
  background: #f8fafc;
  transition: all 0.3s ease;
  box-sizing: border-box;
}

.form-input:focus {
  outline: none;
  border-color: #2ed573;
  background: white;
  box-shadow: 0 0 0 4px rgba(46, 213, 115, 0.1);
}

.password-toggle {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  cursor: pointer;
  color: #64748b;
  padding: 4px;
  border-radius: 4px;
  transition: color 0.3s ease;
}

.password-toggle:hover {
  color: #2ed573;
}

.password-toggle svg {
  width: 16px;
  height: 16px;
}

.form-extras {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}

.checkbox-container {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.checkbox-input {
  display: none;
}

.checkmark {
  width: 18px;
  height: 18px;
  border: 2px solid #e2e8f0;
  border-radius: 4px;
  background: white;
  position: relative;
  transition: all 0.3s ease;
}

.checkbox-input:checked + .checkmark {
  background: #2ed573;
  border-color: #2ed573;
}

.checkbox-input:checked + .checkmark::after {
  content: '';
  position: absolute;
  left: 5px;
  top: 1px;
  width: 4px;
  height: 8px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.checkbox-text {
  font-size: 14px;
  color: #64748b;
}

.forgot-password {
  color: #2ed573;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
}

.forgot-password:hover {
  text-decoration: underline;
}

.login-btn {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 10px;
  background: linear-gradient(135deg, #2ed573 0%, #26af5f 100%);
  color: white;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 20px;
}

.login-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(46, 213, 115, 0.4);
}

.login-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.btn-content {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-content svg {
  width: 18px;
  height: 18px;
}

.btn-loading {
  display: flex;
  align-items: center;
  gap: 8px;
}

.spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);

  border-radius: 50%;
  border-top-color: #2ed573;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
