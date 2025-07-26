<template>
  <div class="product-card">
    <div class="product-image">
      <img :src="product.image" :alt="product.name" loading="lazy" />

      <!-- Badges -->
      <div class="badges" v-if="product.discount || product.isNew">
        <span class="badge discount" v-if="product.discount"> -{{ product.discount }}% </span>
        <span class="badge new" v-if="product.isNew"> NEW </span>
      </div>

      <!-- Quick Actions -->
      <div class="quick-actions">
        <button class="quick-btn wishlist" @click="toggleWishlist">
          <i class="heart" :class="{ filled: isWishlisted }">♡</i>
        </button>
        <button class="quick-btn preview" @click="quickPreview">
          <i class="eye">👁</i>
        </button>
      </div>

      <!-- Rating & Sold -->
      <div class="product-stats" v-if="product.rating || product.sold">
        <div class="rating" v-if="product.rating">
          <span class="stars">★</span>
          <span class="rating-value">{{ product.rating }}</span>
        </div>
        <div class="sold" v-if="product.sold">{{ product.sold }} terjual</div>
      </div>
    </div>

    <div class="product-details">
      <!-- Brand -->
      <div class="product-brand" v-if="product.brand">{{ product.brand }}</div>

      <!-- Name -->
      <h3 class="product-name">{{ product.name }}</h3>

      <!-- Price -->
      <div class="price-section">
        <div class="current-price">Rp {{ formattedPrice }}</div>
        <div class="original-price" v-if="product.originalPrice">
          Rp {{ formattedOriginalPrice }}
        </div>
      </div>

      <!-- Action Button -->
      <button class="add-to-cart-btn" @click="handleAddToCart">
        <span class="btn-icon">🛒</span>
        <span class="btn-text">Tambah ke Keranjang</span>
        <div class="btn-overlay"></div>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductCard',
  props: {
    product: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      isWishlisted: false,
    }
  },
  computed: {
    formattedPrice() {
      return this.product.price.toLocaleString('id-ID')
    },
    formattedOriginalPrice() {
      return this.product.originalPrice ? this.product.originalPrice.toLocaleString('id-ID') : ''
    },

    // Check login status sederhana
    isLoggedIn() {
      return !!localStorage.getItem('token')
    },
  },
  methods: {
    handleAddToCart() {
      console.log('=== PRODUCTCARD DEBUG ===')
      console.log('Button clicked!')
      console.log('Is authenticated:', this.isLoggedIn)

      if (this.isLoggedIn) {
        console.log('User authenticated, adding to cart...')
        this.$emit('add-to-cart', this.product)
      } else {
        console.log('User not authenticated, triggering modal...')
        this.triggerLoginModal()
      }
    },

    triggerLoginModal() {
      console.log('ProductCard: Triggering login modal')

      // Method 1: Global function
      if (window.showLoginModal) {
        console.log('ProductCard: Using window.showLoginModal')
        window.showLoginModal()
        return
      }

      // Method 2: Custom event
      console.log('ProductCard: Using custom event')
      window.dispatchEvent(
        new CustomEvent('show-login-modal', {
          detail: { product: this.product },
        }),
      )

      // Method 3: Manual DOM manipulation
      setTimeout(() => {
        const modal = document.querySelector('.modal-overlay')
        if (modal) {
          console.log('ProductCard: Found modal, showing manually')
          modal.style.display = 'flex'
          modal.style.opacity = '1'
          modal.style.visibility = 'visible'
          modal.style.zIndex = '99999'
          document.body.style.overflow = 'hidden'
          document.body.style.height = '100vh'
        } else {
          console.log('ProductCard: Modal not found in DOM')
          alert('Silakan login terlebih dahulu!')
        }
      }, 100)
    },

    toggleWishlist() {
      this.isWishlisted = !this.isWishlisted
      this.$emit('toggle-wishlist', {
        product: this.product,
        isWishlisted: this.isWishlisted,
      })
    },
    quickPreview() {
      this.$emit('quick-preview', this.product)
    },
  },
}
</script>

<style scoped>
.product-card {
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.1),
    0 2px 8px rgba(0, 0, 0, 0.05);
  position: relative;
}

.product-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #f5576c);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.product-card:hover {
  transform: translateY(-12px) scale(1.02);
  box-shadow:
    0 20px 60px rgba(0, 0, 0, 0.15),
    0 8px 20px rgba(0, 0, 0, 0.1);
}

.product-card:hover::before {
  opacity: 1;
}

/* Product Image */
.product-image {
  position: relative;
  height: 180px;
  overflow: hidden;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: all 0.4s ease;
}

.product-card:hover .product-image img {
  transform: scale(1.1);
}

/* Badges */
.badges {
  position: absolute;
  top: 12px;
  left: 12px;
  display: flex;
  gap: 8px;
  z-index: 2;
}

.badge {
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  backdrop-filter: blur(10px);
}

.badge.discount {
  background: linear-gradient(45deg, #ff6b6b, #ee5a24);
  color: white;
  animation: pulse 2s infinite;
}

.badge.new {
  background: linear-gradient(45deg, #00b894, #00cec9);
  color: white;
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

/* Quick Actions */
.quick-actions {
  position: absolute;
  top: 12px;
  right: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  opacity: 0;
  transform: translateX(20px);
  transition: all 0.3s ease;
}

.product-card:hover .quick-actions {
  opacity: 1;
  transform: translateX(0);
}

.quick-btn {
  width: 36px;
  height: 36px;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  font-size: 1rem;
}

.quick-btn:hover {
  transform: scale(1.1);
  background: rgba(255, 255, 255, 1);
}

.heart.filled {
  color: #e74c3c;
}

/* Product Stats */
.product-stats {
  position: absolute;
  bottom: 12px;
  left: 12px;
  right: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.rating {
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(10px);
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 600;
}

.stars {
  color: #f39c12;
}

.sold {
  background: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 4px 8px;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 500;
}

/* Product Details */
.product-details {
  padding: 15px;
}

.product-brand {
  font-size: 0.7rem;
  color: #74b9ff;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 600;
  margin-bottom: 8px;
}

.product-name {
  font-size: 1rem;
  font-weight: 600;
  color: #2d3436;
  margin: 0 0 12px 0;
  line-height: 1.3;
  min-height: 40px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Price Section */
.price-section {
  margin-bottom: 15px;
}

.current-price {
  font-size: 1.1rem;
  font-weight: 700;
  background: linear-gradient(45deg, #00b894, #00cec9);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 4px;
}

.original-price {
  font-size: 0.9rem;
  color: #b2bec3;
  text-decoration: line-through;
}

/* Add to Cart Button */
.add-to-cart-btn {
  width: 100%;
  position: relative;
  background: #2ed573;
  border: none;
  border-radius: 12px;
  padding: 10px 16px;
  color: white;
  font-weight: 600;
  font-size: 0.85rem;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}

.btn-overlay {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: #26af5f;
  transition: left 0.3s ease;
  z-index: 0;
}

.btn-icon,
.btn-text {
  position: relative;
  z-index: 1;
}

.add-to-cart-btn:hover {
  background: #26af5f;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(46, 213, 115, 0.4);
}

.add-to-cart-btn:hover .btn-overlay {
  left: 0;
}

.add-to-cart-btn:active {
  transform: translateY(0);
}

/* Responsive Design */
@media (max-width: 768px) {
  .product-image {
    height: 200px;
  }

  .product-details {
    padding: 16px;
  }

  .product-name {
    font-size: 1rem;
    min-height: 40px;
  }

  .current-price {
    font-size: 1.2rem;
  }

  .add-to-cart-btn {
    padding: 12px 16px;
    font-size: 0.8rem;
  }
}

@media (max-width: 480px) {
  .product-image {
    height: 180px;
  }

  .product-details {
    padding: 12px;
  }

  .quick-actions {
    position: static;
    opacity: 1;
    transform: none;
    flex-direction: row;
    justify-content: center;
    margin-top: 8px;
  }
}
</style>
