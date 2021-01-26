<template>
  <div class="home">
    <!-- Section1: Upload file -->
    <div>
      <b-card id="uploadCard" title="Drag and drop to upload" img-src="../assets/upload.png" img-alt="upload logo" img-top>
        <b-form-file
          :state="formState()"
          accept=".wav"
          placeholder="Choose a file or drop it here..."
          drop-placeholder="Drop file here..."
          v-on:change="checkFileExt"
        ></b-form-file>
        <span v-if="errStatus" style="color:red">{{ errStatus }}</span>
        <br />
        <b-overlay :show="busy" rounded opacity="0.6" spinner-small spinner-variant="primary" class="">
          <b-button id="uploadButton" variant="primary" @click="uploadFile" :disabled="!Boolean(file)">Upload</b-button>
        </b-overlay>
        <b-card-text>
          (Up to 100 Mb)<br /><br />
          *Recommend microphone: Behringer ECM 8000 or Primo EM172<br />
          *Only support Waveform Audio File Format (WAV)<br />
          *Length of the upload file is 1 to 60 seconds<br />
          *Mono channel
        </b-card-text>
        <b-progress v-if="busy" :value="uploadPercentage" :max="100"></b-progress>
      </b-card>
    </div>

    <!-- Section2: table of uploaded files -->
    <div>
      <h3 id="uploadedFiles">Uploaded files{{ ' ' }}<b-spinner v-if="isLoading" type="grow" label="Spinning"></b-spinner></h3>
    </div>
    <div>
      <vue-good-table
        id="table"
        :columns="columns"
        :rows="rows"
        :search-options="{ enabled: true }"
        :sort-options="{
          enabled: true,
          initialSortBy: [
            { field: 'date', type: 'desc' },
            { field: 'time', type: 'desc' },
          ],
        }"
        :pagination-options="{ enabled: true, mode: 'pages', perPageDropdown: [3, 5, 7, 10, 15], perPage: 5 }"
      >
        <!-- Section3: Modal (After click "More details" button) -->
        <!--        @on-selected-rows-change="selectionChanged"-->
        <template slot="table-row" slot-scope="props">
          <span v-if="props.column.field === 'result'">
            <ModalMoreDetail test-prop="88" v-bind:file="props.row" v-on:delete="onDeleteFile" />
          </span>
        </template>
      </vue-good-table>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { uploadFile } from '@/service/upload';
import { getFiles } from '@/service/get';
import { deleteFile } from '@/service/delete';
import { limitSize } from '@/constant/config';
import ModalMoreDetail from '@/components/ModalMoreDetail';

export default {
  name: 'Home',
  components: {
    ModalMoreDetail,
  },
  data() {
    return {
      uploadPercentage: 0,
      busy: false,
      file: null,
      info: null,
      isTouch: false,
      errStatus: null,
      isLoading: true,
      columns: [
        {
          label: 'File Name',
          field: 'filename',
          tdClass: 'body-table',
          width: '20%',
        },
        {
          label: 'Date',
          field: 'date',
          type: 'date',
          dateInputFormat: 'yyyy-MM-dd',
          dateOutputFormat: 'dd/MM/yyyy',
          thClass: 'text-center',
          tdClass: 'text-center body-table',
          width: '20%',
          sortable: true,
        },
        {
          label: 'Time',
          field: 'time',
          thClass: 'text-center',
          tdClass: 'text-center body-table',
          width: '20%',
        },
        {
          label: 'Length',
          field: 'length',
          thClass: 'text-center',
          tdClass: 'text-center body-table',
          width: '20%',
        },
        {
          label: 'Result',
          field: 'result',
          sortable: false,
          thClass: 'text-center',
          tdClass: 'text-center body-table',
          width: '20%',
        },
      ],
      rows: [],
    };
  },
  created() {
    this.getAllFiles();
  },
  methods: {
    async uploadFile() {
      this.busy = true;
      const res = await uploadFile(this.file, event => {
        this.uploadPercentage = Math.round((100 * event.loaded) / event.total);
      });
      if (res.status === 400) {
        this.errStatus = res.data.description;
      } else if (res.status === 201) {
        await this.getAllFiles();
      }
      this.busy = false;
      this.uploadPercentage = 0;
    },
    async getAllFiles() {
      const json = await getFiles();
      this.rows = json.files;
      this.isLoading = false;
    },
    checkFileExt(e) {
      this.isTouch = true;
      this.file = null;
      this.errStatus = null;
      const fileSize = e.target.files[0].size / (1024 * 1024);
      if (e.target.files.length === 0 || e.target.files[0].type !== 'audio/wav') {
        return;
      }
      if (fileSize < limitSize) {
        this.file = e.target.files[0];
        return;
      }
      this.errStatus = 'File size too large';
    },
    formState() {
      if (this.file && !this.errStatus) return true;
      else if (!this.isTouch) return null;
      else return false;
    },
    async onDeleteFile(filename) {
      const res = await deleteFile(filename);
      if (res.status === 404) {
        this.errStatus = res.data.description;
      } else if (res.status === 200) {
        await this.getAllFiles();
      }
    },
  },
};
</script>

<style>
#uploadCard {
  float: none;
  margin: 30px auto 100px;
  max-width: 40rem;
  background: #ebf5ff;
  border: 2px dashed #a1d6fb;
  box-sizing: border-box;
  border-radius: 10px;
}

#uploadCard > img {
  width: 50%;
  margin-left: auto;
  margin-right: auto;
}

#uploadButton {
  margin-top: 10px;
  margin-bottom: 10px;
}

#uploadedFiles {
  margin-bottom: 50px;
}

#table {
  float: none;
  margin: auto auto 70px;
  width: 80%;
}

.body-table {
  vertical-align: middle !important;
}
</style>
