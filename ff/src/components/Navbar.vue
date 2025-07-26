<template>
  <div class="app-layout">
    <!-- 1. Top Bar -->
    <div class="top-bar">
      <div class="top-bar-content">
        Holaaa Welcome, Vendor application here. Latest step in digitalization era.
      </div>
    </div>

    <!-- 2. Floating Navbar -->
    <div class="floating-navbar">
      <div class="nav-island">
        <div class="nav-brand">
          <span @click="goToHome" class="logo-text">Fresoré</span>
        </div>

        <div class="nav-categories">
          <button
            v-for="category in categories"
            :key="category"
            @click="navigate(category)"
            :class="{ active: activeCategory === category }"
          >
            {{ category }}
          </button>
        </div>

        <div class="nav-actions">
          <button @click="toggleSearch">
            <span class="icon">🔍</span>
          </button>
          <router-link to="/cart" class="cart-btn">
            <div class="cart-icon">🛒</div>
            <span class="cart-count" v-if="cartCount > 0">{{ cartCount }}</span>
          </router-link>

          <!-- Profile/Login Button - Dynamic based on auth state -->
          <div class="profile-section">
            <!-- Logged in: Show profile dropdown -->
            <div v-if="isAuthenticated" class="profile-dropdown" ref="profileDropdown">
              <button @click="toggleProfileMenu" class="profile-btn logged-in">
                <div class="user-avatar">{{ userInitials }}</div>
                <span class="username">{{ user?.name || 'User' }}</span>
                <svg
                  class="dropdown-arrow"
                  :class="{ open: showProfileMenu }"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                >
                  <polyline points="6,9 12,15 18,9"></polyline>
                </svg>
              </button>

              <!-- Dropdown Menu -->
              <div v-if="showProfileMenu" class="dropdown-menu">
                <router-link to="/profile" @click="closeProfileMenu" class="dropdown-item">
                  <span class="item-icon">👤</span>
                  <span>My Profile</span>
                </router-link>
                <router-link to="/orders" @click="closeProfileMenu" class="dropdown-item">
                  <span class="item-icon">📦</span>
                  <span>Orders</span>
                </router-link>
                <router-link to="/wishlist" @click="closeProfileMenu" class="dropdown-item">
                  <span class="item-icon">❤️</span>
                  <span>Wishlist</span>
                </router-link>
                <div class="dropdown-divider"></div>
                <button @click="handleLogout" class="dropdown-item logout">
                  <span class="item-icon">🚪</span>
                  <span>Logout</span>
                </button>
              </div>
            </div>

            <!-- Not logged in: Show login button -->
            <button v-else @click="showLoginModal" class="profile-btn not-logged-in">
              <span class="icon">👤</span>
              <span class="login-text">Login</span>
            </button>
          </div>
        </div>

        <!-- Expanded Search -->
        <div class="search-box" v-if="showSearch">
          <input
            type="text"
            placeholder="Search products..."
            v-model="searchQuery"
            @keyup.enter="performSearch"
            ref="searchInput"
          />
          <button @click="toggleSearch" class="close-btn">✕</button>
        </div>
      </div>
    </div>

    <!-- Login Modal -->
    <LoginModal />
  </div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '@/composables/useAuth.js'
import LoginModal from '@/components/LoginModal.vue'

export default {
  name: 'AppLayout',
  components: {
    LoginModal,
  },
  setup() {
    const router = useRouter()
    const { user, isAuthenticated, logout } = useAuth()

    // Reactive data
    const categories = ref(['Fruits', 'Vegetables', 'Groceries', 'Meat'])
    const cartCount = ref(3) // This should come from cart store
    const showSearch = ref(false)
    const searchQuery = ref('')
    const activeCategory = ref('Vegetables')
    const showProfileMenu = ref(false)
    const profileDropdown = ref(null)

    // Computed properties
    const userInitials = computed(() => {
      if (user.value?.name) {
        return user.value.name
          .split(' ')
          .map((word) => word.charAt(0))
          .join('')
          .toUpperCase()
          .substring(0, 2)
      }
      return 'U'
    })

    // Methods
    const goToHome = () => {
      router.push('/')
      // Reset active category ke default
      activeCategory.value = 'Vegetables'

      // Clear search if open
      if (showSearch.value) {
        showSearch.value = false
        searchQuery.value = ''
      }

      // Close profile menu if open
      if (showProfileMenu.value) {
        showProfileMenu.value = false
      }

      // Dispatch event untuk reset ke home
      window.dispatchEvent(new CustomEvent('page-change', { detail: 'home' }))

      console.log('Navigating to home...')
    }

    const navigate = (destination) => {
      console.log(`Navigating to ${destination}`)

      const categoryMap = {
        Fruits: 'fruits',
        Vegetables: 'vegetables',
        Groceries: 'groceries',
        Meat: 'meat',
      }

      if (categoryMap[destination]) {
        activeCategory.value = destination
        window.dispatchEvent(
          new CustomEvent('category-change', {
            detail: categoryMap[destination],
          }),
        )
        window.dispatchEvent(
          new CustomEvent('page-change', {
            detail: 'products',
          }),
        )
      }
    }

    const toggleSearch = () => {
      showSearch.value = !showSearch.value
      if (showSearch.value) {
        // Focus search input in next tick
        setTimeout(() => {
          const searchInput = document.querySelector('.search-box input')
          if (searchInput) searchInput.focus()
        }, 100)
      }
    }

    const performSearch = () => {
      if (searchQuery.value.trim()) {
        console.log(`Searching for: ${searchQuery.value}`)
        searchQuery.value = ''
        showSearch.value = false
      }
    }

    const showLoginModal = () => {
      window.showLoginModal()
    }

    const toggleProfileMenu = () => {
      showProfileMenu.value = !showProfileMenu.value
    }

    const closeProfileMenu = () => {
      showProfileMenu.value = false
    }

    const handleLogout = () => {
      logout()
      closeProfileMenu()

      // Show logout notification
      const notification = document.createElement('div')
      notification.innerHTML = '👋 Logged out successfully!'
      notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #f59e0b, #d97706);
        color: white;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(245, 158, 11, 0.3);
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

      // Redirect to home
      router.push('/')
    }

    // Close dropdown when clicking outside
    const handleClickOutside = (event) => {
      if (profileDropdown.value && !profileDropdown.value.contains(event.target)) {
        showProfileMenu.value = false
      }
    }

    onMounted(() => {
      document.addEventListener('click', handleClickOutside)
    })

    onUnmounted(() => {
      document.removeEventListener('click', handleClickOutside)
    })

    return {
      categories,
      cartCount,
      showSearch,
      searchQuery,
      activeCategory,
      showProfileMenu,
      profileDropdown,
      user,
      isAuthenticated,
      userInitials,
      goToHome,
      navigate,
      toggleSearch,
      performSearch,
      showLoginModal,
      toggleProfileMenu,
      closeProfileMenu,
      handleLogout,
    }
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Satisfy&display=swap');
@import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@100..900&display=swap');

/* Top Bar Styles */
.top-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: #8bc34a;
  padding: 5px 0;
  text-align: center;
  font-size: 0.85rem;
  color: #fdfff5;
  z-index: 1000;
  font-family: 'League Spartan', sans-serif;
}

.top-bar-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Floating Navbar Styles */
.floating-navbar {
  position: fixed;
  top: 50px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1001;
  width: 90%;
  max-width: 1200px;
}

.nav-island {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fdf6e3;
  border-radius: 30px;
  padding: 12px 25px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(25px);
}

.nav-brand {
  flex: 1;
  position: relative;
  z-index: 10;
}

/* Logo Text Styles (Alternative) */
.logo-text {
  font-size: 1.4rem;
  font-weight: bold;
  color: #2ecc71;
  font-family: 'Satisfy', cursive;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 4px 8px;
  border-radius: 8px;
  display: inline-block;
  user-select: none;
  position: relative;
  z-index: 10;
}

.logo-text:hover {
  color: #27ae60;
  transform: scale(1.05);
  background-color: rgba(46, 204, 113, 0.1);
}

.logo-text:active {
  transform: scale(0.98);
}

.nav-categories {
  display: flex;
  gap: 15px;
  flex: 2;
  justify-content: center;
}

.nav-categories button {
  background: none;
  border: none;
  padding: 8px 16px;
  font-size: 0.95rem;
  color: #2ecc71;
  cursor: pointer;
  border-radius: 20px;
  transition: all 0.3s ease;
  font-family: 'League Spartan', sans-serif;
}

.nav-categories button:hover {
  background-color: rgba(46, 204, 113, 0.1);
}

.nav-categories button.active {
  background-color: #2ecc71;
  color: white;
}

.nav-categories button.active:hover {
  background-color: #27ae60;
}

.nav-actions {
  display: flex;
  gap: 15px;
  flex: 1;
  justify-content: flex-end;
  align-items: center;
}

.nav-actions button {
  background: none;
  border: none;
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  cursor: pointer;
  transition: background-color 0.3s ease;
  position: relative;
}

.nav-actions button:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.cart-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  position: relative;
  transition: background-color 0.3s ease;
  text-decoration: none;
}

.cart-btn:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.cart-count {
  position: absolute;
  top: -1px;
  right: 0;
  background-color: #8bc34a;
  color: white;
  border-radius: 50%;
  width: 15px;
  height: 15px;
  font-size: 0.7rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Profile Section Styles */
.profile-section {
  position: relative;
}

.profile-dropdown {
  position: relative;
}

.profile-btn {
  background: none;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 20px;
  padding: 6px 12px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: 'League Spartan', sans-serif;
}

.profile-btn:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

/* Not logged in state */
.profile-btn.not-logged-in {
  color: #2ecc71;
  font-weight: 600;
  font-size: 0.9rem;
}

.profile-btn.not-logged-in:hover {
  background-color: rgba(46, 204, 113, 0.1);
}

/* Logged in state */
.profile-btn.logged-in {
  color: #333;
  font-weight: 500;
  font-size: 0.85rem;
}

.user-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: linear-gradient(135deg, #2ecc71, #27ae60);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: bold;
}

.username {
  max-width: 80px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.dropdown-arrow {
  width: 16px;
  height: 16px;
  transition: transform 0.3s ease;
}

.dropdown-arrow.open {
  transform: rotate(180deg);
}

/* Dropdown Menu */
.dropdown-menu {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 8px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(0, 0, 0, 0.1);
  min-width: 180px;
  overflow: hidden;
  animation: dropdownSlide 0.3s ease;
  z-index: 1002;
}

@keyframes dropdownSlide {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.dropdown-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  color: #333;
  text-decoration: none;
  transition: background-color 0.3s ease;
  font-size: 0.9rem;
  border: none;
  background: none;
  width: 100%;
  cursor: pointer;
}

.dropdown-item:hover {
  background-color: #f8f9fa;
}

.dropdown-item.logout {
  color: #dc3545;
}

.dropdown-item.logout:hover {
  background-color: #fff5f5;
}

.item-icon {
  font-size: 1rem;
}

.dropdown-divider {
  height: 1px;
  background-color: #e9ecef;
  margin: 4px 0;
}

/* Search Box */
.search-box {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: white;
  padding: 15px;
  border-radius: 0 0 20px 20px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  display: flex;
  margin-top: 5px;
}

.search-box input {
  flex: 1;
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 20px;
  font-size: 0.95rem;
  outline: none;
}

.close-btn {
  background: none;
  border: none;
  margin-left: 10px;
  cursor: pointer;
  font-size: 1.2rem;
  color: #777;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .top-bar {
    font-size: 0.75rem;
  }

  .floating-navbar {
    top: 30px;
    width: 95%;
  }

  .nav-island {
    padding: 10px 15px;
  }

  .logo-text {
    font-size: 1.2rem;
  }

  .nav-categories {
    gap: 8px;
  }

  .nav-categories button {
    padding: 6px 10px;
    font-size: 0.85rem;
  }

  .username {
    display: none;
  }

  .dropdown-menu {
    right: -10px;
  }
}

@media (max-width: 480px) {
  .top-bar {
    padding: 6px 10px;
  }

  .nav-brand {
    display: flex;
    align-items: center;
  }

  .logo-text {
    font-size: 1.1rem;
  }

  .profile-btn.not-logged-in .login-text {
    display: none;
  }
}
</style>
