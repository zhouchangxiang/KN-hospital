<template>
  <el-row>
    <el-col :span="24">
      <el-form :inline="true">
        <el-form-item label="记录日期：">
          <el-date-picker v-model="searchDate" type="date" value-format="yyyy-MM-dd" placeholder="选择日期" size="small" @change="getTableData(),getNoCleanTableData()"></el-date-picker>
        </el-form-item>
      </el-form>
      <div class="page-title">
        <span style="margin-left: 10px;" class="text-size-normol">清洗记录</span>
      </div>
      <div class="platformContainer">
        <tableView :tableData="TableData" @getTableData="getTableData"></tableView>
      </div>
      <div class="page-title">
        <span style="margin-left: 10px;" class="text-size-normol">未清洗记录</span>
      </div>
      <div class="platformContainer">
        <tableView :tableData="NoCleanTableData" @getTableData="getNoCleanTableData"></tableView>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  import tableView from '@/components/CommonTable'
  export default {
    name: "KTmaintenance",
    components:{tableView},
    data(){
      return{
        searchDate:"",
        TableData:{
          tableName:"CleanRecord",
          column:[
            {label:"ID",prop:"ID",type:"input",value:"",disabled:true,showField:false,searchProp:false},
            {label:"日期",prop:"Time",type:"date",value:""},
            {label:"具体位置",prop:"Position",type:"input",value:""},
            {label:"盘管台数",prop:"PanAmount",type:"input",value:""},
            {label:"清洗消毒回风口过滤网及台数",prop:"HuiFengAmount",type:"input",value:""},
            {label:"清洗消毒送风口个数",prop:"SongFengAmount",type:"input",value:""},
            {label:"托水盘清洗加药台数",prop:"TuoPanAmount",type:"input",value:""},
            {label:"乙方人员",prop:"YUser",type:"input",value:""},
            {label:"甲方人员",prop:"JUser",type:"input",value:""},
            {label:"备注",prop:"Comment",type:"input",value:""},
          ],
          data:[],
          limit:5,
          offset:1,
          total:0,
          tableSelection:true, //是否在第一列添加复选框
          multipleSelection: [],
          dialogVisible: false,
          dialogTitle:'',
          handleType:[
            {type:"primary",label:"添加"},
            {type:"warning",label:"修改"},
            {type:"danger",label:"删除"},
          ],
        },
        NoCleanTableData:{
          tableName:"NoClean",
          column:[
            {label:"ID",prop:"ID",type:"input",value:"",disabled:true,showField:false,searchProp:false},
            {label:"日期",prop:"Time",type:"date",value:""},
            {label:"具体位置",prop:"Position",type:"input",value:""},
            {label:"设备编号",prop:"EquipmentNo",type:"input",value:""},
          ],
          data:[],
          limit:5,
          offset:1,
          total:0,
          tableSelection:true, //是否在第一列添加复选框
          multipleSelection: [],
          dialogVisible: false,
          dialogTitle:'',
          handleType:[
            {type:"primary",label:"添加"},
            {type:"warning",label:"修改"},
            {type:"danger",label:"删除"},
          ],
        },
      }
    },
    mounted() {
      this.getTableData()
      this.getNoCleanTableData()
    },
    methods:{
      getTableData(){
        var that = this
        var params = {
          tableName: this.TableData.tableName,
          Time: this.searchDate,
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
      getNoCleanTableData(){
        var that = this
        var params = {
          tableName: this.NoCleanTableData.tableName,
          Time: this.searchDate,
          limit:this.NoCleanTableData.limit,
          offset:this.NoCleanTableData.offset - 1
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res =>{
            if(res.data.code === "200"){
              that.NoCleanTableData.data = res.data.data.rows
              that.NoCleanTableData.total = res.data.data.total
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
