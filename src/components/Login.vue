<template>
<div class="column is-4 is-offset-4">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css" />
    <h3 class="title">Login</h3>
    <div class="box" style="width: 100%">
        <b-form>
            <div class="field">
                <div class="control">
                    <input class="input is-large"
                       v-model="email"
                       type="email"
                       name="email"
                       placeholder="Your Email"
                       autofocus="">
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <input class="input is-large" v-model="password"
                       type="password" name="password" placeholder="Your Password">
                </div>
            </div>
            <div class="field">
                <label class="checkbox">
                    <input type="checkbox">
                    Remember me
                </label>
            </div>
            <b-button @click="Login" class="button is-block is-info is-large is-fullwidth">
                      Login</b-button>
        </b-form>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      email: null,
      password: null,
    };
  },
  methods: {
    Login() {
      const path = 'http://localhost:5000/authenticate';
      axios.get(path, { params: { email: this.email, password: this.password } })
        .then((response) => this.$router.push({ name: 'user', params: { id: response.data.user_id } }));
    },
  },
};
</script>
