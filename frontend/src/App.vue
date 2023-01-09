<template class="container">
  

<div class="row p-3">
  <div class="col-3">
  <button type="submit button" class="btn btn-dark " @click="getPosts">Show Dogs</button>
  <div class="p-3" v-for="p in post" :key="p.id">
    <ul><li>{{ p.name }} - {{ p.sort }}</li>
    <li>{{ p.description }}</li></ul>

  </div>  

</div>
<div class="col-3">
<button type="submit button" class="btn btn-dark " @click="getStores">Show Stores</button>
  <div class="p-3" v-for="p in store" :key="p.id">
    <ul><li>{{ p.name }} - {{ p.id }}</li></ul></div> 

</div><div class="col-3">
<button type="submit button" class="btn btn-dark " @click="getOwners">Show Owners</button>
<div class="p-3" v-for="p in owners" :key="p.id">
    <ul><li>{{ p.email }} - {{ p.is_active }}</li></ul></div> 
</div>

<div class="col-3">
  <section >
    <form @submit.prevent="setPost" >
      <div>
        <label for="name">Name : </label>
        <input type="text" id="name" v-model="postData.name">
      </div>
      
      <button type="button" class="btn btn-dark " >Create Post</button>
    </form>
  </section>
</div>
</div>


</template>

<script>
export default {
  data() {
    return {
      post: {},
      owners: {},
      postData: {
        name: "",
        id: "",
        items: ""
      },
      store:{}
    }
    
    
  },
  methods: {
    getPosts() {
      fetch('https://app-mykyta-garbuzov.cloud.okteto.net/dogs')
      
        .then(response => response.json())
        .then(data => this.post = data)
    },
    getStores() {
      fetch('https://app-mykyta-garbuzov.cloud.okteto.net/stores')
      
        .then(response => response.json())
        .then(data => this.store = data)
    },
    getOwners() {
      fetch('https://app-mykyta-garbuzov.cloud.okteto.net/owners/',{
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer 93876439bdee6d3dab4e9d75cc73eed82b580067eb2555a062273ff0c8650b2e'
        },
      })
      
        .then(response => response.json())
        .then(data => this.owners = data)
    },
    setPost() {
      fetch('https://app-mykyta-garbuzov.cloud.okteto.net/stores',{
        method:  'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer 93876439bdee6d3dab4e9d75cc73eed82b580067eb2555a062273ff0c8650b2e'
         
        },
        body: JSON.stringify({
          name: this.name
        })
      })
        .then(response => response.json())
        .then(data => console.log(data))
    }
  }
}

</script>