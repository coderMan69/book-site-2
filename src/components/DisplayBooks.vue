<template>
    <table id="BookTable">
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Image</th>
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
              <a href="http://localhost:8080">
                <img v-if="book.cover"
                    :src="book.cover"
                    :title="`${book.title}\n${book.author}`">
                <img v-else
                      :src="noCover"
                      :title="`${book.title}\n${book.author}`">
              </a>
            </td>
            <td>
              <EditBook @book-edited="emit" :book="book" :userId="userID">Edit</EditBook>
            </td>
          </tr>
        </tbody>
      </table>
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
