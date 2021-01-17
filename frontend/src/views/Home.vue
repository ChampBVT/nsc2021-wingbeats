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
      <b-table striped hover :items="items" :fields="fields"></b-table>
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
      fields: [
        {
          key: 'file_name',
          label: 'File Name',
          sortable: true,
        },
        {
          key: 'date',
          label: 'Date',
          sortable: true,
        },
        {
          key: 'time',
          label: 'Time',
          sortable: true,
        },
        {
          key: 'length',
          label: 'Length',
          sortable: true,
        },
        {
          key: 'result',
          label: 'Result',
          sortable: false,
        },
      ],
      items: [
        {
          isActive: true,
          file_name: 'Mosquitoes_1',
          date: '21/06/2019',
          time: '9.09 AM',
          length: '11 seconds',
          result: 'More details',
        },
        {
          isActive: true,
          file_name: 'Mosquitoes_2',
          date: '17/06/2019',
          time: '10.34 AM',
          length: '45 seconds',
          result: 'More details',
        },
        {
          isActive: true,
          file_name: 'Mosquitoes_3',
          date: '08/06/2019',
          time: '6.12 PM',
          length: '2 seconds',
          result: 'More details',
        },
        {
          isActive: true,
          file_name: 'Mosquitoes_4',
          date: '13/05/2019',
          time: '11.55 PM',
          length: '37 seconds',
          result: 'More details',
        },
      ],
    };
  },
  mounted() {},
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
  margin: 30px auto 70px;
  max-width: 40rem;
  background: #ebf5ff;
  border: 2px dashed #a1d6fb;
  box-sizing: border-box;
  border-radius: 10px;
}

.button {
  margin-top: 10px;
  margin-bottom: 10px;
}
</style>
