<template>
  <div class="login-page">
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

    <!-- Login Form Container -->
    <div class="login-container">
      <div class="login-card">
        <!-- Header -->
        <div class="login-header">
          <h1 class="brand-name">Fresoré</h1>
          <p class="welcome-text">Belanja Fresh, Hidup Sehat! 🥬</p>
        </div>

        <!-- Login Form -->
        <form @submit.prevent="handleLogin" class="login-form">
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
                v-model="loginData.email"
                type="email"
                placeholder="Email"
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
                v-model="loginData.password"
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

          <!-- Login Button -->
          <button type="submit" class="login-btn" :disabled="isLoggingIn">
            <span v-if="!isLoggingIn" class="btn-content">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
                <polyline points="10,17 15,12 10,7"></polyline>
                <line x1="15" y1="12" x2="3" y2="12"></line>
              </svg>
              Masuk Sekarang
            </span>
            <span v-else class="btn-loading">
              <div class="spinner"></div>
              Memanen...
            </span>
          </button>
        </form>

        <!-- Register Link -->
        <div class="register-link">
          <span class="register-text">Belum punya akun? </span>
          <router-link to="/register" class="register-btn-link">Daftar di sini</router-link>
        </div>
      </div>
    </div>

    <!-- Success Animation -->
    <div v-if="showSuccess" class="success-animation">
      <div class="success-fruits">
        <div
          v-for="fruit in successFruits"
          :key="fruit.id"
          class="success-fruit"
          :style="fruit.style"
        >
          {{ fruit.emoji }}
        </div>
      </div>
      <div class="success-message">
        <h2>Selamat Datang! 🎉</h2>
        <p>Login berhasil, menuju toko segar...</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '@/composables/useAuth'

export default {
  name: 'LoginPage',
  setup() {
    const router = useRouter()
    const { login } = useAuth()

    const particles = ref([])
    const isLoggingIn = ref(false)
    const showPassword = ref(false)
    const showSuccess = ref(false)
    const successFruits = ref([])

    const loginData = reactive({
      email: '',
      password: '',
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

    const createSuccessAnimation = () => {
      successFruits.value = []
      for (let i = 0; i < 15; i++) {
        successFruits.value.push({
          id: i,
          emoji: allItems[Math.floor(Math.random() * allItems.length)],
          style: {
            left: Math.random() * 100 + '%',
            animationDelay: Math.random() * 2 + 's',
            animationDuration: Math.random() * 2 + 3 + 's',
          },
        })
      }
    }

    const handleLogin = async () => {
      isLoggingIn.value = true
      try {
        const success = await login(loginData.email, loginData.password)
        if (success) {
          showSuccess.value = true
          createSuccessAnimation()
          loginData.email = ''
          loginData.password = ''
          setTimeout(() => {
            const redirectPath = localStorage.getItem('redirectAfterLogin') || '/'
            localStorage.removeItem('redirectAfterLogin')
            router.push(redirectPath)
          }, 2000)
        } else {
          alert('Login gagal! Email atau password salah.')
        }
      } catch (error) {
        alert('Login gagal! Terjadi kesalahan.')
      } finally {
        isLoggingIn.value = false
      }
    }

    onMounted(() => {
      createParticles()
    })

    return {
      particles,
      loginData,
      isLoggingIn,
      showPassword,
      showSuccess,
      successFruits,
      handleLogin,
    }
  },
}
</script>

<style scoped>
.login-page {
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
  will-change: transform, opacity;
}

@keyframes particleFloat {
  0% {
    transform: translateY(0);
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    transform: translateY(-100px);
    opacity: 0;
  }
}

.login-container {
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

.login-card {
  background: rgba(255, 255, 255, 0.95);
  -webkit-backdrop-filter: blur(20px);
  backdrop-filter: blur(20px);
  border-radius: 20px;
  padding: 1.5rem;
  box-shadow:
    0 32px 64px rgba(0, 0, 0, 0.2),
    0 16px 32px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(255, 255, 255, 0.3);
  animation: cardSlideIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
  width: 100%;
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

.login-header {
  text-align: center;
  margin-bottom: 1.5rem;
}

.brand-name {
  font-size: 2rem;
  font-weight: 700;
  background: linear-gradient(135deg, #2ed573, #26af5f);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.3rem;
}

.welcome-text {
  color: #64748b;
  font-size: 0.9rem;
  font-weight: 500;
}

.login-form {
  margin-bottom: 1.5rem;
}

.input-group {
  margin-bottom: 1rem;
}

.input-container {
  position: relative;
}

.input-icon {
  position: absolute;
  left: 0.7rem;
  top: 50%;
  transform: translateY(-50%);
  width: 16px;
  height: 16px;
  color: #64748b;
  z-index: 2;
}

.form-input {
  width: 100%;
  padding: 0.7rem 0.7rem 0.7rem 2.5rem;
  border: 2px solid #e2e8f0;
  border-radius: 10px;
  font-size: 0.85rem;
  background: rgba(255, 255, 255, 0.8);
  -webkit-backdrop-filter: blur(10px);
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
  right: 0.7rem;
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
  width: 16px;
  height: 16px;
}

.login-btn {
  width: 100%;
  padding: 0.8rem;
  border: none;
  border-radius: 10px;
  background: linear-gradient(135deg, #2ed573 0%, #26af5f 100%);
  color: white;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  margin-bottom: 1rem;
  box-sizing: border-box;
}

.login-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(46, 213, 115, 0.4);
}

.login-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.btn-content {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.btn-content svg {
  width: 16px;
  height: 16px;
}

.btn-loading {
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.spinner {
  width: 16px;
  height: 16px;
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

.register-link {
  text-align: center;
  padding-top: 1rem;
  border-top: 1px solid #e2e8f0;
}

.register-text {
  color: #64748b;
  font-size: 0.8rem;
}

.register-btn-link {
  color: #2ed573;
  font-weight: 600;
  text-decoration: none;
  margin-left: 0.25rem;
  font-size: 0.8rem;
}

.register-btn-link:hover {
  text-decoration: underline;
}

/* Success Animation */
.success-animation {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #2ed573, #26af5f);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  color: white;
}

.success-fruits {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.success-fruit {
  position: absolute;
  font-size: 2rem;
  animation: fruitFall 4s ease-in-out forwards;
}

@keyframes fruitFall {
  0% {
    top: -10%;
    transform: rotate(0deg);
  }
  100% {
    top: 110%;
    transform: rotate(360deg);
  }
}

.success-message {
  text-align: center;
  z-index: 1001;
  animation: fadeInUp 1s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.success-message h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.success-message p {
  font-size: 1rem;
  opacity: 0.9;
}

@media (max-width: 768px) {
  .login-container {
    max-width: 360px;
    padding: 0.8rem;
  }

  .login-card {
    padding: 1.3rem;
  }

  .brand-name {
    font-size: 1.8rem;
  }
}

@media (max-width: 480px) {
  .login-container {
    max-width: 340px;
    padding: 0.5rem;
  }

  .login-card {
    padding: 1.2rem;
  }

  .form-input {
    padding: 0.6rem 0.6rem 0.6rem 2.2rem;
    font-size: 0.8rem;
  }

  .input-icon {
    width: 14px;
    height: 14px;
    left: 0.6rem;
  }

  .password-toggle svg {
    width: 14px;
    height: 14px;
  }
}
</style>
