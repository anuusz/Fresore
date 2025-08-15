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

      <!-- Date Filter -->
      <div class="date-filter-container">
        <div class="date-filter">
          <span class="date-text">{{ selectedDate }}</span>
          <button class="date-btn" @click="showDatePicker = !showDatePicker">
            <i class="fas fa-calendar-alt"></i>
          </button>
        </div>
      </div>

      <!-- Surat Jalan Container -->
      <div class="surat-jalan-container">
        <div class="surat-jalan-table">
          <div class="table-header">
            <div class="header-cell name-col">Nama</div>
            <div class="header-cell status-col">Keterangan</div>
            <div class="header-cell action-col">Action</div>
          </div>

          <div
            v-for="(suratJalan, index) in filteredSuratJalan"
            :key="index"
            class="table-row"
          >
            <div class="cell name-col">{{ suratJalan.name }}</div>
            <div class="cell status-col">
              <span :class="['status-badge', suratJalan.status.toLowerCase()]">
                {{ suratJalan.status }}
              </span>
            </div>
            <div class="cell action-col">
              <button class="download-btn" @click="downloadSuratJalan(suratJalan)">
                Download
              </button>
            </div>
          </div>

          <!-- Empty State -->
          <div v-if="filteredSuratJalan.length === 0" class="empty-state">
            <i class="fas fa-file-alt empty-icon"></i>
            <p class="empty-text">Tidak ada surat jalan untuk tanggal ini</p>
          </div>
        </div>

        <!-- Summary Stats -->
        <div class="summary-stats">
          <div class="stat-card">
            <div class="stat-icon">
              <i class="fas fa-truck"></i>
            </div>
            <div class="stat-content">
              <div class="stat-value">{{ filteredSuratJalan.length }}</div>
              <div class="stat-label">Total Surat Jalan</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">
              <i class="fas fa-check-circle"></i>
            </div>
            <div class="stat-content">
              <div class="stat-value">{{ deliveredCount }}</div>
              <div class="stat-label">Terkirim</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">
              <i class="fas fa-exclamation-triangle"></i>
            </div>
            <div class="stat-content">
              <div class="stat-value">{{ returnCount }}</div>
              <div class="stat-label">Return</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'

export default {
  name: 'SuratJalanApp',
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

    // Surat Jalan data
    const suratJalanData = ref([
      {
        id: 1,
        name: 'Swiss-Belhotel Airport Jakarta',
        status: 'Deliver',
        date: '2025-07-27',
        recipient: 'Hotel Management',
        items: ['Produk A', 'Produk B', 'Produk C']
      },
      {
        id: 2,
        name: 'Savana Golf & Resort',
        status: 'Return',
        date: '2025-07-27',
        recipient: 'Resort Management',
        items: ['Produk D', 'Produk E']
      },
      {
        id: 3,
        name: 'Grand Hyatt Jakarta',
        status: 'Deliver',
        date: '2025-07-26',
        recipient: 'Procurement Department',
        items: ['Produk F', 'Produk G', 'Produk H']
      },
      {
        id: 4,
        name: 'Mandarin Oriental',
        status: 'Pending',
        date: '2025-07-26',
        recipient: 'Operations Manager',
        items: ['Produk I', 'Produk J']
      },
      {
        id: 5,
        name: 'The Ritz-Carlton Jakarta',
        status: 'Deliver',
        date: '2025-07-25',
        recipient: 'Food & Beverage',
        items: ['Produk K', 'Produk L', 'Produk M', 'Produk N']
      }
    ])

    const selectedDate = ref('27 July 2025')
    const currentTime = ref('')
    const showDatePicker = ref(false)

    // Computed properties
    const filteredSuratJalan = computed(() => {
      // Convert display date to internal format for filtering
      const filterDate = convertDisplayDateToInternal(selectedDate.value)
      return suratJalanData.value.filter(item => item.date === filterDate)
    })

    const deliveredCount = computed(() => {
      return filteredSuratJalan.value.filter(item => item.status === 'Deliver').length
    })

    const returnCount = computed(() => {
      return filteredSuratJalan.value.filter(item => item.status === 'Return').length
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

    const downloadSuratJalan = (suratJalan) => {
      console.log('Download surat jalan:', suratJalan.name)
      // Implement download logic here
      alert(`Download surat jalan: ${suratJalan.name}`)
    }

    const convertDisplayDateToInternal = (displayDate) => {
      // Convert "27 July 2025" to "2025-07-27"
      const months = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08',
        'September': '09', 'October': '10', 'November': '11', 'December': '12'
      }

      const parts = displayDate.split(' ')
      if (parts.length === 3) {
        const day = parts[0].padStart(2, '0')
        const month = months[parts[1]]
        const year = parts[2]
        return `${year}-${month}-${day}`
      }
      return '2025-07-27' // default
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
      suratJalanData,
      selectedDate,
      currentTime,
      showDatePicker,
      filteredSuratJalan,
      deliveredCount,
      returnCount,
      goTo,
      isActive,
      handleLogout,
      downloadSuratJalan,
      updateTime
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

/* Clock Display */
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

/* Date Filter */
.date-filter-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.date-filter {
  background: #ffffff;
  border: 1px solid #dee2e6;
  border-radius: 25px;
  padding: 12px 20px;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.date-text {
  font-size: 1rem;
  font-weight: 600;
  color: #333;
}

.date-btn {
  background: none;
  border: none;
  color: #8bc34a;
  cursor: pointer;
  padding: 4px;
  border-radius: 50%;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.date-btn:hover {
  background: #f0f9ff;
  color: #7cb342;
}

/* Surat Jalan Container */
.surat-jalan-container {
  background: #ffffff;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* Surat Jalan Table */
.surat-jalan-table {
  flex: 1;
  margin-bottom: 24px;
}

.table-header {
  display: grid;
  grid-template-columns: 3fr 1.5fr 1fr;
  gap: 16px;
  padding: 16px 20px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 8px;
  font-weight: 600;
  color: #333;
}

.header-cell {
  font-size: 0.9rem;
}

.table-row {
  display: grid;
  grid-template-columns: 3fr 1.5fr 1fr;
  gap: 16px;
  padding: 16px 20px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  margin-bottom: 8px;
  transition: all 0.3s ease;
}

.table-row:hover {
  background: #f8f9fa;
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.cell {
  display: flex;
  align-items: center;
  font-size: 0.9rem;
  color: #333;
}

/* Status Badge */
.status-badge {
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: capitalize;
}

.status-badge.deliver {
  background: #d4edda;
  color: #155724;
}

.status-badge.pending {
  background: #fff3cd;
  color: #856404;
}

.status-badge.return {
  background: #f8d7da;
  color: #721c24;
}

/* Download Button */
.download-btn {
  background: #6c757d;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.download-btn:hover {
  background: #5a6268;
}

/* Empty State */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  color: #6c757d;
}

.empty-icon {
  font-size: 3rem;
  margin-bottom: 16px;
  opacity: 0.5;
}

.empty-text {
  font-size: 1rem;
  margin: 0;
}

/* Summary Stats */
.summary-stats {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.stat-card {
  background: linear-gradient(135deg, #8bc34a, #7cb342);
  color: white;
  padding: 20px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 16px;
  flex: 1;
  min-width: 200px;
  box-shadow: 0 4px 6px rgba(139, 195, 74, 0.3);
}

.stat-icon {
  font-size: 2rem;
  opacity: 0.8;
}

.stat-content {
  flex: 1;
}

.stat-value {
  font-size: 1.5rem;
  font-weight: 700;
  line-height: 1.2;
}

.stat-label {
  font-size: 0.85rem;
  opacity: 0.9;
  margin-top: 4px;
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

  .surat-jalan-container {
    padding: 16px;
  }

  .table-header,
  .table-row {
    grid-template-columns: 1fr;
    gap: 8px;
  }

  .summary-stats {
    flex-direction: column;
  }

  .stat-card {
    min-width: auto;
  }

  .logo-text {
    font-size: 42px;
  }
}
</style>
