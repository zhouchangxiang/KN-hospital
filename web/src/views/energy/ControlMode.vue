<template>
  <el-row :gutter="15">
    <el-col :span="24">
      <el-col :span="18">
        <el-row :gutter="10">
          <el-col :span="24">
            <el-card shadow="never" class="marginBottom">
              <div slot="header">楼层实时数据</div>
              <div style="overflow: hidden;clear: both;min-height:300px;">
                <el-form :inline="true">
                  <el-form-item>
                    <el-radio-group v-model="energyType" size="small" @change="getTagsData">
                      <el-radio-button label="电表"></el-radio-button>
                      <el-radio-button label="水表"></el-radio-button>
                      <el-radio-button label="照明设备"></el-radio-button>
                      <el-radio-button label="制冷设备"></el-radio-button>
                    </el-radio-group>
                  </el-form-item>
                </el-form>
                <el-col :span="8" v-for="(item,index) in currentTagsValue" :key="index">
                  <p class="marginBottom"><span>{{ item.label }}：</span><span>{{ item.value }}</span></p>
                </el-col>
              </div>
            </el-card>
          </el-col>
          <el-col :span="24">
            <el-card shadow="never" class="marginBottom">
              <div slot="header">设备控制</div>
              <div style="overflow: hidden;clear: both;">
                <el-form :inline="true">
                  <el-form-item>
                    <el-radio-group v-model="EqType" size="small">
                      <el-radio-button label="照明设备"></el-radio-button>
                      <el-radio-button label="制冷设备"></el-radio-button>
                    </el-radio-group>
                  </el-form-item>
                </el-form>
              </div>
              <div style="overflow: hidden;clear: both;min-height:220px;" v-if="EqType === '照明设备'">
                <p class="marginBottom">照明控制</p>
                <el-col :span="12" class="marginBottom">
                  <el-switch v-model="allLightOpen" active-text="全开" active-color="#20C7B3"></el-switch>
                </el-col>
                <el-col :span="12" class="marginBottom">
                  <el-switch v-model="allLightClose" active-text="全关" active-color="#20C7B3"></el-switch>
                </el-col>
                <el-col :span="12" class="marginBottom">
                  <el-switch v-model="halfLightOpen" active-text="半开" active-color="#20C7B3"></el-switch>
                </el-col>
                <el-col :span="12" class="marginBottom">
                  <el-switch v-model="halfLightClose" active-text="半开" active-color="#20C7B3"></el-switch>
                </el-col>
              </div>
              <div style="overflow: hidden;clear: both;min-height:100px;" v-if="EqType === '制冷设备'">
                <p class="marginBottom">空调控制</p>
                <el-col :span="12" class="marginBottom">
                  空调1
                  <el-switch v-model="KT1Open" active-color="#20C7B3"></el-switch>
                </el-col>
                <el-col :span="12" class="marginBottom">
                  空调2
                  <el-switch v-model="KT2Open" active-color="#20C7B3"></el-switch>
                </el-col>
              </div>
            </el-card>
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
    name: "ControlMode",
    data(){
      return {
        energyType:"电表",
        EqType:"照明设备",
        allLightOpen:false,
        allLightClose:false,
        halfLightOpen:false,
        halfLightClose:false,
        KT1Open:false,
        KT2Open:false,
        floorAct:"厚德楼1楼",
        floorOption:[
          {label:"厚德楼1楼"},
          {label:"厚德楼2楼"},
          {label:"厚德楼3楼"},
          {label:"厚德楼4楼"},
          {label:"厚德楼5楼"},
          {label:"厚德楼6楼"},
          {label:"厚德楼7楼"},
          {label:"厚德楼8楼"},
          {label:"厚德楼9楼"},
          {label:"厚德楼10楼"},
          {label:"厚德楼11楼"},
          {label:"厚德楼12楼"},
        ],
        currentTags:[],
        websockVarData:{},
        websock:null,
        currentTagsValue:[],
      }
    },
    mounted(){
      this.getTagsData()
    },
    destroyed() {
      if(this.websock){
        this.websock.close() //离开路由之后断开websocket连接
      }
    },
    methods:{
      selectFloor(label){
        this.floorAct = label
        this.closesocket()
        this.getTagsData()
      },
      getTagsData(){
        var that = this
        var params = {
          tableName: "Tags",
          Floor:this.floorAct,
          EquipmentType:this.energyType
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res =>{
          if(res.data.code === "200"){
            that.currentTags = []
            var data = res.data.data.rows
            data.forEach(item =>{
              that.currentTags.push({
                Tag:item.Tag,
                Comment:item.Comment,
              })
            })
            that.initWebSocket()
          }
        },res =>{
          console.log("请求错误")
        })
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
        this.currentTagsValue = []
        this.currentTags.forEach(item =>{
          this.currentTagsValue.push({
            label:item.Comment,
            value:this.websockVarData[item.Tag]
          })
        })
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

<style scoped>

</style>
