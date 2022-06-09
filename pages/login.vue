<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="8">
        <v-card class="elevation-12">
          <v-window v-model="step">
            <v-window-item :value="1">
              <v-row>
                <v-col cols="12" md="8">
                  <v-card-text class="mt-12">
                    <h1
                      class="text-center display-2"
                      :class="
                        this.$vuetify.theme.dark
                          ? 'white--text'
                          : 'prometeon--text'
                      "
                    >
                      Log in to App
                    </h1>
                    <h4 class="text-center my-16">
                      Ensure your email for registration
                    </h4>
                    <v-form class="mx-6">
                      <v-text-field
                        label="Email"
                        name="Email"
                        prepend-icon="mdi-email"
                        type="text"
                        color="prometeon"
                      />

                      <v-text-field
                        id="password"
                        label="Password"
                        name="password"
                        prepend-icon="mdi-lock"
                        type="password"
                        color="prometeon"
                      />
                    </v-form>
                    <!-- <h3 class="text-center mt-4">Forgot your password ?</h3> -->
                  </v-card-text>
                  <div class="text-center mt-3">
                    <v-btn rounded class="mb-12" color="prometeon" dark
                      >SIGN IN</v-btn
                    >
                  </div>
                </v-col>
                <v-col
                  cols="12"
                  md="4"
                  class="prometeon"
                  style="min-height: 550px"
                >
                  <v-card-text class="white--text mt-12">
                    <v-flex class="pa-auto pb-8 text-center">
                      <img
                        class="mx-auto"
                        src="@/assets/images/logoWhite.png"
                        style="max-height: 30px"
                      />
                    </v-flex>
                    <h1 class="text-center display-1 mt-12">Hello, Friend!</h1>
                    <h5 class="text-center">
                      Enter your personal details and start
                    </h5>
                  </v-card-text>
                  <div class="text-center my-auto">
                    <v-btn rounded outlined dark @click="step++">SIGN UP</v-btn>
                  </div>
                </v-col>
              </v-row>
            </v-window-item>
            <v-window-item :value="2">
              <v-row class="fill-height">
                <v-col
                  cols="12"
                  md="4"
                  class="prometeon"
                  style="min-height: 550px"
                >
                  <v-card-text class="white--text mt-12">
                    <v-flex class="pa-auto pb-8 text-center">
                      <img
                        class="mx-auto"
                        src="@/assets/images/logoWhite.png"
                        style="max-height: 30px"
                      />
                    </v-flex>
                    <h1 class="text-center display-1 mt-12">Welcome Back!</h1>
                    <h5 class="text-center">Do you have an account?</h5>
                  </v-card-text>
                  <div class="text-center">
                    <v-btn rounded outlined dark @click="step--">Sign in</v-btn>
                  </div>
                </v-col>

                <v-col cols="12" md="8">
                  <v-card-text class="mt-12">
                    <h1
                      class="text-center display-2"
                      :class="
                        this.$vuetify.theme.dark
                          ? 'white--text'
                          : 'prometeon--text'
                      "
                    >
                      Create Account
                    </h1>
                    <h4 class="text-center mt-16">
                      Ensure your email for registration
                    </h4>
                    <v-form class="mx-6">
                      <v-text-field
                        label="Name"
                        name="Name"
                        prepend-icon="mdi-account"
                        type="text"
                        color="prometeon"
                      />
                      <v-text-field
                        label="Email"
                        name="Email"
                        prepend-icon="mdi-email"
                        type="text"
                        color="prometeon"
                      />

                      <v-text-field
                        id="password"
                        label="Password"
                        name="password"
                        prepend-icon="mdi-lock"
                        type="password"
                        color="prometeon"
                      />
                    </v-form>
                  </v-card-text>
                  <div class="text-center mt-3">
                    <v-btn rounded class="mb-12" color="prometeon" dark
                      >SIGN UP</v-btn
                    >
                  </div>
                </v-col>
              </v-row>
            </v-window-item>
          </v-window>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    step: 1,
  }),
  props: {
    source: String,
  },
};
</script>

<style scoped>
/* .v-window {
  min-height: 800px;
} */
</style>
