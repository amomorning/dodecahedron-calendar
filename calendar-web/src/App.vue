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
      <DatePicker/>
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

export default {
  name: 'App',

  components: {
    DatePicker,
  },

  data: () => ({
    //
  }),
};
</script>
