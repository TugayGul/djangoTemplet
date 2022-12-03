<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h3>List:</h3>
        <v-list>
          <v-list-item-group v-model="selected" color="black" multiple>
            <v-list-item
              v-for="item in productlist"
              :key="item.id"
              @click="updateStatus(item)"
            >
              <v-list-item-icon>
                {{ item.id }}
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>
                  <strong>{{ item.name }}</strong>
                </v-list-item-title>

                <v-list-item-subtitle>
                  {{ item.description }}
                </v-list-item-subtitle>
              </v-list-item-content>

              <v-list-item-action>
                <v-checkbox
                  :input-value="item.is_complete"
                  color="green"
                ></v-checkbox>
              </v-list-item-action>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    selected: [],
    newProduct: {
      title: "",
      description: "",
      titleRules: [
        (v) => !!v || "Title is required",
        (v) => (v && v.length <= 64) || "Title must be less than 64 characters",
      ],
      is_complete: false,
      user: 1,
    },
    productlist: [],
    url: "http://localhost:8000/api/product/",
  }),
  mounted() {
    // Get
    this.getProducts();
  },
  methods: {
    getProducts() {
      axios.get(`${this.url}?ordering=is_complete`).then((response) => {
        this.todoList = response.data;
        response.data.forEach((element, index) => {
          if (!element.is_complete) this.selected.push(index);
          this.$forceUpdate();
        });
      });
    },
    reset() {
      this.$refs.form.reset();
    },
    add() {
      var data = this.newProduct;
      axios.post(this.url, data).then((response) => {
        console.log(response);
        this.getProducts();
      });
    },
    updateStatus(item) {
      item.is_complete = !item.is_complete;
      const url = `${this.url}${item.id}/`;
      var data = {
        is_complete: item.is_complete,
      };
      axios.patch(url, data).then((response) => {
        console.log(response);
        this.getProducts();
      });
    },
  },
};
</script>
