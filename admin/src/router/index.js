import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductManagement from '@/components/ProductManagement.vue'
import CustomerApp from '@/components/CustomerApp.vue'
import SalesApp from '@/components/SalesApp.vue'
import InvoiceApp from '@/components/InvoiceApp.vue'
import SuratJalanApp from '@/components/SuratJalanApp.vue'
import Login from '@/components/Login.vue'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/admin/products',
      name: 'home',
      component: HomeView,
    },
    {
    path: '/admin/customers',
    name: 'Customers',
    component: CustomerApp
  },
  {
    path: '/admin/sales',
    name: 'Sales',
    component: SalesApp
  },
  {
    path: '/admin/invoices',
    name: 'invoices',
    component: InvoiceApp
  },
  {
    path: '/admin/surat-jalan',
    name: 'surat-jalan',
    component: SuratJalanApp
  },

  ]
})

export default router
