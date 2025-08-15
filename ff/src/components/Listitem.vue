<template>
  <div class="marketplace-container">
    <!-- Compact Hero Section -->
    <div
      class="hero-section"
      :style="{
        background: currentData.hero.gradient,
        backgroundSize: '300% 300%',
        boxShadow: `0 8px 32px ${currentData.hero.shadowColor}`,
      }"
    >
      <div class="hero-content">
        <div class="hero-text">
          <h1 :key="activeCategory">{{ currentData.hero.title }}</h1>
          <p>{{ currentData.hero.description }}</p>
        </div>
        <div class="hero-stats">
          <div class="stat-item" v-for="(stat, index) in currentData.hero.stats" :key="index">
            <span class="stat-number" :style="{ color: currentData.hero.glowColor }">{{
              stat.number
            }}</span>
            <span class="stat-label">{{ stat.label }}</span>
          </div>
        </div>
      </div>

      <!-- Floating animated icons -->
      <div class="floating-icons">
        <div class="floating-icon icon-1" v-if="activeCategory === 'vegetables'">🥕</div>
        <div class="floating-icon icon-2" v-if="activeCategory === 'vegetables'">🥬</div>
        <div class="floating-icon icon-3" v-if="activeCategory === 'vegetables'">🍅</div>
        <div class="floating-icon icon-4" v-if="activeCategory === 'vegetables'">🥒</div>
        <div class="floating-icon icon-5" v-if="activeCategory === 'vegetables'">🌽</div>
        <div class="floating-icon icon-6" v-if="activeCategory === 'vegetables'">🥦</div>

        <div class="floating-icon icon-1" v-if="activeCategory === 'fruits'">🍎</div>
        <div class="floating-icon icon-2" v-if="activeCategory === 'fruits'">🍊</div>
        <div class="floating-icon icon-3" v-if="activeCategory === 'fruits'">🍌</div>
        <div class="floating-icon icon-4" v-if="activeCategory === 'fruits'">🍇</div>
        <div class="floating-icon icon-5" v-if="activeCategory === 'fruits'">🥭</div>
        <div class="floating-icon icon-6" v-if="activeCategory === 'fruits'">🍓</div>

        <div class="floating-icon icon-1" v-if="activeCategory === 'groceries'">🛒</div>
        <div class="floating-icon icon-2" v-if="activeCategory === 'groceries'">🏪</div>
        <div class="floating-icon icon-3" v-if="activeCategory === 'groceries'">📦</div>
        <div class="floating-icon icon-4" v-if="activeCategory === 'groceries'">🥫</div>
        <div class="floating-icon icon-5" v-if="activeCategory === 'groceries'">🧴</div>
        <div class="floating-icon icon-6" v-if="activeCategory === 'groceries'">🧽</div>

        <div class="floating-icon icon-1" v-if="activeCategory === 'meat'">🥩</div>
        <div class="floating-icon icon-2" v-if="activeCategory === 'meat'">🍗</div>
        <div class="floating-icon icon-3" v-if="activeCategory === 'meat'">🐟</div>
        <div class="floating-icon icon-4" v-if="activeCategory === 'meat'">🦐</div>
        <div class="floating-icon icon-5" v-if="activeCategory === 'meat'">🥓</div>
        <div class="floating-icon icon-6" v-if="activeCategory === 'meat'">🐄</div>
      </div>
    </div>

    <!-- Products Section -->
    <div class="products-section">
      <!-- Dynamic Sections -->
      <div
        v-for="(section, sectionIndex) in currentData.sections"
        :key="sectionIndex"
        class="section-wrapper"
      >
        <div class="section-header">
          <div class="section-title">
            <span class="trend-icon">{{ section.icon }}</span>
            <h2>{{ section.title }}</h2>
            <span class="dynamic-badge" :style="{ background: section.badgeColor }">{{
              section.badge
            }}</span>
          </div>
          <button class="view-all-btn">
            Lihat Semua
            <i class="arrow">→</i>
          </button>
        </div>

        <div class="products-grid" v-if="section.products.length > 0">
          <ProductCard
            v-for="product in section.products"
            :key="product.id"
            :product="product"
            @add-to-cart="handleAddToCart"
          />
        </div>

        <!-- Coming Soon untuk kategori yang belum ada data -->
        <div v-else class="coming-soon">
          <div class="coming-soon-content">
            <h3>🚧 Segera Hadir!</h3>
            <p>Produk {{ section.title.toLowerCase() }} akan segera tersedia. Stay tuned!</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProductCard from './ProductCard.vue'

export default {
  name: 'ListItem',
  components: {
    ProductCard,
  },
  data() {
    return {
      activeCategory: 'vegetables', // Default kategori
      categories: {
        fruits: {
          hero: {
            title: 'Buah Segar, Hidup Manis! 🍎',
            description: 'Nikmati buah-buahan segar pilihan terbaik langsung dari kebun',
            stats: [
              { number: '500+', label: 'Buah Fresh' },
              { number: '24/7', label: 'Delivery' },
              { number: '100%', label: 'Natural' },
            ],
            gradient:
              'linear-gradient(135deg, #ff6b6b 0%, #ee5a24 25%, #c0392b 50%, #ee5a24 75%, #ff6b6b 100%)',
            shadowColor: 'rgba(255, 107, 107, 0.3)',
            glowColor: '#ffb3ba',
          },
          sections: [
            {
              icon: '🔥',
              title: 'Buah Trending',
              badge: 'HOT',
              badgeColor: 'linear-gradient(45deg, #ff6b6b, #ee5a24)',
              products: [
                {
                  id: 101,
                  name: 'Apel Fuji Premium',
                  price: 65000,
                  originalPrice: 75000,
                  image:
                    'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=400&h=400&fit=crop',
                  brand: 'FRUIT DAILY',
                  discount: 13,
                  isNew: true,
                  rating: 4.9,
                  sold: 234,
                },
                {
                  id: 102,
                  name: 'Jeruk Manis Lokal',
                  price: 35000,
                  originalPrice: 42000,
                  image:
                    'https://images.unsplash.com/photo-1547514701-42782101795e?w=400&h=400&fit=crop',
                  brand: 'FRESH FRUITS',
                  discount: 17,
                  rating: 4.7,
                  sold: 189,
                },
                {
                  id: 103,
                  name: 'Pisang Cavendish',
                  price: 25000,
                  image:
                    'https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=400&h=400&fit=crop',
                  brand: 'TROPICAL FRESH',
                  isNew: true,
                  rating: 4.8,
                  sold: 156,
                },
                {
                  id: 104,
                  name: 'Anggur Hijau Import',
                  price: 95000,
                  image:
                    'https://images.unsplash.com/photo-1537640538966-79f369143f8f?w=400&h=400&fit=crop',
                  brand: 'PREMIUM FRUITS',
                  rating: 4.9,
                  sold: 78,
                },
                {
                  id: 105,
                  name: 'Mangga Harum Manis',
                  price: 45000,
                  originalPrice: 52000,
                  image:
                    'https://images.unsplash.com/photo-1553279768-865429fa0078?w=400&h=400&fit=crop',
                  brand: 'TROPICAL FRESH',
                  discount: 13,
                  rating: 4.6,
                  sold: 167,
                },
                {
                  id: 106,
                  name: 'Strawberry Premium',
                  price: 85000,
                  image:
                    'https://images.unsplash.com/photo-1464965911861-746a04b4bca6?w=400&h=400&fit=crop',
                  brand: 'PREMIUM FRUITS',
                  isNew: true,
                  rating: 5.0,
                  sold: 89,
                },
              ],
            },
            {
              icon: '🌟',
              title: 'Buah Segar Hari Ini',
              badge: 'FRESH',
              badgeColor: 'linear-gradient(45deg, #ffd700, #ff8c00)',
              products: [
                {
                  id: 107,
                  name: 'Nanas Madu Sweet',
                  price: 32000,
                  image:
                    'https://images.unsplash.com/photo-1550258987-190a2d41a8ba?w=400&h=400&fit=crop',
                  brand: 'TROPICAL FRESH',
                  rating: 4.7,
                  sold: 123,
                },
                {
                  id: 108,
                  name: 'Semangka Merah',
                  price: 28000,
                  originalPrice: 35000,
                  image:
                    'https://images.unsplash.com/photo-1571068316344-75bc76f77890?w=400&h=400&fit=crop',
                  brand: 'FRESH FRUITS',
                  discount: 20,
                  rating: 4.5,
                  sold: 145,
                },
                {
                  id: 109,
                  name: 'Kiwi Import',
                  price: 75000,
                  image:
                    'https://images.unsplash.com/photo-1612528443702-f6741f70a049?w=400&h=400&fit=crop',
                  brand: 'PREMIUM FRUITS',
                  isNew: true,
                  rating: 4.8,
                  sold: 67,
                },
                {
                  id: 110,
                  name: 'Pepaya California',
                  price: 22000,
                  image:
                    'https://images.unsplash.com/photo-1571068316344-75bc76f77890?w=400&h=400&fit=crop',
                  brand: 'TROPICAL FRESH',
                  rating: 4.4,
                  sold: 234,
                },
                {
                  id: 111,
                  name: 'Alpukat Mentega',
                  price: 38000,
                  originalPrice: 45000,
                  image:
                    'https://images.unsplash.com/photo-1583240915511-c2c89f2fb38d?w=400&h=400&fit=crop',
                  brand: 'FRESH FRUITS',
                  discount: 16,
                  rating: 4.9,
                  sold: 198,
                },
                {
                  id: 112,
                  name: 'Blueberry Fresh',
                  price: 125000,
                  image:
                    'https://images.unsplash.com/photo-1498557850523-fd3d118b962e?w=400&h=400&fit=crop',
                  brand: 'PREMIUM FRUITS',
                  rating: 4.8,
                  sold: 45,
                },
              ],
            },
          ],
        },
        vegetables: {
          hero: {
            title: 'Belanja Fresh, Hidup Sehat! 🥬',
            description: 'Dapatkan sayuran segar langsung dari kebun dengan kualitas terbaik',
            stats: [
              { number: '1000+', label: 'Produk Fresh' },
              { number: '24/7', label: 'Delivery' },
              { number: '100%', label: 'Organic' },
            ],
            gradient:
              'linear-gradient(135deg, #2ed573 0%, #26af5f 25%, #1e7e34 50%, #26af5f 75%, #2ed573 100%)',
            shadowColor: 'rgba(46, 213, 115, 0.3)',
            glowColor: '#a8f5d1',
          },
          sections: [
            {
              icon: '🔥',
              title: 'Trending Sekarang',
              badge: 'HOT',
              badgeColor: 'linear-gradient(45deg, #ff6b6b, #ee5a24)',
              products: [
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
                  rating: 4.8,
                  sold: 150,
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
                  rating: 4.7,
                  sold: 89,
                },
                {
                  id: 3,
                  name: 'Bayam Merah Fresh',
                  price: 24000,
                  image:
                    'https://images.unsplash.com/photo-1576045057995-568f588f82fb?w=400&h=400&fit=crop',
                  brand: 'FRESH DAILY',
                  isNew: true,
                  rating: 4.9,
                  sold: 67,
                },
                {
                  id: 4,
                  name: 'Selada Romaine',
                  price: 35000,
                  image:
                    'https://images.unsplash.com/photo-1622206151226-18ca2c9ab4a1?w=400&h=400&fit=crop',
                  brand: 'PREMIUM GREENS',
                  rating: 4.6,
                  sold: 123,
                },
                {
                  id: 5,
                  name: 'Pak Choy Segar',
                  price: 22000,
                  image:
                    'https://images.unsplash.com/photo-1576045057995-568f588f82fb?w=400&h=400&fit=crop',
                  brand: 'FRESH DAILY',
                  rating: 4.5,
                  sold: 95,
                },
                {
                  id: 6,
                  name: 'Pakcoy Baby',
                  price: 28000,
                  originalPrice: 31000,
                  image:
                    'https://images.unsplash.com/photo-1515543237350-b3eea1ec8082?w=400&h=400&fit=crop',
                  brand: 'ORGANIC FARM',
                  discount: 10,
                  rating: 4.7,
                  sold: 78,
                },
              ],
            },
            {
              icon: '🌱',
              title: 'Sayuran Segar Hari Ini',
              badge: 'FRESH',
              badgeColor: 'linear-gradient(45deg, #2ed573, #26af5f)',
              products: [
                {
                  id: 7,
                  name: 'Brokoli Hijau',
                  price: 45000,
                  originalPrice: 50000,
                  image:
                    'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400&h=400&fit=crop',
                  brand: 'FRESH DAILY',
                  discount: 10,
                  rating: 4.8,
                  sold: 45,
                },
                {
                  id: 8,
                  name: 'Wortel Baby',
                  price: 28000,
                  image:
                    'https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?w=400&h=400&fit=crop',
                  brand: 'ORGANIC FARM',
                  rating: 4.7,
                  sold: 78,
                },
                {
                  id: 9,
                  name: 'Kubis Ungu',
                  price: 32000,
                  image:
                    'https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=400&h=400&fit=crop',
                  brand: 'FRESH DAILY',
                  isNew: true,
                  rating: 4.9,
                  sold: 34,
                },
                {
                  id: 10,
                  name: 'Timun Jepang',
                  price: 25000,
                  image:
                    'https://images.unsplash.com/photo-1604977042946-1eecc30f269e?w=400&h=400&fit=crop',
                  brand: 'PREMIUM GREENS',
                  rating: 4.5,
                  sold: 56,
                },
                {
                  id: 11,
                  name: 'Kol Putih Segar',
                  price: 18000,
                  image:
                    'https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=400&h=400&fit=crop',
                  brand: 'FRESH DAILY',
                  rating: 4.6,
                  sold: 89,
                },
                {
                  id: 12,
                  name: 'Tomat Cherry',
                  price: 35000,
                  originalPrice: 40000,
                  image:
                    'https://images.unsplash.com/photo-1592841200221-21e1c4ae6766?w=400&h=400&fit=crop',
                  brand: 'PREMIUM GREENS',
                  discount: 12,
                  rating: 4.8,
                  sold: 67,
                },
              ],
            },
          ],
        },
        groceries: {
          hero: {
            title: 'Belanja Kebutuhan, Hidup Praktis! 🛒',
            description: 'Lengkapi kebutuhan dapur dengan produk berkualitas',
            stats: [
              { number: '2000+', label: 'Produk Lengkap' },
              { number: '24/7', label: 'Delivery' },
              { number: '100%', label: 'Trusted' },
            ],
            gradient:
              'linear-gradient(135deg, #74b9ff 0%, #0984e3 25%, #2d3436 50%, #0984e3 75%, #74b9ff 100%)',
            shadowColor: 'rgba(116, 185, 255, 0.3)',
            glowColor: '#a8d8ff',
          },
          sections: [
            {
              icon: '🛍️',
              title: 'Kebutuhan Pokok',
              badge: 'DAILY',
              badgeColor: 'linear-gradient(45deg, #74b9ff, #0984e3)',
              products: [],
            },
          ],
        },
        meat: {
          hero: {
            title: 'Daging Segar, Protein Terbaik! 🥩',
            description: 'Pilihan daging segar berkualitas tinggi untuk hidangan terbaik!',
            stats: [
              { number: '300+', label: 'Daging Fresh' },
              { number: '24/7', label: 'Delivery' },
              { number: '100%', label: 'Halal' },
            ],
            gradient:
              'linear-gradient(135deg, #e17055 0%, #d63031 25%, #74323f 50%, #d63031 75%, #e17055 100%)',
            shadowColor: 'rgba(225, 112, 85, 0.3)',
            glowColor: '#ffb3a8',
          },
          sections: [
            {
              icon: '🥩',
              title: 'Daging Premium',
              badge: 'HALAL',
              badgeColor: 'linear-gradient(45deg, #e17055, #d63031)',
              products: [],
            },
          ],
        },
      },
    }
  },
  computed: {
    currentData() {
      return this.categories[this.activeCategory]
    },

    // Check login status sederhana
    isLoggedIn() {
      return !!localStorage.getItem('token')
    },
  },
  methods: {
    // Method sederhana untuk handle add to cart
    handleAddToCart(product) {
      console.log('=== SIMPLE DEBUG ===')
      console.log('Add to cart clicked for:', product.name)
      console.log('Is logged in:', this.isLoggedIn)

      if (this.isLoggedIn) {
        console.log('User logged in, adding to cart...')
        this.addToCart(product)
      } else {
        console.log('User not logged in, showing modal...')
        this.triggerLoginModal(product)
      }
    },

    addToCart(product) {
      console.log('Adding to cart:', product)
      alert(`✅ ${product.name} berhasil ditambahkan ke keranjang!`)
    },

    triggerLoginModal(product) {
      console.log('Triggering login modal for:', product.name)

      // Method 1: Langsung set showLoginModal jika bisa akses
      if (window.showLoginModal) {
        console.log('Using window.showLoginModal')
        window.showLoginModal()
        return
      }

      // Method 2: Emit custom event
      console.log('Using custom event')
      window.dispatchEvent(
        new CustomEvent('show-login-modal', {
          detail: { product },
        }),
      )

      // Method 3: Manual DOM manipulation
      setTimeout(() => {
        const modal = document.querySelector('.modal-overlay')
        if (modal) {
          console.log('Found modal, showing manually')
          modal.style.display = 'flex'
          modal.style.opacity = '1'
          modal.style.visibility = 'visible'
          document.body.style.overflow = 'hidden'
        } else {
          console.log('Modal not found in DOM')
          alert('Silakan login terlebih dahulu!')
        }
      }, 100)
    },

    changeCategory(category) {
      this.activeCategory = category
      this.$nextTick(() => {
        window.scrollTo({ top: 0, behavior: 'smooth' })
      })
    },
  },
  mounted() {
    window.addEventListener('category-change', (event) => {
      this.changeCategory(event.detail)
    })
  },
}
</script>

<style scoped>
.marketplace-container {
  min-height: 100vh;
  background: transparent;
  margin-top: 125px;
  max-width: 1200px; /* Sejajar dengan navbar max-width */
  margin-left: auto;
  margin-right: auto;
  padding: 0 5%; /* Padding sesuai navbar width 90% */
}

/* Compact Hero Section */
.hero-section {
  padding: 30px 0;
  background: linear-gradient(135deg, #2ed573 0%, #26af5f 50%, #1e7e34 100%);
  color: white;
  border-radius: 25px;
  margin: 20px 0;
  box-shadow: 0 8px 32px rgba(46, 213, 115, 0.3);
  position: relative;
  overflow: hidden;
  animation: slideInDown 0.8s ease-out;
}

/* Background floating elements */
.hero-section::before {
  content: '';
  position: absolute;
  top: -50%;
  right: -10%;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.15) 0%, transparent 70%);
  border-radius: 50%;
  animation: float 6s ease-in-out infinite;
}

.hero-section::after {
  content: '';
  position: absolute;
  bottom: -30%;
  left: -5%;
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
  border-radius: 50%;
  animation: float 8s ease-in-out infinite reverse;
}

/* Animated gradient background */
.hero-section {
  background: linear-gradient(
    135deg,
    #2ed573 0%,
    #26af5f 25%,
    #1e7e34 50%,
    #26af5f 75%,
    #2ed573 100%
  );
  background-size: 300% 300%;
  animation:
    slideInDown 0.8s ease-out,
    gradientShift 12s ease-in-out infinite 1s;
}

@keyframes slideInDown {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes float {
  0%,
  100% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(10deg);
  }
}

@keyframes gradientShift {
  0%,
  100% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
}

.hero-content {
  max-width: 100%;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 40px;
  padding: 0 40px; /* Padding dalam hero */
  position: relative;
  z-index: 2;
}

.hero-text {
  flex: 2;
}

.hero-text h1 {
  font-size: 2.2rem;
  font-weight: 700;
  margin-bottom: 15px;
  line-height: 1.2;
  animation:
    fadeInLeft 1s ease-out 0.3s both,
    textGlow 4s ease-in-out infinite 2s;
}

.hero-text p {
  font-size: 1rem;
  margin-bottom: 0;
  opacity: 0.9;
  line-height: 1.5;
  animation:
    fadeInLeft 1s ease-out 0.5s both,
    subtleFloat 6s ease-in-out infinite 3s;
}

@keyframes fadeInLeft {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 0.9;
    transform: translateX(0);
  }
}

@keyframes textGlow {
  0%,
  100% {
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
  }
  50% {
    text-shadow:
      0 0 20px rgba(255, 255, 255, 0.8),
      0 0 30px rgba(168, 245, 209, 0.6);
  }
}

@keyframes subtleFloat {
  0%,
  100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-3px);
  }
}

.hero-stats {
  display: flex;
  gap: 30px;
  flex: 1;
  justify-content: flex-end;
  animation: fadeInRight 1s ease-out 0.7s both;
}

.stat-item {
  text-align: center;
  animation: scaleIn 0.6s ease-out both;
}

.stat-item:nth-child(1) {
  animation-delay: 0.9s;
}
.stat-item:nth-child(2) {
  animation-delay: 1.1s;
}
.stat-item:nth-child(3) {
  animation-delay: 1.3s;
}

@keyframes fadeInRight {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.stat-number {
  display: block;
  font-size: 1.8rem;
  font-weight: 700;
  color: #a8f5d1; /* Hijau terang yang match */
  animation:
    pulse 2s ease-in-out infinite,
    countUp 3s ease-out 2s;
}

.stat-label {
  font-size: 0.8rem;
  opacity: 0.8;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  animation: fadeGlow 3s ease-in-out infinite;
}

@keyframes pulse {
  0%,
  100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

@keyframes countUp {
  0% {
    transform: rotateY(180deg);
    opacity: 0;
  }
  50% {
    transform: rotateY(90deg);
    opacity: 0.5;
  }
  100% {
    transform: rotateY(0deg);
    opacity: 1;
  }
}

@keyframes fadeGlow {
  0%,
  100% {
    opacity: 0.8;
  }
  50% {
    opacity: 1;
    text-shadow: 0 0 10px rgba(168, 245, 209, 0.7);
  }
}

/* Floating Icons */
.floating-icons {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 1;
}

.floating-icon {
  position: absolute;
  font-size: 1.5rem;
  opacity: 0.6;
  animation: floatAround 15s linear infinite;
}

.icon-1 {
  top: 20%;
  left: 10%;
  animation-delay: 0s;
  animation-duration: 12s;
}

.icon-2 {
  top: 60%;
  left: 15%;
  animation-delay: -2s;
  animation-duration: 18s;
}

.icon-3 {
  top: 30%;
  right: 20%;
  animation-delay: -4s;
  animation-duration: 14s;
}

.icon-4 {
  bottom: 40%;
  right: 10%;
  animation-delay: -6s;
  animation-duration: 16s;
}

.icon-5 {
  top: 10%;
  left: 50%;
  animation-delay: -8s;
  animation-duration: 20s;
}

.icon-6 {
  bottom: 20%;
  left: 60%;
  animation-delay: -10s;
  animation-duration: 13s;
}

@keyframes floatAround {
  0% {
    transform: translate(0, 0) rotate(0deg);
  }
  25% {
    transform: translate(30px, -20px) rotate(90deg);
  }
  50% {
    transform: translate(-20px, -40px) rotate(180deg);
  }
  75% {
    transform: translate(-40px, 20px) rotate(270deg);
  }
  100% {
    transform: translate(0, 0) rotate(360deg);
  }
}

.stat-label {
  font-size: 0.8rem;
  opacity: 0.8;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Products Section */
.products-section {
  padding: 40px 0;
  max-width: 100%;
  margin: 0 auto;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 40px;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 15px;
}

.trend-icon {
  font-size: 2rem;
}

.section-title h2 {
  font-size: 2.2rem;
  font-weight: 700;
  color: #2d3436;
  margin: 0;
}

.trend-badge,
.fresh-badge,
.premium-badge {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.trend-badge {
  background: linear-gradient(45deg, #ff6b6b, #ee5a24);
  color: white;
}

.fresh-badge {
  background: linear-gradient(45deg, #2ed573, #26af5f);
  color: white;
}

.premium-badge {
  background: linear-gradient(45deg, #ffd700, #ff8c00);
  color: white;
}

.view-all-btn {
  background: #2ed573;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 25px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.view-all-btn:hover {
  background: #26af5f;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(46, 213, 115, 0.3);
}

.arrow {
  transition: transform 0.3s ease;
}

.view-all-btn:hover .arrow {
  transform: translateX(5px);
}

/* Products Grid */
.products-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr); /* Paksa 6 kolom */
  gap: 15px;
  margin-bottom: 60px;
  width: 100%;
}

/* Responsive Design */
@media (max-width: 1024px) {
  .hero-content {
    flex-direction: column;
    text-align: center;
    gap: 20px;
  }

  .hero-stats {
    justify-content: center;
  }

  .hero-text h1 {
    font-size: 1.8rem;
  }

  .products-grid {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 18px;
  }

  .products-section {
    padding: 30px 30px;
  }

  .hero-section {
    margin: 20px 30px;
    padding: 25px 30px;
  }
}

@media (max-width: 768px) {
  .hero-section {
    padding: 20px 20px;
    margin: 15px 20px;
  }

  .hero-text h1 {
    font-size: 1.6rem;
  }

  .hero-stats {
    gap: 20px;
  }

  .stat-number {
    font-size: 1.5rem;
  }

  .products-grid {
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 15px;
  }

  .section-header {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }

  .products-section {
    padding: 30px 20px;
  }
}

@media (max-width: 480px) {
  .products-grid {
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 12px;
  }

  .section-title h2 {
    font-size: 1.6rem;
  }

  .hero-stats {
    flex-direction: column;
    gap: 15px;
  }
}
</style>
