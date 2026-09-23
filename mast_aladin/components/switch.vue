<template>
  <div style="justify-content: center; display: flex;">
    <v-switch
      v-model="value"
      :label="`${value}`"
      false-value="Sync"
      true-value="Desync"
      hide-details
      color="#FF9D42"
      :disabled="disabled"
    ></v-switch>
  </div>
</template>