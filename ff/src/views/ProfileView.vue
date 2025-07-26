<template>
  <div class="profile-container">
    <!-- Navbar yang sudah ada -->
    <Navbar />

    <div class="main-content">
      <!-- Komponen belum login -->
      <ProfileNotLoggedIn
        v-if="!isAuthenticated"
        @go-to-login="goToLogin"
        @go-to-register="goToRegister"
      />

      <!-- Komponen sudah login -->
      <ProfileLoggedIn
        v-else
        :userData="currentUserData"
        @logout="handleLogout"
        @menu-click="handleMenuClick"
      />
    </div>
  </div>
</template>

<script>
import { onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import ProfileNotLoggedIn from '@/components/ProfileNotLoggedIn.vue'
import ProfileLoggedIn from '@/components/ProfileLoggedIn.vue'
import { useAuth } from '@/composables/useAuth.js'

export default {
  name: 'ProfileView',
  components: {
    Navbar,
    ProfileNotLoggedIn,
    ProfileLoggedIn,
  },
  setup() {
    const router = useRouter()
    const { user, isAuthenticated, logout, checkAuth } = useAuth()

    // Computed untuk data user dengan fallback default
    const currentUserData = computed(() => {
      if (user.value) {
        return {
          name: user.value.name || 'User',
          email: user.value.email || 'user@email.com',
          totalOrders: user.value.totalOrders || 0,
          favoriteProducts: user.value.favoriteProducts || 0,
          points: user.value.points || 0,
        }
      }
      return {
        name: 'User',
        email: 'user@email.com',
        totalOrders: 0,
        favoriteProducts: 0,
        points: 0,
      }
    })

    const goToLogin = () => {
      router.push('/login')
    }

    const goToRegister = () => {
      router.push('/register')
    }

    const handleLogout = () => {
      logout()
      router.push('/')
      console.log('User logged out')
    }

    const handleMenuClick = (menuType) => {
      console.log('Menu clicked:', menuType)

      switch (menuType) {
        case 'edit-profile':
          // router.push('/profile/edit')
          alert('Edit Profile - Coming Soon!')
          break
        case 'orders':
          // router.push('/orders')
          alert('Riwayat Pesanan - Coming Soon!')
          break
        case 'wishlist':
          alert('Wishlist - Coming Soon!')
          break
        case 'address':
          alert('Alamat - Coming Soon!')
          break
        case 'security':
          alert('Keamanan - Coming Soon!')
          break
        case 'reviews':
          alert('Ulasan - Coming Soon!')
          break
        case 'rewards':
          alert('Poin & Reward - Coming Soon!')
          break
        case 'help':
          alert('Bantuan - Coming Soon!')
          break
        default:
          console.log('Unknown menu:', menuType)
      }
    }

    // Cek status login saat komponen dimount
    onMounted(() => {
      checkAuth()
      console.log('Auth status checked:', isAuthenticated.value)
      console.log('User data:', user.value)
    })

    return {
      isAuthenticated,
      currentUserData,
      goToLogin,
      goToRegister,
      handleLogout,
      handleMenuClick,
    }
  },
}
</script>

<style scoped>
.profile-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.main-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 40px 20px;
}

@media (max-width: 768px) {
  .main-content {
    padding: 20px 15px;
  }
}
</style>
