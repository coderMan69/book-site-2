<template>
  <div>
    <b-button
      v-b-modal.edit-profile-modal
      variant="outline-light"
      class="py-0"
      @click="initUser"
      >Edit Profile</b-button
    >
    <b-modal
      ref="editProfileModal"
      id="edit-profile-modal"
      title="Edit Profile"
      hide-footer
    >
      <b-form @submit="onSubmit" @reset="onReset">
        <b-form-group
          id="form-name-group"
          label="Name:"
          label-for="form-name-input"
        >
          <b-form-input
            id="form-name-input"
            type="text"
            v-model="user.name"
            required
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-email-group"
          label="Email:"
          label-for="form-email-input"
        >
          <b-form-input
            id="form-email-input"
            type="email"
            v-model="user.email"
            required
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-location-group"
          label="Location:"
          label-for="form-location-input"
        >
          <b-form-input
            id="form-location-input"
            type="text"
            v-model="user.location"
            required
          >
          </b-form-input>
        </b-form-group>
        <b-form-file
          :v-model="file"
          :state="Boolean(file)"
          placeholder="Chose a file or drop it here..."
          drop-placeholder="Drop file here..."
        >
        </b-form-file>
        <div>Selected file: {{ file ? file.name : "" }}</div>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {},
      file: null,
    };
  },
  props: {
    userId: {
      type: String,
      required: true,
    },
  },
  name: 'EditProfile',
  emits: ['profile-edited'],
  methods: {
    initUser() {
      const path = `http://localhost:5000/readers/${this.userId}`;
      console.log(`editProfile ${path}`);
      axios
        .get(path)
        .then((res) => {
          this.user = res.data.user;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.editProfileModal.hide();
      const payload = {
        id: this.user.id,
        name: this.user.name,
        location: this.user.location,
        email: this.user.email,
      };
      this.editUser(payload);
    },
    editUser(payload) {
      const path = 'http://localhost:5000/readers';
      axios
        .put(path, payload)
        .then(() => {
          this.$emit('profile-edited');
        })
        .catch((error) => {
          console.error(error);
        });
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.editProfileModal.hide();
    },
  },
};
</script>
