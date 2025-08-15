<template>
  <div class="admin-container">
    <!-- Sidebar -->
    <div class="sidebar">
      <!-- Logo -->
      <div class="logo-container">
        <p class="logo-text">Fresore</p>
      </div>

      <!-- Navigation -->
      <div class="nav-container">
        <ul>
          <li
            v-for="(item, index) in navigation"
            :key="index"
            :class="{ active: isActive(item.path) }"
            @click="goTo(item.path)"
          >
            <i :class="['nav-icon', isActive(item.path) ? item.icon_active : item.icon]"></i>
            <span class="nav-text">{{ item.name }}</span>
          </li>
        </ul>
      </div>

      <!-- Logout -->
      <div class="logout-container" @click="handleLogout">
        <i class="fas fa-sign-out-alt logout-icon"></i>
        <span class="logout-text">Logout</span>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Clock Display -->
      <div class="clock-container">
        <div class="clock">
          <i class="fas fa-clock"></i>
          {{ currentTime }}
        </div>
      </div>

      <!-- Header -->
      <div class="content-header">
        <div class="category-tags">
          <div class="category-group">
            <button
              v-for="(tag, index) in tags"
              :key="index"
              :class="['category-btn', { active: selectedCategory === tag }]"
              @click="filterByCategory(tag)"
            >
              <i class="fas fa-tag tag-icon"></i> {{ tag }}
            </button>
          </div>
          <button class="add-btn-header" @click="addProduct">
            <i class="fas fa-plus-circle"></i> Tambah Item
          </button>
        </div>
      </div>

      <!-- Product Table -->
      <div class="product-table">
        <table>
          <thead>
            <tr>
              <th v-for="(header, index) in tableHeaders" :key="index">
                <i v-if="index === 0" class="fas fa-box-open header-icon"></i>
                <i v-else-if="index === 1" class="fas fa-tag header-icon"></i>
                <i v-else-if="index === 2" class="fas fa-info-circle header-icon"></i>
                <i v-else-if="index === 3" class="fas fa-edit header-icon"></i>
                {{ header }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(product, index) in filteredProducts" :key="index">
              <td>
                <div class="product-info">
                  <div class="product-image-container" @click="selectImage(index)">
                    <img
                      v-if="product.image"
                      :src="product.image"
                      :alt="product.name"
                      class="product-image"
                    />
                    <div v-else class="product-placeholder">
                      <i class="fas fa-camera"></i>
                      <span>Foto</span>
                    </div>
                  </div>
                  <span class="product-name">{{ product.name }}</span>
                </div>
              </td>
              <td>{{ product.price }}</td>
              <td>
                <span :class="['status', product.statusClass]">
                  <i
                    :class="product.statusClass === 'available' ? 'fas fa-check' : 'fas fa-times'"
                  ></i>
                  {{ product.status }}
                </span>
              </td>
              <td>
                <button class="edit-btn" @click="editProduct(index)">
                  <i class="fas fa-edit"></i> Ubah
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Hidden File Input -->
      <input
        type="file"
        ref="imageInput"
        @change="handleImageUpload"
        accept="image/*"
        style="display: none"
      />
    </div>

    <!-- Edit Product Modal -->
    <div v-if="showEditModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <div class="modal-header">
          <h3><i class="fas fa-edit"></i> Edit Produk</h3>
          <button class="close-btn" @click="closeModal">
            <i class="fas fa-times"></i>
          </button>
        </div>

        <div class="modal-body">
          <div class="form-group">
            <label for="productName">
              <i class="fas fa-box-open"></i> Nama Produk
            </label>
            <input
              id="productName"
              v-model="editForm.name"
              type="text"
              class="form-input"
              placeholder="Masukkan nama produk"
            />
          </div>

          <div class="form-group">
            <label for="productPrice">
              <i class="fas fa-tag"></i> Harga
            </label>
            <input
              id="productPrice"
              v-model="editForm.price"
              type="text"
              class="form-input"
              placeholder="Masukkan harga produk"
            />
          </div>

          <div class="form-group">
            <label for="productCategory">
              <i class="fas fa-list"></i> Kategori
            </label>
            <select
              id="productCategory"
              v-model="editForm.category"
              class="form-select"
            >
              <option value="Buah">Buah</option>
              <option value="Sayuran">Sayuran</option>
              <option value="Groceries">Groceries</option>
              <option value="Daging">Daging</option>
            </select>
          </div>

          <div class="form-group">
            <label for="productStatus">
              <i class="fas fa-info-circle"></i> Status
            </label>
            <select
              id="productStatus"
              v-model="editForm.status"
              class="form-select"
            >
              <option value="Tersedia">Tersedia</option>
              <option value="Tidak Tersedia">Tidak Tersedia</option>
            </select>
          </div>
        </div>

        <div class="modal-footer">
          <button class="cancel-btn" @click="closeModal">
            <i class="fas fa-times"></i> Batal
          </button>
          <button class="save-btn" @click="saveProduct">
            <i class="fas fa-save"></i> Simpan
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'

export default {
  name: 'AdminPanel',
  setup() {
    const router = useRouter()
    const route = useRoute()

    const navigation = ref([
      {
        name: 'Product List',
        path: '/admin/products',
        icon: 'fas fa-boxes',
        icon_active: 'fas fa-boxes text-white',
      },
      {
        name: 'Customer',
        path: '/admin/customers',
        icon: 'fas fa-users',
        icon_active: 'fas fa-users text-white',
      },
      {
        name: 'Penjualan',
        path: '/admin/sales',
        icon: 'fas fa-chart-line',
        icon_active: 'fas fa-chart-line text-white',
      },
      {
        name: 'Invoice',
        path: '/admin/invoices',
        icon: 'fas fa-file-invoice',
        icon_active: 'fas fa-file-invoice text-white',
      },
      {
    name: 'Surat Jalan',
    path: '/admin/surat-jalan',
    icon: 'fas fa-truck',
    icon_active: 'fas fa-truck text-white',
  },
    ])

    const goTo = (path) => {
      router.push(path)
    }

    const isActive = (path) => {
      return route.path.startsWith(path)
    }

    const handleLogout = () => {
      console.log('Logout clicked')
    }

    return {
      navigation,
      goTo,
      isActive,
      handleLogout,
    }
  },
  data() {
    return {
      tags: ['Semua', 'Buah', 'Sayuran', 'Groceries', 'Daging'],
      selectedCategory: 'Semua',
      tableHeaders: ['Nama', 'Harga', 'Keterangan', 'Aksi'],
      products: [
        {
          name: 'Sawi Hijau',
          price: 'Rp 14 000',
          status: 'Tersedia',
          statusClass: 'available',
          category: 'Sayuran',
          image: null,
        },
        {
          name: 'Daging Sapi',
          price: 'Rp 75 000',
          status: 'Tidak Tersedia',
          statusClass: 'unavailable',
          category: 'Daging',
          image: null,
        },
        {
          name: 'Apel Fuji',
          price: 'Rp 25 000',
          status: 'Tersedia',
          statusClass: 'available',
          category: 'Buah',
          image: null,
        },
        {
          name: 'Beras Premium',
          price: 'Rp 45 000',
          status: 'Tersedia',
          statusClass: 'available',
          category: 'Groceries',
          image: null,
        },
        {
          name: 'Ayam Kampung',
          price: 'Rp 35 000',
          status: 'Tidak Tersedia',
          statusClass: 'unavailable',
          category: 'Daging',
          image: null,
        },
        {
          name: 'Bayam',
          price: 'Rp 8 000',
          status: 'Tersedia',
          statusClass: 'available',
          category: 'Sayuran',
          image: null,
        },
        {
          name: 'Jeruk Manis',
          price: 'Rp 18 000',
          status: 'Tersedia',
          statusClass: 'available',
          category: 'Buah',
          image: null,
        },
        {
          name: 'Minyak Goreng',
          price: 'Rp 22 000',
          status: 'Tidak Tersedia',
          statusClass: 'unavailable',
          category: 'Groceries',
          image: null,
        },
      ],
      currentTime: '',
      selectedProductIndex: null,
      showEditModal: false,
      editingProductIndex: null,
      editForm: {
        name: '',
        price: '',
        category: '',
        status: ''
      }
    }
  },
  computed: {
    filteredProducts() {
      if (this.selectedCategory === 'Semua') {
        return this.products
      }
      return this.products.filter(product => product.category === this.selectedCategory)
    }
  },
  mounted() {
    this.updateTime()
    setInterval(this.updateTime, 1000)
  },
  methods: {
    editProduct(filteredIndex) {
      // Find the original index in the products array
      const originalIndex = this.products.findIndex(p => p === this.filteredProducts[filteredIndex])
      this.editingProductIndex = originalIndex

      // Populate the form with current product data
      const product = this.products[originalIndex]
      this.editForm = {
        name: product.name,
        price: product.price,
        category: product.category,
        status: product.status
      }

      this.showEditModal = true
    },
    closeModal() {
      this.showEditModal = false
      this.editingProductIndex = null
      this.editForm = {
        name: '',
        price: '',
        category: '',
        status: ''
      }
    },
    saveProduct() {
      if (this.editingProductIndex !== null) {
        // Update the product
        this.products[this.editingProductIndex] = {
          ...this.products[this.editingProductIndex],
          name: this.editForm.name,
          price: this.editForm.price,
          category: this.editForm.category,
          status: this.editForm.status,
          statusClass: this.editForm.status === 'Tersedia' ? 'available' : 'unavailable'
        }

        console.log('Product updated:', this.products[this.editingProductIndex])
        this.closeModal()
      }
    },
    addProduct() {
      console.log('Add new product')
    },
    updateTime() {
      const now = new Date()
      const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        timeZone: 'Asia/Jakarta'
      }
      this.currentTime = now.toLocaleDateString('id-ID', options)
    },
    filterByCategory(category) {
      this.selectedCategory = category
    },
    selectImage(filteredIndex) {
      // Find the original index in the products array
      const originalIndex = this.products.findIndex(p => p === this.filteredProducts[filteredIndex])
      this.selectedProductIndex = originalIndex
      this.$refs.imageInput.click()
    },
    handleImageUpload(event) {
      const file = event.target.files[0]
      if (file && this.selectedProductIndex !== null) {
        const reader = new FileReader()
        reader.onload = (e) => {
          this.products[this.selectedProductIndex].image = e.target.result
        }
        reader.readAsDataURL(file)
      }
      // Reset the input
      event.target.value = ''
      this.selectedProductIndex = null
    },
  },
}
</script>

<style>
/* Font Awesome import */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
@import url('https://fonts.googleapis.com/css2?family=Satisfy&display=swap');
/* Global reset */
html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: hidden;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

</style>

<style scoped>
/* Main Container */
.admin-container {
  display: flex;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

/* Sidebar Styles */
.sidebar {
  width: 240px;
  background: #fdf6e3;
  border-right: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.logo-container {
  padding: 16px;
  border-bottom: 1px solid #e5e7eb;
}

.logo-text {
  font-weight: 700;
  color: #8bc34a;
  white-space: nowrap;
  font-family: 'Satisfy', cursive;
  font-size: 58px;
  margin: 0;
  text-align: center;
}

.nav-container {
  flex: 1;
  padding: 16px 0;
  overflow-y: auto;
}

.nav-container ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.nav-container li {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  cursor: pointer;
  border-radius: 0 125px 125px 0;
  transition: all 0.5s ease;
  color: #4b5563;
}

.nav-container li:hover {
  background: #8bc34a;
  color: #fdf6e3;
}

.nav-container li.active {
  background: #8bc34a;
  color: #fdf6e3;
}

.nav-icon {
  font-size: 16px;
  width: 20px;
  text-align: center;
}

.nav-text {
  font-size: 14px;
  font-weight: 500;
}

.logout-container {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px;
  border-top: 1px solid #e5e7eb;
  cursor: pointer;
  transition: color 0.3s ease;
  color: #4b5563;
}

.logout-container:hover {
  color: #dc2626;
}

/* Main Content Styles */
.main-content {
  flex: 1;
  padding: 24px;
  background: #fdf6e3;
  overflow-y: auto;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Content Header */
.content-header {
  margin-bottom: 20px;
}

.category-tags {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
}

/* Group kategori tags di kiri */
.category-group {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

/* Category Button Styles */
.category-btn {
  background: #f8f9fa;
  color: #6c757d;
  border: 1px solid #dee2e6;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: inherit;
}

.category-btn:hover {
  background: #e9ecef;
  color: #495057;
  transform: translateY(-1px);
}

.category-btn.active {
  background: #8bc34a;
  color: #fdf6e3;
  border-color: #8bc34a;
}

/* Header Add Button */
.add-btn-header {
  padding: 10px 15px;
  background: #8bc34a;
  color: #fdf6e3;
  border: none;
  border-radius: 25px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.5s ease;
  display: flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
  flex-shrink: 0;
  margin-left: auto;
}

.add-btn-header:hover {
  background: #7cb342;
}

/* Clock Display - Topbar Style */
.clock-container {
  margin-bottom: 16px;
  display: flex;
  justify-content: center;
  width: 100%;
}

.clock {
  background: #fdf6e3;
  border: 1px solid #e5e7eb;
  border-radius: 25px;
  padding: 15px 30px;
  font-size: 1rem;
  color: #4b5563;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  box-shadow: 0 2.5px 5px rgb(139, 195, 74, 1);
  width: 100%;
  font-weight: 500;
}

/* Product Table Styles */
.product-table {
  background: #fefdfa;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  overflow-x: auto;
  flex-grow: 1;
  margin-bottom: 20px;
}

.product-table table {
  width: 100%;
  border-collapse: collapse;
  min-width: 600px;
}

.product-table th,
.product-table td {
  padding: 16px 20px;
  text-align: left;
  border-bottom: 1px solid #eee;
  vertical-align: middle;
}

.product-table th {
  background: #fefdfa;
  color: #7f8c8d;
  font-weight: 600;
  font-size: 0.9rem;
}

.product-table th .header-icon {
  margin-right: 8px;
}

.product-table td {
  color: #333;
}

.product-table td .product-icon {
  margin-right: 8px;
  color: #8bc34a;
}

/* Product Image Styles */
.product-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.product-image-container {
  width: 50px;
  height: 50px;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  border: 2px dashed #dee2e6;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  flex-shrink: 0;
}

.product-image-container:hover {
  border-color: #8bc34a;
  background: #f8f9fa;
}

.product-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #6c757d;
  font-size: 0.7rem;
  text-align: center;
  padding: 4px;
}

.product-placeholder i {
  font-size: 16px;
  margin-bottom: 2px;
}

.product-placeholder span {
  font-size: 0.65rem;
}

.product-name {
  font-weight: 500;
}

/* Status Badges */
.status {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  width: fit-content;
}

.status.available {
  background: #e6ffed;
  color: #22863a;
}

.status.unavailable {
  background: #ffeef0;
  color: #cb2431;
}

/* Button Styles */
.edit-btn {
  color: #8bc34a;
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px 12px;
  font-size: 0.9rem;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.3s ease;
  border-radius: 4px;
}

.edit-btn:hover {
  background: #f0f9ff;
  text-decoration: underline;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.3s ease;
}

.modal-content {
  background: #fefdfa;
  border-radius: 12px;
  width: 90%;
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  animation: slideIn 0.3s ease;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  border-bottom: 1px solid #e5e7eb;
}

.modal-header h3 {
  margin: 0;
  color: #333;
  font-size: 1.25rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 10px;
}

.close-btn {
  background: none;
  border: none;
  font-size: 1.25rem;
  cursor: pointer;
  color: #6b7280;
  padding: 4px;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.close-btn:hover {
  background: #f3f4f6;
  color: #374151;
}

.modal-body {
  padding: 24px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #374151;
  font-size: 0.9rem;
  display: flex;
  align-items: center;
  gap: 8px;
}

.form-input,
.form-select {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #d1d5db;
  border-radius: 8px;
  font-size: 0.95rem;
  transition: all 0.3s ease;
  font-family: inherit;
  background: #ffffff;
}

.form-input:focus,
.form-select:focus {
  outline: none;
  border-color: #8bc34a;
  box-shadow: 0 0 0 3px rgba(139, 195, 74, 0.1);
}

.form-input::placeholder {
  color: #9ca3af;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  padding: 20px 24px;
  border-top: 1px solid #e5e7eb;
  background: #f9fafb;
}

.cancel-btn,
.save-btn {
  padding: 10px 20px;
  border: none;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 8px;
}

.cancel-btn {
  background: #f3f4f6;
  color: #374151;
  border: 1px solid #d1d5db;
}

.cancel-btn:hover {
  background: #e5e7eb;
  color: #1f2937;
}

.save-btn {
  background: #8bc34a;
  color: #ffffff;
}

.save-btn:hover {
  background: #7cb342;
  transform: translateY(-1px);
}

/* Animations */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideIn {
  from {
    transform: translateY(-50px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .admin-container {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
    height: auto;
  }

  .main-content {
    padding: 16px;
    height: auto;
  }

  .content-header {
    margin-bottom: 16px;
  }

  .category-tags {
    flex-direction: column;
    align-items: stretch;
    gap: 12px;
  }

  .add-btn-header {
    width: 100%;
    justify-content: center;
  }

  .clock-container {
    justify-content: center;
  }

  .logo-text {
    font-size: 42px;
  }

  .product-table th,
  .product-table td {
    padding: 12px 16px;
    font-size: 0.85rem;
  }

  .modal-content {
    width: 95%;
    margin: 20px;
  }

  .modal-header,
  .modal-body,
  .modal-footer {
    padding: 16px 20px;
  }

  .modal-footer {
    flex-direction: column;
  }

  .cancel-btn,
  .save-btn {
    width: 100%;
    justify-content: center;
  }
}
</style>
