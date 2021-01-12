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
        <el-dialog title="设备详情" :visible.sync="EqDetailsDialogVisible" :close-on-click-modal="false" :append-to-body="true" width="40%">
          <el-form label-width="110px">
            <el-form-item label="设备编号">

            </el-form-item>
          </el-form>
          <span slot="footer" class="dialog-footer">
            <el-button @click="EqDetailsDialogVisible = false">取 消</el-button>
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
        this.RowData = row
        this.EqDetailsDialogVisible = true
        this.getEqTags()
      },
      getEqTags(){
        var that = this
        var params = {
          tableName: "Tags"
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res =>{
          if(res.data.code === "200"){
            console.log(res.data.data.rows)
          }
        },res =>{
          console.log("请求错误")
        })
      }
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
