<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="column is-9">
        <h1 class="title">{{product.name}}</h1>
        <p> {{ product.description }}</p>
      </div>
      <div class="column is-3">
        <h2 class="subtitle">Information</h2>
        <p><strong>Daily Hiring Price:</strong>${{ product.daily_hiring_price }} </p>
        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity">
          </div>
          <div class="control">
            <a class="button is-dark">Add to cart</a>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
export default {
  name: "Product",
  data(){
    return {
      product: {},
      quantity: 1
    }
  },
  mounted() {
    this.getProduct()
  },
  methods: {
    async getProduct() {
      this.$store.commit('setIsLoading', true)

      const product_id = this.$route.params.product_id

      await axios
          .get(`api/product/${product_id}`)
          .then(response =>{
                    this.product = response.data
                    document.title = this.product.name + ' | Products'
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
          }
    }
}
</script>

<style scoped>

</style>