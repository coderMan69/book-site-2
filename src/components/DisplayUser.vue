<template>
  <div>
    <div class=".col-md-4 mb-3">
      <div class="card">
        <div class="card-body">
          <div class="d-flex flex-column align-items-center text-center">
            <img :src="profilePhoto" alt="Admin" class="square" width="175">
            <div class="mt-3">
              <h4>{{ name }}</h4>
              <p class="text-secondary mb-1">{{ location }}</p>
              <p class="text-muted font-size-sm">{{ email }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- <AddPost @post-added="addPost"></AddPost> -->
    <AddPost @post-added="getPosts"></AddPost>
    <div v-for="(post, index) in posts" :key="index" class="post">
      {{ post.message }}
    </div>

    <div class="py-4 px-4">
      <div class="d-flex align-items-center justify-content-between mb-3">
        <h5 class="mb-0">Books</h5>
        <AddBook @book-added="getBooks"></AddBook>
        <a href="#" class="btn btn-link text-muted">Show all</a>
      </div>

      <div class="col-lg-6 mb-2 pr-lg-1" v-for="(book, index) in books" :key="index">
        <img v-if="book.cover" :src="book.cover">
        <p v-else>{{ book.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
// import add-book from './AddBook.js';
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
      // { id: 0, data: 'I Love books' },
      // ],
      /* eslint-disable global-require */
      profilePhoto: require('../assets/photos/sam_test.jpg'),
      friends: [],
      books: [
        /* {
          id: 0,
          title: 'Moby Dick',
          author: 'whale guy',
          cover: '../assets/photos/mobyDick.jpeg',
        }, */
        // {id:1, title:"The Adventures of Huckleberry Finn",
        // author:"Kid guy", cover:"./assets/photos/huckFinn.jpg"}
      ],
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
    /* addBook(book) {
      if (book === '') {
        this.getBooks();
      } else {
        // for (let b in this.books) {
        this.books.forEach((element) => {
          if (element.title === book) {
            alert(`${book} is already in your list of books!`);
            console.log('book in array');
          }
          console.log(`adding ${book}`);
        });
        const newBook = { title: book };
        this.books.push(newBook);
      }
    }, */
    // addBook() {}
    addPost(post) {
      if (post === null || post === '' || post === undefined) {
        console.warn('Attempting to add an empty post');
      } else {
        const newPost = { id: this.posts.length, data: post };
        // Add posts to the beggining of the array to display newest posts first
        this.posts.unshift(newPost);
        // console.log(this.posts)
        // console.log('adding ' + post + ' to ' + this.name);
        console.log(`adding ${post} to ${this.name}`);
      }
    },
  },
};

</script>
