<script setup>
import { ref } from "vue";
const audioUrl = ref("");
const loading = ref(false);
const testPythonCall = async () => {
  loading.value = true
  const ret = await window.pywebview.api.selectAudioFiles();
  audioUrl.value = ret;
  loading.value = false
};
</script>

<template>
  <div class="card">
    <button type="button" :disabled="loading" @click="testPythonCall">{{loading?'正在生成...':'一键卡点视频'}}</button>
  </div>
</template>

<style scoped>
</style>
