<template>
  <el-row :gutter="15">
    <el-col :span="24">
      <el-col :span="18">
        <el-radio-group v-model="area">
          <el-radio-button label="病房区"></el-radio-button>
          <el-radio-button label="办公区"></el-radio-button>
        </el-radio-group>
      </el-col>
      <el-col :span="6">
        <div class="platformContainer">9F</div>
        <div class="platformContainer">8F</div>
        <div class="platformContainer">7F</div>
        <div class="platformContainer">6F</div>
        <div class="platformContainer">5F</div>
        <div class="platformContainer">4F</div>
        <div class="platformContainer">3F</div>
        <div class="platformContainer">2F</div>
        <div class="platformContainer">1F</div>
      </el-col>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "floorData",
    data(){
      return {
        area:"病房区",
      }
    }
  }
</script>

<style scoped>

</style>
