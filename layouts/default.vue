<template>
  <v-app dark>
    <libnav :state="layout" />
    <libappbar :state="layout" />
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
    <libfooter />
  </v-app>
</template>

<script>
import libnav from '~/components/LibNav.vue'
import libappbar from '~/components/LibAppBar.vue'
import libfooter from '~/components/LibFooter.vue'
export default {
  name: 'DefaultLayout',
  components: {
    libfooter,
    libappbar,
    libnav,
  },
  data() {
    return {
      layout: {
        drawer: false,
      },
    }
  },
}
</script>
