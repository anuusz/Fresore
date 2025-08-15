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
              v-for="(filter, index) in statusFilters"
              :key="index"
              :class="['category-btn', { active: selectedFilter === filter }]"
              @click="filterByStatus(filter)"
            >
              <i class="fas fa-filter tag-icon"></i> {{ filter }}
            </button>
          </div>
          <button class="add-btn-header" @click="addCustomer">
            <i class="fas fa-user-plus"></i> Tambah Customer
          </button>
        </div>
      </div>

      <!-- Customer Table -->
      <div class="customer-table">
        <table>
          <thead>
            <tr>
              <th v-for="(header, index) in currentHeaders" :key="index">
                <i v-if="index === 0" class="fas fa-user header-icon"></i>
                <i v-else-if="index === 1 && !hasExpandedItems" class="fas fa-info-circle header-icon"></i>
                <i v-else-if="index === 1 && hasExpandedItems" class="fas fa-map-marker-alt header-icon"></i>
                <i v-else-if="index === 2" class="fas fa-phone header-icon"></i>
                {{ header }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(customer, index) in filteredCustomers"
              :key="customer.id"
              :class="['customer-row', { expanded: customer.isExpanded }]"
              @click="toggleCustomerExpand(customer.id)"
            >
              <td>
                <div class="customer-info">
                  <div class="customer-avatar">
                    <i class="fas fa-building"></i>
                  </div>
                  <span class="customer-name">{{ customer.nama }}</span>
                </div>
              </td>

              <!-- Show Keterangan when not expanded -->
              <td v-if="!customer.isExpanded && !hasExpandedItems">
                <span :class="['status', customer.statusClass]">
                  <i :class="customer.statusClass === 'paid' ? 'fas fa-check' : 'fas fa-clock'"></i>
                  {{ customer.status }}
                </span>
              </td>

              <!-- Show Alamat when expanded -->
              <td v-if="customer.isExpanded || hasExpandedItems" class="address-cell">
                {{ customer.alamat }}
              </td>

              <!-- Show No Telp when expanded -->
              <td v-if="customer.isExpanded || hasExpandedItems" class="phone-cell">
                <div class="phone-info">
                  <i class="fas fa-phone phone-icon"></i>
                  {{ customer.noTelp }}
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

export default {
  name: 'CustomerApp',
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

    // Data customers
    const customers = ref([
      {
        id: 1,
        nama: 'Swiss-Belhotel Airport Jakarta',
        status: 'Lunas',
        statusClass: 'paid',
        alamat: 'Jl. Husein Sastranegara No.Jax 1, Benda, Kec. Benda, Kota Tangerang, Banten',
        noTelp: '08125456789',
        isExpanded: false
      },
      {
        id: 2,
        nama: 'Mercure Hotel Cikaini',
        status: 'Lunas',
        statusClass: 'paid',
        alamat: 'Jl. Raya Cikaini No. 45, Jakarta Selatan, DKI Jakarta',
        noTelp: '08123456780',
        isExpanded: false
      },
      {
        id: 3,
        nama: 'Mercure Hotel BSD',
        status: 'Belum Lunas',
        statusClass: 'pending',
        alamat: 'BSD City, Serpong, Tangerang Selatan, Banten',
        noTelp: '08156789123',
        isExpanded: false
      },
      {
        id: 4,
        nama: 'Hotel Grand Indonesia',
        status: 'Lunas',
        statusClass: 'paid',
        alamat: 'Jl. MH Thamrin No. 1, Jakarta Pusat, DKI Jakarta',
        noTelp: '08198765432',
        isExpanded: false
      },
      {
        id: 5,
        nama: 'Shangri-La Hotel Jakarta',
        status: 'Belum Lunas',
        statusClass: 'pending',
        alamat: 'Jl. Jend. Sudirman Kav. 1, Jakarta Pusat, DKI Jakarta',
        noTelp: '08123456789',
        isExpanded: false
      }
    ])

    const selectedFilter = ref('Semua')
    const currentTime = ref('')

    // Computed properties
    const hasExpandedItems = computed(() => {
      return customers.value.some(customer => customer.isExpanded)
    })

    const currentHeaders = computed(() => {
      if (hasExpandedItems.value) {
        return ['Nama', 'Alamat', 'No Telp']
      } else {
        return ['Nama', 'Keterangan']
      }
    })

    const filteredCustomers = computed(() => {
      if (selectedFilter.value === 'Semua') {
        return customers.value
      }
      return customers.value.filter(customer => customer.status === selectedFilter.value)
    })

    // Methods
    const goTo = (path) => {
      router.push(path)
    }

    const isActive = (path) => {
      return route.path.startsWith(path)
    }

    const handleLogout = () => {
      console.log('Logout clicked')
    }

    const toggleCustomerExpand = (customerId) => {
      const customer = customers.value.find(c => c.id === customerId)
      if (customer) {
        // Reset all other customers to collapsed state
        customers.value.forEach(c => {
          if (c.id !== customerId) {
            c.isExpanded = false
          }
        })
        // Toggle the clicked customer
        customer.isExpanded = !customer.isExpanded
      }
    }

    const filterByStatus = (status) => {
      selectedFilter.value = status
    }

    const addCustomer = () => {
      console.log('Add new customer')
    }

    const updateTime = () => {
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
      currentTime.value = now.toLocaleDateString('id-ID', options)
    }

    return {
      navigation,
      customers,
      selectedFilter,
      currentTime,
      hasExpandedItems,
      currentHeaders,
      filteredCustomers,
      goTo,
      isActive,
      handleLogout,
      toggleCustomerExpand,
      filterByStatus,
      addCustomer,
      updateTime
    }
  },
  data() {
    return {
      statusFilters: ['Semua', 'Lunas', 'Belum Lunas'],
    }
  },
  mounted() {
    this.updateTime()
    setInterval(this.updateTime, 1000)
  }
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

/* Customer Table Styles */
.customer-table {
  background: #fefdfa;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  overflow-x: auto;
  flex-grow: 1;
  margin-bottom: 20px;
}

.customer-table table {
  width: 100%;
  border-collapse: collapse;
  min-width: 600px;
}

.customer-table th,
.customer-table td {
  padding: 16px 20px;
  text-align: left;
  border-bottom: 1px solid #eee;
  vertical-align: middle;
}

.customer-table th {
  background: #fefdfa;
  color: #7f8c8d;
  font-weight: 600;
  font-size: 0.9rem;
}

.customer-table th .header-icon {
  margin-right: 8px;
}

.customer-table td {
  color: #333;
}

/* Customer Row Styles */
.customer-row {
  cursor: pointer;
  transition: all 0.3s ease;
}

.customer-row:hover {
  background-color: #f8f9fa;
}

.customer-row.expanded {
  background-color: #f0f8f0;
  border-left: 4px solid #8bc34a;
}

/* Customer Info Styles */
.customer-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.customer-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: linear-gradient(135deg, #8bc34a, #7cb342);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 20px;
  flex-shrink: 0;
}

.customer-name {
  font-weight: 500;
  font-size: 16px;
}

/* Address and Phone Styles */
.address-cell {
  color: #666;
  font-size: 14px;
  line-height: 1.4;
  max-width: 300px;
}

.phone-cell {
  text-align: right;
}

.phone-info {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 8px;
  color: #666;
  font-size: 14px;
  font-weight: 500;
}

.phone-icon {
  color: #8bc34a;
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

.status.paid {
  background: #e6ffed;
  color: #22863a;
}

.status.pending {
  background: #fff3cd;
  color: #856404;
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

  .customer-table th,
  .customer-table td {
    padding: 12px 16px;
    font-size: 0.85rem;
  }

  .customer-info {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }

  .customer-avatar {
    width: 40px;
    height: 40px;
    font-size: 16px;
  }

  .phone-info {
    justify-content: flex-start;
  }
}
</style>
