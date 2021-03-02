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
              <h4>{{ books.length }} Books</h4>
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
        <button class="mb-0" @click="toggleBooksDisplay">Books</button>
        <AddBook @book-added="getBooks"></AddBook>
      </div>

      <!-- Toggle between all books and currently reading -->
      <!-- Made the toggle the "books" button, need to make prettier later -->
      <div v-if="showAllBooks">
        <h5>All Books</h5>
        <displayBooks :books="books"></displayBooks>
      </div>
      <div v-else>
        <h5>Currently Reading</h5>
        <displayBooks :books="readBooks"></displayBooks>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import AddBook from './AddBook.vue';
import DisplayBooks from './DisplayBooks.vue';

export default {
  data() {
    return {
      name: '',
      location: '',
      email: '',
      // posts: [],
      /* eslint-disable global-require */
      profilePhoto: '',
      // friends: [],
      books: [],
      showAllBooks: true,
      user: [],

      // Can set userID to 0 or 1 at the momment
      userID: 2,
    };
  },
  name: 'DisplayUser',
  components: {
    AddBook,
    DisplayBooks,
  },
  created() {
    this.getBooks(this.userID);
    this.getUser(this.userID);
  },
  methods: {
    getBooks(userID) {
      const path = `http://localhost:5000/books/${userID}`;
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
        // eslint-disable-next-line
          console.error(error);
        });
    },
    getUser(userID) {
      const path = `http://localhost:5000/user/${userID}`;
      axios.get(path)
        .then((res) => {
          this.user = res.data.user;
          this.name = res.data.user.name;
          this.location = res.data.user.location;
          this.email = res.data.user.email;
          this.profilePhoto = res.data.user.profile_photo;
        })
        .catch((error) => {
        // eslint-disable-next-line
          console.error(error);
        });
    },
    // Display all books or only ready books
    toggleBooksDisplay() {
      this.showAllBooks = !this.showAllBooks;
    },
  },
  computed: {
    readBooks() {
      return this.books.filter((book) => book.reading);
    },
  },
};

</script>
