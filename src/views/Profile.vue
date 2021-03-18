<template>
  <div class="profile">
    <DisplayUser :userID="$route.params.id"/>
  </div>
</template>

<script>
// @ is an alias to /src
import DisplayUser from '@/components/DisplayUser.vue';

export default {
  name: 'Profile',
  components: {
    DisplayUser,
  },
};
</script>
