<template>
    <div>
        <button v-b-modal="modalId">Edit Book</button>
        <b-modal ref="editBookModal"
                 :id=modalId
                 :title=modalTitle
                 hide-footer>
                 {{book.title}}
                 <br/>
                 <span v-for="(author, index) in book.author" :key="index">{{author}}</span>
                 {{ read[0] }}
                 {{ reading[0] }}
            <b-form @submit="onSubmit" @reset="onReset">
                <b-form-group id="form-read-group">
                    <b-form-checkbox-group v-model="read" id="form-checks">
                        <b-form-checkbox value="true">Read?</b-form-checkbox>
                    </b-form-checkbox-group>
                </b-form-group>
                <b-form-group id="form-reading-group">
                    <b-form-checkbox-group v-model="reading" id="form-checks">
                        <b-form-checkbox value="true">Currently Reading?</b-form-checkbox>
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
      type: Number,
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
      return `edit${this.book.title}Modal`;
    },
    modalId() {
      return `edit-${this.book.title}-Modal`;
    },
  },
  created() {
    this.initBook();
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
      const payload = {
        reader_id: this.userId,
        book_id: this.book.id,
        read,
        reading,
      };
      // console.log(payload);
      // console.log(payload.book_id);
      this.editBook(payload);
    },
    editBook(payload) {
      const path = 'http://localhost:5000/reader_book';
      axios.put(path, payload)
        .then(() => {
          this.$emit('book-edited');
          this.initBook();
        })
        .catch((error) => {
          console.error(error);
          this.initBook();
        });
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      this.initBook();
    },
  },
};
</script>
