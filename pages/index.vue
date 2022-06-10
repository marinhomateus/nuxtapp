<template>
  <div class="ma-4">
    <v-row>
      <v-col>
        <v-card class="pa-4">
          <v-card-title primary-title class="justify-center"
            >Dashboard</v-card-title
          >
          <v-card-actions>
            <v-spacer />
            <v-btn dark color="prometeon">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="3">
        <v-card class="mx-auto">
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 my-3">
                Item Title
              </v-list-item-title>
              <Chart1 />
              <v-list-item-subtitle class="mb-3">Profit</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
      <v-col cols="3">
        <v-card class="mx-auto">
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 my-3">
                Item Title
              </v-list-item-title>
              <Chart1 />
              <v-list-item-subtitle class="mb-3"
                >Production</v-list-item-subtitle
              >
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
      <v-col cols="3">
        <v-card class="mx-auto">
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 my-3">
                Item Title
              </v-list-item-title>
              <Chart1 />
              <v-list-item-subtitle class="mb-3">Costs</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
      <v-col cols="3">
        <v-card class="mx-auto">
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 my-3">
                Item Title
              </v-list-item-title>
              <Chart1 />
              <v-list-item-subtitle class="mb-3">Cash</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" lg="4">
        <v-card>
          <v-list-item>
            <v-list-item-content>
              <v-card-title>Item</v-card-title>
            </v-list-item-content>

            <v-icon class="ml-4"> mdi-basket </v-icon>
          </v-list-item>
          <v-list-item>
            <v-list-item-content> </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
      <v-col cols="12" lg="4">
        <v-card>
          <v-list-item>
            <v-list-item-content>
              <v-card-title>Item</v-card-title>
            </v-list-item-content>

            <v-icon class="ml-4"> mdi-basket </v-icon>
          </v-list-item>
          <v-list-item>
            <v-list-item-content> </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
      <v-col cols="12" lg="4">
        <v-card>
          <v-list-item>
            <v-list-item-content>
              <v-card-title>Item</v-card-title>
            </v-list-item-content>

            <v-icon class="ml-4"> mdi-basket </v-icon>
          </v-list-item>
          <v-list-item>
            <v-list-item-content> </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
      <v-col cols="12">
        <v-card>
          <v-list-item>
            <v-list-item-content>
              <v-card-title>Example</v-card-title>
            </v-list-item-content>

            <v-icon class="ml-4"> mdi-basket </v-icon>
          </v-list-item>
          <v-list-item>
            <v-list-item-content class="pa-4">
              <Chart2 />
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
      <v-col cols="7">
        <v-card>
          <v-list-item>
            <v-list-item-content>
              <v-card-title>Item</v-card-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-data-table
                :headers="orderHeaders"
                :items="orders"
              ></v-data-table>
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
      <v-col cols="5">
        <v-card>
          <v-list-item>
            <v-list-item-content>
              <v-card-title>Latest Notifications</v-card-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <Avatars />
            </v-list-item-content>
          </v-list-item>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "Home",
  data: () => ({
    search: "",
    orderHeaders: [
      { text: "Column", value: "title" },
      { text: "Column", value: "price" },
      { text: "Column", value: "send" },
      { text: "Column", value: "date" },
      { text: "Column", value: "status" },
    ],
    orders: [
      {
        title: "Item",
        price: "price",
        send: "qty",
        date: "date",
        status: "status",
      },
      {
        title: "Item",
        price: "price",
        send: "qty",
        date: "date",
        status: "status",
      },
      {
        title: "Item",
        price: "price",
        send: "qty",
        date: "date",
        status: "status",
      },
    ],
    commentsHeaders: [
      { text: "Column", value: "user" },
      { text: "Column", value: "title" },
      { text: "Column", value: "product" },
    ],
    comments: [
      {
        user: "user",
        title: "brand",
        product: "model",
      },
      {
        user: "user",
        title: "brand",
        product: "model",
      },
    ],
  }),
  metaInfo() {
    return {
      title: "Title",
    };
  },
};
</script>
