<template>
  <div class="app-wrapper">
    <!-- Navbar Component -->
    <div class="app-layout">
      <!-- Top Bar -->
      <div class="top-bar">
        <div class="top-bar-content">
          Holaaa Welcome, Vendor application here. Latest step in digitalization era.
        </div>
      </div>

      <!-- Floating Navbar -->
      <div class="floating-navbar">
        <div class="nav-island">
          <div class="nav-brand">
            <span
              @click.prevent="goToHome"
              class="logo-text"
              role="button"
              tabindex="0"
              @keyup.enter="goToHome"
              >Fresoré</span
            >
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
            <button class="cart-btn active-cart">
              <div class="cart-icon">🛒</div>
              <span class="cart-count" v-if="cartItemCount > 0">{{ cartItemCount }}</span>
            </button>
            <button @click="navigate('profile')">
              <span class="icon">👤</span>
            </button>
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
    </div>

    <!-- Cart Container -->
    <div class="cart-container">
      <!-- Hero Section Mini -->
      <div class="cart-hero" data-aos="fade-down">
        <div class="hero-content">
          <h1>🛒 Keranjang Belanja</h1>
          <p>{{ cartItems.length }} produk di keranjang Anda</p>
          <div class="hero-decoration">
            <div class="floating-leaf leaf-1">🌿</div>
            <div class="floating-leaf leaf-2">🍃</div>
            <div class="floating-leaf leaf-3">🌱</div>
          </div>
        </div>
      </div>

      <div class="cart-content">
        <!-- Cart Items -->
        <div class="cart-items-section" data-aos="fade-right">
          <div class="cart-header">
            <h2>Produk Yang Dipilih</h2>
            <button class="clear-cart pulse-btn" @click="clearCart" v-if="cartItems.length > 0">
              🗑️ Hapus Semua
            </button>
          </div>

          <!-- Empty Cart -->
          <div v-if="cartItems.length === 0" class="empty-cart" data-aos="zoom-in">
            <div class="empty-cart-content">
              <div class="empty-icon bounce-animation">🛒</div>
              <h3>Keranjang Masih Kosong</h3>
              <p>Ayo mulai belanja produk segar terbaik!</p>
              <button class="start-shopping gradient-btn" @click="goToProducts">
                <span class="btn-icon">🛍️</span>
                Mulai Belanja
              </button>
            </div>
          </div>

          <!-- Cart Items List -->
          <div v-else class="cart-items-list">
            <div
              v-for="(item, index) in cartItems"
              :key="item.id"
              class="cart-item slide-in-item"
              :style="{ animationDelay: `${index * 0.1}s` }"
              data-aos="fade-up"
              :data-aos-delay="index * 100"
            >
              <div class="item-image">
                <img :src="item.image" :alt="item.name" />
                <div class="item-badges" v-if="item.discount || item.isNew">
                  <span class="badge discount glow-effect" v-if="item.discount"
                    >-{{ item.discount }}%</span
                  >
                  <span class="badge new pulse-effect" v-if="item.isNew">NEW</span>
                </div>
                <div class="image-overlay"></div>
              </div>

              <div class="item-details">
                <div class="item-info">
                  <div class="item-brand">{{ item.brand }}</div>
                  <h3 class="item-name">{{ item.name }}</h3>
                  <div class="item-price">
                    <span class="current-price">Rp {{ formatPrice(item.price) }}</span>
                    <span v-if="item.originalPrice" class="original-price">
                      Rp {{ formatPrice(item.originalPrice) }}
                    </span>
                  </div>
                </div>

                <div class="item-actions">
                  <div class="quantity-controls modern-controls">
                    <button
                      class="qty-btn minus hover-effect"
                      @click="updateQuantity(item.id, item.quantity - 1)"
                      :disabled="item.quantity <= 1"
                    >
                      −
                    </button>
                    <span class="quantity">{{ item.quantity }}</span>
                    <button
                      class="qty-btn plus hover-effect"
                      @click="updateQuantity(item.id, item.quantity + 1)"
                    >
                      +
                    </button>
                  </div>

                  <div class="item-total">
                    <span class="total-price"
                      >Rp {{ formatPrice(item.price * item.quantity) }}</span
                    >
                  </div>

                  <button class="remove-item hover-scale" @click="removeItem(item.id)">
                    <span class="remove-icon">🗑️</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Cart Summary -->
        <div class="cart-summary sticky-summary" v-if="cartItems.length > 0" data-aos="fade-left">
          <div class="summary-card glass-effect">
            <div class="summary-header">
              <h3>💰 Ringkasan Belanja</h3>
              <div class="summary-decoration">
                <div class="sparkle sparkle-1">✨</div>
                <div class="sparkle sparkle-2">⭐</div>
              </div>
            </div>

            <div class="summary-row">
              <span>Subtotal ({{ totalItems }} produk)</span>
              <span class="amount-animation">Rp {{ formatPrice(subtotal) }}</span>
            </div>

            <div class="summary-row">
              <span>Diskon</span>
              <span class="discount-amount">-Rp {{ formatPrice(totalDiscount) }}</span>
            </div>

            <div class="summary-row">
              <span>Ongkos Kirim</span>
              <span class="shipping-cost">{{
                shippingCost === 0 ? 'GRATIS 🎉' : 'Rp ' + formatPrice(shippingCost)
              }}</span>
            </div>

            <hr class="summary-divider animated-divider" />

            <div class="summary-row total-row">
              <span>Total</span>
              <span class="total-amount scale-in">Rp {{ formatPrice(finalTotal) }}</span>
            </div>

            <!-- Promo Code -->
            <div class="promo-section">
              <div class="promo-input" :class="{ expanded: showPromoInput }">
                <input
                  v-if="showPromoInput"
                  v-model="promoCode"
                  type="text"
                  placeholder="Masukkan kode promo"
                  @keyup.enter="applyPromo"
                  class="promo-input-field"
                />
                <button
                  v-if="!showPromoInput"
                  class="promo-toggle gradient-border"
                  @click="showPromoInput = true"
                >
                  🎫 Punya Kode Promo?
                </button>
                <button
                  v-else
                  class="apply-promo gradient-btn"
                  @click="applyPromo"
                  :disabled="!promoCode.trim()"
                >
                  Terapkan
                </button>
              </div>
            </div>

            <!-- Checkout Button -->
            <button class="checkout-btn mega-gradient" @click="proceedToCheckout">
              <span class="checkout-icon">💳</span>
              <span>Lanjut ke Pembayaran</span>
              <div class="btn-ripple"></div>
            </button>

            <!-- Additional Info -->
            <div class="cart-benefits">
              <div class="benefit-item fade-in-benefit" style="animation-delay: 0.1s">
                <span class="benefit-icon">🚚</span>
                <span>Gratis ongkir min. Rp 100.000</span>
              </div>
              <div class="benefit-item fade-in-benefit" style="animation-delay: 0.2s">
                <span class="benefit-icon">✅</span>
                <span>Garansi produk segar</span>
              </div>
              <div class="benefit-item fade-in-benefit" style="animation-delay: 0.3s">
                <span class="benefit-icon">⚡</span>
                <span>Pengiriman same day</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Recommended Products -->
      <div class="recommended-section" v-if="cartItems.length > 0" data-aos="fade-up">
        <div class="section-header">
          <h3>🌟 Mungkin Anda Juga Suka</h3>
          <div class="header-line"></div>
        </div>
        <div class="recommended-grid">
          <div
            v-for="(product, index) in recommendedProducts"
            :key="product.id"
            class="recommended-item card-hover"
            :style="{ animationDelay: `${index * 0.1}s` }"
            data-aos="zoom-in"
            :data-aos-delay="index * 100"
          >
            <div class="recommended-image">
              <img :src="product.image" :alt="product.name" />
              <div class="image-hover-overlay">
                <span class="quick-view">👁️</span>
              </div>
            </div>
            <div class="recommended-info">
              <h4>{{ product.name }}</h4>
              <span class="recommended-price">Rp {{ formatPrice(product.price) }}</span>
              <button class="add-recommended gradient-btn" @click="addToCart(product)">
                <span class="btn-icon">+</span>
                Tambah
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EnhancedCartItem',
  data() {
    return {
      // Navbar data
      categories: ['Fruits', 'Vegetables', 'Groceries', 'Meat'],
      showSearch: false,
      searchQuery: '',
      activeCategory: 'Vegetables',

      // Cart data
      showPromoInput: false,
      promoCode: '',
      appliedPromo: null,
      cartItems: [
        {
          id: 1,
          name: 'Sawi Hijau Premium',
          price: 26500,
          originalPrice: 32000,
          image:
            'https://images.unsplash.com/photo-1576045057995-568f588f82fb?w=400&h=400&fit=crop',
          brand: 'FRESH DAILY',
          discount: 20,
          isNew: true,
          quantity: 2,
        },
        {
          id: 2,
          name: 'Kangkung Organik',
          price: 18500,
          originalPrice: 22000,
          image:
            'https://images.unsplash.com/photo-1515543237350-b3eea1ec8082?w=400&h=400&fit=crop',
          brand: 'ORGANIC FARM',
          discount: 15,
          quantity: 1,
        },
        {
          id: 3,
          name: 'Apel Fuji Premium',
          price: 65000,
          originalPrice: 75000,
          image: 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=400&h=400&fit=crop',
          brand: 'FRUIT DAILY',
          discount: 13,
          quantity: 3,
        },
      ],
      recommendedProducts: [
        {
          id: 101,
          name: 'Tomat Cherry',
          price: 35000,
          image:
            'https://images.unsplash.com/photo-1592841200221-21e1c4ae6766?w=400&h=400&fit=crop',
        },
        {
          id: 102,
          name: 'Timun Jepang',
          price: 25000,
          image:
            'https://images.unsplash.com/photo-1604977042946-1eecc30f269e?w=400&h=400&fit=crop',
        },
        {
          id: 103,
          name: 'Selada Romaine',
          price: 35000,
          image:
            'https://images.unsplash.com/photo-1622206151226-18ca2c9ab4a1?w=400&h=400&fit=crop',
        },
        {
          id: 104,
          name: 'Brokoli Hijau',
          price: 45000,
          image: 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=400&fit=crop',
        },
      ],
    }
  },
  computed: {
    cartItemCount() {
      return this.cartItems.reduce((total, item) => total + item.quantity, 0)
    },
    totalItems() {
      return this.cartItems.reduce((total, item) => total + item.quantity, 0)
    },
    subtotal() {
      return this.cartItems.reduce((total, item) => total + item.price * item.quantity, 0)
    },
    totalDiscount() {
      return this.cartItems.reduce((total, item) => {
        if (item.discount && item.originalPrice) {
          const discountPerItem = item.originalPrice - item.price
          return total + discountPerItem * item.quantity
        }
        return total
      }, 0)
    },
    shippingCost() {
      return this.subtotal >= 100000 ? 0 : 15000
    },
    promoDiscount() {
      if (this.appliedPromo) {
        return this.subtotal * (this.appliedPromo.percentage / 100)
      }
      return 0
    },
    finalTotal() {
      return this.subtotal - this.totalDiscount - this.promoDiscount + this.shippingCost
    },
  },
  methods: {
    // Navbar methods
    goToHome() {
      // Reset state when going home
      this.activeCategory = 'Vegetables'

      // Clear search if open
      if (this.showSearch) {
        this.showSearch = false
        this.searchQuery = ''
      }

      // Dispatch events for home navigation
      window.dispatchEvent(new CustomEvent('page-change', { detail: 'home' }))

      // For router navigation (if using Vue Router)
      // this.$router.push('/')

      console.log('Navigating to home from cart...')
    },

    navigate(destination) {
      console.log(`Navigating to ${destination}`)

      // Handle profile navigation
      if (destination === 'profile') {
        // Multiple ways to navigate to profile

        // Method 1: Using Vue Router
        if (this.$router) {
          this.$router.push('/profile')
          console.log('Navigating to profile via Vue Router...')
        }
        // Method 2: Using window.location
        else if (typeof window !== 'undefined') {
          window.location.href = '/profile'
          console.log('Navigating to profile via window.location...')
        }

        // Method 3: Emit event to parent
        this.$emit('navigate-to-profile')

        // Method 4: Dispatch custom events
        window.dispatchEvent(new CustomEvent('page-change', { detail: 'profile' }))
        window.dispatchEvent(new CustomEvent('navigate-profile'))

        return
      }

      // Handle category navigation
      const categoryMap = {
        Fruits: 'fruits',
        Vegetables: 'vegetables',
        Groceries: 'groceries',
        Meat: 'meat',
      }

      if (categoryMap[destination]) {
        this.activeCategory = destination

        // Method 1: Using Vue Router
        if (this.$router) {
          this.$router.push(`/products/${categoryMap[destination]}`)
          console.log(`Navigating to ${destination} via Vue Router...`)
        }
        // Method 2: Using window.location
        else if (typeof window !== 'undefined') {
          window.location.href = `/products/${categoryMap[destination]}`
          console.log(`Navigating to ${destination} via window.location...`)
        }

        // Method 3: Emit events to parent
        this.$emit('navigate-to-category', categoryMap[destination])

        // Method 4: Dispatch custom events
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
    },
    toggleSearch() {
      this.showSearch = !this.showSearch
      if (this.showSearch) {
        this.$nextTick(() => {
          this.$refs.searchInput?.focus()
        })
      }
    },
    performSearch() {
      if (this.searchQuery.trim()) {
        console.log(`Searching for: ${this.searchQuery}`)
        this.searchQuery = ''
        this.showSearch = false
      }
    },

    // Cart methods
    formatPrice(price) {
      return price.toLocaleString('id-ID')
    },
    updateQuantity(itemId, newQuantity) {
      if (newQuantity <= 0) return
      const item = this.cartItems.find((item) => item.id === itemId)
      if (item) {
        item.quantity = newQuantity
      }
    },
    removeItem(itemId) {
      this.cartItems = this.cartItems.filter((item) => item.id !== itemId)
    },
    clearCart() {
      if (confirm('Apakah Anda yakin ingin menghapus semua produk dari keranjang?')) {
        this.cartItems = []
      }
    },
    addToCart(product) {
      const existingItem = this.cartItems.find((item) => item.id === product.id)
      if (existingItem) {
        existingItem.quantity += 1
      } else {
        this.cartItems.push({
          ...product,
          quantity: 1,
        })
      }
    },
    applyPromo() {
      const validPromos = {
        FRESH20: { percentage: 20, name: 'Diskon Fresh 20%' },
        NEWUSER: { percentage: 15, name: 'Diskon New User 15%' },
        WEEKEND: { percentage: 10, name: 'Diskon Weekend 10%' },
      }

      if (validPromos[this.promoCode.toUpperCase()]) {
        this.appliedPromo = validPromos[this.promoCode.toUpperCase()]
        alert(`Promo ${this.appliedPromo.name} berhasil diterapkan!`)
        this.showPromoInput = false
        this.promoCode = ''
      } else {
        alert('Kode promo tidak valid!')
      }
    },
    proceedToCheckout() {
      alert('Menuju halaman pembayaran...')
    },
    goToProducts() {
      // Navigate to products page
      if (this.$router) {
        this.$router.push('/products')
        console.log('Navigating to products via Vue Router...')
      } else if (typeof window !== 'undefined') {
        window.location.href = '/products'
        console.log('Navigating to products via window.location...')
      }

      // Emit events
      this.$emit('go-to-products')
      window.dispatchEvent(new CustomEvent('page-change', { detail: 'products' }))
    },
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Satisfy&display=swap');
@import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@100..900&display=swap');

/* App wrapper */
.app-wrapper {
  min-height: 100vh;
  background: linear-gradient(135deg, #f8f9fa 0%, #e8f5e8 100%);
}

/* Navbar Styles */
.top-bar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: linear-gradient(90deg, #8bc34a, #66bb6a);
  padding: 5px 0;
  text-align: center;
  font-size: 0.85rem;
  color: #fdfff5;
  z-index: 1000;
  font-family: 'League Spartan', sans-serif;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

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
  background: rgba(253, 246, 227, 0.95);
  border-radius: 30px;
  padding: 12px 25px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(25px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.nav-brand {
  flex: 1;
  position: relative;
  z-index: 10;
}

/* Logo Text Styles (Clickable) */
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
  pointer-events: auto;
  outline: none;
}

.logo-text:hover {
  color: #27ae60;
  transform: scale(1.05);
  background-color: rgba(46, 204, 113, 0.1);
  box-shadow: 0 2px 8px rgba(46, 204, 113, 0.3);
}

.logo-text:active {
  transform: scale(0.98);
  background-color: rgba(46, 204, 113, 0.2);
}

.logo-text:focus {
  outline: 2px solid rgba(46, 204, 113, 0.5);
  outline-offset: 2px;
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
  transform: translateY(-2px);
}

.nav-categories button.active {
  background-color: #2ecc71;
  color: white;
  box-shadow: 0 4px 15px rgba(46, 204, 113, 0.3);
}

.nav-actions {
  display: flex;
  gap: 15px;
  flex: 1;
  justify-content: flex-end;
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
  transition: all 0.3s ease;
  position: relative;
}

.nav-actions button:hover {
  background-color: rgba(46, 204, 113, 0.1);
  transform: scale(1.1);
}

.cart-btn.active-cart {
  background: linear-gradient(45deg, #2ecc71, #27ae60);
  color: white;
  animation: pulse 2s infinite;
}

.cart-count {
  position: absolute;
  top: -2px;
  right: -2px;
  background-color: #e74c3c;
  color: white;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  font-size: 0.7rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  animation: bounce 1s infinite;
}

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

/* Cart Styles */
.cart-container {
  margin-top: 140px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  padding: 0 5%;
  min-height: calc(100vh - 140px);
}

/* Hero Section with Animation */
.cart-hero {
  background: linear-gradient(135deg, #2ed573 0%, #26af5f 100%);
  border-radius: 25px;
  padding: 40px;
  margin: 20px 0;
  color: white;
  text-align: center;
  position: relative;
  overflow: hidden;
  animation: slideInDown 0.8s ease-out;
}

.cart-hero::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
  animation: rotate 20s linear infinite;
}

.hero-content {
  position: relative;
  z-index: 2;
}

.cart-hero h1 {
  font-size: 2.5rem;
  margin-bottom: 15px;
  font-weight: 700;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
}

.cart-hero p {
  font-size: 1.2rem;
  opacity: 0.95;
}

.floating-leaf {
  position: absolute;
  font-size: 2rem;
  animation: float 3s ease-in-out infinite;
}

.leaf-1 {
  top: 20%;
  left: 10%;
  animation-delay: 0s;
}

.leaf-2 {
  top: 60%;
  right: 15%;
  animation-delay: 1s;
}

.leaf-3 {
  bottom: 20%;
  left: 20%;
  animation-delay: 2s;
}

/* Cart Content */
.cart-content {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 30px;
  margin: 30px 0;
}

.cart-items-section {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 20px;
  padding: 30px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.cart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 3px solid #f8f9fa;
  position: relative;
}

.cart-header::after {
  content: '';
  position: absolute;
  bottom: -3px;
  left: 0;
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #2ed573, #26af5f);
  border-radius: 3px;
}

.cart-header h2 {
  font-size: 1.8rem;
  color: #2d3436;
  margin: 0;
  font-weight: 700;
}

.clear-cart.pulse-btn {
  background: linear-gradient(45deg, #e74c3c, #c0392b);
  border: none;
  color: white;
  padding: 10px 20px;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.9rem;
  font-weight: 600;
  animation: pulse 2s infinite;
}

.clear-cart.pulse-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(231, 76, 60, 0.4);
}

/* Empty Cart */
.empty-cart {
  text-align: center;
  padding: 80px 20px;
}

.empty-icon.bounce-animation {
  font-size: 5rem;
  margin-bottom: 25px;
  animation: bounce 2s infinite;
}

.empty-cart h3 {
  font-size: 1.8rem;
  color: #2d3436;
  margin-bottom: 15px;
  font-weight: 600;
}

.empty-cart p {
  color: #636e72;
  margin-bottom: 30px;
  font-size: 1.1rem;
}

.start-shopping.gradient-btn {
  background: linear-gradient(45deg, #2ed573, #26af5f);
  color: white;
  border: none;
  padding: 15px 35px;
  border-radius: 30px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 1.1rem;
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

.start-shopping.gradient-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(46, 213, 115, 0.4);
}

/* Cart Items with Animations */
.cart-item.slide-in-item {
  display: flex;
  gap: 25px;
  padding: 25px 0;
  border-bottom: 1px solid #f1f3f4;
  transition: all 0.3s ease;
  animation: slideInLeft 0.6s ease-out forwards;
  opacity: 0;
  transform: translateX(-50px);
}

.cart-item:hover {
  background: rgba(46, 213, 115, 0.02);
  border-radius: 15px;
  padding: 25px 15px;
  transform: translateY(-2px);
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.05);
}

.item-image {
  position: relative;
  width: 140px;
  height: 140px;
  border-radius: 20px;
  overflow: hidden;
  flex-shrink: 0;
}

.item-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.item-image:hover img {
  transform: scale(1.1);
}

.image-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, rgba(46, 213, 115, 0.1), rgba(38, 175, 95, 0.1));
  opacity: 0;
  transition: opacity 0.3s ease;
}

.item-image:hover .image-overlay {
  opacity: 1;
}

.item-badges {
  position: absolute;
  top: 10px;
  left: 10px;
  display: flex;
  gap: 5px;
}

.badge {
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

.badge.discount.glow-effect {
  background: linear-gradient(45deg, #ff4757, #ff3742);
  color: white;
  animation: glow 2s ease-in-out infinite alternate;
}

.badge.new.pulse-effect {
  background: linear-gradient(45deg, #2ed573, #26af5f);
  color: white;
  animation: pulse 1.5s infinite;
}

.item-details {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.item-brand {
  font-size: 0.85rem;
  color: #74b9ff;
  text-transform: uppercase;
  font-weight: 700;
  margin-bottom: 8px;
  letter-spacing: 0.5px;
}

.item-name {
  font-size: 1.2rem;
  font-weight: 600;
  color: #2d3436;
  margin-bottom: 12px;
  line-height: 1.4;
}

.current-price {
  font-size: 1.3rem;
  font-weight: 700;
  color: #2ed573;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.original-price {
  font-size: 1rem;
  color: #95a5a6;
  text-decoration: line-through;
  margin-left: 10px;
}

.item-actions {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 20px;
}

.quantity-controls.modern-controls {
  display: flex;
  align-items: center;
  background: linear-gradient(45deg, #f8f9fa, #e9ecef);
  border-radius: 15px;
  padding: 8px;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);
}

.qty-btn.hover-effect {
  width: 35px;
  height: 35px;
  border: none;
  background: white;
  border-radius: 10px;
  cursor: pointer;
  font-size: 1.3rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.qty-btn.hover-effect:hover:not(:disabled) {
  background: linear-gradient(45deg, #2ed573, #26af5f);
  color: white;
  transform: scale(1.1);
  box-shadow: 0 4px 10px rgba(46, 213, 115, 0.3);
}

.qty-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.quantity {
  padding: 0 20px;
  font-weight: 700;
  font-size: 1.1rem;
  min-width: 50px;
  text-align: center;
  color: #2d3436;
}

.total-price {
  font-size: 1.4rem;
  font-weight: 700;
  color: #2d3436;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.remove-item.hover-scale {
  background: linear-gradient(45deg, #ff4757, #ff3742);
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 12px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(255, 71, 87, 0.3);
}

.remove-item.hover-scale:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 15px rgba(255, 71, 87, 0.5);
}

.remove-icon {
  color: white;
  font-size: 1.1rem;
}

/* Cart Summary Enhanced */
.cart-summary.sticky-summary {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 25px;
  padding: 30px;
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.1);
  height: fit-content;
  position: sticky;
  top: 170px;
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.summary-card.glass-effect {
  position: relative;
}

.summary-header {
  position: relative;
  text-align: center;
  margin-bottom: 25px;
}

.summary-header h3 {
  font-size: 1.5rem;
  color: #2d3436;
  font-weight: 700;
  margin: 0;
}

.sparkle {
  position: absolute;
  font-size: 1.2rem;
  animation: sparkle 2s ease-in-out infinite;
}

.sparkle-1 {
  top: -5px;
  right: 20px;
  animation-delay: 0s;
}

.sparkle-2 {
  top: -5px;
  left: 20px;
  animation-delay: 1s;
}

.summary-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  font-size: 1rem;
  transition: all 0.3s ease;
}

.summary-row:hover {
  background: rgba(46, 213, 115, 0.05);
  border-radius: 8px;
  padding: 12px 10px;
}

.amount-animation {
  animation: countUp 0.5s ease-out;
}

.discount-amount {
  color: #e74c3c;
  font-weight: 700;
}

.shipping-cost {
  color: #2ed573;
  font-weight: 700;
}

.summary-divider.animated-divider {
  border: none;
  height: 2px;
  background: linear-gradient(90deg, #2ed573, #26af5f);
  margin: 20px 0;
  border-radius: 2px;
  animation: shimmer 2s ease-in-out infinite;
}

.total-row {
  font-size: 1.3rem;
  font-weight: 700;
  color: #2d3436;
  padding: 20px 0 15px 0;
  border-top: 1px solid #f1f3f4;
}

.total-amount.scale-in {
  color: #2ed573;
  animation: scaleIn 0.5s ease-out;
}

/* Promo Section Enhanced */
.promo-section {
  margin: 25px 0;
}

.promo-input {
  display: flex;
  gap: 12px;
  align-items: center;
  transition: all 0.3s ease;
}

.promo-input.expanded {
  background: linear-gradient(45deg, #f8f9fa, #e9ecef);
  border-radius: 15px;
  padding: 15px;
  box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.1);
}

.promo-input-field {
  flex: 1;
  border: none;
  background: white;
  outline: none;
  font-size: 1rem;
  padding: 10px 15px;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.promo-toggle.gradient-border {
  background: white;
  border: 2px solid transparent;
  background-clip: padding-box;
  color: #2ed573;
  padding: 12px 20px;
  border-radius: 15px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 600;
  width: 100%;
  transition: all 0.3s ease;
  position: relative;
}

.promo-toggle.gradient-border::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, #2ed573, #26af5f);
  border-radius: 15px;
  z-index: -1;
  padding: 2px;
  background-clip: border-box;
}

.promo-toggle.gradient-border:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(46, 213, 115, 0.3);
}

.apply-promo.gradient-btn {
  background: linear-gradient(45deg, #2ed573, #26af5f);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 10px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}

.apply-promo.gradient-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(46, 213, 115, 0.4);
}

.apply-promo.gradient-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Checkout Button Enhanced */
.checkout-btn.mega-gradient {
  width: 100%;
  background: linear-gradient(45deg, #2ed573, #26af5f, #2ed573);
  background-size: 200% 200%;
  color: white;
  border: none;
  padding: 18px 25px;
  border-radius: 20px;
  font-size: 1.2rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin: 25px 0;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  animation: gradientShift 3s ease-in-out infinite;
}

.checkout-btn.mega-gradient:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(46, 213, 115, 0.4);
}

.checkout-icon {
  font-size: 1.3rem;
}

.btn-ripple {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
  transform: translate(-50%, -50%);
  transition:
    width 0.6s,
    height 0.6s;
}

.checkout-btn:active .btn-ripple {
  width: 200px;
  height: 200px;
}

/* Benefits */
.cart-benefits {
  margin-top: 25px;
  padding-top: 25px;
  border-top: 1px solid #f1f3f4;
}

.benefit-item.fade-in-benefit {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 0;
  font-size: 0.95rem;
  color: #636e72;
  animation: fadeInUp 0.6s ease-out forwards;
  opacity: 0;
  transform: translateY(20px);
}

.benefit-icon {
  font-size: 1.2rem;
}

/* Recommended Products Enhanced */
.recommended-section {
  margin: 50px 0;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 25px;
  padding: 35px;
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
}

.section-header {
  text-align: center;
  margin-bottom: 30px;
  position: relative;
}

.section-header h3 {
  font-size: 1.8rem;
  color: #2d3436;
  font-weight: 700;
  margin-bottom: 15px;
}

.header-line {
  width: 80px;
  height: 4px;
  background: linear-gradient(90deg, #2ed573, #26af5f);
  margin: 0 auto;
  border-radius: 2px;
}

.recommended-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 25px;
}

.recommended-item.card-hover {
  background: white;
  border-radius: 20px;
  padding: 20px;
  text-align: center;
  transition: all 0.4s ease;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(46, 213, 115, 0.1);
  position: relative;
  overflow: hidden;
}

.recommended-item.card-hover::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(46, 213, 115, 0.1), transparent);
  transition: left 0.5s ease;
}

.recommended-item.card-hover:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(46, 213, 115, 0.2);
}

.recommended-item.card-hover:hover::before {
  left: 100%;
}

.recommended-image {
  position: relative;
  margin-bottom: 15px;
  border-radius: 15px;
  overflow: hidden;
}

.recommended-image img {
  width: 100%;
  height: 140px;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.image-hover-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(46, 213, 115, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.recommended-image:hover .image-hover-overlay {
  opacity: 1;
}

.recommended-image:hover img {
  transform: scale(1.1);
}

.quick-view {
  color: white;
  font-size: 1.5rem;
}

.recommended-info h4 {
  font-size: 1rem;
  color: #2d3436;
  margin-bottom: 8px;
  font-weight: 600;
}

.recommended-price {
  font-size: 1.1rem;
  font-weight: 700;
  color: #2ed573;
  display: block;
  margin-bottom: 15px;
}

.add-recommended.gradient-btn {
  background: linear-gradient(45deg, #2ed573, #26af5f);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 12px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 600;
  transition: all 0.3s ease;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

.add-recommended.gradient-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(46, 213, 115, 0.4);
}

.btn-icon {
  font-size: 1rem;
  font-weight: bold;
}

/* Keyframe Animations */
@keyframes slideInDown {
  from {
    opacity: 0;
    transform: translateY(-100px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInLeft {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}

@keyframes bounce {
  0%,
  20%,
  53%,
  80%,
  100% {
    transform: translateY(0);
  }
  40%,
  43% {
    transform: translateY(-15px);
  }
  70% {
    transform: translateY(-7px);
  }
  90% {
    transform: translateY(-3px);
  }
}

@keyframes glow {
  from {
    box-shadow: 0 0 5px rgba(255, 71, 87, 0.5);
  }
  to {
    box-shadow: 0 0 20px rgba(255, 71, 87, 0.8);
  }
}

@keyframes sparkle {
  0%,
  100% {
    opacity: 0;
    transform: scale(0.5);
  }
  50% {
    opacity: 1;
    transform: scale(1.2);
  }
}

@keyframes shimmer {
  0% {
    background-position: -200% 0;
  }
  100% {
    background-position: 200% 0;
  }
}

@keyframes scaleIn {
  from {
    transform: scale(0.5);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

@keyframes countUp {
  from {
    transform: translateY(-10px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes gradientShift {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Responsive Design */
@media (max-width: 1024px) {
  .cart-content {
    grid-template-columns: 1fr;
    gap: 25px;
  }

  .cart-summary.sticky-summary {
    position: static;
  }
}

@media (max-width: 768px) {
  .floating-navbar {
    top: 35px;
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

  .cart-container {
    padding: 0 3%;
    margin-top: 120px;
  }

  .cart-hero {
    padding: 25px;
  }

  .cart-hero h1 {
    font-size: 2rem;
  }

  .cart-items-section,
  .cart-summary {
    padding: 20px;
  }

  .cart-item {
    flex-direction: column;
    gap: 20px;
  }

  .item-image {
    width: 120px;
    height: 120px;
    align-self: center;
  }

  .item-details {
    flex-direction: column;
    gap: 20px;
  }

  .item-actions {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }

  .recommended-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
  }
}

@media (max-width: 480px) {
  .nav-brand {
    display: flex;
    align-items: center;
  }

  .logo-text {
    font-size: 1.1rem;
  }

  .recommended-grid {
    grid-template-columns: 1fr;
  }

  .cart-hero h1 {
    font-size: 1.6rem;
  }
}
</style>
