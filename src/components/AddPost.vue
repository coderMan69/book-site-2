<template>
  <input id="addPost" v-model="post" placeholder="Add a post" @keyup.enter="onSubmit()">
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      post: '',
    };
  },
  name: 'AddPost',
  emits: ['post-added'],
  methods: {
    addPost(payload) {
      const path = 'http://localhost:5000/posts';
      if (payload !== '') {
        axios.post(path, payload)
          .then(() => {
            console.log(`posted ${payload.data}`);
            this.$emit('post-added');
          });
      } else {
        alert('Write something to be posted!');
      }
    },
    onSubmit() {
      // evt.preventDefault();
      const payload = {
        data: this.post,
      };
      this.addPost(payload);
      this.post = '';
    },
  },
};
</script>
