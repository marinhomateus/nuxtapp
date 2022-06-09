<template>
  <v-row class="fill-height" justify="center" align="center">
    <v-col cols="12" sm="12" md="12">
      <v-card flat tile color="transparent">
        <v-window v-model="onboarding" reverse>
          <v-window-item v-for="n in items" :key="`card-${n}`">
            <v-card color="grey" height="85vh">
              <v-img src="https://source.unsplash.com/1920x1090/?nature">
                <v-row class="fill-height" align="center" justify="center">
                  <h1 style="font-size: 5rem" class="white--text">
                    Slide {{ n }}
                  </h1>
                </v-row>
              </v-img>
            </v-card>
          </v-window-item>
        </v-window>

        <v-card-actions class="justify-space-between">
          <v-btn text @click="prev">
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
          <v-item-group v-model="onboarding" class="text-center" mandatory>
            <v-item
              v-for="n in items"
              :key="`btn-${n}`"
              v-slot="{ active, toggle }"
            >
              <v-btn :input-value="active" icon @click="toggle">
                <v-icon>mdi-record</v-icon>
              </v-btn>
            </v-item>
          </v-item-group>
          <v-btn text @click="next">
            <v-icon>mdi-chevron-right</v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "IndexPage",
  data: () => ({
    items: 3,
    onboarding: 0,
  }),

  methods: {
    next() {
      this.onboarding =
        this.onboarding + 1 === this.items ? 0 : this.onboarding + 1;
    },
    prev() {
      this.onboarding =
        this.onboarding - 1 < 0 ? this.items - 1 : this.onboarding - 1;
    },
  },
};
</script>
