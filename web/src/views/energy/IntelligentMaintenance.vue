<template>
  <el-row :gutter="15">
    <el-col :span="24">
      <el-row :gutter="15">
        <el-col :span="24" v-if="!showEqDetails">
          <div class="page-title">资产列表</div>
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
            <el-form :inline="true">
              <el-form-item>
                <el-button type="primary" size="small" @click="add">新增</el-button>
              </el-form-item>
              <el-form-item>
                <el-button type="danger" size="small" @click="del">删除</el-button>
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
              <el-table-column label="操作" fixed="right" width="230">
                <template slot-scope="scope">
                  <el-button size="mini" type="primary" @click="handleXJ(scope.$index, scope.row)">巡检</el-button>
                  <el-button size="mini" type="info" @click="handleDetails(scope.$index, scope.row)">详情</el-button>
                  <el-button size="mini" type="success" @click="handleBY(scope.$index, scope.row)">保养</el-button>
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
            </div>
            <el-dialog :title="TableData.dialogTitle" :visible.sync="TableData.dialogVisible" :close-on-click-modal="false" :append-to-body="true" width="40%">
              <el-form label-width="110px">
                <el-form-item label="设备编号">
                  <el-input v-model="TableData.field.EquipmentNo"></el-input>
                </el-form-item>
                <el-form-item label="设备编码">
                  <el-input v-model="TableData.field.EquipmentCode"></el-input>
                </el-form-item>
                <el-form-item label="设备类型">
                  <el-input v-model="TableData.field.EquipmentType"></el-input>
                </el-form-item>
                <el-form-item label="设备型号">
                  <el-input v-model="TableData.field.EquipmentModel"></el-input>
                </el-form-item>
                <el-form-item label="设备名称">
                  <el-input v-model="TableData.field.EquipmentName"></el-input>
                </el-form-item>
                <el-form-item label="楼层">
                  <el-input v-model="TableData.field.Floor"></el-input>
                </el-form-item>
                <el-form-item label="区域">
                  <el-input v-model="TableData.field.Area"></el-input>
                </el-form-item>
              </el-form>
              <span slot="footer" class="dialog-footer">
                <el-button @click="TableData.dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="save">保存</el-button>
              </span>
            </el-dialog>
            <el-dialog title="巡检" :visible.sync="XJdialogVisible" :close-on-click-modal="false" :append-to-body="true" width="40%">
              <el-form label-width="110px">
                <el-form-item label="设备编号">
                  <el-input v-model="XJField.EquipmentNo"></el-input>
                </el-form-item>
                <el-form-item label="计划状态">
                  <el-select v-model="XJField.Status">
                    <el-option label="正常" value="正常"></el-option>
                    <el-option label="预警" value="预警"></el-option>
                    <el-option label="故障" value="故障"></el-option>
                    <el-option label="保养" value="保养"></el-option>
                  </el-select>
                </el-form-item>
                <el-form-item label="巡检时间">
                  <el-date-picker v-model="XJField.InspectionTime" type="datetime" value-format="yyyy-MM-dd HH:mm:ss" placeholder="选择日期时间"></el-date-picker>
                </el-form-item>
                <el-form-item label="注释">
                  <el-input v-model="XJField.Comment"></el-input>
                </el-form-item>
              </el-form>
              <span slot="footer" class="dialog-footer">
                <el-button @click="XJdialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="saveXJ">立即提交</el-button>
              </span>
            </el-dialog>
            <el-dialog title="保养" :visible.sync="BYdialogVisible" :close-on-click-modal="false" :append-to-body="true" width="40%">
              <el-form label-width="110px">
                <el-form-item label="设备编号">
                  <el-input v-model="BYField.EquipmentNo"></el-input>
                </el-form-item>
                <el-form-item label="保养时间">
                  <el-date-picker v-model="BYField.BaoYangTime" type="datetime" value-format="yyyy-MM-dd HH:mm:ss" placeholder="选择日期时间"></el-date-picker>
                </el-form-item>
                <el-form-item label="注释">
                  <el-input v-model="BYField.Comment"></el-input>
                </el-form-item>
              </el-form>
              <span slot="footer" class="dialog-footer">
                <el-button @click="BYdialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="saveBY">立即提交</el-button>
              </span>
            </el-dialog>
          </div>
        </el-col>
        <el-col :span="24" v-if="showEqDetails">
          <el-card shadow="never" class="marginBottom">
            <div slot="header">设备参数</div>
            <div style="overflow: hidden;clear: both;">
              <el-col :span="6">
                <label>设备名称</label>
                <span>{{ RowData.EquipmentName }}</span>
              </el-col>
              <el-col :span="6">
                <label>设备编号</label>
                <span>{{ RowData.EquipmentNo }}</span>
              </el-col>
              <el-col :span="6">
                <label>设备类型</label>
                <span>{{ RowData.EquipmentType }}</span>
              </el-col>
              <el-col :span="6">
                <label>设备型号</label>
                <span>{{ RowData.EquipmentModel }}</span>
              </el-col>
            </div>
          </el-card>
          <el-card shadow="never" class="marginBottom">
            <div slot="header">全生命周期</div>
            <el-table :data="XJTableData.data" border>
              <el-table-column type="selection"></el-table-column>
              <el-table-column prop="EquipmentNo" label="设备编号"></el-table-column>
              <el-table-column prop="InspectionTime" label="巡检时间"></el-table-column>
              <el-table-column prop="Status" label="计划状态"></el-table-column>
              <el-table-column prop="Comment" label="注释"></el-table-column>
            </el-table>
            <div class="paginationClass">
              <el-pagination background  layout="total, sizes, prev, pager, next, jumper"
               :total="XJTableData.total"
               :current-page="XJTableData.offset"
               :page-sizes="[5,10,20]"
               :page-size="XJTableData.limit"
               @size-change="handleXJSizeChange"
               @current-change="handleXJCurrentChange">
              </el-pagination>
            </div>
          </el-card>
          <el-card shadow="never">
            <div slot="header">设备运行趋势变化图</div>
            <ve-histogram :data="chartData"></ve-histogram>
          </el-card>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
  var moment = require('moment');
  export default {
    name: "IntelligentMaintenance",
    data(){
      return {
        showEqDetails:false,
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
        XJdialogVisible:false,
        XJField:{
          EquipmentNo:"",
          InspectionTime:"",
          Status:"",
          Comment:"",
        },
        BYdialogVisible:false,
        BYField:{
          EquipmentNo:"",
          BaoYangTime:"",
          Comment:"",
        },
        XJTableData:{
          tableName:"Inspection",
          data:[],
          limit:5,
          offset:1,
          total:0,
        },
        chartData:{
          columns: ['时间', '故障次数', '预警次数', '保养次数'],
          rows: [
            {"时间":"2019-04","故障次数":3,"预警次数":0,"保养次数":0},
            {"时间":"2019-05","故障次数":0,"预警次数":1,"保养次数":0},
            {"时间":"2019-07","故障次数":0,"预警次数":1,"保养次数":0},
            {"时间":"2019-11","故障次数":2,"预警次数":0,"保养次数":0},
            {"时间":"2020-03","故障次数":0,"预警次数":0,"保养次数":0},
          ]
        }
      }
    },
    created(){
      this.getEQTable()
    },
    mounted(){

    },
    watch:{

    },
    computed:{

    },
    methods: {
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
      add(){
        this.TableData.dialogVisible = true
        this.TableData.dialogTitle = "新增"
      },
      save(){
        if(this.TableData.dialogTitle === "新增"){
          var params = {
            tableName:this.TableData.tableName,
            EquipmentNo:this.TableData.field.EquipmentNo,
            EquipmentCode:this.TableData.field.EquipmentCode,
            EquipmentType:this.TableData.field.EquipmentType,
            EquipmentModel:this.TableData.field.EquipmentModel,
            EquipmentName:this.TableData.field.EquipmentName,
            Floor:this.TableData.field.Floor,
            Area:this.TableData.field.Area,
            AddTime:moment().format("YYYY-MM-DD HH:mm:ss")
          }
          this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
              this.getEQTable()
            }else{
              this.$message({
                type: 'info',
                message: res.data.message
              });
            }
            this.TableData.dialogVisible = false
          },res =>{
            console.log("请求错误")
          })
        }
      },
      del(){
        var params = {tableName:this.TableData.tableName}
          var mulId = []
          if(this.TableData.multipleSelection.length >= 1){
            this.TableData.multipleSelection.forEach(item =>{
              mulId.push({id:item.ID});
            })
            params.delete_data = JSON.stringify(mulId)
            this.$confirm('确定删除所选记录？', '提示', {
              distinguishCancelAndClose:true,
              type: 'warning'
            }).then(()  => {
              this.axios.delete("/api/CUID",{
                params: params
              }).then(res =>{
                if(res.data.code === "200"){
                  this.$message({
                    type: 'success',
                    message: res.data.message
                  });
                }
                this.getEQTable()
              },res =>{
                console.log("请求错误")
              })
            }).catch(() => {
              this.$message({
                type: 'info',
                message: '已取消删除'
              });
            });
          }else{
            this.$message({
              message: '至少选择一条数据进行删除',
              type: 'warning'
            });
          }
      },
      handleXJ(index,row){
        this.XJdialogVisible = true
        this.RowData = row
        this.XJField.EquipmentNo = row.EquipmentNo
      },
      handleDetails(index,row){
        this.RowData = row
        this.showEqDetails = true
        this.getXJTableData()
      },
      handleBY(index,row){
        this.BYdialogVisible = true
        this.RowData = row
        this.BYField.EquipmentNo = row.EquipmentNo
      },
      saveXJ(){
        var params = {
          tableName:"Inspection",
          EquipmentNo:this.XJField.EquipmentNo,
          InspectionTime:this.XJField.InspectionTime,
          Status:this.XJField.Status,
          Comment:this.XJField.Comment,
        }
        this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
          if(res.data.code === "200"){
            this.$message({
              type: 'success',
              message: res.data.message
            });
          }else{
            this.$message({
              type: 'info',
              message: res.data.message
            });
          }
          this.XJdialogVisible = false
        },res =>{
          console.log("请求错误")
        })
      },
      saveBY(){
        var params = {
          tableName:"BaoYang",
          EquipmentNo:this.RowData.EquipmentNo,
          BaoYangTime:this.BYField.BaoYangTime,
          Comment:this.BYField.Comment,
        }
        this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
          if(res.data.code === "200"){
            this.$message({
              type: 'success',
              message: res.data.message
            });
          }else{
            this.$message({
              type: 'info',
              message: res.data.message
            });
          }
          this.BYdialogVisible = false
        },res =>{
          console.log("请求错误")
        })
      },
      getXJTableData(){
        var that = this
        var params = {
          tableName: this.XJTableData.tableName,
          EquipmentNo: this.RowData.EquipmentNo,
          limit:this.XJTableData.limit,
          offset:this.XJTableData.offset - 1
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res =>{
          if(res.data.code === "200"){
            that.XJTableData.data = res.data.data.rows
            that.XJTableData.total = res.data.data.total
          }
        },res =>{
          console.log("请求错误")
        })
      },
      handleXJSizeChange(limit){
        this.XJTableData.limit = limit
        this.getXJTableData()
      },
      handleXJCurrentChange(offset){
        this.XJTableData.offset = offset
        this.getXJTableData()
      },
    }
  }
</script>
<style>

</style>
