<template>
  <div class="home">
    <DisplayUser/>
  </div>
</template>

<script>
// @ is an alias to /src
import DisplayUser from '@/components/DisplayUser.vue';

export default {
  name: 'Home',
  components: {
    DisplayUser,
  },
};
</script>
