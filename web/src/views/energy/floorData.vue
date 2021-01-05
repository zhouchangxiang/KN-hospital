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
        <div class="platformContainer" v-for="(item,index) in floorOption" :class="{'bg-darkblue':item.label === floorAct}" :key="index" @click="selectFloor(item.label)">{{ item.label }}</div>
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
        floorAct:"1F",
        floorOption:[
          {label:"1F"},
          {label:"2F"},
          {label:"3F"},
          {label:"4F"},
          {label:"5F"},
          {label:"6F"},
          {label:"7F"},
          {label:"8F"},
          {label:"9F"},
          {label:"10F"},
          {label:"11F"},
          {label:"12F"},
        ]
      }
    },
    methods:{
      selectFloor(label){
        this.floorAct = label
      }
    }
  }
</script>

<style scoped>

</style>
