<template>
  <div class="register-page">
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

    <!-- Register Form Container -->
    <div class="register-container">
      <div class="register-card">
        <!-- Header -->
        <div class="register-header">
          <h1 class="brand-name">Fresoré</h1>
          <p class="welcome-text">Bergabung dengan Keluarga Fresh! 🌱</p>
        </div>

        <!-- Register Form -->
        <form @submit.prevent="handleRegister" class="register-form">
          <!-- Full Name -->
          <div class="input-group">
            <div class="input-container">
              <svg
                class="input-icon"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
              <input
                v-model="registerData.fullName"
                type="text"
                placeholder="Nama Lengkap"
                required
                class="form-input"
              />
            </div>
          </div>

          <!-- Email -->
          <div class="input-group">
            <div class="input-container">
              <svg
                class="input-icon"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"
                ></path>
                <polyline points="22,6 12,13 2,6"></polyline>
              </svg>
              <input
                v-model="registerData.email"
                type="email"
                placeholder="Email"
                required
                class="form-input"
              />
            </div>
          </div>

          <!-- Phone Number -->
          <div class="input-group">
            <div class="input-container">
              <svg
                class="input-icon"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
                ></path>
              </svg>
              <input
                v-model="registerData.phone"
                type="tel"
                placeholder="Nomor Telepon"
                required
                class="form-input"
              />
            </div>
          </div>

          <!-- Password -->
          <div class="input-group">
            <div class="input-container">
              <svg
                class="input-icon"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <circle cx="12" cy="16" r="1"></circle>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
              <input
                v-model="registerData.password"
                :type="showPassword ? 'text' : 'password'"
                placeholder="Password"
                required
                class="form-input"
              />
              <button type="button" @click="showPassword = !showPassword" class="password-toggle">
                <svg
                  v-if="showPassword"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"
                  ></path>
                  <line x1="1" y1="1" x2="23" y2="23"></line>
                </svg>
                <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                </svg>
              </button>
            </div>
          </div>

          <!-- Confirm Password -->
          <div class="input-group">
            <div class="input-container">
              <svg
                class="input-icon"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
              >
                <path d="M9 12l2 2 4-4"></path>
                <path d="M21 12c-1 0-3-1-3-3s2-3 3-3 3 1 3 3-2 3-3 3"></path>
                <path d="M3 12c1 0 3-1 3-3s-2-3-3-3-3 1-3 3 2 3 3 3"></path>
              </svg>
              <input
                v-model="registerData.confirmPassword"
                :type="showConfirmPassword ? 'text' : 'password'"
                placeholder="Konfirmasi Password"
                required
                class="form-input"
              />
              <button
                type="button"
                @click="showConfirmPassword = !showConfirmPassword"
                class="password-toggle"
              >
                <svg
                  v-if="showConfirmPassword"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <path
                    d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"
                  ></path>
                  <line x1="1" y1="1" x2="23" y2="23"></line>
                </svg>
                <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                </svg>
              </button>
            </div>
          </div>

          <!-- Terms and Conditions -->
          <div class="checkbox-group">
            <label class="checkbox-container">
              <input
                v-model="registerData.agreeTerms"
                type="checkbox"
                required
                class="checkbox-input"
              />
              <span class="checkmark"></span>
              <span class="checkbox-text">
                Saya setuju dengan
                <a href="#" class="terms-link">Syarat & Ketentuan</a>
                dan
                <a href="#" class="terms-link">Kebijakan Privasi</a>
              </span>
            </label>
          </div>

          <!-- Register Button -->
          <button type="submit" class="register-btn" :disabled="isRegistering">
            <span v-if="!isRegistering" class="btn-content">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <line x1="19" y1="8" x2="19" y2="14"></line>
                <line x1="22" y1="11" x2="16" y2="11"></line>
              </svg>
              Daftar Sekarang
            </span>
            <span v-else class="btn-loading">
              <div class="spinner"></div>
              Mendaftarkan...
            </span>
          </button>
        </form>

        <!-- Login Link -->
        <div class="login-link">
          <span class="login-text">Sudah punya akun? </span>
          <a href="#" @click.prevent="showLoginModal" class="login-btn-link">Masuk Sekarang</a>
        </div>
      </div>
    </div>

    <!-- Login Modal -->
    <LoginModal />
  </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '@/composables/useAuth.js'
import api from '@/axios.js'
import LoginModal from '@/components/LoginModal.vue'

export default {
  name: 'RegisterPage',
  components: {
    LoginModal,
  },
  setup() {
    const router = useRouter()
    const { login } = useAuth()

    const particles = ref([])
    const isRegistering = ref(false)
    const showPassword = ref(false)
    const showConfirmPassword = ref(false)

    const registerData = reactive({
      fullName: '',
      email: '',
      phone: '',
      password: '',
      confirmPassword: '',
      agreeTerms: false,
    })

    const vegetables = ['🥬', '🥕', '🍅', '🥒', '🌽', '🥦', '🍆', '🥔', '🧅', '🥑']
    const fruits = ['🍎', '🍊', '🍌', '🍇', '🍓', '🥝', '🍑', '🍒']
    const allItems = [...vegetables, ...fruits]

    const createParticles = () => {
      particles.value = []
      for (let i = 0; i < 15; i++) {
        particles.value.push({
          emoji: allItems[Math.floor(Math.random() * allItems.length)],
          style: {
            left: Math.random() * 100 + '%',
            top: Math.random() * 100 + '%',
            animationDelay: Math.random() * 10 + 's',
            animationDuration: Math.random() * 10 + 15 + 's',
            fontSize: Math.random() * 25 + 20 + 'px',
            opacity: Math.random() * 0.8 + 0.2,
          },
        })
      }
    }

    const showLoginModal = () => {
      // Use global function instead of local modal
      window.showLoginModal()
    }

    const handleRegister = async () => {
      // Validate passwords match
      if (registerData.password !== registerData.confirmPassword) {
        alert('Password tidak cocok!')
        return
      }
      if (registerData.password.length < 6) {
        alert('Password minimal 6 karakter!')
        return
      }
      isRegistering.value = true
      try {
        // POST ke backend Django
        await api.post('/api/auth/register/', {
          username: registerData.email.split('@')[0], // gunakan bagian depan email jika tidak ada username
          email: registerData.email,
          password: registerData.password,
        })
        // Setelah register, langsung login
        const loginSuccess = await login(registerData.email, registerData.password)
        if (loginSuccess) {
          // Show success notification
          const notification = document.createElement('div')
          notification.innerHTML = '🎉 Pendaftaran berhasil! Selamat datang di Fresoré!'
          notification.className = 'success-notification'
          notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, #2ed573, #26af5f);
            color: white;
            padding: 15px 20px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(46, 213, 115, 0.3);
            z-index: 9999;
            font-weight: 600;
            animation: slideIn 0.5s ease;
          `
          document.body.appendChild(notification)
          setTimeout(() => {
            if (document.body.contains(notification)) {
              document.body.removeChild(notification)
            }
            // Redirect to profile or home
            const redirectTo = localStorage.getItem('redirectAfterLogin') || '/profile'
            localStorage.removeItem('redirectAfterLogin')
            router.push(redirectTo)
          }, 2000)
        } else {
          alert('Registrasi berhasil, tapi gagal login otomatis. Silakan login manual.')
        }
      } catch (error) {
        console.error('Registration failed:', error)
        alert('Pendaftaran gagal! Email sudah terdaftar atau data tidak valid.')
      } finally {
        isRegistering.value = false
      }
    }

    onMounted(() => {
      createParticles()
    })

    return {
      particles,
      registerData,
      isRegistering,
      showPassword,
      showConfirmPassword,
      handleRegister,
      showLoginModal,
    }
  },
}
</script>

<style scoped>
/* [Previous CSS remains the same] */
.register-page {
  min-height: 100vh;
  width: 100vw;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  position: fixed;
  top: 0;
  left: 0;
  overflow: hidden;
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

.register-container {
  width: 100%;
  max-width: 380px;
  z-index: 10;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  box-sizing: border-box;
}

.register-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 1.3rem;
  box-shadow:
    0 32px 64px rgba(0, 0, 0, 0.2),
    0 16px 32px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.3);
  animation: cardSlideIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
  width: 100%;
  max-height: none;
  overflow: visible;
  box-sizing: border-box;
}

@keyframes cardSlideIn {
  from {
    transform: translateY(50px) scale(0.9);
    opacity: 0;
  }
  to {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
}

.register-header {
  text-align: center;
  margin-bottom: 1rem;
}

.brand-name {
  font-size: 1.8rem;
  font-weight: 700;
  background: linear-gradient(135deg, #2ed573, #26af5f);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.2rem;
}

.welcome-text {
  color: #64748b;
  font-size: 0.8rem;
  font-weight: 500;
}

.register-form {
  space-y: 1.5rem;
}

.input-group {
  margin-bottom: 0.7rem;
}

.input-container {
  position: relative;
}

.input-icon {
  position: absolute;
  left: 0.6rem;
  top: 50%;
  transform: translateY(-50%);
  width: 14px;
  height: 14px;
  color: #64748b;
  z-index: 2;
}

.form-input {
  width: 100%;
  padding: 0.6rem 0.6rem 0.6rem 2.2rem;
  border: 2px solid #e2e8f0;
  border-radius: 8px;
  font-size: 0.8rem;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
  box-sizing: border-box;
}

.form-input:focus {
  outline: none;
  border-color: #2ed573;
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 0 0 4px rgba(46, 213, 115, 0.1);
}

.password-toggle {
  position: absolute;
  right: 0.6rem;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  cursor: pointer;
  color: #64748b;
  padding: 2px;
  border-radius: 4px;
  transition: color 0.3s ease;
}

.password-toggle:hover {
  color: #2ed573;
}

.password-toggle svg {
  width: 14px;
  height: 14px;
}

.checkbox-group {
  margin: 1rem 0;
}

.checkbox-container {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  cursor: pointer;
  line-height: 1.5;
}

.checkbox-input {
  display: none;
}

.checkmark {
  width: 20px;
  height: 20px;
  border: 2px solid #e2e8f0;
  border-radius: 6px;
  background: white;
  position: relative;
  transition: all 0.3s ease;
  flex-shrink: 0;
  margin-top: 2px;
}

.checkbox-input:checked + .checkmark {
  background: #2ed573;
  border-color: #2ed573;
}

.checkbox-input:checked + .checkmark::after {
  content: '';
  position: absolute;
  left: 6px;
  top: 2px;
  width: 4px;
  height: 8px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.checkbox-text {
  font-size: 0.9rem;
  color: #64748b;
}

.terms-link {
  color: #2ed573;
  text-decoration: none;
  font-weight: 500;
}

.terms-link:hover {
  text-decoration: underline;
}

.register-btn {
  width: 100%;
  padding: 0.6rem;
  border: none;
  border-radius: 8px;
  background: linear-gradient(135deg, #2ed573 0%, #26af5f 100%);
  color: white;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.3rem;
  margin-top: 0.2rem;
  box-sizing: border-box;
}

.register-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(46, 213, 115, 0.4);
}

.register-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.btn-content {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-content svg {
  width: 20px;
  height: 20px;
}

.btn-loading {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
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

.login-link {
  text-align: center;
  margin: 0.8rem 0 0 0;
  padding-top: 0.6rem;
  border-top: 1px solid #e2e8f0;
}

.login-text {
  color: #64748b;
  font-size: 0.75rem;
}

.login-btn-link {
  color: #2ed573;
  font-weight: 600;
  text-decoration: none;
  margin-left: 0.25rem;
  font-size: 0.75rem;
}

.login-btn-link:hover {
  text-decoration: underline;
  cursor: pointer;
}

/* Success notification animation */
@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .register-container {
    max-width: 360px;
    padding: 0.8rem;
  }

  .register-card {
    padding: 1.2rem;
  }

  .brand-name {
    font-size: 1.6rem;
  }
}

@media (max-width: 480px) {
  .register-container {
    max-width: 340px;
    padding: 0.5rem;
  }

  .register-card {
    padding: 1rem;
  }

  .input-group {
    margin-bottom: 0.6rem;
  }

  .form-input {
    padding: 0.5rem 0.5rem 0.5rem 2rem;
    font-size: 0.75rem;
  }

  .input-icon {
    width: 12px;
    height: 12px;
    left: 0.5rem;
  }

  .password-toggle svg {
    width: 12px;
    height: 12px;
  }
}
</style>
