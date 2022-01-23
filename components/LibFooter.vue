<template>
  <v-footer :absolute="!fixed" app>
    <v-spacer />
    <span> Mateus Marinho &copy; {{ new Date().getFullYear() }}</span>
    <v-spacer />
  </v-footer>
</template>

<script>
export default {
  name: 'libfooter',
}
</script>
