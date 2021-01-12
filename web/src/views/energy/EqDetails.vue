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
    <div class="tableContainer">
      <el-form :inline="true">
        <el-form-item label="设备类型">
          <el-radio-group v-model="EquipmentTypeValue">
            <el-radio v-for="(item,index) in EquipmentTypeOptions" :key="index" :label="item.value">{{ item.name }}</el-radio>
          </el-radio-group>
        </el-form-item>
      </el-form>
      <el-form :inline="true">
        <el-form-item label="设备编码">
          <el-input v-model="searchField.EquipmentCode" placeholder="请输入设备编码" size="small"></el-input>
        </el-form-item>
        <el-form-item label="设备名称">
          <el-input v-model="searchField.EquipmentName" placeholder="请输入设备名称" size="small"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" size="small" @click="getEQTable">查询</el-button>
        </el-form-item>
      </el-form>
      <el-table :data="TableData.data" border ref="multipleTable">
        <el-table-column type="selection"></el-table-column>
        <el-table-column prop="EquipmentNo" label="设备编号"></el-table-column>
        <el-table-column prop="EquipmentCode" label="设备编码"></el-table-column>
        <el-table-column prop="EquipmentType" label="设备类型"></el-table-column>
        <el-table-column prop="EquipmentModel" label="设备型号"></el-table-column>
        <el-table-column prop="EquipmentName" label="设备名称"></el-table-column>
        <el-table-column prop="Floor" label="楼层"></el-table-column>
        <el-table-column prop="Area" label="区域"></el-table-column>
        <el-table-column prop="AddTime" label="添加日期"></el-table-column>
        <el-table-column prop="Status" label="设备状态"></el-table-column>
        <el-table-column label="操作" fixed="right" width="120">
          <template slot-scope="scope">
            <el-button size="mini" type="info" @click="handleDetails(scope.$index, scope.row)">详情</el-button>
          </template>
        </el-table-column>
      </el-table>
      <div class="paginationClass">
        <el-pagination background  layout="total, sizes, prev, pager, next, jumper"
         :total="TableData.total"
         :current-page="TableData.offset"
         :page-sizes="[5,10,20]"
         :page-size="TableData.limit"
         @size-change="handleSizeChange"
         @current-change="handleCurrentChange">
        </el-pagination>
        <el-dialog title="设备详情" :visible.sync="EqDetailsDialogVisible" :close-on-click-modal="false" :append-to-body="true" width="60%">
          <el-col :span="8" v-for="(item,index) in currentTagsValue" :key="index">
            <p class="marginBottom"><span>{{ item.label }}：</span><span>{{ item.value }}</span></p>
          </el-col>
          <span slot="footer" class="dialog-footer">
            <el-button @click="closeEqDetails">取 消</el-button>
          </span>
        </el-dialog>
      </div>
    </div>
  </el-row>
</template>

<script>
  export default {
    name: "EqDetails",
    data(){
      return {
        websockVarData:{},
        websock:null,
        TableData:{
          tableName:"Equipment",
          data:[],
          limit:5,
          offset:1,
          total:0,
          multipleSelection:[],
          dialogTitle:"",
          dialogVisible:false,
          field: {
            EquipmentNo:"",
            EquipmentCode:"",
            EquipmentType:"",
            EquipmentModel:"",
            EquipmentName:"",
            Floor:"",
            Area:"",
          }
        },
        EquipmentTypeValue:"",
        EquipmentTypeOptions:[
          {name:"所有",value:""},
          {name:"电表",value:"电表"},
          {name:"水表",value:"水表"},
          {name:"制冷设备",value:"制冷设备"},
          {name:"照明设备",value:"照明设备"},
        ],
        searchField:{
          EquipmentCode:"",
          EquipmentName:"",
        },
        RowData:{},
        EqDetailsDialogVisible:false,
        currentTags:[], //当前选择设备的所有tag点
        currentTagsValue:[], //当前选择设备的所有tag点的数据
      }
    },
    mounted(){
      this.getEQTable()
    },
    methods:{
      getEQTable(){
        var that = this
        var params = {
          tableName: this.TableData.tableName,
          EquipmentType: this.EquipmentTypeValue,
          EquipmentCode:this.searchField.EquipmentCode,
          EquipmentName:this.searchField.EquipmentName,
          limit:this.TableData.limit,
          offset:this.TableData.offset - 1
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res =>{
          if(res.data.code === "200"){
            that.TableData.data = res.data.data.rows
            that.TableData.total = res.data.data.total
          }
        },res =>{
          console.log("请求错误")
        })
      },
      handleSizeChange(limit){
        this.TableData.limit = limit
        this.getEQTable()
      },
      handleCurrentChange(offset){
        this.TableData.offset = offset
        this.getEQTable()
      },
      handleDetails(index,row){
        this.EqDetailsDialogVisible = true
        var that = this
        var params = {
          tableName: "Tags"
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res =>{
          if(res.data.code === "200"){
            that.currentTags = []
            var data = res.data.data.rows
            data.forEach(item =>{
              if(item.EquipmentCode === row.EquipmentCode){
                that.currentTags.push({
                  Tag:item.Tag,
                  Comment:item.Comment,
                })
              }
            })
            that.initWebSocket()
          }
        },res =>{
          console.log("请求错误")
        })
      },
      closeEqDetails(){
        this.EqDetailsDialogVisible = false
        this.closesocket()
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
