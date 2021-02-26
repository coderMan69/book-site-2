<template>
  <div>
    <div class=".col-md-4 mb-3">
      <div class="card">
        <div class="card-body">
          <div class="d-flex flex-column align-items-center text-center">
            <div class="container">
              <a href="http://localhost:8080">
                <img :src="profilePhoto" alt="Admin" class="square" width="175">
              </a>
              <h4>Books:</h4>
              <h6>{{ books.length }}</h6>
            </div>
            <div class="mt-3">
              <h4>{{ name }}</h4>
              <p class="text-secondary mb-1">{{ location }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="py-4 px-4">
      <div class="d-flex align-items-center justify-content-between mb-3">
        <h5 class="mb-0">Books</h5>
        <AddBook @book-added="getBooks"></AddBook>
      </div>
    <div>
    <table id="BookTable">
      <thead>
        <tr>
          <th>Title</th>
          <th>Author</th>
          <th>Image</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(book, index) in books" :key="index">
          <td>{{book.title}}</td>
          <td><span v-for="(author, index) in book.author" :key="index">
            {{ author }}<br/>
          </span></td>
          <td>
            <a href="http://localhost:8080">
              <img v-if="book.cover"
                  :src="book.cover"
                  :title="`${book.title}\n${book.author}`">
              <img v-else
                    :src="noCover"
                    :title="`${book.title}\n${book.author}`">
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
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
      noCover: require('../assets/photos/no_cover.jpg'),
      friends: [],
      books: [],
    };
  },
  name: 'DisplayUser',
  components: {
    AddBook,
  },
  created() {
    this.getBooks();
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
  },
};

</script>
