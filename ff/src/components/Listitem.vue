<template>
  <div class="product-list">
    <div class="product-card" v-for="(product, index) in products" :key="index">
      <div class="product-image">
        <img :src="product.image" :alt="product.name" />
        <div class="product-badges" v-if="product.discount || product.isNew">
          <span class="badge discount" v-if="product.discount">-{{ product.discount }}%</span>
          <span class="badge new" v-if="product.isNew">New</span>
        </div>
        <button class="wishlist-button" @click="toggleWishlist(index)">
          <i class="fas fa-heart" :class="{ active: product.isWishlisted }"></i>
        </button>
      </div>
      <div class="product-details">
        <div class="product-brand" v-if="product.brand">{{ product.brand }}</div>
        <div class="product-name">{{ product.name }}</div>
        <div class="product-rating" v-if="product.rating">
          <span class="stars">
            <i class="fas fa-star" v-for="n in Math.floor(product.rating)" :key="n"></i>
            <i class="fas fa-star-half-alt" v-if="product.rating % 1 !== 0"></i>
          </span>
          <span class="rating-count">({{ product.reviewCount }})</span>
        </div>
        <div class="price-container">
          <div class="product-price">Rp {{ formatPrice(product.price) }}</div>
          <div class="original-price" v-if="product.discount">
            Rp
            {{ formatPrice(product.originalPrice || product.price / (1 - product.discount / 100)) }}
          </div>
        </div>
        <div class="product-actions">
          <button class="cart-button" @click="addToCart(index)">
            <i class="fas fa-shopping-cart"></i>
            Add to Cart
          </button>
          <button class="buy-button" @click="handleBuy(index)">Buy Now</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const products = ref([])

onMounted(() => {
// fetch data dari fe
// simpen data ke var products

  products.value = [
    {
      name: 'Seledri 1 kg',
      price: 26499,
      image: '../assets/images/sawihijau.jpg',
      brand: 'Organic Farm',
      rating: 4.5,
      reviewCount: 128,
      discount: 10,
      isNew: true,
      isWishlisted: false,
    },
    {
      name: 'Apples 500g',
      price: 34999,
      image: '../assets/images/apples.jpg',
      brand: 'Fruit Garden',
      rating: 4.8,
      reviewCount: 256,
      discount: 0,
      isNew: false,
      isWishlisted: true,
    },
    {
      name: 'Pisang 1000g',
      price: 39000,
      image: '../assets/images/pisang.jpg',
      brand: 'Sunpride',
      rating: 4.8,
      reviewCount: 194,
      discount: 20,
      isNew: true,
      isWishlisted: true,
    },
  ]
})

function formatPrice(price) {
  return price.toLocaleString('id-ID')
}

function toggleWishlist(index) {
  products.value[index].isWishlisted = !products.value[index].isWishlisted
}

function addToCart(index) {
  console.log('Added to cart:', products.value[index])
  // Tambahkan logika cart di sini
}

function handleBuy(index) {
  console.log('Buying:', products.value[index])
  // Tambahkan logika pembelian di sini
}
</script>

<style scoped>
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 20px;
  padding: 20px;
}

.product-card {
  width: 100%;
  border-radius: 10px;
  overflow: hidden;
  background-color: #fdf6e3;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.product-image {
  position: relative;
  height: 120px;
  overflow: hidden;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.product-card:hover .product-image img {
  transform: scale(1.05);
}

.product-badges {
  position: absolute;
  top: 8px;
  left: 8px;
  display: flex;
  gap: 5px;
}

.badge {
  padding: 3px 6px;
  border-radius: 4px;
  font-size: 10px;
  font-weight: bold;
  color: white;
}

.badge.discount {
  background-color: #e74c3c;
}

.badge.new {
  background-color: #2ecc71;
}

.wishlist-button {
  position: absolute;
  top: 8px;
  right: 8px;
  background: rgba(255, 255, 255, 0.8);
  border: none;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.wishlist-button i {
  color: #ccc;
  font-size: 12px;
}

.wishlist-button i.active {
  color: #e74c3c;
}

.product-details {
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.product-brand {
  font-size: 10px;
  color: #7f8c8d;
  text-transform: uppercase;
}

.product-name {
  font-size: 14px;
  font-weight: 500;
  color: #333;
  height: 36px;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.product-rating {
  display: flex;
  align-items: center;
  gap: 4px;
}

.stars {
  color: #f39c12;
  font-size: 12px;
}

.rating-count {
  font-size: 10px;
  color: #7f8c8d;
}

.price-container {
  margin: 4px 0;
}

.product-price {
  font-size: 15px;
  font-weight: bold;
  color: #2ecc71;
}

.original-price {
  font-size: 12px;
  color: #95a5a6;
  text-decoration: line-through;
}

.product-actions {
  display: flex;
  gap: 8px;
  margin-top: 8px;
}

.cart-button,
.buy-button {
  flex: 1;
  padding: 6px;
  border: none;
  border-radius: 5px;
  font-size: 12px;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  transition: background-color 0.25s;
}

.cart-button {
  background-color: #f1c40f;
  color: #2c3e50;
}

.cart-button:hover {
  background-color: #f39c12;
}

.buy-button {
  background-color: #2ecc71;
  color: white;
}

.buy-button:hover {
  background-color: #27ae60;
}

@media (max-width: 480px) {
  .product-list {
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 15px;
    padding: 15px;
  }

  .product-image {
    height: 100px;
  }
}
</style>
