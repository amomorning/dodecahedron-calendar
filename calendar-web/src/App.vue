<template>
  <v-app>
    <v-app-bar app color="white">
      <div class="d-flex">
        <v-img
          alt="Dodecahedron"
          class="shrink mr-2"
          contain
          src="@/assets/dodecahedron.png"
          transition="scale-transition"
          width="40"
        />
        <h1 class="text-darken-1 ma-2">dodecahedron calendar</h1>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/amomorning/dodecahedron-calendar"
        target="_blank"
        text
      >
        <span class="mr-2">Github</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-card
        width="360"
        align="center"
        justify="center"
        elevation="0"
        class="ma-10"
      >
        <DatePicker ref="dates" />

        <vue-select-image
          :dataImages="dataImages"
          h="90px"
          w="90px"
          @onselectimage="onSelectImage"
          ref="mainstyle"
          color="#EEEEEE"
        ></vue-select-image>
        <ColorPicker initialColor="#E1ECF4" ref="maincolor"></ColorPicker>
        <ColorPicker initialColor="#E45C18" ref="percolor"></ColorPicker>

        <v-row justify="center" class="ma-4">
          <v-btn dark @click="collectData">Update</v-btn>
        </v-row>
      </v-card>
    </v-main>

    <v-footer absolute class="font-weight-medium">
      <v-col class="text" cols="12">
        {{ new Date().getFullYear() }} —
        <strong>Amomorning</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
import DatePicker from "./components/DatePicker";
import ColorPicker from "./components/ColorPicker";
import VueSelectImage from "vue-select-image";
import axios from "axios";
// import socket from "./socket"
// add stylesheet
require("vue-select-image/dist/vue-select-image.css");
export default {
  name: "App",

  components: {
    DatePicker,
    ColorPicker,
    VueSelectImage,
  },

  data: () => ({
    dataImages: [
      {
        id: "1",
        src: "/img/filled.png",
        alt: "filled",
      },
      {
        id: "2",
        src: "/img/doubled.png",
        alt: "doubled",
      },
      {
        id: "3",
        src: "/img/flipped.png",
        alt: "flipped",
      },
    ],
  }),
  methods: {
    onSelectImage: function (data) {
      this.imageSelected = data;
    },
    collectData: function () {
      console.log(this.$refs.dates.dates.slice(0));
      console.log(this.$refs.maincolor.color);
      console.log(this.$refs.percolor.color);
      var select = this.imageSelected;
      if (typeof select != "undefined") console.log(select.alt);

      // socket.emit("exchangeParams", "hello");

      const path = `http://localhost:5000/api/calendar`;
      axios
        .get(path, {
          responseType: "blob" //重要
        })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          // let head = response.headers['content-disposition'];
          let fname = Date.now().toString() + ".pdf";
          link.href = url;
          link.setAttribute("download", fname);
          document.body.appendChild(link);
          link.click();

          document.body.removeChild(link);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    console.log(DatePicker.data().dates);
  },
};
</script>
