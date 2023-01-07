<template>
  <button @click="getPosts">Show Posts</button>
 
  <div v-for="p in post" :key="p.id">
    <h2>{{ p.name }} - {{ p.sort }}</h2>
    <p>{{ p.description }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      post: {}
    }
  },
  methods: {
    getPosts() {
      fetch('https://api-mykyta-garbuzov.cloud.okteto.net/dogs')
      
        .then(response => response.json())
        .then(data => this.post = data)
    }
  }
}

</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>