<template>
  <el-row :gutter="15">
    <el-col :span="24">
      <el-col :span="18">
        <el-radio-group v-model="area">
          <el-radio-button label="病房区"></el-radio-button>
          <el-radio-button label="办公区"></el-radio-button>
        </el-radio-group>
        <el-row :gutter="10" style="margin-top: 30px;">
          <el-col :span="24">
            <el-col :span="4">
              <div class="tableContainer" style="height: 70px;">病房7</div>
              <div class="tableContainer" style="height: 70px;">病房8</div>
              <div class="tableContainer" style="height: 70px;">病房9</div>
              <div class="tableContainer" style="height: 70px;">病房10</div>
            </el-col>
            <el-col :span="2">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
            <el-col :span="2">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
            <el-col :span="2">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
            <el-col :span="2">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
            <el-col :span="2">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
            <el-col :span="2">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
            <el-col :span="4">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
          </el-col>
        </el-row>
        <el-row :gutter="10">
          <el-col :span="24">
            <el-col :span="4">
              <div class="tableContainer" style="height: 160px;">病房11</div>
            </el-col>
            <el-col :span="2">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
            <el-col :span="4">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
            <el-col :span="2">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
            <el-col :span="2">
              <div class="tableContainer" style="height: 160px;"></div>
            </el-col>
            <el-col :span="4">
              <div class="tableContainer" style="height: 160px;">康复活动区</div>
            </el-col>
          </el-col>
        </el-row>
      </el-col>
      <el-col :span="6">
        <div class="platformContainer">
          <p>夜灯模式</p>
          <p class="marginTop">
            <el-switch v-model="NightLightPattern" active-color="#13ce66"></el-switch>
          </p>
          <el-divider></el-divider>
          <p class="marginBottom">病房照明控制</p>
          <el-col :span="12" class="marginBottom">
            <el-switch v-model="allOpen" active-text="全开" active-color="#20C7B3"></el-switch>
          </el-col>
          <el-col :span="12" class="marginBottom">
            <el-switch v-model="allClose" active-text="全关" active-color="#20C7B3"></el-switch>
          </el-col>
          <el-col :span="12" class="marginBottom">
            <el-switch v-model="halfOpen" active-text="半开" active-color="#20C7B3"></el-switch>
          </el-col>
          <el-col :span="12" class="marginBottom">
            <el-switch v-model="halfClose" active-text="半开" active-color="#20C7B3"></el-switch>
          </el-col>
        </div>
      </el-col>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "ControlMode",
    data(){
      return {
        area:"病房区",
        NightLightPattern:false,
        allOpen:false,
        allClose:false,
        halfOpen:false,
        halfClose:false,
      }
    }
  }
</script>

<style scoped>

</style>
