<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <b-table striped hover :items="items"></b-table>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://localhost:8000/api/'

export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Counterparties',
      items: [],
    }
  },
  mounted () {
    
  },
  created () {
    axios.get(API_URL + 'counterparties/').then(response => { this.items = response.data['counterparties'] })
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
