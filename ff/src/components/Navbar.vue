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
          <span>Fresoré</span>
        </div>

        <div class="nav-categories">
          <button
            v-for="category in categories"
            :key="category"
            @click="navigate(category)"
          >
            {{ category }}
          </button>
        </div>

        <div class="nav-actions">
          <button @click="toggleSearch">
            <span class="icon">🔍</span>
          </button>
          <button @click="navigate('cart')" class="cart-btn">
            <span class="icon">🛒</span>
            <span class="badge" v-if="cartCount > 0">{{ cartCount }}</span>
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
          >
          <button @click="toggleSearch" class="close-btn">✕</button>
        </div>
      </div>
    </div>

    <!-- 3. Banner -->
    <div class="banner-container">
      <div class="banner">
        <div class="banner-content">
          <h2>Special Promo Fresoré!</h2>
          <p>Get discounts up to 50% on fresh products</p>
          <button class="banner-button" @click="navigate('promo')">
            Shop Now
          </button>
        </div>
        <div class="banner-image">
          <div class="placeholder-image">🛒</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AppLayout',
  data() {
    return {
      categories: ['Fruits', 'Vegetables', 'Groceries', 'Meat'],
      cartCount: 3,
      showSearch: false,
      searchQuery: ''
    }
  },
  methods: {
    navigate(destination) {
      console.log(`Navigating to ${destination}`);
      // this.$router.push(`/${destination}`);
    },
    toggleSearch() {
      this.showSearch = !this.showSearch;
      if (this.showSearch) {
        this.$nextTick(() => {
          this.$refs.searchInput?.focus();
        });
      }
    },
    performSearch() {
      if (this.searchQuery.trim()) {
        console.log(`Searching for: ${this.searchQuery}`);
        this.searchQuery = '';
        this.showSearch = false;
      }
    }
  }
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
  background-color: #8BC34A;
  padding: 5px 0;
  text-align: center;
  font-size: 0.85rem;
  color: #FDFFF5;
  z-index: 1000;
  font-family: "League Spartan", sans-serif;
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
  /* left: 50%; */
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
  backdrop-filter: blur(10px);
}

.nav-brand {
  font-size: 1.4rem;
  font-weight: bold;
  color: #2ecc71;
  flex: 1;
  font-family: "Satisfy", cursive;
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
  font-family: "League Spartan", sans-serif;
}

.nav-categories button:hover {
  background-color: rgba(46, 204, 113, 0.1);
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
  transition: background-color 0.3s ease;
  position: relative;
}

.nav-actions button:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.cart-btn .badge {
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

/* Banner Styles */
.banner-container {
  margin-top: 125px;
  /* padding: 0 20px; */
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

.banner {
  display: flex;
  background: linear-gradient(135deg, #2ecc71, #27ae60);
  border-radius: 25px;
  overflow: hidden;
  transform: translateX(-50%);
  color: #fdf6e3;
}

.banner-content {
  padding: 0 100px;
  justify-content: center;
}

.banner-content h2 {
  font-size: 1.8rem;
  margin-bottom: 10px;
}

.banner-content p {
  font-size: 1rem;
  margin-bottom: 20px;
  opacity: 0.5;
}

.banner-button {
  background: #f0f7e8;
  color: #2ecc71;
  border: none;
  padding: 10px 20px;
  border-radius: 20px;
  font-weight: bold;
  cursor: pointer;
  width: fit-content;
  transition: all 0.3s ease;
}

.banner-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.banner-image {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(255, 255, 255, 0.2);
}

.placeholder-image {
  font-size: 5rem;
  padding: 20px;
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

  .nav-brand {
    font-size: 1.2rem;
  }

  .nav-categories {
    gap: 8px;
  }

  .nav-categories button {
    padding: 6px 10px;
    font-size: 0.85rem;
  }

  .banner-container {
    margin-top: 120px;
  }

  .banner {
    flex-direction: column;
  }

  .banner-content {
    padding: 20px;
  }

  .banner-content h2 {
    font-size: 1.5rem;
  }

  .placeholder-image {
    font-size: 3rem;
    padding: 15px;
  }
}

@media (max-width: 480px) {
  .top-bar {
    padding: 6px 10px;
  }

  .banner-container {
    margin-top: 110px;
    padding: 0 10px;
  }

  .nav-brand {
    display: none;
  }

  .banner-content h2 {
    font-size: 1.3rem;
  }

  .banner-button {
    padding: 8px 16px;
    font-size: 0.9rem;
  }
}
</style>
