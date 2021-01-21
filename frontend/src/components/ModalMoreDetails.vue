<template>
  <div>
    <b-button @click="show = true" variant="primary">More Details</b-button>
    <b-modal v-model="show" centered title="Result" size="lg">
      <!--      :header-bg-variant="headerBgVariant"-->
      <!--      :header-text-variant="headerTextVariant"-->
      <!--      :body-bg-variant="bodyBgVariant"-->
      <!--      :body-text-variant="bodyTextVariant"-->
      <b-container fluid>
        <b-row class="mb-3" cols="4">
          <b-col>File Name:</b-col>
          <b-col>Mosquitoes_1</b-col>
          <b-col>Date:</b-col>
          <b-col>10/10/2020</b-col>
        </b-row>

        <b-row class="mb-3" cols="4">
          <b-col>Time:</b-col>
          <b-col>11.55 PM</b-col>
          <b-col>Length:</b-col>
          <b-col>2 Seconds</b-col>
        </b-row>

        <div>
          <vue-good-table :columns="columns_2" :rows="rows_2" />
        </div>
      </b-container>

      <template #modal-footer>
        <div>
          <b-button variant="primary" size="sm" class="float-right" @click="show = false">Close </b-button>
        </div>
      </template>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: 'ModalMoreDetails',
  props: {
    testProp: String,
  },
  data() {
    return {
      show: false,
      columns_2: [
        {
          label: 'Species',
          field: 'species',
          sortable: false,
        },
        {
          label: 'Sex',
          field: 'sex',
          sortable: false,
        },
        {
          label: 'Probability',
          field: 'prob',
          type: 'percentage',
        },
      ],
      rows_2: [
        { id: 1, species: 'Ae.Aegypti', sex: 'Female', prob: this.testProp },
        { id: 2, species: 'Ae.Aegypti', sex: 'Male', prob: 0.12 },
        { id: 3, species: 'An.Minimus', sex: 'Male', prob: 0.62 },
        { id: 4, species: 'An.Dirus', sex: 'Female', prob: 0.44 },
      ],
    };
  },
};
</script>

<style scoped></style>
