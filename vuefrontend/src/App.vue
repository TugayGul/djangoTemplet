<template>
  <v-app>
    <v-app-bar app color="red" dark>
      <div class="d-flec allign center">
        <v-toolbar-title>
          <nav class="navbar-fixed-top">
            <v-toolbar-title style="display: inline-block"
              ><a href="views/LoginPage.vue">Login</a></v-toolbar-title
            >
            <v-toolbar-title style="display: inline-block"
              ><a href="components/HomePage.vue">Home</a></v-toolbar-title
            >
            <v-toolbar-title style="display: inline-block"
              ><a href="views/LoginPage.vue">Sign Up</a></v-toolbar-title
            >
          </nav></v-toolbar-title
        >
      </div>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
