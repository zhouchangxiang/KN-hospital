<script src="../router/index.js"></script>
<template>
  <el-container class="body-container text-size-72">
    <el-header style="height: 250px;background:#eee;">Header</el-header>
    <el-main>Main</el-main>
    <el-footer style="height: 250px;background:#eee;">Footer</el-footer>
  </el-container>
</template>
<script>
  var moment = require('moment');
  import screenfull from "screenfull"
  export default {
    name: 'Index',
    data () {
      return {
        energyMenulist:[
          {name: "系统监控", icon: "el-icon-zoom-in",url:"/SystemMonitor"},
          {name: "智能分析", icon: "el-icon-data-analysis", url: "/IntelligentAnalysis"},
          {name: "智能维保", icon: "el-icon-set-up", url: "/IntelligentMaintenance"},
          {name: "服务诊断", icon: "el-icon-service", url: "/ServiceDiagnosis"},

        ],
        isFullScreen:false, //是否全屏
        websock:null,
        websockVarData:{},
      }
    },
    mounted(){

    },
    created(){

    },
    destroyed() {

    },
    computed:{

    },
    methods:{
      getFullCreeen () {  //全屏
        if (screenfull.isEnabled) {
          screenfull.toggle()
          if(screenfull.isFullscreen){
            this.isFullScreen = false
          }else{
            this.isFullScreen = true
          }
        }
      },
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
        console.log(this.websockVarData)
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
  .body-container{
    background: #17749D;
    height: 100%;
  }
  .menu-ul{
    border: none;
    clear: both;
    overflow: auto;
    scrollbar-width: none;
    -ms-overflow-style: none;
  }
  .menu-ul::-webkit-scrollbar {
    display: none;
  }
</style>
