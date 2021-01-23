<template>
  <div class="home">
    <!-- Section1: Upload file -->
    <div>
      <b-card id="uploadCard" title="Drag and drop to upload" img-src="../assets/upload.png" img-alt="upload logo" img-top>
        <b-form-file
          v-model="file"
          :state="Boolean(file)"
          accept=".wav"
          placeholder="Choose a file or drop it here..."
          drop-placeholder="Drop file here..."
        ></b-form-file>
        <!--    &lt;!&ndash;    <b-progress :value="50" :max="100" animated></b-progress>&ndash;&gt;-->
        <!--    {{ info }} -->

        <b-button id="uploadButton" variant="primary" @click="uploadFile" :disabled="!Boolean(file)">Upload File</b-button>
        <b-card-text>
          (Up to 50 Mb)<br /><br />
          *Recommend microphone: Behringer ECM 8000 or Primo EM172<br />
          *Only support Waveform Audio File Format (WAV)<br />
          *Length of the upload file is 1 to 60 seconds<br />
          *Mono channel
        </b-card-text>
      </b-card>
    </div>

    <!-- Section2: table of uploaded files -->
    <h3 id="Uploadedfiles">Uploaded files</h3>
    <div>
      <vue-good-table
        id="table"
        :columns="columns"
        :rows="rows"
        :select-options="{ enabled: true }"
        :search-options="{ enabled: true }"
        :sort-options="{ enabled: true }"
        :pagination-options="{ enabled: true, mode: 'pages', perPageDropdown: [3, 5, 7, 10, 15], perPage: 5 }"
      >
        <!-- Section3: Modal (After click "More details" button) -->
        <!--        @on-selected-rows-change="selectionChanged"-->
        <template slot="table-row" slot-scope="props">
          <span v-if="props.column.field === 'result'">
            <ModalMoreDetails test-prop="88" 
            v-bind:file="props.row" />
          </span>
        </template>
      </vue-good-table>
    </div>

    <!-- <b-button variant="primary" @click="downloadFile">DownloadAllFile</b-button>
    <b-button variant="primary" @click.prevent="playSound('http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3')"
      >Play2</b-button
    >
    <audio preload="auto" controls="">
      <source src="http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3" />
      Your browser does not support the audio tag.
    </audio>
    <HelloWorld msg="Welcome to Your Vue.js App" /> --> 
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue';
import { uploadTest } from '@/service/upload';
import { getFiles } from '@/service/get';
import ModalMoreDetails from '@/components/ModalMoreDetails';

export default {
  name: 'Home',
  components: {
    // HelloWorld,
    ModalMoreDetails,
  },
  data() {
    return {
      file: null,
      info: null,
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
          thClass: 'text-center', 
          tdClass: 'text-center body-table',
          width: '20%',
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
  mounted() {
    // this.$ref['my-table'].selectedRows;
    this.getAllFiles();
  },
  methods: {
    uploadFile() {
      uploadTest();
    },
    async getAllFiles() {
      const json = await getFiles();
      // console.log(json.files);
      this.rows = json.files;
    },
    playSound(sound) {
      if (sound) {
        const audio = new Audio(sound);
        audio.play();
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

#Uploadedfiles {
  margin-bottom: 50px;
}

#table {
  float: none;
  margin: auto;
  margin-bottom: 70px;
  width: 80%;
}

.body-table {
  vertical-align: middle !important;
}
</style>
