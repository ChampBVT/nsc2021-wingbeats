<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <b-form-file
      v-model="file"
      :state="Boolean(file)"
      accept=".wav"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
    <!--    &lt;!&ndash;    <b-progress :value="50" :max="100" animated></b-progress>&ndash;&gt;-->
    <!--    {{ info }}-->
    <b-button variant="primary" @click="uploadFile" :disabled="!Boolean(file)">UploadFile</b-button>
    <b-button variant="primary" @click="downloadFile">DownloadAllFile</b-button>
    <b-button variant="primary" @click.prevent="playSound('http://localhost/api/v1/wav')">Play</b-button>
    <audio controls>
      <source src="http://localhost/api/v1/wav" type="audio/mpeg" />
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
