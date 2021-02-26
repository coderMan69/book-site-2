<template>
    <table id="BookTable">
        <thead>
          <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Image</th>
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
          </tr>
        </tbody>
      </table>
</template>

<script>

export default {
  props: {
    books: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      /* eslint-disable global-require */
      noCover: require('../assets/photos/no_cover.jpg'),
    };
  },
  name: 'displayBooks',
};
</script>
