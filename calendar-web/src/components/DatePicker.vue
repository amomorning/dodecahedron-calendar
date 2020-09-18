<template>
<v-row>
    <v-col 
      class="pl-5">
      <v-date-picker
        v-model="dates"
        multiple
        color="black"
      ></v-date-picker>
    </v-col>
  <v-col 
        class="px-10"
  >
    <v-row >
      <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="dates"
        transition="scale-transition"
        offset-y
        min-width="280px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-combobox
            v-model="dates"
            multiple
            chips
            small-chips
            label="Multiple picker in menu"
            prepend-icon="mdi-calendar-blank"
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
      </v-row>

    </v-col>
</v-row> 
</template>
<script>
  export default {
    data: () => ({
      dates: [new Date().getFullYear() +'-09-01'],
      menu: false,
    }),

  }
</script>
