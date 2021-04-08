<template>
<div>
  <div class="tabs">
    <b-nav tabs align="center">
      <b-nav-item id="reading"
                  to="#reading"
                  :active="$route.hash === '#reading' || $route.hash === ''"
                  @click="changeMode(1)">
                  Currently Reading
      </b-nav-item>
      <b-nav-item id="finished"
                  to="#finished"
                  :active="$route.hash === '#finished'"
                  @click="changeMode(2)">
                  Finished
      </b-nav-item>
      <b-nav-item id="all"
                  to="#all"
                  :active="$route.hash === '#all'"
                  v-on:click="changeMode(0)">
                  All Books
      </b-nav-item>
    </b-nav>
  </div>

  <b-card-group deck>
    <b-card
      v-for="(book, index) in books"
      :key="index"
      :img-src="book.cover"
      img-alt="Card Image"
      class="mw-25 p-1 mt-1"
      v-show="showBook(book)">

      <EditBook
        @book-edited="emit"
        :book="book"
        :userId="userID"/>
    </b-card>
  </b-card-group>

<div style="width: 80%; margin: 0 auto;">
  <div
    v-for="(book, index) in books"
    :key="index"
    class="mt-3"
    v-show="showBook(book)">
    <div class="border p-1 m-2" style="float: left; width: 18%;">
      <img
        :src="book.cover"
        :title="`${book.title}\n${authorToString(book)}`"
        class="box">
      <EditBook
          @book-edited="emit"
          :book="book"
          :userId="userID"
          class="mt-2"/>
    </div>
  </div>
</div>
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
                      :userId="userID">Edit</EditBook>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
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
      type: String,
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
      mode: 0,
    };
  },
  name: 'displayBooks',
  emits: ['book-edited'],
  methods: {
    emit() {
      this.$emit('book-edited');
    },
    showBook(book) {
      if (this.mode === 1) {
        return book.reading;
      }
      if (this.mode === 2) {
        return book.read;
      }
      return true;
    },
    changeMode(mode) {
      this.mode = mode;
    },
    authorToString(book) {
      return book.author.join(', ');
    },
  },
};
</script>

<style>
  .box {
    width: 90%;
    height: 90%;
  }
</style>
