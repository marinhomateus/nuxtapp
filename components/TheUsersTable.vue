<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    sort-by="calories"
    class="elevation-1"
    hide-default-footer
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Users</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
              Add
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="8" md="8">
                    <v-text-field
                      v-model="editedItem.name"
                      label="Username"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="4" md="4">
                    <v-checkbox
                      label="Is Active"
                      v-model="editedItem.protein"
                    ></v-checkbox>
                  </v-col>
                  <v-col cols="12" sm="12" md="12">
                    <v-text-field
                      v-model="editedItem.calories"
                      label="Email"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="12">
                    <v-text-field
                      v-model="editedItem.fat"
                      label="Role"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="12">
                    <v-text-field
                      v-model="editedItem.carbs"
                      label="Location"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="12">
                    <v-text-field
                      v-model="editedItem.commom_name"
                      label="Common Name"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
              <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5"
              >Are you sure you want to delete this item?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete"
                >Cancel</v-btn
              >
              <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.protein="{ item }">
      <v-checkbox v-model="item.protein"></v-checkbox>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
      <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize"> Reset </v-btn>
    </template>
  </v-data-table>
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "Username",
        align: "start",
        sortable: false,
        value: "name",
      },
      { text: "Email", value: "calories" },
      { text: "Role", value: "fat" },
      { text: "Location", value: "carbs" },
      { text: "Is Active", value: "protein" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    desserts: [],
    editedIndex: -1,
    editedItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0,
      commom_name: "",
    },
    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0,
      commom_name: "",
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    initialize() {
      this.desserts = [
        {
          name: "Frozen Yogurt",
          calories: "email@email.com",
          fat: "Admin",
          carbs: "HQ",
          protein: true,
          commom_name: "Fulano",
        },
        {
          name: "Ice cream sandwich",
          calories: "email@email.com",
          fat: "Admin",
          carbs: "HQ",
          protein: true,
          commom_name: "Fulano",
        },
        {
          name: "Eclair",
          calories: "email@email.com",
          fat: "Admin",
          carbs: "HQ",
          protein: true,
          commom_name: "Fulano",
        },
        {
          name: "Cupcake",
          calories: "email@email.com",
          fat: "Admin",
          carbs: "HQ",
          protein: true,
          commom_name: "Fulano",
        },
        {
          name: "Gingerbread",
          calories: "email@email.com",
          fat: "Admin",
          carbs: "HQ",
          protein: true,
          commom_name: "Fulano",
        },
        {
          name: "Jelly bean",
          calories: "email@email.com",
          fat: "Admin",
          carbs: "HQ",
          protein: true,
          commom_name: "Fulano",
        },
        {
          name: "Lollipop",
          calories: "email@email.com",
          fat: "Admin",
          carbs: "HQ",
          protein: true,
          commom_name: "Fulano",
        },
        {
          name: "Honeycomb",
          calories: "email@email.com",
          fat: "Admin",
          carbs: "HQ",
          protein: true,
          commom_name: "Fulano",
        },
        {
          name: "Donut",
          calories: "email@email.com",
          fat: "Admin",
          carbs: "HQ",
          protein: true,
          commom_name: "Fulano",
        },
        {
          name: "KitKat",
          calories: "email@email.com",
          fat: "Admin",
          carbs: "HQ",
          protein: true,
          commom_name: "Fulano",
        },
      ];
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.desserts.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.editedItem);
      } else {
        this.desserts.push(this.editedItem);
      }
      this.close();
    },
  },
};
</script>
