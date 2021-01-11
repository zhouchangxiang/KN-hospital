<template>
  <el-row :gutter="15">
    <el-col :span="24">
      <div class="platformContainer">
        <el-row :gutter="15">
          <el-carousel height="130px" indicator-position="none">
            <el-carousel-item>
              <el-col :span="8">
                <div class="carouselCard">
                  <p class="floatLeft marginRight"><i class="fa fa-bolt text-size-24"></i></p>
                  <div class="floatLeft">
                    <p class="marginBottom">今日预估能耗(KWH)</p>
                    <p v-if="yesterday_energy != 0">{{Math.floor(today_energy * yesterday_total_energy/yesterday_energy)}}</p>
                    <p v-else>未知</p>
                  </div>
                </div>
              </el-col>
              <el-col :span="8">
                <div class="carouselCard">
                  <p class="floatLeft marginRight"><i class="el-icon-s-opportunity text-size-24"></i></p>
                  <div class="floatLeft">
                    <p class="marginBottom">综合节能(tce)</p>
                    <p>{{ Math.floor(save_energy * 0.3619) }}</p>
                  </div>
                </div>
              </el-col>
              <el-col :span="8">
                <div class="carouselCard">
                  <p class="floatLeft marginRight"><i class="fa fa-fire text-size-24"></i></p>
                  <div class="floatLeft">
                    <p class="marginBottom">碳排放总值(t)</p>
                    <p>{{ Math.floor(save_energy * 0.6379) }}</p>
                  </div>
                </div>
              </el-col>
            </el-carousel-item>
            <el-carousel-item>
              <el-col :span="8">
                <div class="carouselCard">
                  <p class="floatLeft marginRight"><i class="fa fa-leaf text-size-24"></i></p>
                  <div class="floatLeft">
                    <p class="marginBottom">减排二氧化碳(kg)</p>
                    <p>{{ Math.floor(save_energy * 0.997) }}</p>
                  </div>
                </div>
              </el-col>
              <el-col :span="8">
                <div class="carouselCard">
                  <p class="floatLeft marginRight"><i class="el-icon-cloudy text-size-24"></i></p>
                  <div class="floatLeft">
                    <p class="marginBottom">降低碳粉尘(kg)</p>
                    <p>{{ Math.floor(save_energy * 0.272) }}</p>
                  </div>
                </div>
              </el-col>
              <el-col :span="8">
                <div class="carouselCard">
                  <p class="floatLeft marginRight"><i class="fa fa-tree text-size-24"></i></p>
                  <div class="floatLeft">
                    <p class="marginBottom">相当于种植树(棵)</p>
                    <p>{{ Math.floor(save_energy * 0.6379 / 5.023) }}</p>
                  </div>
                </div>
              </el-col>
            </el-carousel-item>
          </el-carousel>
        </el-row>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  var moment = require('moment');
  export default {
    name: "Home",
    data(){
      return {
        today_energy:"", //今天已经运行小时数的能耗
        yesterday_energy:"", //昨天相同时间小时数的能耗
        yesterday_total_energy:"", //昨天的总能耗
        save_energy:"", //已节约能耗
      }
    },
    created(){
      this.initWebSocket()
    },
    mounted(){

    },
    watch:{

    },
    computed:{

    },
    destroyed() {
      if(this.websock){
        this.websock.close() //离开路由之后断开websocket连接
      }
    },
    methods: {
      initWebSocket(){ //初始化weosocket
        // this.websock = new WebSocket('ws://' + location.host + '/socket');
        this.websock = new WebSocket('ws://127.0.0.1:5002/socket');
        this.websock.onmessage = this.websocketonmessage;
        this.websock.onopen = this.websocketonopen;
        this.websock.onerror = this.websocketonerror;
        this.websock.onclose = this.websocketclose;
      },
      websocketonopen(){ //连接建立之后执行send方法发送数据
        this.websocketsend();
      },
      websocketonerror(){//连接建立失败重连
        console.log("websocket连接失败")
      },
      websocketonmessage(e){ //数据接收
        this.websockVarData = JSON.parse(e.data)
        this.today_energy = this.websockVarData.today_energy
        this.yesterday_energy = this.websockVarData.yesterday_energy
        this.yesterday_total_energy = this.websockVarData.yesterday_total_energy
        this.save_energy = this.websockVarData.save_energy
      },
      websocketsend(Data){//数据发送
        this.websock.send(Data);
      },
      websocketclose(e){  //关闭
        console.log("websocket关闭")
      },
      closesocket(){
        this.websock.close()
      },
    }
  }
</script >
<style scoped>
  .carouselCard{
    background: #008dcd;
    padding: 30px;
    border-radius: 5px;
    color: #fff;
    font-size: 18px;
    overflow: hidden;
  }
  .carouselCard i{
    font-size: 36px;
    margin-top: 10px;
  }
</style>
