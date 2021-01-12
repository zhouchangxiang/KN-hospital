<template>
  <el-row>
    <el-col :span="24">
      <div class="platformContainer">
        <tableView :tableData="TableData" @getTableData="getTableData"></tableView>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  var moment = require('moment');
  import tableView from '@/components/CommonTable'
  export default {
    name: "eqMaintenance",
    components:{tableView},
    data(){
      return {
        TableData:{
          tableName:"KeepPlan",
          column:[
            {label:"ID",prop:"ID",type:"input",value:"",disabled:true,showField:false,searchProp:false},
            {prop:"No",label:"工单号",type:"input",value:""},
            {prop:"KeepName",label:"保养计划名称",type:"input",value:""},
            {prop:"EquipmentName",label:"设备名称",type:"input",value:""},
            {prop:"EquipmentCode",label:"设备编码",type:"input",value:""},
            {prop:"Status",label:"工单状态",type:"input",value:""},
            {prop:"KeepTime",label:"保养时间",type:"input",value:""},
          ],
          data:[],
          limit:5,
          offset:1,
          total:0,
          searchProp:"",
          searchVal:"",
          multipleSelection: [],
          dialogVisible: false,
          dialogTitle:'',
          handleType:[
            {type:"primary",label:"添加"},
            {type:"danger",label:"删除"},
          ],
        },
      }
    },
    created(){
      this.getTableData()
    },
    methods:{
      getTableData(){
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
    }
  }
</script>

<style scoped>

</style>
