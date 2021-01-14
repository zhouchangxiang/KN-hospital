<template>
  <el-row>
    <el-col :span="24">
      <div class="page-title">公告管理</div>
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
    name: "Notice",
    components:{tableView},
    data(){
      return {
        TableData:{
          tableName:"Notice",
          column:[
            {label:"ID",prop:"ID",type:"input",value:"",disabled:true,showField:false,searchProp:false},
            {prop:"Title",label:"公告标题",type:"input",value:""},
            {prop:"Content",label:"工作内容",type:"input",value:""},
            {prop:"NoticeType",label:"类型",type:"input",value:""},
            {prop:"Status",label:"状态",type:"input",value:""},
          ],
          data:[],
          limit:5,
          offset:1,
          total:0,
          searchProp:"",
          searchVal:"",
          multipleSelection: [],
          tableSelection:true, //是否在第一列添加复选框
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
