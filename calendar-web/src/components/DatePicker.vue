<template>
  <v-row
    absolute
  >
    <v-col cols="6" sm="3" offset="1">
      <v-date-picker
        v-model="dates"
        multiple
        landscape
        color="black"
      ></v-date-picker>
    </v-col>
    <v-col cols="6" sm="3">
      <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="dates"
        transition="scale-transition"
        offset-y
        min-width="290px"
        color="black"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-combobox
            v-model="dates"
            multiple
            chips
            small-chips
            label="Multiple picker in menu"
            prepend-icon="event"
            readonly
            v-bind="attrs"
            v-on="on"
            color="black"
          ></v-combobox>
        </template>
        <v-date-picker v-model="dates" multiple no-title scrollable>
          <v-spacer></v-spacer>
          <v-btn text color="black" @click="menu = false">Cancel</v-btn>
          <v-btn text color="black" @click="$refs.menu.save(dates)">OK</v-btn>
        </v-date-picker>
      </v-menu>
    </v-col>
  </v-row>
</template>
<script>
  export default {
    data: () => ({
      dates: ['2018-09-15', '2018-09-20'],
      menu: false,
    }),
  }
</script>
