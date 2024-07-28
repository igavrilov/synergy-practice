<template>
  <div class="currency-converter">
    <h1>Currency Converter</h1>
    <form @submit.prevent="convertCurrency">
      <div>
        <label for="from_currency">From Currency:</label>
        <input v-model="from_currency" id="from_currency" required />
      </div>
      <div>
        <label for="to_currency">To Currency:</label>
        <input v-model="to_currency" id="to_currency" required />
      </div>
      <div>
        <label for="amount">Amount:</label>
        <input v-model.number="amount" id="amount" type="number" required />
      </div>
      <button type="submit">Convert</button>
    </form>
    <div v-if="convertedAmount !== null">
      <h2>Converted Amount: {{ convertedAmount }}</h2>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      from_currency: '',
      to_currency: '',
      amount: null,
      convertedAmount: null
    };
  },
  methods: {
    async convertCurrency() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/convert', {
          from_currency: this.from_currency,
          to_currency: this.to_currency,
          amount: this.amount
        });
        this.convertedAmount = response.data.converted_amount;
      } catch (error) {
        console.error('Error converting currency:', error);
        alert('Failed to convert currency. Please check the currency codes and try again.');
      }
    }
  }
};
</script>

<style scoped>
.currency-converter {
  max-width: 400px;
  margin: 0 auto;
  text-align: center;
}
form div {
  margin-bottom: 10px;
}
button {
  padding: 10px 20px;
}
</style>
