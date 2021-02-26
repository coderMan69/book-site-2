<template>
    <div>
        <div>
            <b-alert dismissible show v-show="showMessage">{{ message }}</b-alert>
        </div>
        <button v-b-modal.book-modal>Add a Book</button>
        <b-modal ref="addBookModal"
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
                            placeholder="Enter author (Seperate multiple with a comma)">
                </b-form-input>
            </b-form-group>
            <b-button type="submit" variant="primary">Submit</b-button>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: '',
      showMessage: false,
      /* Will need to add ability to upload a file if we want user to be
       able to add a book cover */
      book: {
        title: '',
        author: '',
        // cover: '',
      },
    };
  },
  name: 'AddBook',
  emits: ['book-added'],
  methods: {
    initBook() {
      this.book.title = '';
      this.book.author = '';
    },
    addBook(payload) {
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then((res) => {
          this.message = res.data.message;
          this.showMessage = true;
          this.$emit('book-added');
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      const payload = {
        title: this.book.title,
        author: this.book.author.split(','),
      };
      this.addBook(payload);
      this.initBook();
    },
  },
};
</script>
