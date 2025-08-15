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
        <div class="sales-header">
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

          <!-- Year Navigation -->
          <div class="year-navigation">
            <button class="year-btn" @click="previousYear">
              <i class="fas fa-chevron-left"></i>
            </button>
            <span class="current-year">{{ selectedYear }}</span>
            <button class="year-btn" @click="nextYear">
              <i class="fas fa-chevron-right"></i>
            </button>
          </div>
        </div>
      </div>

      <!-- Chart Container -->
      <div class="chart-container">
        <div class="chart-header">
          <div class="chart-title">
            <h3>Data Penjualan {{ selectedYear }}</h3>
            <p class="chart-subtitle">Grafik penjualan per bulan dalam tahun {{ selectedYear }}</p>
          </div>
        </div>

        <!-- Chart Area -->
        <div class="chart-wrapper">
          <div class="chart-canvas">
            <!-- Y-axis labels -->
            <div class="y-axis">
              <div v-for="label in yAxisLabels" :key="label" class="y-label">
                {{ label }}
              </div>
            </div>

            <!-- Chart bars -->
            <div class="bars-container">
              <div
                v-for="(month, index) in monthsData"
                :key="index"
                class="bar-column"
              >
                <div
                  class="bar"
                  :style="{ height: getBarHeight(month.value) + '%' }"
                  @mouseover="showTooltip(month, $event)"
                  @mouseleave="hideTooltip"
                >
                  <div class="bar-value">{{ month.value }}</div>
                </div>
                <div class="month-label">{{ month.name }}</div>
              </div>
            </div>
          </div>

          <!-- Tooltip -->
          <div
            v-if="tooltip.show"
            class="tooltip"
            :style="{ left: tooltip.x + 'px', top: tooltip.y + 'px' }"
          >
            <div class="tooltip-title">{{ tooltip.month }}</div>
            <div class="tooltip-value">Penjualan: {{ tooltip.value }}</div>
          </div>
        </div>

        <!-- Summary Stats -->
        <div class="summary-stats">
          <div class="stat-card">
            <div class="stat-icon">
              <i class="fas fa-chart-line"></i>
            </div>
            <div class="stat-content">
              <div class="stat-value">{{ totalSales }}</div>
              <div class="stat-label">Total Penjualan</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">
              <i class="fas fa-calendar-check"></i>
            </div>
            <div class="stat-content">
              <div class="stat-value">{{ averageSales }}</div>
              <div class="stat-label">Rata-rata Bulanan</div>
            </div>
          </div>

          <div class="stat-card">
            <div class="stat-icon">
              <i class="fas fa-trophy"></i>
            </div>
            <div class="stat-content">
              <div class="stat-value">{{ bestMonth.name }}</div>
              <div class="stat-label">Bulan Terbaik</div>
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
  name: 'PenjualanApp',
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

    // Sales data for different years
    const salesData = ref({
      2023: [
        { name: 'Januari', value: 320 },
        { name: 'Februari', value: 450 },
        { name: 'Maret', value: 520 },
        { name: 'April', value: 280 },
        { name: 'Mei', value: 380 },
        { name: 'Juni', value: 420 },
        { name: 'Juli', value: 250 },
        { name: 'Agustus', value: 680 },
        { name: 'September', value: 0 },
        { name: 'Oktober', value: 0 },
        { name: 'November', value: 0 },
        { name: 'Desember', value: 0 }
      ],
      2024: [
        { name: 'Januari', value: 380 },
        { name: 'Februari', value: 520 },
        { name: 'Maret', value: 620 },
        { name: 'April', value: 340 },
        { name: 'Mei', value: 480 },
        { name: 'Juni', value: 520 },
        { name: 'Juli', value: 350 },
        { name: 'Agustus', value: 750 },
        { name: 'September', value: 0 },
        { name: 'Oktober', value: 0 },
        { name: 'November', value: 0 },
        { name: 'Desember', value: 0 }
      ],
      2025: [
        { name: 'Januari', value: 420 },
        { name: 'Februari', value: 580 },
        { name: 'Maret', value: 680 },
        { name: 'April', value: 380 },
        { name: 'Mei', value: 520 },
        { name: 'Juni', value: 580 },
        { name: 'Juli', value: 380 },
        { name: 'Agustus', value: 820 },
        { name: 'September', value: 0 },
        { name: 'Oktober', value: 0 },
        { name: 'November', value: 0 },
        { name: 'Desember', value: 0 }
      ]
    })

    const selectedYear = ref(2025)
    const activeTab = ref('Nama')
    const currentTime = ref('')
    const tooltip = ref({
      show: false,
      x: 0,
      y: 0,
      month: '',
      value: 0
    })

    // Computed properties
    const monthsData = computed(() => {
      return salesData.value[selectedYear.value] || []
    })

    const maxValue = computed(() => {
      const values = monthsData.value.map(m => m.value).filter(v => v > 0)
      return Math.max(...values, 1000)
    })

    const yAxisLabels = computed(() => {
      const max = maxValue.value
      const step = Math.ceil(max / 5 / 100) * 100
      return Array.from({ length: 6 }, (_, i) => step * i).reverse()
    })

    const totalSales = computed(() => {
      return monthsData.value.reduce((sum, month) => sum + month.value, 0)
    })

    const averageSales = computed(() => {
      const activeMonths = monthsData.value.filter(m => m.value > 0)
      if (activeMonths.length === 0) return 0
      return Math.round(totalSales.value / activeMonths.length)
    })

    const bestMonth = computed(() => {
      return monthsData.value.reduce((best, current) =>
        current.value > best.value ? current : best, monthsData.value[0]
      )
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

    const previousYear = () => {
      if (selectedYear.value > 2023) {
        selectedYear.value--
      }
    }

    const nextYear = () => {
      if (selectedYear.value < 2025) {
        selectedYear.value++
      }
    }

    const setActiveTab = (tab) => {
      activeTab.value = tab
    }

    const getBarHeight = (value) => {
      if (value === 0) return 0
      return (value / maxValue.value) * 80
    }

    const showTooltip = (month, event) => {
      tooltip.value = {
        show: true,
        x: event.clientX - 50,
        y: event.clientY - 60,
        month: month.name,
        value: month.value
      }
    }

    const hideTooltip = () => {
      tooltip.value.show = false
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
      salesData,
      selectedYear,
      activeTab,
      currentTime,
      tooltip,
      monthsData,
      maxValue,
      yAxisLabels,
      totalSales,
      averageSales,
      bestMonth,
      goTo,
      isActive,
      handleLogout,
      previousYear,
      nextYear,
      setActiveTab,
      getBarHeight,
      showTooltip,
      hideTooltip,
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

/* Sales Header */
.sales-header {
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

/* Year Navigation */
.year-navigation {
  display: flex;
  align-items: center;
  gap: 16px;
  background: #ffffff;
  padding: 8px 16px;
  border-radius: 25px;
  border: 1px solid #dee2e6;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.year-btn {
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

.year-btn:hover {
  background: #f0f9ff;
  color: #7cb342;
}

.current-year {
  font-weight: 600;
  color: #333;
  font-size: 1.1rem;
  min-width: 60px;
  text-align: center;
}

/* Chart Container */
.chart-container {
  background: #ffffff;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  flex: 1;
  display: flex;
  flex-direction: column;
}

.chart-header {
  margin-bottom: 24px;
}

.chart-title h3 {
  margin: 0 0 8px 0;
  color: #333;
  font-size: 1.5rem;
  font-weight: 600;
}

.chart-subtitle {
  margin: 0;
  color: #666;
  font-size: 0.9rem;
}

/* Chart Wrapper */
.chart-wrapper {
  flex: 1;
  position: relative;
  min-height: 400px;
}

.chart-canvas {
  height: 400px;
  display: flex;
  align-items: flex-end;
  position: relative;
  margin: 20px 0;
}

/* Y-axis */
.y-axis {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  width: 60px;
  margin-right: 20px;
  padding: 20px 0;
}

.y-label {
  font-size: 0.8rem;
  color: #666;
  text-align: right;
  line-height: 1;
}

/* Bars Container - Fixed for bottom-to-top display */
.bars-container {
  display: flex;
  justify-content: space-between;
  align-items: flex-end; /* This ensures bars start from bottom */
  flex: 1;
  height: 100%;
  padding: 20px 10px 40px 10px;
  position: relative;
}

.bar-column {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end; /* This pushes bars to bottom */
  flex: 1;
  height: 100%;
  position: relative;
}

.bar {
  background: linear-gradient(135deg, #8bc34a, #7cb342); /* Changed to green gradient */
  width: 80%;
  max-width: 60px;
  min-height: 20px;
  border-radius: 4px 4px 0 0;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  margin-bottom: 10px;
  display: flex;
  align-items: flex-start; /* Changed to flex-start to show values at top of bars */
  justify-content: center;
  padding-top: 4px; /* Changed from padding-bottom to padding-top */
  box-shadow: 0 2px 4px rgba(139, 195, 74, 0.3); /* Added shadow */
}

.bar:hover {
  background: linear-gradient(135deg, #9ccc65, #8bc34a); /* Lighter green on hover */
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(139, 195, 74, 0.4);
}

.bar-value {
  color: white;
  font-size: 0.7rem;
  font-weight: 600;
  text-shadow: 0 1px 2px rgba(0,0,0,0.3);
}

.month-label {
  font-size: 0.75rem;
  color: #666;
  text-align: center;
  margin-top: 8px;
  transform: rotate(0deg);
  white-space: nowrap;
  position: absolute;
  bottom: -30px; /* Positioned below the bar */
  left: 50%;
  transform: translateX(-50%);
}

/* Tooltip */
.tooltip {
  position: fixed;
  background: #333;
  color: white;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 0.8rem;
  pointer-events: none;
  z-index: 1000;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.tooltip-title {
  font-weight: 600;
  margin-bottom: 2px;
}

.tooltip-value {
  font-size: 0.75rem;
  opacity: 0.9;
}

/* Summary Stats */
.summary-stats {
  display: flex;
  gap: 20px;
  margin-top: 24px;
  flex-wrap: wrap;
}

.stat-card {
  background: linear-gradient(135deg, #8bc34a, #7cb342);
  color: #fdf6e3;
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

  .sales-header {
    flex-direction: column;
    align-items: stretch;
  }

  .header-tabs {
    justify-content: center;
  }

  .year-navigation {
    justify-content: center;
  }

  .chart-container {
    padding: 16px;
  }

  .chart-canvas {
    height: 300px;
  }

  .bars-container {
    padding: 20px 5px 40px 5px;
  }

  .month-label {
    font-size: 0.65rem;
    transform: rotate(-45deg) translateX(-50%);
    transform-origin: center;
    bottom: -35px;
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
