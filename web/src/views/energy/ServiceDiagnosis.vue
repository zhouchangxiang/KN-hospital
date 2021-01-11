<template>
  <el-row :gutter="15">
    <el-col :span="24">
      <el-row :gutter="25">
        <el-col :span="9">
          <p class="text-size-18 marginBottom">websocket 服务</p>
          <div class="platformContainer" style="height: 400px;">
            <div class="scrollable" style="padding-bottom: 36px;">
              <p v-for="(item,index) in newArr" class="marginBottom">
                <i class="dotState bg-lightgreen" v-if="item.tagData.toLowerCase() != 'NONE' || item.tagData.toLowerCase() != 'INIT'"></i>
                <i class="dotState bg-red" v-if="item.tagData.toLowerCase() === 'NONE' || item.tagData.toLowerCase() === 'INIT'"></i>
                {{ item.tag }}
                <span class="floatRight color-lightgreen" v-if="item.tagData.toLowerCase() != 'NONE' || item.tagData.toLowerCase() != 'INIT'">数据正常</span>
                <span class="floatRight color-red" v-if="item.tagData.toLowerCase() === 'NONE' || item.tagData.toLowerCase() === 'INIT'">无数据</span>
              </p>
            </div>
          </div>
        </el-col>
        <el-col :span="5">
          <p class="text-size-18 marginBottom">OPC 服务</p>
          <div class="platformContainer" style="height: 400px;">
            <p>
              <i class="dotState bg-grayblack" v-if="opcState != '执行正常'"></i>
              <i class="dotState bg-lightgreen" v-if="opcState === '执行正常'"></i>
              <span class="">运行状态</span>
              <span class="floatRight color-grayblack" v-if="opcState != '执行正常'">{{ opcState }}</span>
              <span class="floatRight color-lightgreen" v-if="opcState === '执行正常'">{{ opcState }}</span>
            </p>
          </div>
        </el-col>
        <el-col :span="5">
          <p class="text-size-18 marginBottom">历史数据采集服务</p>
          <div class="platformContainer" style="height: 400px;">
            <p>
              <i class="dotState bg-grayblack" v-if="History_Stutus != '执行正常'"></i>
              <i class="dotState bg-lightgreen" v-if="History_Stutus === '执行正常'"></i>
              <span class="">运行状态</span>
              <span class="floatRight color-grayblack" v-if="History_Stutus != '执行正常'">{{ History_Stutus }}</span>
              <span class="floatRight color-lightgreen" v-if="History_Stutus === '执行正常'">{{ History_Stutus }}</span>
            </p>
          </div>
        </el-col>
        <el-col :span="5">
          <p class="text-size-18 marginBottom">采集服务统计</p>
          <div class="platformContainer" style="height: 400px;">
            <p>
              <span class="">运行成功次数</span>
              <span class="floatRight color-lightgreen">{{ Successcount }}</span>
            </p>
            <p>
              <span class="">运行总次数</span>
              <span class="floatRight color-lightgreen">{{ Totalcount }}</span>
            </p>
          </div>
        </el-col>
        <el-col :span="24">
          <transition name="el-zoom-in-top">
            <p id="newArrInfo" v-show="showNewArr" class="text-size-18">
              共检测tag值 {{ newArrNum }}个，其中未获取到数据的tag有{{ newArrErrorNum }}个，您可以
              <span class="color-darkblue" style="cursor: pointer;" @click="initWebSocket" v-if="!initLoadding">重新检测服务</span>
              <span class="color-darkblue" v-if="initLoadding">即将重新检测...</span>
            </p>
          </transition>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
  var moment = require('moment');
  export default {
    name: "ServiceDiagnosis",
    data(){
      return {
        socket:null,
        websockVarData:{},
        initLoadding:false, //是否在请求和加载tag值
        arr:[],
        newArr:[],
        newArrErrorNum:0,
        newArrNum:0,
        showNewArr:false,
        opcState:'',
        History_Stutus:'',
        Successcount:'',
        Totalcount:'',
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
    methods: {
      initWebSocket(){ //初始化weosocket
        this.initLoadding = true
        // this.websock = new WebSocket('ws://' + location.host + '/socket');
        this.websock = new WebSocket('ws://127.0.0.1:5002/socket');
        // this.websock = new WebSocket('ws://192.168.100.254:5002/socket');
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
        var that = this
        that.arr = []
        that.newArr = []
        that.newArrErrorNum = 0
        that.newArrNum = 0
        that.showNewArr=false
        that.opcState=''
        that.History_Stutus=''
        that.Successcount=''
        that.Totalcount=''
        for(var key in that.websockVarData){//循环返回的对象，并转成数组格式
          that.arr.push({[key]:that.websockVarData[key]})
        }
        that.arr.forEach((item,index) =>{  //循环数组
          (function(index) {
            setTimeout(function() { //延迟循环，依次导入新的数组，实现延迟加载数据的效果
              for(var skey in item){
                that.newArrNum++
                if(item[skey].toLowerCase() != 'NONE' || item[skey].toLowerCase() != 'INIT'){
                  that.newArr.push({
                    tag:skey,
                    tagData:item[skey]
                  })
                }else{
                  that.newArr.push({
                    tag:skey,
                    tagData:item[skey]
                  })
                  that.newArrErrorNum++
                }
                if(skey === 'History_Stutus'){  //历史数据采集的tag值
                  that.History_Stutus = item[skey]
                }
                if(skey === 'Stutus'){ //opc服务的tag值
                  that.opcState = item[skey]
                }
                if(skey === 'Successcount'){ //成功次数
                  that.Successcount = item[skey]
                }
                if(skey === 'Totalcount'){ //总运行次数
                  that.Totalcount = item[skey]
                }
                var scrollHeight = $('.scrollable').prop("scrollHeight");
                $(".scrollable").scrollTop(scrollHeight) //将滚动条移动到最底部
              }
              if(index === that.arr.length -1){
                that.showNewArr = true
              }
            }, (index + 1) * 50);
          })(index)
        })
        that.websock.close()
        that.initLoadding = false
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
</script>
<style>

</style>
