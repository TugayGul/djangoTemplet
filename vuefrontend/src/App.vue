<template>
  <v-app>
    <v-app-bar app color="red" dark>
      <div class="d-flec allign center">
        <v-toolbar-title>
          <nav class="nav" onclick="">
            <v-toolbar-title style="display: block">Login</v-toolbar-title>
            <v-toolbar-title style="display: block">Sign Up</v-toolbar-title>
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
