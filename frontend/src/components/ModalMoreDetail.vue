<template>
  <div>
    <b-button
      @click="
        show = true;
        getPrediction();
      "
      variant="primary"
      >More Detail</b-button
    >
    <div class="modal">
      <b-modal
        v-model="show"
        centered
        title="Result"
        size="lg"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
      >
        <b-container fluid="">
          <b-row class="mb-3" cols="2">
            <b-col cols="2" class="font-weight-bold">File Name:</b-col>
            <b-col cols="9" class="border">{{ file.filename }}</b-col>
          </b-row>
          <b-row class="mb-3" cols="4">
            <b-col cols="2" class="font-weight-bold">Date:</b-col>
            <b-col cols="3" class="border">{{ file.date }}</b-col>
            <b-col cols="1"></b-col>
            <b-col cols="2" class="font-weight-bold">Time:</b-col>
            <b-col cols="3" class="border">{{ file.time }}</b-col>
          </b-row>
          <b-row class="mb-3" cols="2">
            <b-col cols="2" class="font-weight-bold">Length:</b-col>
            <b-col cols="3" class="border">{{ file.length }}</b-col>
          </b-row>

          <div>
            <vue-good-table :columns="columns_2" :rows="rows_2">
              <template slot="table-row" slot-scope="props">
                <span v-if="props.column.field === 'prob'">
                  <span v-if="props.row.prob >= 80">
                    <span style="color: #7FC008">{{ props.row.prob }}%</span>
                  </span>
                  <span v-if="props.row.prob < 80 && props.row.prob >= 60">
                    <span style="color: #F0DB1B">{{ props.row.prob }}%</span>
                  </span>
                  <span v-if="props.row.prob < 60 && props.row.prob >= 40">
                    <span style="color: #FFA800">{{ props.row.prob }}%</span>
                  </span>
                  <span v-if="props.row.prob < 40">
                    <span style="color: #CF0808">{{ props.row.prob }}%</span>
                  </span>
                </span>
              </template>
            </vue-good-table>
          </div>
        </b-container>

        <template #modal-footer>
          <div>
            <b-button variant="primary" size="sm" class="float-right" @click="show = false">Close</b-button>
          </div>
        </template>
      </b-modal>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ModalMoreDetail',
  props: {
    testProp: String,
    file: Object,
  },
  data() {
    return {
      show: false,
      headerBgVariant: 'primary',
      headerTextVariant: 'light',
      columns_2: [
        {
          label: 'Species',
          field: 'species',
          sortable: false,
          width: '35%',
        },
        {
          label: 'Sex',
          field: 'sex',
          sortable: false,
          thClass: 'text-center',
          tdClass: 'text-center',
          width: '30%',
        },
        {
          label: 'Probability',
          field: 'prob',
          type: 'number',
          thClass: 'text-center',
          tdClass: 'text-center',
          width: '30%',
        },
      ],
      rows_2: [
        { id: 1, species: 'Ae.Aegypti', sex: 'Female', prob: this.testProp },
        { id: 2, species: 'Ae.Aegypti', sex: 'Male', prob: 22 },
        { id: 3, species: 'An.Minimus', sex: 'Male', prob: 67 },
        { id: 4, species: 'An.Dirus', sex: 'Female', prob: 54 },
      ],
    };
  },
  methods: {
    getPrediction() {
      console.log(this.file.filename);
    },
  },
};
</script>

<style>
.modal-content {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
