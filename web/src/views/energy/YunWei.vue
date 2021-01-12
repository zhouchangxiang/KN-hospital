<template>
  <el-row>
    <el-col :span="24">
      <div class="page-title">
        <span style="margin-left: 10px;" class="text-size-normol">病患管理</span>
      </div>
      <div class="platformContainer">
        <tableView class="blackComponents" :tableData="TableData" @getTableData="getTableData"></tableView>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  import tableView from '@/components/CommonTable'
  export default {
    name: "YunWei",
    components:{tableView},
    data(){
      return{
        TableData:{
          tableName:"YunWei",
          column:[
            {label:"ID",prop:"ID",type:"input",value:"",disabled:true,showField:false,searchProp:false},
            {label:"设备编号",prop:"EquipmentNo",type:"input",value:""},
            {label:"人员编号",prop:"UserNo",type:"input",value:""},
            {label:"时间",prop:"YunWeiTime",type:"datetime",value:""},
            {label:"维护位置",prop:"Position",type:"input",value:""},
            {label:"问题数量",prop:"WNumber",type:"input",value:""},
            {label:"平台指令",prop:"Instructions",type:"input",value:""},
            {label:"结果",prop:"Result",type:"input",value:""},
          ],
          data:[],
          limit:5,
          offset:1,
          total:0,
          tableSelection:true, //是否在第一列添加复选框
          searchProp:"",
          searchVal:"",
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
      }
    }
  }
</script>

<style scoped>

</style>
