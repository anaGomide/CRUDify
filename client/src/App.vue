<template>
  <v-app>
    <div class="app-container">
      <headerComponent />
      <v-main>
        <router-view />
      </v-main>
      <footerComponent />
    </div>
  </v-app>
</template>

<script>
//UI Components
import headerComponent from "../src/components/layout/header.vue";
import footerComponent from "../src/components/layout/footer.vue";

export default {
  components: {
    headerComponent,
    footerComponent,
  },
};
</script>

<style scoped lang="scss">
.app-container {
  max-height: 95vh;
}
</style>
