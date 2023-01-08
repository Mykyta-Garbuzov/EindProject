<template>


  <button type="submit" class="btn btn__primary btn__lg" @click="getPosts">Show Posts</button>
 
  <div v-for="p in post" :key="p.id">
    <h2>{{ p.name }} - {{ p.sort }}</h2>
    <p>{{ p.description }}</p>
  </div>  
  <section>
    <form @submit.prevent="setPost">
      <div>
        <label for="name">UserID:</label>
        <input type="text" id="name" v-model="postData.userId">
      </div>
      <div>
        <label for="sort">Title: </label>
        <input type="text" id="sort" v-model="postData.title">
      </div>
      <div>
        <label for="description">Body: </label>
        <textarea id="description" rows="6" cols="22" v-model="postData.body"></textarea>
      </div>
      <button>Create Post</button>
    </form>
  </section>
</template>

<script>
export default {
  data() {
    return {
      post: {},
      postData: {
        userId: '',
        title:  '',
        body:   ''
      }
    }
    
    
  },
  methods: {
    getPosts() {
      fetch('https://api-mykyta-garbuzov.cloud.okteto.net/dogs')
      
        .then(response => response.json())
        .then(data => this.post = data)
    },
    setPost() {
      fetch('https://api-mykyta-garbuzov.cloud.okteto.net/dogs',{
        method:  'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          name: this.name,
          sort:  this.sort,
          description:   this.description
        })
      })
        .then(response => response.json())
        .then(data => console.log(data))
    }
  }
};

</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#app {
  background: #fff;
  margin: 2rem 0 4rem 0;
  padding: 1rem;
  padding-top: 0;
  position: relative;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2), 0 2.5rem 5rem 0 rgba(0, 0, 0, 0.1);
}
@media screen and (min-width: 550px) {
  #app {
    padding: 4rem;
  }
}
#app > * {
  max-width: 50rem;
  margin-left: auto;
  margin-right: auto;
}
#app > form {
  max-width: 100%;
}
#app h1 {
  display: block;
  min-width: 100%;
  width: 100%;
  text-align: center;
  margin: 0;
  margin-bottom: 1rem;
}
</style>