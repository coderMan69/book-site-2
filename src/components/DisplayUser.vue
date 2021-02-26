<template>
  <div>
    <div class=".col-md-4 mb-3">
      <div class="card">
        <div class="card-body">
          <div class="d-flex flex-column align-items-center text-center">
            <a href="http://localhost:8080">
              <img :src="profilePhoto" alt="Admin" class="square" width="175">
            </a>
            <div class="mt-3">
              <h4>{{ name }}</h4>
              <p class="text-secondary mb-1">{{ location }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Tried moving the posts to the left -->
    <div class="container">
      <div class="row justify-content-start">
        <AddPost @post-added="getPosts"></AddPost>
        <div v-for="(post, index) in posts" :key="index" class="w-100">
          {{ post.message }}
        </div>
      </div>
    </div>

    <div class="py-4 px-4">
      <div class="d-flex align-items-center justify-content-between mb-3">
        <h5 class="mb-0">Books</h5>
        <AddBook @book-added="getBooks"></AddBook>
        <a href="#" class="btn btn-link text-muted">Show all</a>
      </div>

      <div class="col-lg-6 mb-2 pr-lg-1" v-for="(book, index) in books" :key="index">
        <!-- Link will become link to that book's page -->
        <a v-if="book.cover" href="http://localhost:8080">
          <img :src="book.cover" :title="`${book.title}\n${book.author}`">
        </a>
        <!-- if the book doesnt have a cover, that means it was a user created book -->
        <!-- That won't have a book page so no link -->
        <p v-else :title="`${book.title}\n${book.author}`">{{ book.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import AddPost from './AddPost.vue';
import AddBook from './AddBook.vue';

export default {
  data() {
    return {
      id: 1,
      name: 'Samuel',
      location: 'Detroit, MI',
      email: 'sam.teklitz@gmail.com',
      posts: [],
      /* eslint-disable global-require */
      profilePhoto: require('../assets/photos/cat_man.jpg'),
      friends: [],
      books: [],
    };
  },
  name: 'DisplayUser',
  components: {
    AddPost,
    AddBook,
  },
  created() {
    this.getBooks();
    this.getPosts();
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
          // console.log(this.books);
        })
        .catch((error) => {
        // eslint-disable-next-line
          console.error(error);
        });
    },
    getPosts() {
      const path = 'http://localhost:5000/posts';
      axios.get(path)
        .then((res) => {
          this.posts = res.data.posts;
          // console.log(this.posts);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};

</script>
