<template>
    <div>
        <button v-b-modal.edit-profile-modal>Edit Profile</button>
        <b-modal ref="editProfileModal"
                 id="edit-profile-modal"
                 title="Edit Profile"
                 hide-footer>
            <b-form @submit="onSubmit" @reset="onReset">
                <b-form-group id="form-name-group"
                            label="Name:"
                            label-for="form-name-input">
                    <b-form-input id="form-name-input"
                                type="text"
                                v-model="name"
                                required>
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-email-group"
                            label="Email:"
                            label-for="form-email-input">
                    <b-form-input id="form-email-input"
                                type="text"
                                v-model="email"
                                required>
                    </b-form-input>
                </b-form-group>
                <b-form-group id="form-location-group"
                            label="Location:"
                            label-for="form-location-input">
                    <b-form-input id="form-location-input"
                                type="text"
                                v-model="location"
                                required>
                    </b-form-input>
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
  data() {
    return {
      name: '',
      location: '',
      email: '',
    };
  },
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  created() {
    this.initUser();
  },
  name: 'EditProfile',
  emits: ['profile-edited'],
  methods: {
    initUser() {
      const path = `http://localhost:5000/user/${this.id}`;
      axios.get(path)
        .then((res) => {
          this.name = res.data.user.name;
          this.location = res.data.user.location;
          this.email = res.data.user.email;
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
        id: this.id,
        name: this.name,
        location: this.location,
        email: this.email,
      };
      this.editUser(payload);
      this.initUser();
    },
    editUser(payload) {
      const path = `http://localhost:5000/user/${payload.id}`;
      axios.put(path, payload)
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
      this.initUser();
    },
  },
};
</script>
