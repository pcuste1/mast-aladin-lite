<template>
  <v-container
    fluid
    id="input_selector"
  >
    <v-row
        align="end"
        no-gutters
      >
        <v-col cols="6">
          <v-label>{{ title }}</v-label>
        </v-col>
    </v-row>
    <v-row no-gutters>
      <v-col cols="12">
        <v-autocomplete
          v-model="selected_column"
          :items="column_items"
          item-title="title"
          item-value="value"
          :label="label"
          variant="outlined"
          hide-details
          :menu-props="{ attach: '#input_selector' }"
          rounded="0" 
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<style>
#input_selector {
  color-scheme: light dark;
}

#input_selector .v-label {
  color: light-dark(#013b4d, #b4dbe9);
  font-weight: 900;
}

#input_selector .v-list .v-list-item--link:not(.v-list-item--prepend):hover,
#input_selector .v-list .v-list-item--link:not(.v-list-item--prepend):focus,
#input_selector .v-list .v-list-item--active:not(.v-list-item--prepend):focus
{
  /* List item hover */
  background-color: light-dark(#FF9D42, #A75000);
}

#input_selector .v-icon--clickable:not(.v-data-table-header__sort-icon):hover,
#input_selector .v-icon--clickable:not(.v-data-table-header__sort-icon):focus {
  color: light-dark(#FF9D42, #A75000);
}

#input_selector .v-list .v-list-item--active:not(.v-list-item--prepend) {
  /* List item, active item */
  background-color: light-dark(#C6F0FD, #00617E);
}

#input_selector .mdi-close-box:hover,
#input_selector .mdi-close-box:focus {
  color: #A75000;
}
</style>