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
        @hidden="onClose"
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
            <b-col cols="9" class="border">
              <div style="overflow-wrap: anywhere;">{{ file.filename }}</div>
            </b-col>
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
            <vue-good-table
              :columns="columns_2"
              :rows="rows_2"
              :sort-options="{
                enabled: false,
                initialSortBy: { field: 'prob', type: 'desc' },
              }"
            >
              <div slot="emptystate">
                <div class="text-center">
                  <strong style="vertical-align: super">Predicting... </strong>
                  <b-spinner variant="primary" label="Text Centered"></b-spinner>
                </div>
              </div>
              <template slot="table-row" slot-scope="props">
                <span v-if="props.column.field === 'prob'">
                  <span v-if="props.row.prob >= 70">
                    <span style="color: #7FC008">{{ props.row.prob }}%</span>
                  </span>
                  <span v-if="props.row.prob < 70 && props.row.prob >= 50">
                    <span style="color: #F0DB1B">{{ props.row.prob }}%</span>
                  </span>
                  <span v-if="props.row.prob < 50 && props.row.prob >= 30">
                    <span style="color: #FFA800">{{ props.row.prob }}%</span>
                  </span>
                  <span v-if="props.row.prob < 30">
                    <span style="color: #CF0808">{{ props.row.prob }}%</span>
                  </span>
                </span>
              </template>
            </vue-good-table>
          </div>
        </b-container>

        <template #modal-footer>
          <div style="display: flex; width: 100%; justify-content: space-between;">
            <b-button variant="danger" size="sm" class="float-left" @click="onDelete">Delete</b-button>
            <a @click="downloadFile" target="_self" download>
              <b-button variant="success" size="sm" class="float-right">Download</b-button>
            </a>
          </div>
        </template>
      </b-modal>
    </div>
  </div>
</template>

<script>
import { predictSpecies } from '@/service/predict';
import { CancelToken } from 'axios';
import { getFileHref } from '@/service/get';

export default {
  name: 'ModalMoreDetail',
  props: {
    testProp: String,
    file: Object,
  },
  data() {
    return {
      cancelToken: null,
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
          label: 'Gender',
          field: 'gender',
          sortable: false,
          thClass: 'text-center',
          tdClass: 'text-center',
          width: '30%',
        },
        {
          label: 'Confidence',
          field: 'prob',
          type: 'number',
          thClass: 'text-center',
          tdClass: 'text-center',
          width: '30%',
        },
      ],
      rows_2: [],
    };
  },
  methods: {
    async getPrediction() {
      this.cancelToken = CancelToken.source();
      const json = await predictSpecies(this.file.filename, this.cancelToken);
      this.rows_2 = json.species.filter(sp => sp.prob > 0);
    },
    onDelete() {
      this.$emit('delete', this.file.filename);
      this.show = false;
    },
    onClose() {
      this.show = false;
      this.cancelToken.cancel('Closing modal');
    },
    downloadFile() {
      const fileLink = document.createElement('a');
      fileLink.href = getFileHref(this.file.filename);
      document.body.appendChild(fileLink);
      fileLink.click();
      fileLink.remove();
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
