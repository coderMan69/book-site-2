<template>
  <div class="container-fluid">
    <table id="BookTable" class="table table-hover">
      <thead>
        <tr>
          <th>Title</th>
          <th>Author</th>
          <th>Cover</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(book, index) in books" :key="index">
          <td>{{book.title}}</td>
          <td><span v-for="(author, index) in book.author" :key="index">
            {{ author }}<br/>
          </span></td>
          <td>
            <div class="box">
              <a href="http://localhost:8080">
                <img v-if="book.cover"
                    :src="book.cover"
                    :title="`${book.title}\n${book.author}`"
                    class="container-fluid">
                <img v-else
                    :src="noCover"
                    :title="`${book.title}\n${book.author}`">
              </a>
            </div>
          </td>
          <td>
            <EditBook @book-edited="emit"
                      :book="book"
                      :userId="userID"
                      :fixButton="fixButtons">Edit</EditBook>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import EditBook from './EditBook.vue';

export default {
  props: {
    books: {
      type: Array,
      required: true,
    },
    userID: {
      type: Number,
      required: true,
    },
    fixButtons: {
      type: String,
      required: true,
    },
  },
  components: {
    EditBook,
  },
  data() {
    return {
      /* eslint-disable global-require */
      noCover: require('../assets/photos/no_cover.jpg'),
    };
  },
  name: 'displayBooks',
  emits: ['book-edited'],
  methods: {
    emit() {
      this.$emit('book-edited');
    },
  },
};
</script>

<style>
  .box {
    width: 200px;
    height: auto;
  }
</style>
