<template>
  <div class="login-required">
    <div class="login-card">
      <div class="icon">👤</div>
      <h2>Profil Saya</h2>
      <p class="subtitle">Anda belum login, login dulu ya!</p>
      <p class="description">
        Untuk mengakses profil dan bertransaksi, silakan masuk terlebih dahulu
      </p>

      <div class="action-buttons">
        <button @click="$emit('go-to-login')" class="btn-login">🔑 Masuk Sekarang</button>
        <button @click="$emit('go-to-register')" class="btn-register">📝 Daftar di sini</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileNotLoggedIn',
  emits: ['go-to-login', 'go-to-register'],
}
</script>

<style scoped>
.login-required {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  min-height: auto;
  padding: 20px;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.login-card {
  background: white;
  padding: 35px 40px;
  border-radius: 20px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 420px;
  width: 100%;
  position: relative;
  overflow: hidden;
  margin-top: 60px;
}

.login-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #52c41a, #2ecc71);
}

.icon {
  font-size: 3.5rem;
  margin-bottom: 15px;
  color: #52c41a;
  text-shadow: 0 2px 6px rgba(82, 196, 26, 0.3);
}

h2 {
  color: #2c3e50;
  margin-bottom: 8px;
  font-size: 1.8rem;
  font-weight: 700;
  letter-spacing: -0.5px;
}

.subtitle {
  color: #52c41a;
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 12px;
  text-shadow: 0 1px 3px rgba(82, 196, 26, 0.2);
}

.description {
  color: #7f8c8d;
  margin-bottom: 25px;
  line-height: 1.5;
  font-size: 0.95rem;
  max-width: 300px;
  margin-left: auto;
  margin-right: auto;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 20px;
}

.btn-login,
.btn-register {
  padding: 12px 28px;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  font-size: 0.95rem;
  letter-spacing: 0.5px;
  position: relative;
  overflow: hidden;
}

.btn-login {
  background: linear-gradient(135deg, #52c41a, #2ecc71);
  color: white;
  box-shadow: 0 4px 12px rgba(82, 196, 26, 0.3);
}

.btn-login:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(82, 196, 26, 0.4);
}

.btn-login:active {
  transform: translateY(-1px);
}

.btn-register {
  background: transparent;
  color: #52c41a;
  border: 2px solid #52c41a;
  box-shadow: 0 2px 8px rgba(82, 196, 26, 0.1);
}

.btn-register:hover {
  background: #52c41a;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(82, 196, 26, 0.3);
}

.btn-register:active {
  transform: translateY(-1px);
}

/* Responsive Design */
@media (max-width: 768px) {
  .login-required {
    padding: 15px;
  }

  .login-card {
    padding: 30px 25px;
    border-radius: 15px;
    margin-top: 50px;
  }

  .icon {
    font-size: 3rem;
  }

  h2 {
    font-size: 1.6rem;
  }

  .subtitle {
    font-size: 1rem;
  }

  .description {
    font-size: 0.9rem;
  }

  .btn-login,
  .btn-register {
    padding: 10px 24px;
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .login-card {
    padding: 25px 20px;
    margin: 10px;
  }

  .icon {
    font-size: 2.8rem;
  }

  h2 {
    font-size: 1.5rem;
  }

  .action-buttons {
    gap: 10px;
  }
}
</style>
