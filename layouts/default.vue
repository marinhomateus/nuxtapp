<template>
  <v-app dark>
    <v-navigation-drawer
      :mini-variant="miniVariant"
      :clipped="clipped"
      color="navAndFooter"
      expand-on-hover
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <template v-slot:append>
        <div class="pa-0">
          <v-btn block @click="darkMode" class="mx-auto" color="transparent">
            <v-row align="center" justify="center">
              <v-tooltip v-if="!$vuetify.theme.dark" bottom>
                <template v-slot:activator="{ on }">
                  <v-btn text v-on="on" x-small fab>
                    <v-icon color="black">mdi-moon-waxing-crescent</v-icon>
                  </v-btn>
                </template>
                <span>Dark Mode On</span>
              </v-tooltip>

              <v-tooltip v-else bottom>
                <template v-slot:activator="{ on }">
                  <v-btn text v-on="on" x-small fab>
                    <v-icon color="white">mdi-white-balance-sunny</v-icon>
                  </v-btn>
                </template>
                <span>Dark Mode Off</span>
              </v-tooltip>
            </v-row>
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" color="prometeon" dense fixed app>
      <v-spacer />
      <v-flex class="pa-10 pb-8 text-center">
        <img src="@/assets/images/logoWhite.png" style="max-height: 30px" />
      </v-flex>
      <v-spacer />
    </v-app-bar>
    <v-content class="app">
      <nuxt />
    </v-content>
    <v-footer dense color="navAndFooter" app>
      <v-spacer />
      <span>
        Powered by <strong>Your Team</strong> &copy;
        {{ new Date().getFullYear() }}</span
      >
      <v-spacer />
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "DefaultLayout",
  head() {
    return {
      bodyAttrs: {
        class: "reset-body",
      },
    };
  },
  data() {
    return {
      clipped: true,
      drawer: true,
      fixed: false,
      miniVariant: true,
      items: [
        {
          icon: "mdi-apps",
          title: "Welcome",
          to: "/",
        },
        {
          icon: "mdi-google-maps",
          title: "Maps",
          to: "/maps",
        },
        {
          icon: "mdi-chart-bubble",
          title: "Inspire",
          to: "/windows",
        },
        {
          icon: "mdi-account-group",
          title: "Users",
          to: "/users",
        },
      ],
      right: true,
      rightDrawer: false,
      title: "Vuetify.js",
    };
  },
  methods: {
    darkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    },
  },
};
</script>

<style>
.reset-body {
  margin: 0;
}
</style>
