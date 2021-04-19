<template>
  <div>
    <!-- <div class="container"> -->
    <div class="row">
      <div class="col" />
      <div class="tabs col-6 text-center">
        <b-nav tabs align="center">
          <b-nav-item
            id="reading"
            to="#reading"
            :active="$route.hash === '#reading'"
            @click="changedisplayBooksMode(1)"
          >
            Currently Reading
          </b-nav-item>
          <b-nav-item
            id="finished"
            to="#finished"
            :active="$route.hash === '#finished'"
            @click="changedisplayBooksMode(2)"
          >
            Finished
          </b-nav-item>
          <b-nav-item
            id="all"
            to="#all"
            :active="$route.hash === '#all' || $route.hash === ''"
            v-on:click="changedisplayBooksMode(0)"
          >
            All Books
          </b-nav-item>
        </b-nav>
      </div>
      <div class="col text-right mr-3">
        <b-button @click="toggleDisplay">{{ displayFormat }}</b-button>
      </div>
    </div>
    <div
      style="display: flex; flex-wrap: wrap; justify-content: center"
      v-show="!showTable()"
    >
      <div
        v-for="(book, index) in books"
        :key="index"
        class="mt-3 hov"
        v-show="showBook(book)"
      >
        <b-modal
          :id="book.title"
          centered
          hide-backdrop
          hide-footer
          hide-header
          content-class="shadow"
          body-bg-variant="dark"
          body-text-variant="light"
          size="xl"
        >
        <b-img
          right
          class="pl-2"
          :src="book.cover"
          :alt="book.title"
        />
        <h2>Title:</h2>
        <h2><strong>{{ book.title }}</strong></h2>
        <h2>Author:</h2>
        <h2 v-for="(author, index) in book.author" :key=index><strong>{{ author }}</strong></h2>
        </b-modal>
        <div class="border p-1 m-2">
          <img
            :src="book.cover"
            :title="`${book.title}\n${authorToString(book)}`"
            :alt="book.title"
            class="box"
            v-b-modal="book.title"
          />
          <!-- Need v-if to prevent double push of buttons -->
          <EditBook
            @book-edited="emit"
            :book="book"
            :userId="userID"
            v-if="!showTable()"
            class="mt-2"
          />
        </div>
      </div>
    </div>

    <div class="container-fluid" v-show="showTable()">
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
          <tr
            v-for="(book, index) in books"
            :key="index"
            v-show="showBook(book)"
          >
            <td>{{ book.title }}</td>
            <td>
              <span v-for="(author, index) in book.author" :key="index">
                {{ author }}<br />
              </span>
            </td>
            <td>
              <div class="box">
                <a href="#">
                  <img
                    v-if="book.cover"
                    :src="book.cover"
                    :title="`${book.title}\n${book.author}`"
                    :alt="book.title"
                  />
                  <img
                    v-else
                    :src="noCover"
                    :alt="book.title"
                    :title="`${book.title}\n${book.author}`"
                  />
                </a>
                <!-- <b-popover :target="book.title" triggers="hover"
                  placement="top">
                  <template #title>{{book.title}}</template>
                  {{book.author}}
                </b-popover> -->
              </div>
            </td>
            <td>
              <!-- Need v-if to prevent double push of buttons -->
              <EditBook
                @book-edited="emit"
                :book="book"
                :userId="userID"
                v-if="showTable()"
              />
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="modal fade" id="modal1">Hello</div>
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
      displayBooksMode: 0,
      displayFormat: 'Table',
    };
  },
  name: 'displayBooks',
  emits: ['book-edited'],
  methods: {
    emit() {
      this.$emit('book-edited');
    },
    showBook(book) {
      if (this.displayBooksMode === 1) {
        return book.reading;
      }
      if (this.displayBooksMode === 2) {
        return book.read;
      }
      return true;
    },
    // display format holds what format button will be used if the button is clicked
    // So we want to display in the opposite format of what display format holds
    showTable() {
      return this.displayFormat !== 'Table';
    },
    changedisplayBooksMode(displayBooksMode) {
      this.displayBooksMode = displayBooksMode;
    },
    authorToString(book) {
      return book.author.join(', ');
    },
    toggleDisplay() {
      if (this.displayFormat === 'Table') {
        this.displayFormat = 'Covers';
      } else {
        this.displayFormat = 'Table';
      }
    },
  },
};
</script>

<style>

.box {
  width: 15em;
  height: 22em;
}

.hov:hover {
  animation-name: rotate;
  animation-duration: 400ms;
}

@keyframes rotate {
  100% {
    transform: rotate(-360deg);
  }
}
</style>
