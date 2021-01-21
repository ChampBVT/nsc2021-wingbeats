<template>
  <div class="home">
    <!-- Section1: Upload file -->
    <div>
      <b-card class="card" title="Drag and drop to upload" img-src="../assets/upload.png" img-alt="upload logo" img-top>
        <b-form-file
          v-model="file"
          :state="Boolean(file)"
          accept=".wav"
          placeholder="Choose a file or drop it here..."
          drop-placeholder="Drop file here..."
        ></b-form-file>
        <!--    &lt;!&ndash;    <b-progress :value="50" :max="100" animated></b-progress>&ndash;&gt;-->
        <!--    {{ info }} -->

        <b-button class="button" variant="primary" @click="uploadFile" :disabled="!Boolean(file)">Upload File</b-button>
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
    <h3>Uploaded files</h3>
    <div>
      <vue-good-table class="table"
        @on-selected-rows-change="selectionChanged"
        :columns="columns"
        :rows="rows"
        :select-options="{ enabled: true }"
        :search-options="{ enabled: true }"
        :sort-options="{ enabled: true }"
        :pagination-options="{ enabled: true, mode: 'pages', perPageDropdown: [3, 5, 7, 10, 15],  perPage: 5}">
      </vue-good-table>
    </div>

    <!-- Section3: Modal (After click "More details" button) -->
    <div>
      <b-button @click="show=true" variant="primary">More Details</b-button>

      <b-modal
        v-model="show"
        centered title="Result"
        size="lg"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant">
        
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
              <vue-good-table
                  :columns="columns_2"
                  :rows="rows_2"/>
          </div>

        </b-container>

        <template #modal-footer>
          <div>
            <b-button
              variant="primary"
              size="sm"
              class="float-right"
              @click="show=false">Close
            </b-button>
          </div>
        </template>
      </b-modal>
    </div>



    <b-button variant="primary" @click="downloadFile">DownloadAllFile</b-button>

    <b-button variant="primary" @click.prevent="playSound('http://localhost/api/v1/mp3')">Play</b-button>
    <b-button variant="primary" @click.prevent="playSound('http://localhost/api/v1/wav')">Play3</b-button>
    <b-button
      variant="primary"
      @click.prevent="playSound('http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3')"
      >Play2</b-button
    >
    <audio preload="auto" controls="">
      <source src="http://localhost/api/v1/mp3" />
      Your browser does not support the audio tag.
    </audio>
    <audio preload="auto" controls="">
      <source src="http://localhost/api/v1/wav" />
      Your browser does not support the audio tag.
    </audio>
    <audio preload="auto" controls="">
      <source src="http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3" />
      Your browser does not support the audio tag.
    </audio>
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';
import { getTest, uploadTest } from '@/service/upload';

export default {
  name: 'Home',
  components: {
    HelloWorld,
  },
  data() {
    return {
      file: null,
      info: null,
      columns: [
        {
          label: 'File Name',
          field: 'name',
        },
        {
          label: 'Date',
          field: 'date',
          type: 'date',
          dateInputFormat: 'dd-MM-yyyy',
          dateOutputFormat: 'dd/MM/yyyy',
        },
        {
          label: 'Time',
          field: 'time',
          type: 'time',
          timeInputFormat: 'hh:mm',
          timeOutputFormat: 'hh:mm',
        },
        {
          label: 'Length (Second)',
          field: 'length',
          type: 'number',
        },
        {
          label: 'Result',
          field: 'result',
          sortable: false,
        },
      ],
      rows: [
        { id:1, name:"Mosquitoes_1", date: '10-10-2020', time: '11.55 PM', length: 2 , result: 'More Details' },
        { id:2, name:"Mosquitoes_2", date: '31-10-2020', time: '12.00 AM', length: 11 ,result: 'More Details' },
        { id:3, name:"Mosquitoes_3", date: '12-10-2020', time: '10.55 AM', length: 7 ,result: 'More Details' },
        { id:4, name:"Mosquitoes_4", date: '1-10-2020', time: '09.55 PM', length: 41 ,result: 'More Details' },
        { id:5, name:"Mosquitoes_5", date: '4-11-2020', time: '12.55 AM', length: 35 ,result: 'More Details' },
        { id:6, name:"Mosquitoes_6", date: '5-11-2020', time: '01.55 PM', length: 5 ,result: 'More Details' },
      ],
      show: false,
      headerBgVariant: 'primary',
      headerTextVariant: 'light',
      bodyBgVariant: 'light',
      bodyTextVariant: 'dark',
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
          { id:1, species:"Ae.Aegypti", sex: "Female", prob: 0.88},
          { id:2, species:"Ae.Aegypti", sex: "Male", prob: 0.12},
          { id:3, species:"An.Minimus", sex: "Male", prob: 0.62},
          { id:4, species:"An.Dirus", sex: "Female", prob: 0.44},
      ],
    };
  },
  mounted() {
    this.$ref['my-table'].selectedRows;
  },
  methods: {
    uploadFile() {
      uploadTest();
    },
    downloadFile() {
      getTest();
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

<style scoped>
.card {
  float: none;
  margin: 30px auto 100px;
  max-width: 40rem;
  background: #ebf5ff;
  border: 2px dashed #a1d6fb;
  box-sizing: border-box;
  border-radius: 10px;
}

img {
  width: 50%;
  margin-left: auto;
  margin-right: auto;
}

.button {
  margin-top: 10px;
  margin-bottom: 10px;
}

h3 {
  margin-bottom: 50px;
}

.table {
  float: none;
  margin: auto;
  margin-bottom: 70px;
  width: 80%;
}
</style>
