<template>
  <div>
    <CartItem @go-to-products="goToProducts" />
  </div>
</template>

<script>
import CartItem from '@/components/CartItem.vue'

export default {
  name: 'CartView',
  components: {
    CartItem,
  },
  methods: {
    goToProducts() {
      // Navigate to products page
      this.$router.push('/') // atau route yang sesuai
    },
  },
}
</script>
