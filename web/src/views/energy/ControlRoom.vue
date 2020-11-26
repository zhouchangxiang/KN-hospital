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
        <el-radio-group v-model="conditioner">
          <el-radio-button label="空调1"></el-radio-button>
          <el-radio-button label="空调2"></el-radio-button>
        </el-radio-group>
        <div class="platformContainer marginTop">
          <el-switch v-model="NightLightPattern" active-color="#13ce66"></el-switch>
        </div>
      </el-col>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "ControlRoom",
    data(){
      return {
        area:false,
        conditioner:false,
        NightLightPattern:false
      }
    }
  }
</script>

<style scoped>

</style>
