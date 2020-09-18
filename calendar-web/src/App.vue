<template>
  <v-app>
    <v-app-bar
      app
      color="white"
    >
      <div class="d-flex">
        <v-img
          alt="Dodecahedron"
          class="shrink mr-2"
          contain
          src="@/assets/dodecahedron.png"
          transition="scale-transition"
          width="40"
        />
        <h1 class="text-darken-1 ma-2"> dodecahedron calendar </h1>

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
  class="ma-10">
      <DatePicker ref="dates"/>

      <v-row class="pl-7 pr-5">
        <h3>Display</h3>
      </v-row>
      <v-row class="px-7"> 
        <v-radio-group class="horizontal" ref="mainstyle">
          <v-radio label="Filled" value="Filled"></v-radio>
          <v-radio label="Doubled" value="Doubled"></v-radio>
          <v-radio label="Filpped" value="Filpped"></v-radio>
        </v-radio-group>
      </v-row>

      <ColorPicker initialColor="#E1ECF4" ref="maincolor"> </ColorPicker>
      <ColorPicker initialColor="#E45C18" ref="percolor"> </ColorPicker>

      <v-row justify="center" class="ma-4">
          <v-btn dark @click="collectData"> Update</v-btn>
      </v-row>
      </v-card>
    </v-main>

    <v-footer
      absolute
      class="font-weight-medium"
    >
      <v-col
        class="text"
        cols="12"
      >
        {{ new Date().getFullYear() }} — <strong>Amomorning</strong>
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
import DatePicker from './components/DatePicker';
import ColorPicker from './components/ColorPicker'

export default {
  name: 'App',

  components: {
    DatePicker,
    ColorPicker,
  },

  data: () => ({
    //
  }),
  methods: {
    collectData : function() {
      console.log(this.$refs.dates.dates);
      console.log(this.$refs.maincolor.color);
      console.log(this.$refs.percolor.color);
      console.log(this.$refs.mainstyle);

    }
  },
  mounted() {
    console.log(DatePicker.data().dates);
    
  }
};
</script>
