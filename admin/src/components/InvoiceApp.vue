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
        <div class="invoice-header">
          <div class="header-tabs">
            <button
              v-for="(tab, index) in headerTabs"
              :key="index"
              :class="['tab-btn', { active: activeTab === tab }]"
              @click="setActiveTab(tab)"
            >
              {{ tab }}
            </button>
          </div>

          <!-- Month Navigation -->
          <div class="month-navigation">
            <button class="nav-btn" @click="previousMonth">
              <i class="fas fa-chevron-left"></i>
            </button>
            <span class="current-month">{{ formatMonth(selectedMonth) }}</span>
            <button class="nav-btn" @click="nextMonth">
              <i class="fas fa-chevron-right"></i>
            </button>
          </div>
        </div>
      </div>

      <!-- Invoice Container -->
      <div class="invoice-container">
        <!-- Main Invoice View -->
        <div v-if="!showDetailView" class="invoice-main-view">
          <div class="invoice-table">
            <div class="table-header">
              <div class="header-cell">Nama</div>
              <div class="header-cell">Keterangan</div>
              <div class="header-cell">Status</div>
              <div class="header-cell">Action</div>
            </div>

            <div
              v-for="(invoice, index) in monthlyInvoices"
              :key="index"
              class="table-row"
              @click="openDetailView(invoice)"
            >
              <div class="cell">{{ invoice.name }}</div>
              <div class="cell">{{ invoice.description }}</div>
              <div class="cell">
                <span :class="['status-badge', invoice.status.toLowerCase()]">
                  {{ invoice.status }}
                </span>
              </div>
              <div class="cell">
                <button class="action-btn download" @click.stop="downloadInvoice(invoice)">
                  Download
                </button>
              </div>
            </div>
          </div>

          <!-- Monthly Summary -->
          <div class="monthly-summary">
            <div class="summary-card">
              <div class="summary-icon">
                <i class="fas fa-file-invoice"></i>
              </div>
              <div class="summary-content">
                <div class="summary-value">{{ monthlyInvoices.length }}</div>
                <div class="summary-label">Total Invoice</div>
              </div>
            </div>

            <div class="summary-card">
              <div class="summary-icon">
                <i class="fas fa-check-circle"></i>
              </div>
              <div class="summary-content">
                <div class="summary-value">{{ completedInvoices }}</div>
                <div class="summary-label">Selesai</div>
              </div>
            </div>

            <div class="summary-card">
              <div class="summary-icon">
                <i class="fas fa-money-bill-wave"></i>
              </div>
              <div class="summary-content">
                <div class="summary-value">{{ formatCurrency(totalAmount) }}</div>
                <div class="summary-label">Total Nilai</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Detail Invoice View -->
        <div v-else class="invoice-detail-view">
          <div class="detail-header">
            <button class="back-btn" @click="closeDetailView">
              <i class="fas fa-arrow-left"></i>
              Kembali
            </button>
            <h3>Detail Invoice - {{ selectedInvoice.name }}</h3>
          </div>

          <div class="detail-table">
            <div class="table-header">
              <div class="header-cell date">Tanggal</div>
              <div class="header-cell">Kode Invoice</div>
              <div class="header-cell">Keterangan</div>
              <div class="header-cell">Total</div>
            </div>

            <div
              v-for="(detail, index) in selectedInvoice.details"
              :key="index"
              class="table-row"
            >
              <div class="cell date">{{ formatDate(detail.date) }}</div>
              <div class="cell">{{ detail.invoiceCode }}</div>
              <div class="cell">{{ detail.description }}</div>
              <div class="cell total">{{ formatCurrency(detail.total) }}</div>
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
  name: 'InvoiceApp',
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

    // Invoice data
    const invoiceData = ref({
      '2025-01': [
        {
          name: 'Invoice Bulanan Januari 2025',
          description: '1725-SBAJ',
          status: 'Lunas',
          amount: 12600000,
          details: [
            { date: '2025-01-01', invoiceCode: '1725-SBAJ-001', description: 'Pembayaran produk A', total: 2500000 },
            { date: '2025-01-03', invoiceCode: '1725-SBAJ-002', description: 'Pembayaran produk B', total: 1800000 },
            { date: '2025-01-05', invoiceCode: '1725-SBAJ-003', description: 'Pembayaran produk C', total: 3200000 },
            { date: '2025-01-10', invoiceCode: '1725-SBAJ-004', description: 'Pembayaran produk D', total: 1500000 },
            { date: '2025-01-15', invoiceCode: '1725-SBAJ-005', description: 'Pembayaran produk E', total: 2100000 },
            { date: '2025-01-20', invoiceCode: '1725-SBAJ-006', description: 'Pembayaran produk F', total: 1500000 }
          ]
        }
      ],
      '2025-02': [
        {
          name: 'Invoice Bulanan Februari 2025',
          description: '1725-SBAJ',
          status: 'Pending',
          amount: 15900000,
          details: [
            { date: '2025-02-01', invoiceCode: '1725-SBAJ-007', description: 'Pembayaran produk G', total: 2800000 },
            { date: '2025-02-05', invoiceCode: '1725-SBAJ-008', description: 'Pembayaran produk H', total: 3100000 },
            { date: '2025-02-10', invoiceCode: '1725-SBAJ-009', description: 'Pembayaran produk I', total: 2500000 },
            { date: '2025-02-15', invoiceCode: '1725-SBAJ-010', description: 'Pembayaran produk J', total: 4200000 },
            { date: '2025-02-20', invoiceCode: '1725-SBAJ-011', description: 'Pembayaran produk K', total: 1800000 },
            { date: '2025-02-25', invoiceCode: '1725-SBAJ-012', description: 'Pembayaran produk L', total: 1500000 }
          ]
        }
      ],
      '2025-03': [
        {
          name: 'Invoice Bulanan Maret 2025',
          description: '1725-SBAJ',
          status: 'Belum Lunas',
          amount: 10700000,
          details: [
            { date: '2025-03-01', invoiceCode: '1725-SBAJ-013', description: 'Pembayaran produk M', total: 2200000 },
            { date: '2025-03-08', invoiceCode: '1725-SBAJ-014', description: 'Pembayaran produk N', total: 1900000 },
            { date: '2025-03-12', invoiceCode: '1725-SBAJ-015', description: 'Pembayaran produk O', total: 2800000 },
            { date: '2025-03-18', invoiceCode: '1725-SBAJ-016', description: 'Pembayaran produk P', total: 1700000 },
            { date: '2025-03-25', invoiceCode: '1725-SBAJ-017', description: 'Pembayaran produk Q', total: 2100000 }
          ]
        }
      ]
    })

    const selectedMonth = ref('2025-01')
    const activeTab = ref('Nama')
    const currentTime = ref('')
    const showDetailView = ref(false)
    const selectedInvoice = ref(null)

    // Computed properties
    const monthlyInvoices = computed(() => {
      return invoiceData.value[selectedMonth.value] || []
    })

    const completedInvoices = computed(() => {
      return monthlyInvoices.value.filter(invoice => invoice.status === 'Lunas').length
    })

    const totalAmount = computed(() => {
      return monthlyInvoices.value.reduce((sum, invoice) => sum + invoice.amount, 0)
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

    const previousMonth = () => {
      const [year, month] = selectedMonth.value.split('-')
      let newMonth = parseInt(month) - 1
      let newYear = parseInt(year)

      if (newMonth === 0) {
        newMonth = 12
        newYear -= 1
      }

      const newDate = `${newYear}-${newMonth.toString().padStart(2, '0')}`
      if (invoiceData.value[newDate]) {
        selectedMonth.value = newDate
      }
    }

    const nextMonth = () => {
      const [year, month] = selectedMonth.value.split('-')
      let newMonth = parseInt(month) + 1
      let newYear = parseInt(year)

      if (newMonth === 13) {
        newMonth = 1
        newYear += 1
      }

      const newDate = `${newYear}-${newMonth.toString().padStart(2, '0')}`
      if (invoiceData.value[newDate]) {
        selectedMonth.value = newDate
      }
    }

    const setActiveTab = (tab) => {
      activeTab.value = tab
    }

    const formatMonth = (monthStr) => {
      const [year, month] = monthStr.split('-')
      const months = [
        'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
        'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'
      ]
      return `${months[parseInt(month) - 1]} ${year}`
    }

    const formatDate = (dateStr) => {
      const date = new Date(dateStr)
      return date.toLocaleDateString('id-ID', {
        day: '2-digit',
        month: 'long',
        year: 'numeric'
      })
    }

    const formatCurrency = (amount) => {
      return `Rp ${amount.toLocaleString('id-ID')}`
    }

    const openDetailView = (invoice) => {
      selectedInvoice.value = invoice
      showDetailView.value = true
    }

    const closeDetailView = () => {
      showDetailView.value = false
      selectedInvoice.value = null
    }

    const downloadInvoice = (invoice) => {
      console.log('Download invoice:', invoice.name)
      // Implement download logic
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
      invoiceData,
      selectedMonth,
      activeTab,
      currentTime,
      showDetailView,
      selectedInvoice,
      monthlyInvoices,
      completedInvoices,
      totalAmount,
      goTo,
      isActive,
      handleLogout,
      previousMonth,
      nextMonth,
      setActiveTab,
      formatMonth,
      formatDate,
      formatCurrency,
      openDetailView,
      closeDetailView,
      downloadInvoice,
      updateTime
    }
  },
  data() {
    return {
      headerTabs: ['Nama', 'Keterangan']
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

/* Invoice Header */
.invoice-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  flex-wrap: wrap;
  gap: 16px;
}

.header-tabs {
  display: flex;
  gap: 8px;
}

.tab-btn {
  background: #f8f9fa;
  color: #6c757d;
  border: 1px solid #dee2e6;
  padding: 8px 20px;
  border-radius: 25px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: inherit;
}

.tab-btn:hover {
  background: #e9ecef;
  color: #495057;
}

.tab-btn.active {
  background: #8bc34a;
  color: #fdf6e3;
  border-color: #8bc34a;
}

/* Month Navigation */
.month-navigation {
  display: flex;
  align-items: center;
  gap: 16px;
  background: #ffffff;
  padding: 8px 16px;
  border-radius: 25px;
  border: 1px solid #dee2e6;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.nav-btn {
  background: none;
  border: none;
  color: #8bc34a;
  cursor: pointer;
  padding: 8px;
  border-radius: 50%;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-btn:hover {
  background: #f0f9ff;
  color: #7cb342;
}

.current-month {
  font-weight: 600;
  color: #333;
  font-size: 1.1rem;
  min-width: 120px;
  text-align: center;
}

/* Invoice Container */
.invoice-container {
  background: #ffffff;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* Main Invoice View */
.invoice-main-view {
  flex: 1;
  display: flex;
  flex-direction: column;
}

/* Invoice Table */
.invoice-table {
  flex: 1;
  margin-bottom: 24px;
}

.table-header {
  display: grid;
  grid-template-columns: 2fr 2fr 1fr 1fr;
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
  grid-template-columns: 2fr 2fr 1fr 1fr;
  gap: 16px;
  padding: 16px 20px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  margin-bottom: 8px;
  cursor: pointer;
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
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
}

.status-badge.lunas {
  background: #d4edda;
  color: #155724;
}

.status-badge.pending {
  background: #fff3cd;
  color: #856404;
}

.status-badge.belum {
  background: #f8d7da;
  color: #721c24;
}

/* Action Button */
.action-btn {
  background: #8bc34a;
  color: white;
  border: none;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.action-btn:hover {
  background: #7cb342;
}

/* Monthly Summary */
.monthly-summary {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.summary-card {
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

.summary-icon {
  font-size: 2rem;
  opacity: 0.8;
}

.summary-content {
  flex: 1;
}

.summary-value {
  font-size: 1.5rem;
  font-weight: 700;
  line-height: 1.2;
}

.summary-label {
  font-size: 0.85rem;
  opacity: 0.9;
  margin-top: 4px;
}

/* Detail View */
.invoice-detail-view {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.detail-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid #e5e7eb;
}

.back-btn {
  background: #8bc34a;
  color: white;
  border: none;
  padding: 10px 16px;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.back-btn:hover {
  background: #7cb342;
}

.detail-header h3 {
  margin: 0;
  color: #333;
  font-size: 1.3rem;
}

/* Detail Table */
.detail-table {
  flex: 1;
}

.detail-table .table-header {
  grid-template-columns: 1.5fr 1.5fr 2fr 1fr;
}

.detail-table .table-row {
  grid-template-columns: 1.5fr 1.5fr 2fr 1fr;
}

.header-cell.date,
.cell.date {
  font-size: 0.85rem;
}

.cell.total {
  font-weight: 600;
  color: #8bc34a;
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

  .invoice-header {
    flex-direction: column;
    align-items: stretch;
  }

  .header-tabs {
    justify-content: center;
  }

  .month-navigation {
    justify-content: center;
  }

  .invoice-container {
    padding: 16px;
  }

  .table-header,
  .table-row {
    grid-template-columns: 1fr;
    gap: 8px;
  }

  .detail-table .table-header,
  .detail-table .table-row {
    grid-template-columns: 1fr;
  }

  .monthly-summary {
    flex-direction: column;
  }

  .summary-card {
    min-width: auto;
  }

  .logo-text {
    font-size: 42px;
  }

  .current-month {
    min-width: auto;
  }
}
</style>
