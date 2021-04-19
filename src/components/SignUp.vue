<template>
<div class="column is-4 is-offset-4">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css" />
    <h3 class="title">Sign Up</h3>
    <div class="box" style="width: 100%">
          <div class="field">
              <div class="control">
                  <input class="input is-large" v-model="name"
                     type="text" name="name" placeholder="Username">
              </div>
          </div>

          <div class="field">
            <div class="control">
                <input class="input is-large" v-model="email"
                   type="text" name="email" placeholder="Email">
            </div>
          </div>

          <div class="field">
            <div class="control">
                <input class="input is-large" v-model="password"
                   type="password" name="password" placeholder="Password">
            </div>
          </div>
          <div class="field">
          Confirm Password
            <div class="control">
                <input class="input is-large" v-model="password"
                   type="password" name="password" placeholder="Password">
            </div>
          </div>

          <b-button @click="Sign_Up" class="button is-block is-info is-large is-fullwidth">
                    Sign Up</b-button>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SignUp',
  data() {
    return {
      email: null,
      name: null,
      password: null,
    };
  },
  methods: {
    Sign_Up() {
      const path = 'http://localhost:5000/signup';
      axios.get(path, { params: { email: this.email, name: this.name, password: this.password } });
    },
  },
};
</script>
