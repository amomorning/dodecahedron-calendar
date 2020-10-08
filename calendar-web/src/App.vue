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
        <ColorPicker initialColor="#C7D3DD" ref="maincolor"></ColorPicker>
        <ColorPicker initialColor="#E45C18" ref="percolor"></ColorPicker>
        <ColorPicker initialColor="#EDF1F4" ref="backcolor"></ColorPicker>

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
var _ = require('lodash');
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
      const data = {
        year : new Array(),
        dates : new Array(),
        maincolor : new String(),
        percolor : new String(),
        backcolor : new String(),
        select : new String(),
      }

      const year = new Set();
      const dates = new Set();
      this.$refs.dates.dates.forEach(function (date) {
        let y, m, d;
        [y, m, d] = _.split(date, '-');
        console.log(y, m+d);
        year.add(y)
        dates.add(m+d)
      });

      data.year = Array.from(year)
      data.dates = Array.from(dates)

      data.maincolor = this.$refs.maincolor.color.substr(1);
      data.percolor = this.$refs.percolor.color.substr(1);
      data.backcolor = this.$refs.backcolor.color.substr(1);
      var select = this.imageSelected;
      data.select = typeof select == "undefined" ? "doubled" : select.alt;

      console.log(data)

      // socket.emit("exchangeParams", "hello");
      let js = JSON.stringify(data);
      console.log(js)
      let path = `http://localhost:5000/api/calenda`;
      path += `?data=${js}`
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
