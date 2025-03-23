<template>
  <v-bottom-navigation bg-color="#8D4E98" class="footer-container border rounded" :elevation="5">
    <v-btn
      href="https://www.linkedin.com/in/ana-luiza-gomide-0113/"
      target="_blank"
    >
      <v-icon>mdi-linkedin</v-icon>
      <span>My Linkedin</span>
    </v-btn>

    <v-btn href="https://github.com/anaGomide" target="_blank">
      <v-icon>mdi-github</v-icon>
      <span>My Github</span>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>

.header-container {
  background-color: #8D4E98;
}

</style>