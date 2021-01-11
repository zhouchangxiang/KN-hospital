<template>
  <el-container class="body-container">
    <!-- 头部 -->
    <el-header class="body-head">
      <div class="head-menu floatLeft">
        <router-link to='/home'>
          <el-image style="width: 135px;" :src="require('../assets/img/logo.png')"></el-image>
        </router-link>
      </div>
      <div class="head-menu floatRight">
        <ul>
          <li>
            <el-tooltip class="head-menu-item" effect="dark" content="全屏" placement="bottom">
              <i :class="isFullScreen?'el-icon-aim':'el-icon-full-screen'" @click="getFullCreeen"></i>
            </el-tooltip>
          </li>
          <li>
            <el-tooltip class="head-menu-item" effect="dark" content="返回主看板" placement="bottom">
              <i class="el-icon-monitor" @click="$router.push('/')"></i>
            </el-tooltip>
          </li>
          <li>
            <el-dropdown class="head-menu-item" trigger="click" @command="handleCommand">
              <span class="el-dropdown-link text-size-16">
                <i class="dotState bg-darkblue"></i>{{ this.$store.state.UserName }}<i class="el-icon-arrow-down el-icon--right text-size-12"></i>
              </span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="a">个人信息</el-dropdown-item>
                <el-dropdown-item command="b" style="text-align: center"><i class="fa fa-power-off"></i></el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
            <el-dialog title="用户信息" :visible.sync="dialogUserVisible" :append-to-body="true" width="50%">
              <el-form>
                <el-form-item label="用户名：">{{ userInfo.Name }}</el-form-item>
                <el-form-item label="工号：">{{ userInfo.WorkNumber }}</el-form-item>
                <el-form-item label="最近登录时间：">{{ userInfo.LastLoginTime }}</el-form-item>
                <el-form-item label="权限：">{{ userInfo.Permissions }}</el-form-item>
              </el-form>
              <span slot="footer" class="dialog-footer">
                <el-button @click="dialogUserVisible = false">取 消</el-button>
              </span>
            </el-dialog>
          </li>
        </ul>
      </div>
    </el-header>
    <el-container>
      <!-- 侧边栏 -->
      <el-aside width="220px" class="left-aside">
        <el-row>
          <el-col :span="24">
            <div :style="selfHeight" class="aside-menu">
            <el-menu class="menu-ul" :collapse="menuIsCollapse">
              <el-menu-item @click="$router.push('/home')"><i class="el-icon-office-building"></i><span slot="title">智慧能源</span></el-menu-item>
            </el-menu>
            <el-menu class="menu-ul" :default-active="defaultActiveUrl" :collapse="menuIsCollapse" :router="true" @select="menuSelect">
              <template v-for="item in mainMenu" :index="item.url">
                <el-menu-item v-if="!item.children" :index="item.url"><i :class="item.icon"></i><span slot="title">{{ item.title }}</span></el-menu-item>
                <el-submenu v-if="item.children" :index="item.title">
                  <template slot="title"><i :class="item.icon"></i><span>{{ item.title }}</span></template>
                  <el-menu-item v-for="(child,childIndex) in item.children" :key="childIndex" :index="child.url"><span style="margin-left:10px;">{{child.title}}</span></el-menu-item>
                </el-submenu>
              </template>
            </el-menu>
          </div>
            <div class="aside-foot">
              <el-button :icon="sideIcon" size="mini" circle @click="iconToggle"></el-button>
            </div>
          </el-col>
        </el-row>
      </el-aside>
      <!-- 页面主体 -->
      <el-main style="clear: both;">
        <transition name="move" mode="out-in">
         <!--渲染子页面-->
          <router-view :key="$route.fullPath"></router-view>
        </transition>
      </el-main>
    </el-container>
  </el-container>
</template>
<script>
  var moment = require('moment');
  import screenfull from "screenfull"
  export default {
    name: 'Index',
    data () {
      return {
        selfHeight:{ //自适应高度
          height:''
        },
        menuIsCollapse: false, //左侧菜单栏是否缩进了
        sideIcon:'el-icon-arrow-left', //左侧菜单栏缩进点击切换图标
        defaultActiveUrl:"",
        dialogUserVisible:false, //是否弹出个人信息
        userInfo:{},
        isFullScreen:false, //是否全屏
        mainMenu:[
          {title: "楼层选择", url: "/floorData", icon:"fa fa-bars"},
          {title: "总控模式", url: "/ControlMode", icon:"el-icon-set-up"},
          {title: "房间控制", url: "/ControlRoom", icon:"el-icon-s-grid"},
          {title: "资产管理", icon:"fa fa-wrench",children:[
              {title:"资产列表", url: "/IntelligentMaintenance"},
              {title:"保养任务", url: "/eqMaintenance"},
            ]
          },
          {title: "按需配能", url: "/EqDetails", icon:"el-icon-files"},
          {title: "病患管理", url: "/Disease", icon:"fa fa-bed"},
          {title: "数据报表", url: "/DataReport", icon:"el-icon-document"},
          {title: "服务诊断", url: "/ServiceDiagnosis", icon:"fa fa-imdb"},
          {title: "系统管理", icon:"el-icon-setting",children:[
              {title:"用户架构", url: "/Organization"},
              {title:"人员管理", url: "/Personnel"},
              {title:"角色管理", url: "/Role"},
              {title:"权限维护", url: "/Permission"},
              {title: "系统日志", url: "/log"},
            ]
          },
        ],
        routeLocation:"",
        websock:null,
        websockVarData:{},
      }
    },
    mounted(){
      this.routeLocation = this.$route.path
    },
    created(){
      document.body.style.zoom = 0
      window.onresize = function(){
        document.body.style.zoom = 0
      }
      window.addEventListener('resize', this.getMenuHeight);
      this.getMenuHeight()
      // if(sessionStorage.getItem("LoginStatus")) {
      //   this.$store.commit('setUser',sessionStorage.getItem('WorkNumber'))
      // }else{
      //   this.$router.push("/login");
      // }
    },
    destroyed() {

    },
    computed:{

    },
    methods:{
      getMenuHeight(){
        if(this.menuIsCollapse){
          this.selfHeight.height = window.innerHeight - 170 + 'px';
        }else{
          this.selfHeight.height = window.innerHeight - 170 + 'px';
        }
      },
      menuSelect(url,title){  //点击菜单跳转时  添加query参数避免相同路由跳转时报错
        this.$router.push({
          query:moment()
        })
      },
      handleCommand(command) {  //判断用户下拉点击
        if(command === "a"){
          this.dialogUserVisible = true
          this.userInfo.LastLoginTime = sessionStorage.getItem('LastLoginTime')
          this.userInfo.WorkNumber = sessionStorage.getItem('WorkNumber')
          this.userInfo.Name = sessionStorage.getItem('UserName')
          this.userInfo.Permissions = JSON.parse(sessionStorage.getItem('Permissions')).join('，')
        }else if(command === "b"){
          this.$store.commit('removeUser')
          this.$router.replace("/login")
        }
      },
      iconToggle() {  //折叠菜单
        this.menuIsCollapse = !this.menuIsCollapse
        this.getMenuHeight()
        if(this.menuIsCollapse){
          this.sideIcon = 'el-icon-arrow-right'
          $(".left-aside").animate({"width":"64px"})
        }else{
          this.sideIcon = 'el-icon-arrow-left'
          $(".left-aside").animate({"width":"220px"})
        }
      },
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
      selectNav(url){
        this.routeLocation = url
        this.$router.replace(url)
      }
    }
  }
</script>

<style>

</style>
