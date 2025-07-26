<template>
  <div class="profile-content">
    <!-- Profile Header -->
    <div class="profile-header">
      <div class="profile-avatar">
        <div class="avatar-circle">
          {{ userInitials }}
        </div>
        <button class="change-photo-btn" @click="changePhoto">📷</button>
      </div>
      <div class="profile-info">
        <h1>{{ userData.name }}</h1>
        <p class="email">{{ userData.email }}</p>
        <div class="badges">
          <span class="badge member">Member Fresoré</span>
          <span class="badge verified">✅ Terverifikasi</span>
        </div>
      </div>
    </div>

    <!-- Profile Stats -->
    <div class="profile-stats">
      <div class="stat-card">
        <div class="stat-number">{{ userData.totalOrders }}</div>
        <div class="stat-label">Total Pesanan</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">{{ userData.favoriteProducts }}</div>
        <div class="stat-label">Produk Favorit</div>
      </div>
      <div class="stat-card">
        <div class="stat-number">{{ userData.points }}</div>
        <div class="stat-label">Poin Reward</div>
      </div>
    </div>

    <!-- Profile Menu -->
    <div class="profile-menu">
      <div class="menu-section">
        <h3>Akun Saya</h3>
        <div class="menu-item" @click="handleMenuClick('edit-profile')">
          <span class="menu-icon">👤</span>
          <span class="menu-text">Edit Profil</span>
          <span class="menu-arrow">›</span>
        </div>
        <div class="menu-item" @click="handleMenuClick('address')">
          <span class="menu-icon">📍</span>
          <span class="menu-text">Alamat Pengiriman</span>
          <span class="menu-arrow">›</span>
        </div>
        <div class="menu-item" @click="handleMenuClick('security')">
          <span class="menu-icon">🔒</span>
          <span class="menu-text">Keamanan</span>
          <span class="menu-arrow">›</span>
        </div>
      </div>

      <div class="menu-section">
        <h3>Pesanan</h3>
        <div class="menu-item" @click="handleMenuClick('orders')">
          <span class="menu-icon">📦</span>
          <span class="menu-text">Riwayat Pesanan</span>
          <span class="menu-arrow">›</span>
        </div>
        <div class="menu-item" @click="handleMenuClick('wishlist')">
          <span class="menu-icon">❤️</span>
          <span class="menu-text">Wishlist</span>
          <span class="menu-arrow">›</span>
        </div>
        <div class="menu-item" @click="handleMenuClick('reviews')">
          <span class="menu-icon">⭐</span>
          <span class="menu-text">Ulasan Saya</span>
          <span class="menu-arrow">›</span>
        </div>
      </div>

      <div class="menu-section">
        <h3>Lainnya</h3>
        <div class="menu-item" @click="handleMenuClick('rewards')">
          <span class="menu-icon">🎁</span>
          <span class="menu-text">Poin & Reward</span>
          <span class="menu-arrow">›</span>
        </div>
        <div class="menu-item" @click="handleMenuClick('help')">
          <span class="menu-icon">📞</span>
          <span class="menu-text">Bantuan</span>
          <span class="menu-arrow">›</span>
        </div>
        <div class="menu-item" @click="$emit('logout')">
          <span class="menu-icon">🚪</span>
          <span class="menu-text">Keluar</span>
          <span class="menu-arrow">›</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileLoggedIn',
  props: {
    userData: {
      type: Object,
      required: true,
    },
  },
  emits: ['logout', 'menu-click'],
  computed: {
    userInitials() {
      if (this.userData.name) {
        return this.userData.name
          .split(' ')
          .map((word) => word.charAt(0))
          .join('')
          .toUpperCase()
          .substring(0, 2)
      }
      return 'U'
    },
  },
  methods: {
    changePhoto() {
      console.log('Change photo clicked')
      // Logic ganti foto nanti
    },
    handleMenuClick(menuType) {
      this.$emit('menu-click', menuType)
    },
  },
}
</script>

<style scoped>
.profile-content {
  background: white;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

/* Profile Header */
.profile-header {
  background: linear-gradient(135deg, #52c41a, #73d13d);
  padding: 40px;
  color: white;
  display: flex;
  align-items: center;
  gap: 30px;
}

.profile-avatar {
  position: relative;
}

.avatar-circle {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: bold;
  border: 3px solid rgba(255, 255, 255, 0.3);
}

.change-photo-btn {
  position: absolute;
  bottom: 0;
  right: 0;
  background: white;
  border: none;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  cursor: pointer;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s;
}

.change-photo-btn:hover {
  transform: scale(1.1);
}

.profile-info h1 {
  margin: 0 0 5px 0;
  font-size: 2rem;
}

.email {
  opacity: 0.9;
  margin: 0 0 15px 0;
}

.badges {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.badge {
  background: rgba(255, 255, 255, 0.2);
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 0.9rem;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

/* Profile Stats */
.profile-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0;
  border-bottom: 1px solid #f0f0f0;
}

.stat-card {
  padding: 30px 20px;
  text-align: center;
  border-right: 1px solid #f0f0f0;
  transition: background 0.3s;
}

.stat-card:hover {
  background: #f9f9f9;
}

.stat-card:last-child {
  border-right: none;
}

.stat-number {
  font-size: 2rem;
  font-weight: bold;
  color: #52c41a;
  margin-bottom: 5px;
}

.stat-label {
  color: #666;
  font-size: 0.9rem;
}

/* Profile Menu */
.profile-menu {
  padding: 30px;
}

.menu-section {
  margin-bottom: 30px;
}

.menu-section:last-child {
  margin-bottom: 0;
}

.menu-section h3 {
  color: #333;
  margin-bottom: 15px;
  font-size: 1.1rem;
}

.menu-item {
  display: flex;
  align-items: center;
  padding: 15px 0;
  border-bottom: 1px solid #f0f0f0;
  cursor: pointer;
  transition: all 0.3s;
  border-radius: 10px;
}

.menu-item:hover {
  background: #f9f9f9;
  margin: 0 -15px;
  padding-left: 15px;
  padding-right: 15px;
  border-bottom: 1px solid transparent;
}

.menu-item:last-child {
  border-bottom: none;
}

.menu-icon {
  font-size: 1.2rem;
  margin-right: 15px;
  width: 24px;
}

.menu-text {
  flex: 1;
  color: #333;
}

.menu-arrow {
  color: #999;
  font-size: 1.5rem;
}

/* Responsive */
@media (max-width: 768px) {
  .profile-header {
    flex-direction: column;
    text-align: center;
    gap: 20px;
    padding: 30px 20px;
  }

  .profile-stats {
    grid-template-columns: 1fr;
  }

  .stat-card {
    border-right: none;
    border-bottom: 1px solid #f0f0f0;
  }

  .stat-card:last-child {
    border-bottom: none;
  }

  .profile-menu {
    padding: 20px;
  }
}
</style>
