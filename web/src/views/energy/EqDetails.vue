<template>
  <el-row :gutter="20">
    <div class="platformContainer">
      <div class="col20 floatLeft">
        <div class="carouselCard">
          <p class="marginBottomS">水耗</p>
          <p class="marginBottomS">1234</p>
          <p>m³</p>
        </div>
      </div>
      <div class="col20 floatLeft">
        <div class="carouselCard">
          <p class="marginBottomS">电耗</p>
          <p class="marginBottomS">1234</p>
          <p>KW·H</p>
        </div>
      </div>
      <div class="col20 floatLeft">
        <div class="carouselCard">
          <p class="marginBottomS">冷耗</p>
          <p class="marginBottomS">0</p>
          <p>KW·H</p>
        </div>
      </div>
      <div class="col20 floatLeft">
        <div class="carouselCard">
          <p class="marginBottomS">暖耗</p>
          <p class="marginBottomS">0</p>
          <p>KW·H</p>
        </div>
      </div>
      <div class="col20 floatLeft">
        <div class="carouselCard">
          <p class="marginBottomS">气耗</p>
          <p class="marginBottomS">0</p>
          <p>m³</p>
        </div>
      </div>
    </div>
  </el-row>
</template>

<script>
  export default {
    name: "EqDetails"
  }
</script>

<style scoped>
  .carouselCard{
    background: #008dcd;
    padding: 30px;
    border-radius: 5px;
    color: #fff;
    font-size: 16px;
    text-align: center;
    overflow: hidden;
  }
</style>
