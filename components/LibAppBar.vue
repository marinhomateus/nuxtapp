<template>
  <v-app-bar dense fixed app>
    <v-app-bar-nav-icon @click.stop="state.drawer = !state.drawer" />
    <v-spacer />
    <v-toolbar-title v-text="title" />
    <v-spacer />
    <v-btn icon @click.stop="">
      <v-icon>mdi-logout</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: 'libappbar',
  props: ['state'],
  data() {
    return {
      title: 'Vuetify.js',
    }
  },
}
</script>
