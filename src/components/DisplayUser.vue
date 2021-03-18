<template>
<div>
    <div class=".col-md-4 mb-3">
      <div class="card">
        <div class="card-body">
          <div class="d-flex flex-column align-items-center text-center">
            <div class="container">
              <a href="http://localhost:8080">
                <img :src="profilePhoto" alt="Admin" class="rounded mb-3" width="175">
              </a>
            </div>
            <div class="mt-3">
              <div class="row">
                <h4 class="mr-3">{{ name }}</h4>
                <EditProfile :userId="userID" @profile-edited="refreshUser"/>
              </div>
              <div class="row justify-content-center">
                <a href="#reading" style="color: #404040; text-decoration: none;">
                  <h4 class="mr-3">{{ readingBooks.length }} reading</h4>
                </a>
                <a href="#all" style="color: #404040; text-decoration: none;">
                  <h4 v-if="books.length !== 1" class="mx-3">{{ books.length }} books</h4>
                  <h4 v-else class="ml-3">{{ books.length }} book</h4>
                </a>
                <!-- Add books does not work -->
                <AddBook :userID="userID" class="ml-3" @book-added="refreshBooks"/>
              </div>
              <p class="text-secondary mb-1">{{ location }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="tabs">
      <b-nav tabs align="center">
        <b-nav-item id="reading"
                    to="#reading"
                    :active="$route.hash === '#reading' || $route.hash === ''">
                    Currently Reading
        </b-nav-item>
        <b-nav-item id="finished"
                    to="#finished"
                    :active="$route.hash === '#finished'">
                    Finished
        </b-nav-item>
        <b-nav-item id="all"
                    to="#all"
                    :active="$route.hash === '#all'">
                    All Books
        </b-nav-item>
      </b-nav>
      <div class="tab-content">
        <div :class="['tab-pane', { 'active': $route.hash === '#reading' || $route.hash == '' }]">
          <DisplayBooks @book-edited="refreshBooks"
                      :books="readingBooks"
                      :userID="userID"
                      fixButtons="reading"/>
        </div>
        <div :class="['tab-pane', { 'active': $route.hash === '#finished' }]">
          <DisplayBooks @book-edited="refreshBooks"
                      :books="readBooks"
                      :userID="userID"
                      fixButtons="finished"/>
        </div>
        <div :class="['tab-pane', { 'active': $route.hash === '#all' }]">
          <DisplayBooks @book-edited="refreshBooks"
                      :books="books"
                      :userID="userID"
                      fixButtons="all"/>
        </div>
      </div>
    </div>
    <br/>
    <a>links</a>
    <br/>
    <p class="text-muted">copyright</p>
  </div>
</template>

<script>
import axios from 'axios';
import AddBook from './AddBook.vue';
import DisplayBooks from './DisplayBooks.vue';
import EditProfile from './EditProfile.vue';

export default {
  data() {
    return {
      name: '',
      location: '',
      email: '',
      // posts: [],
      profilePhoto: '',
      // friends: [],
      books: [],
      user: {},

      // Can set userID to 1 or 2 at the moment
      // userID: 2,
    };
  },
  name: 'DisplayUser',
  components: {
    AddBook,
    DisplayBooks,
    EditProfile,
  },
  props: {
    userID: {
      type: Number,
      required: true,
    },
  },
  created() {
    this.getBooks(this.userID);
    this.getUser(this.userID);
  },
  methods: {
    refreshBooks() {
      this.getBooks(this.userID);
    },
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
    refreshUser() {
      this.getUser(this.userID);
    },
    getUser(userID) {
      const path = `http://localhost:5000/readers/${userID}`;
      console.log(`GetUser ${path}`);
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
  },
  computed: {
    readBooks() {
      return this.books.filter((book) => book.read);
    },
    readingBooks() {
      return this.books.filter((book) => book.reading);
    },
  },
};
</script>
