<template>
    <div>
        <b-button
          v-b-modal="modalId"
          @click="initBook"
          variant="outline-dark"
          class="mr-1">Edit Book</b-button>
        <b-button @click="removeBook" variant="outline-danger">Remove Book</b-button>
        <b-modal ref="editBookModal"
                 :id="modalId"
                 :title="modalTitle"
                 hide-footer>
            <b-form @submit="onSubmit" @reset="onReset">
                <b-form-group id="form-title-group"
                              label="Title:"
                              label-for="form-title-input">
                    <b-form-input id="form-title-input"
                                  type="text"
                                  :placeholder="book.title"
                                  required
                                  readonly>
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-author-group"
                              label="Author:"
                              label-for="form-author-input">
                    <b-form-input id="form-author-input"
                                  type="text"
                                  :placeholder="authorsString"
                                  required
                                  readonly>
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-reading-group">
                    <b-form-checkbox-group v-model="reading" id="form-checks">
                        <b-form-checkbox value="true">Reading</b-form-checkbox>
                    </b-form-checkbox-group>
                </b-form-group>
                <b-form-group id="form-read-group">
                    <b-form-checkbox-group v-model="read" id="form-checks">
                        <b-form-checkbox value="true">Finished</b-form-checkbox>
                    </b-form-checkbox-group>
                </b-form-group>
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Cancel</b-button>
            </b-form>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    book: {
      type: Object,
      required: true,
    },
    userId: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      read: [],
      reading: [],
    };
  },
  computed: {
    modalTitle() {
      return `Edit ${this.book.title}`;
    },
    modalRef() {
      return `edit${this.book.title}`;
    },
    modalId() {
      return `edit=${this.book.title}-Modal`;
    },
    authorsString() {
      let returnAuthors = this.book.author[0];
      for (let i = 1; i < this.book.author.length; i += 1) {
        returnAuthors += ', ';
        returnAuthors.concat(this.book.author[i]);
      }
      return returnAuthors;
    },
  },
  methods: {
    initBook() {
      const path = `http://localhost:5000/reader_book/${this.userId}/${this.book.id}`;
      this.read = [];
      this.reading = [];
      axios.get(path)
        .then((res) => {
          if (res.data.read) {
            this.read.push('true');
          }
          if (res.data.reading) {
            this.reading.push('true');
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      const read = this.read.length > 0 ? 1 : 0;
      const reading = this.reading.length > 0 ? 1 : 0;
      console.log(this.book);
      const payload = {
        reader_id: this.userId,
        book_id: this.book.id,
        read,
        reading,
      };
      this.editBook(payload);
    },
    editBook(payload) {
      const path = 'http://localhost:5000/reader_book';
      axios.put(path, payload)
        .then(() => {
          this.$emit('book-edited');
        })
        .catch((error) => {
          console.error(error);
        });
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
    },
    removeBook() {
      const path = 'http://localhost:5000/dl_book';
      const payload = {
        userID: this.userId,
        bookID: this.book.id,
      };
      console.log(payload);
      axios.delete(path, { data: payload })
        .then(() => {
          this.$emit('book-edited');
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
