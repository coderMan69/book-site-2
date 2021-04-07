<template>
    <div>
        <div>
            <b-alert show v-show="showMessage">{{ message }}</b-alert>
        </div>

        <button v-b-modal.add-book-modal @click="removeMessage">Add a Book</button>
        <b-modal ref="addBookModal"
                 id="add-book-modal"
                 title="Add a new book"
                 hide-footer>
          <!-- ADD functionality for adding an existing and new book
               ADD functionality for cancelling either model -->
          <!-- <b-form @submit.stop.prevent
          @submit="onSubmitExisting" @reset="onReset" @create="newBook"> -->
          <div style="position:relative">
            <b-form-group id="form-existing-title"
                          label="Title:"
                          label-for="form-existing-title-input">
            <b-form-input id="something" v-model="selection"
            style="width:100%" autocomplete="off" required autofocus="true"
                   @keyup.down="down"
                   @keyup.up="up"
                   @keyup.enter="enter"
                   @input="change">
            </b-form-input>
            <ul class="dropdown-menu"
                :style="{ display: showAutoComplete }"
                style="width:100%">
              <li v-for="(item, index) in bookSearch"
                  :key="index"
                  :class="{ active: isActive(index)}"
                  class="dropdown-item">
                {{ item.title }}
              </li>
            </ul>
            </b-form-group>
          </div>
          <b-form-group id="form-read-group" v-show="readyForExistingAdd && !showDropdown">
              <b-form-checkbox-group v-model="book.read" id="form-checks">
                <b-form-checkbox value="true">Read?</b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>
            <b-form-group id="form-reading-group" v-show="readyForExistingAdd && !showDropdown">
              <b-form-checkbox-group v-model="book.reading" id="form-checks">
                <b-form-checkbox value="true">Currently Reading?</b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>
          <div class="row justify-content-end">
          <!-- <b-button v-b-modal.book-modal
                    v-show="addBookButton"
                    @click="newBook"> -->
            <b-button v-b-modal.book-modal
                    v-show="addBookButton"
                    @click="newBook">
            Create Book
          </b-button>
          <b-button variant="primary"
                    v-show="!addBookButton"
                    @click="onSubmitExisting">
            Add Book
          </b-button>
          <b-button class="mr-3" variant="danger" @click="onReset">Cancel</b-button>
          </div>
          <!-- </b-form> -->
        </b-modal>
        <b-modal ref="newBookModal"
                 id="book-modal"
                 title="Add a new book"
                 hide-footer>
            <b-form @submit="onSubmit">
            <b-form-group id="form-title-group"
                          label="Title:"
                          label-for="form-title-input">
                <b-form-input id="form-title-input"
                              type="text"
                              v-model="book.title"
                              required
                              placeholder="Enter title">
                </b-form-input>
            </b-form-group>
            <b-form-group id="form-author-group"
                          label="Author:"
                          label-for="form-author-input">
                <b-form-input id="form-author-input"
                              type="text"
                              v-model="book.author"
                              required
                              placeholder="Enter author">
                </b-form-input>
                <small class="form-text text-muted">
                  If multiple authors, seperate each with a comma
                </small>
            </b-form-group>
            <b-form-group id="form-read-group">
              <b-form-checkbox-group v-model="book.read" id="form-checks">
                <b-form-checkbox value="true">Read?</b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>
            <b-form-group id="form-reading-group">
              <b-form-checkbox-group v-model="book.reading" id="form-checks">
                <b-form-checkbox value="true">Currently Reading?</b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>
            <b-button type="submit" variant="primary">Submit</b-button>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    userID: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      message: '',
      showMessage: false,
      selection: '',
      books: [],
      current: 0,
      showDropdown: false,
      /* Will need to add ability to upload a file if we want user to be
       able to add a book cover */
      book: {
        title: '',
        author: '',
        read: [],
        reading: [],
        // cover: '',
      },
    };
  },
  mounted() {
    this.allBooks();
  },
  computed: {
    showAutoComplete() {
      return this.selection.length > 0 && this.bookSearch.length > 0 && this.showDropdown ? 'block' : 'none';
    },
    // Is what has been typed equal to the beginning of any of the book titles
    bookSearch() {
      return this.books.filter((item) => (
        item.title.substr(0, this.selection.length).toUpperCase()
        === this.selection.toUpperCase()));
    },
    addBookButton() {
      return this.selection.length > 0 && this.bookSearch.length === 0;
    },
    readyForExistingAdd() {
      return this.bookSearch.length === 1;
    },
  },
  name: 'AddBook',
  emits: ['book-added'],
  methods: {
    up() {
      if (this.current > 0) {
        this.current -= 1;
      }
    },
    down() {
      if (this.current < this.bookSearch.length - 1) {
        this.current += 1;
      }
    },
    enter() {
      this.selection = this.bookSearch[this.current].title;
      this.showDropdown = false;
    },
    change() {
      this.current = 0;
      this.showDropdown = true;
    },
    removeMessage() {
      this.showMessage = false;
    },
    allBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        });
    },
    isActive(index) {
      return (this.current === index);
    },
    onSubmitExisting(evt) {
      evt.preventDefault();
      if (this.selection !== '') {
        this.$refs.addBookModal.hide();
        console.log(this.bookSearch.length);
        console.log(this.bookSearch[0].id);
        const read = this.book.read.length > 0 ? 1 : 0;
        const reading = this.book.reading.length > 0 ? 1 : 0;
        const payload = {
          readerID: this.userID,
          bookID: this.bookSearch[0].id,
          read,
          reading,
        };
        console.log(payload.bookID);
        this.addExisting(payload);
      }
    },
    addExisting(payload) {
      const path = 'http://localhost:5000/add_book';
      axios.post(path, payload)
        .then((res) => {
          this.$emit('book-added');
          this.message = res.data.message;
          this.showMessage = true;
          this.initExistingBook();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    onReset() {
      this.$refs.addBookModal.hide();
      this.selection = '';
    },
    initNewBook() {
      this.book.title = '';
      this.book.author = '';
      this.book.read = [];
      this.book.reading = [];
    },
    initExistingBook() {
      this.selection = '';
      this.book.read = [];
      this.book.reading = [];
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then((res) => {
          this.message = res.data.message;
          this.showMessage = true;
          if (res.data.added) {
            this.$emit('book-added');
          }
        });
    },
    newBook(evt) {
      evt.preventDefault();
      this.book.title = this.selection;
      this.book.read = [];
      this.book.reading = [];
      this.$refs.addBookModal.hide();
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.newBookModal.hide();
      const read = this.book.read.length > 0 ? 1 : 0;
      const reading = this.book.reading.length > 0 ? 1 : 0;
      const payload = {
        title: this.book.title,
        author: this.book.author.split(','),
        read,
        reading,
      };
      this.addBook(payload);
      this.initNewBook();
    },
  },
};
</script>
