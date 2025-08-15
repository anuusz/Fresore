<template>
  <div class="login-page">
    <!-- Optional overlay for better readability -->
    <div class="background-overlay"></div>

    <div class="login-container">
      <!-- <div class="logo">
        <h1>Fresoré</h1>
        <p>Fresh & Natural Marketplace</p>
      </div> -->

      <!-- Success Message -->
      <Transition name="fade">
        <div v-if="showSuccessMessage" class="success-message">
          {{ successMessage }}
        </div>
      </Transition>

      <!-- Error Message -->
      <Transition name="fade">
        <div v-if="showErrorMessage" class="alert-message alert-error">
          {{ errorMessage }}
        </div>
      </Transition>

      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="email">Email</label>
          <input
            type="email"
            id="email"
            v-model="formData.email"
            :class="{ error: errors.email }"
            required
            :disabled="isLoading"
            @blur="validateEmail"
            placeholder="Masukkan email Anda"
          >
          <div v-if="errors.email" class="error-message">{{ errors.email }}</div>
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model="formData.password"
            :class="{ error: errors.password }"
            required
            :disabled="isLoading"
            @blur="validatePassword"
            placeholder="Masukkan password Anda"
          >
          <div v-if="errors.password" class="error-message">{{ errors.password }}</div>
        </div>

        <div class="forgot-password">
          <a @click="handleForgotPassword">Lupa Password?</a>
        </div>

        <button type="submit" class="login-btn" :disabled="isLoading || !isFormValid">
          <span v-if="isLoading" class="loading-spinner"></span>
          {{ isLoading ? 'Memproses...' : 'Login' }}
        </button>
      </form>

      <div class="register-link">
        <p>Belum punya akun? <a @click="handleRegister">Daftar Sekarang</a></p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'

// Reactive data
const formData = ref({
  email: '',
  password: ''
})

const errors = ref({
  email: '',
  password: ''
})

const isLoading = ref(false)
const showSuccessMessage = ref(false)
const showErrorMessage = ref(false)
const successMessage = ref('')
const errorMessage = ref('')

// Computed properties
const isFormValid = computed(() => {
  return formData.value.email &&
         formData.value.password &&
         !errors.value.email &&
         !errors.value.password
})

// Methods
const validateEmail = () => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!formData.value.email) {
    errors.value.email = 'Email wajib diisi'
  } else if (!emailRegex.test(formData.value.email)) {
    errors.value.email = 'Format email tidak valid'
  } else {
    errors.value.email = ''
  }
}

const validatePassword = () => {
  if (!formData.value.password) {
    errors.value.password = 'Password wajib diisi'
  } else if (formData.value.password.length < 6) {
    errors.value.password = 'Password minimal 6 karakter'
  } else {
    errors.value.password = ''
  }
}

const hideMessages = () => {
  showSuccessMessage.value = false
  showErrorMessage.value = false
}

const handleLogin = async () => {
  // Validate form
  validateEmail()
  validatePassword()

  if (!isFormValid.value) {
    return
  }

  // Set loading state
  isLoading.value = true
  hideMessages()

  try {
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 2000))

    // Simulate login logic
    if (formData.value.email === 'admin@fresore.com' && formData.value.password === 'password') {
      // Success
      successMessage.value = 'Login berhasil! Selamat datang di Fresoré.'
      showSuccessMessage.value = true

      // Emit event to parent component or handle routing
      // emit('login-success', { email: formData.value.email })

      // Simulate redirect after 2 seconds
      setTimeout(() => {
        console.log('Redirect to dashboard...')
        // router.push('/dashboard') // if using Vue Router
      }, 2000)
    } else {
      // Error
      errorMessage.value = 'Email atau password salah. Silakan coba lagi.'
      showErrorMessage.value = true
    }
  } catch (error) {
    errorMessage.value = 'Terjadi kesalahan. Silakan coba lagi.'
    showErrorMessage.value = true
  } finally {
    isLoading.value = false
  }
}

const handleForgotPassword = () => {
  console.log('Handle forgot password')
  // router.push('/forgot-password') // if using Vue Router
  alert('Fitur lupa password akan segera tersedia!')
}

const handleRegister = () => {
  console.log('Handle register')
  // router.push('/register') // if using Vue Router
  alert('Halaman registrasi akan segera tersedia!')
}

// Watchers
watch(() => formData.value.email, () => {
  if (errors.value.email) {
    validateEmail()
  }
  hideMessages()
})

watch(() => formData.value.password, () => {
  if (errors.value.password) {
    validatePassword()
  }
  hideMessages()
})

// Define emits for parent component communication (optional)
// const emit = defineEmits(['login-success', 'navigate-to-register', 'navigate-to-forgot-password'])
</script>

<style scoped>
.login-page {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-image: url('@/assets/Fresorepage.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  margin: 0;
  padding: 20px;
  box-sizing: border-box;
}

/* Background overlay for better readability */
.background-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.1);
  z-index: 1;
}

/* Remove fruit decorations - using background image instead */

.login-container {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(25px) saturate(180%);
  -webkit-backdrop-filter: blur(25px) saturate(180%);
  border-radius: 25px;
  padding: 25px;
  margin-top: 100px;
  box-shadow:
    0 25px 50px rgba(0, 0, 0, 0.15),
    0 8px 16px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.8),
    inset 0 -1px 0 rgba(255, 255, 255, 0.2);
  width: 500px;
  max-width: 90vw;
  position: relative;
  z-index: 10;
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-top: 1px solid rgba(255, 255, 255, 0.5);
}

.logo {
  text-align: center;
  margin-bottom: 30px;
}

.logo h1 {
  color: #059669;
  font-size: 2.5rem;
  font-weight: 300;
  letter-spacing: 2px;
  margin-bottom: 10px;
  font-style: italic;
}

.logo p {
  color: #6b7280;
  font-size: 0.9rem;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 10px;
  color: #2d3748;
  font-weight: 600;
  font-size: 0.95rem;
  text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
}

.form-group input {
  width: 100%;
  padding: 18px;
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 15px;
  font-size: 1rem;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  color: #2d3748;
  box-sizing: border-box;
}

.form-group input:focus {
  outline: none;
  border-color: rgba(16, 185, 129, 0.5);
  box-shadow:
    0 0 0 3px rgba(16, 185, 129, 0.1),
    0 8px 25px rgba(16, 185, 129, 0.15);
  background: rgba(255, 255, 255, 0.2);
}

.form-group input::placeholder {
  color: rgba(45, 55, 72, 0.6);
}

.form-group input.error {
  border-color: #dc2626;
}

.form-group input:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.forgot-password {
  text-align: right;
  margin-bottom: 25px;
}

.forgot-password a {
  color: #059669;
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.3s ease;
  cursor: pointer;
}

.forgot-password a:hover {
  color: #047857;
  text-decoration: underline;
}

.login-btn {
  width: 100%;
  padding: 18px;
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.8) 0%, rgba(5, 150, 105, 0.9) 100%);
  backdrop-filter: blur(10px);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 1px;
  position: relative;
  box-shadow:
    0 8px 25px rgba(16, 185, 129, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.login-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow:
    0 15px 35px rgba(16, 185, 129, 0.3),
    0 8px 15px rgba(0, 0, 0, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.4);
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.9) 0%, rgba(5, 150, 105, 1) 100%);
}

.login-btn:active {
  transform: translateY(0);
}

.login-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.loading-spinner {
  display: inline-block;
  width: 16px;
  height: 16px;
  border: 2px solid #ffffff;
  border-radius: 50%;
  border-top-color: transparent;
  animation: spin 1s linear infinite;
  margin-right: 8px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.divider {
  text-align: center;
  margin: 25px 0;
  position: relative;
}

.divider::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 1px;
  background: #e5e7eb;
}

.divider span {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  padding: 0 20px;
  color: #4a5568;
  font-size: 0.9rem;
  font-weight: 500;
}

.register-link {
  text-align: center;
  margin-top: 20px;
}

.register-link p {
  color: #6b7280;
  font-size: 0.9rem;
}

.register-link a {
  color: #059669;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease;
  cursor: pointer;
}

.register-link a:hover {
  color: #047857;
}

.error-message {
  color: #dc2626;
  font-size: 0.8rem;
  margin-top: 5px;
}

.success-message {
  color: #059669;
  font-size: 0.9rem;
  text-align: center;
  margin-bottom: 20px;
  padding: 15px;
  background: rgba(16, 185, 129, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  border: 1px solid rgba(16, 185, 129, 0.25);
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.1);
}

.alert-message {
  font-size: 0.9rem;
  text-align: center;
  margin-bottom: 20px;
  padding: 15px;
  border-radius: 12px;
  backdrop-filter: blur(10px);
}

.alert-error {
  color: #dc2626;
  background: rgba(220, 38, 38, 0.1);
  border: 1px solid rgba(220, 38, 38, 0.25);
  box-shadow: 0 4px 15px rgba(220, 38, 38, 0.1);
}

/* Transitions */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

/* Responsive */
@media (max-width: 480px) {
  .login-container {
    padding: 30px 20px;
  }

  .logo h1 {
    font-size: 2rem;
  }

  .login-page {
    padding: 10px;
  }
}
</style>
