<template>
  <el-row :gutter="15">
    <el-col :span="24">
      <el-row :gutter="15">
        <el-col :span="24">
          <div class="page-title">资产列表</div>
          <div class="tableContainer">
            <el-form :inline="true">
              <el-form-item>

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
          </div>
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
        TableData:{
          tableName:"Equipment",
          data:[],
          limit:5,
          offset:1,
          total:0,
          multipleSelection:[],
        },
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
    }
  }
</script>
<style>

</style>
