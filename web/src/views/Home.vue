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
    <el-col :span="24">
      <el-row :gutter="15">
        <el-col :span="24">
          <el-form :inline="true">
            <el-form-item>
              <el-radio-group v-model="energyType" size="small">
                <el-radio-button label="水"></el-radio-button>
                <el-radio-button label="电"></el-radio-button>
                <el-radio-button label="冷"></el-radio-button>
                <el-radio-button label="暖"></el-radio-button>
                <el-radio-button label="汽"></el-radio-button>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="起止时间">
              <el-date-picker v-model="startTime" type="datetime" value-format="yyyy-MM-dd HH:mm:ss" placeholder="选择开始时间" size="small"></el-date-picker>
              ~
              <el-date-picker v-model="endTime" type="datetime" value-format="yyyy-MM-dd HH:mm:ss" placeholder="选择结束时间" size="small"></el-date-picker>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="search" size="small">查询</el-button>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col :span="12">
          <el-card shadow="never" class="marginBottom">
            <div slot="header">康宁医院平面展示图</div>
            <div style="overflow: hidden;clear: both;height: 400px;">
              <img src="../assets/img/v2-sketch_03.png" style="width: 100%;max-height: 385px;" alt="">
            </div>
          </el-card>
        </el-col>
        <el-col :span="12">
          <el-card shadow="never" class="marginBottom">
            <div slot="header">能源流向示意图</div>
            <div style="overflow: hidden;clear: both;padding: 30px;">
              <ve-pie :data="pieChartData" height="340px"></ve-pie>
            </div>
          </el-card>
        </el-col>
        <el-col :span="24">
          <el-card shadow="never" class="marginBottom">
            <div slot="header">能耗总况</div>
            <div style="overflow: hidden;clear: both;">
              <ve-histogram :data="histogramChartData" :colors="barColor" :settings="chartSettings"></ve-histogram>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
  var moment = require('moment');
  export default {
    name: "Home",
    data(){
      return {
        websockVarData:{},
        websock:null,
        today_energy:"", //今天已经运行小时数的能耗
        yesterday_energy:"", //昨天相同时间小时数的能耗
        yesterday_total_energy:"", //昨天的总能耗
        save_energy:"", //已节约能耗
        energyType:"水",
        startTime:moment().subtract(1, 'days').format("YYYY-MM-DD HH:mm:ss"),
        endTime:moment().format("YYYY-MM-DD HH:mm:ss"),
        pieChartData:{
          columns: ['设备类型', '能耗'],
          rows: []
        },
        barColor:["#569eee","#3bd0c4","#ffc348","#abd044"],
        chartSettings: {
          showLine: ['去年同比'],
          axisSite: { right: ['去年同比'] },
          yAxisName: ['能耗', '去年同比']
        },
        histogramChartData:{
          columns: ['日期', '已使用', '额定', '预估', '去年同比'],
          rows: [
            { '日期': '2020-01', '已使用': 0, '额定': 0, '预估': 0, '去年同比': 0 },
            { '日期': '2020-02', '已使用': 13430, '额定': 29475.342, '预估': 14356.22, '去年同比': 35.54 },
            { '日期': '2020-03', '已使用': 29329.52, '额定': 32299.02, '预估': 27437.39, '去年同比': 70.83 },
            { '日期': '2020-04', '已使用': 14747.7, '额定': 60882.51, '预估': 15239.35, '去年同比': 18.89 },
            { '日期': '2020-05', '已使用': 181387.27, '额定': 82983.1704, '预估': 175536, '去年同比': 170.49 },
            { '日期': '2020-06', '已使用': 166177.47, '额定': 107196.0864, '预估': 171716.82, '去年同比': 120.92},
            { '日期': '2020-07', '已使用': 185471.15, '额定': 113470.7808, '预估': 179488.17, '去年同比': 127.49 },
            { '日期': '2020-08', '已使用': 163596.98, '额定': 113434.4016, '预估': 163596.93, '去年同比': 112.49 },
            { '日期': '2020-09', '已使用': 137908.2, '额定': 108097.392, '预估': 142505.19, '去年同比': 99.51 },
            { '日期': '2020-10', '已使用': 140505.14, '额定': 101374.8918, '预估': 137908.2, '去年同比': 109.65 },
            { '日期': '2020-11', '已使用': 137908.2, '额定': 60920.4804, '预估': 142505.14, '去年同比': 176.57 },
            { '日期': '2020-12', '已使用': 142505.14, '额定': 19922.4636, '预估': 137908.2, '去年同比': 557.93 },
          ]
        }
      }
    },
    created(){
      this.initWebSocket()
      this.search()
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
      search(){
        var that = this
        var params = {
          energy_type:this.energyType,
          StartTime: this.startTime,
          EndTime: this.endTime,
        }
        this.axios.get("/api/Pie",{
          params: params
        }).then(res =>{
          if(res.data.code === "200"){
            that.pieChartData.rows = res.data.data
          }
        },res =>{
          console.log("请求错误")
        })
      }
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
