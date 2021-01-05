<template>
  <el-container class="body-container">
    <el-header style="height: 90px;position: relative;">
      <div style="position: absolute;top: 20px;left: 20px;color: #fff;">{{ currentTime }}</div>
      <ul class="header-title-list text-center">
        <li class="titleBorderItem" style="height: 30px;"></li>
        <li class="titleBorderItem" style="height: 50px;"></li>
        <li class="titleBorderItem"></li>
        <li>康宁医院空调照明管理系统</li>
        <li class="titleBorderItem"></li>
        <li class="titleBorderItem" style="height: 50px;"></li>
        <li class="titleBorderItem" style="height: 30px;"></li>
      </ul>
      <div style="position: absolute;top: 20px;right: 60px;color: #fff; cursor: pointer;">
        <el-tooltip class="head-menu-item" effect="dark" content="全屏" placement="bottom">
          <i class="color-white text-size-18" :class="isFullScreen?'el-icon-aim':'el-icon-full-screen'" @click="getFullCreeen"></i>
        </el-tooltip>
      </div>
      <div style="position: absolute;top: 20px;right: 20px;color: #fff; cursor: pointer;">
        <el-tooltip class="head-menu-item" effect="dark" content="返回主看板" placement="bottom">
          <i class="color-white text-size-18 el-icon-s-home" @click="$router.push('/')"></i>
        </el-tooltip>
      </div>
      <div style="position: absolute;top: 20px;right: 100px;color: #fff; cursor: pointer;">
        <el-tooltip class="head-menu-item" effect="dark" content="退出登录" placement="bottom">
          <i class="color-white text-size-18 el-icon-circle-close" @click="LoginOut"></i>
        </el-tooltip>
      </div>
    </el-header>
    <el-main style="padding: 15px;">
      <transition name="move" mode="out-in">
        <!--渲染子页面-->
        <router-view :key="$route.fullPath"></router-view>
       </transition>
    </el-main>
    <el-footer style="height: 90px;text-align: center;position: relative;">
      <div class="mainContent">
        <ul class="menu-ul">
          <li v-for="(item,index) in energyMenulist" :key="index" :class="{active:item.url === routeLocation}" @click="selectNav(item.url)">{{ item.name }}</li>
        </ul>
      </div>
      <div style="position: absolute;top: 55px;left: 0;width: 92%;margin-left: 4%;height: 2px;background: #0B5474;"></div>
    </el-footer>
  </el-container>
</template>
<script>
  var moment = require('moment');
  import screenfull from "screenfull"
  export default {
    name: 'Index',
    data () {
      return {
        currentTime:"",
        isFullScreen:false, //是否全屏
        energyMenulist:[
          {name: "楼层选择", url: "/floorData"},
          {name: "总控模式", url: "/ControlMode"},
          {name: "房间控制", url: "/ControlRoom"},
          {name: "数据报表", url: "/DataReport"},
          {name: "智能维保", url: "/IntelligentMaintenance"},
          {name: "服务诊断", url: "/ServiceDiagnosis"},
        ],
        routeLocation:"",
        websock:null,
        websockVarData:{},
      }
    },
    mounted(){
      let _this = this
      this.currentTime = setInterval(() =>{
        _this.currentTime = moment(new Date()).format('YYYY-MM-DD HH:mm:ss');
      },1000);
      this.routeLocation = this.$route.path
    },
    created(){
      document.body.style.zoom = 0;
      window.onresize = function () {
        document.body.style.zoom = 0;
      }
      if(sessionStorage.getItem("LoginStatus")) {
        this.$store.commit('setUser',sessionStorage.getItem('WorkNumber'))
      }else{
        this.$router.push("/login");
      }
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
      LoginOut(){
        this.$store.commit('removeUser')
        this.$router.replace("/login")
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
      selectNav(url){
        this.routeLocation = url
        this.$router.replace(url)
      }
    }
  }
</script>

<style>
  .body-container{
    background: #17749D;
    height: 100%;
  }
  .header-title-list li{
    display: inline-block;
    height: 80px;
    line-height: 80px;
    padding: 0 30px;
    margin: 0 5px;
    background: #0B5474;
    color:#fff;
    vertical-align: top;
    font-size: 20px;
    border-radius: 2px;
  }
  .header-title-list li.titleBorderItem{
    height: 70px;
    padding: 0 10px;
  }
  .mainContent{
    position: absolute;
    width: 100%;
  }
  .menu-ul{
    display: inline-block;
    background: #17749D;
    padding: 0 15px;
    position: relative;
    z-index: 2;
  }
  .menu-ul li{
    display: inline-block;
    height: 60px;
    line-height: 60px;
    padding: 0 15px;
    background: #0B5474;
    color:#fff;
    margin: 30px 5px 0;
    vertical-align: bottom;
    border-radius: 4px;
    cursor: pointer;
  }
  .menu-ul li.active{
    height: 70px;
    line-height: 70px;
    margin-top: 20px;
    background: #20C7B3;
  }
</style>
