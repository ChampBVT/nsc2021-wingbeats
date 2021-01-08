<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <b-form-file
      v-model="file"
      :state="Boolean(file)"
      placeholder="Choose a file or drop it here..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
    <b-progress :value="50" :max="100" animated></b-progress>
    {{ info }}
    <b-button v-on:click="uploadFile()" variant="primary">Submit</b-button>
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import { getTest, uploadTest } from "@/service/upload";

export default {
  name: "Home",
  components: {
    HelloWorld
  },
  data() {
    return {
      file: null,
      info: null
    };
  },
  mounted() {
    getTest().then(response => (this.info = response));
  },
  methods: {
    uploadFile() {
      uploadTest(this.file);
    }
  }
};
</script>
