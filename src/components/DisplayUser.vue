<template>
  <div class="old-paper">
    <div class=".col-md-4 mb-3">
      <div class="card display-user">
        <div class="card-body">
          <div class="d-flex flex-column align-items-center text-center">
            <b-container fluid="lg">
              <a href="#" >
                <b-img
                  left
                  fluid
                  :src="profilePhoto"
                  alt="Profile photo"
                  class="profile-photo mb-3"
                  rounded="circle"
                />
              </a>
              <b-row class="m-3 pb-3 justify-content-center">
                <h1 class="mr-3">{{ name }}</h1>
                <EditProfile
                  :userId="userID"
                  @profile-edited="refreshUser" />
              </b-row>
              <b-row class="m-3 pt-2 justify-content-center">
                <a
                  href="#reading"
                  style="color: #404040; text-decoration: none"
                >
                  <h2 class="mr-3">{{ readingBooks.length }} reading</h2>
                </a>
                <a href="#all" style="color: #404040; text-decoration: none">
                  <h2 v-if="books.length !== 1" class="mx-3">
                    {{ books.length }} books
                  </h2>
                  <h2 v-else class="ml-3">{{ books.length }} book</h2>
                </a>
                <AddBook
                  :userID="userID"
                  class="ml-3"
                  @book-added="refreshBooks"
                />
              </b-row>
            </b-container>
          </div>
        </div>
      </div>
    </div>
    <DisplayBooks
      @book-edited="refreshBooks()"
      :books="books"
      :userID="userID"
      fixButtons="sam"
    />
    <footer>
      <br />
      <a>links</a>
      <br />
      <p class="text-muted">copyright</p>
    </footer>
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
      type: String,
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
      axios
        .get(path)
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
      axios
        .get(path)
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
    showModal(modal) {
      this.$refs[modal].show();
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

<style>
  .display-user {
    background: linear-gradient(75deg,  #E9E9E9, #99D3Df);
  }

  .old-paper {
    background: linear-gradient(75deg,#99D3DF, #E9E9E9);
  }

  .profile-photo {
    width: 10em;
    height: 100%;
  }

  h1 {
    font-size: 2rem !important;
  }

  h2 {
    font-size: 1.5rem !important;
  }

</style>
