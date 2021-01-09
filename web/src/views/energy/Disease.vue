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
    name: "Disease",
    components:{tableView},
    data(){
      return{
        TableData:{
          tableName:"Disease",
          column:[
            {label:"ID",prop:"ID",type:"input",value:"",disabled:true,showField:false,searchProp:false},
            {label:"楼层",prop:"Floor",type:"input"},
            {label:"轻人数",prop:"LightNumber",type:"input"},
            {label:"中人数",prop:"CentreNumber",type:"input"},
            {label:"重人数 ",prop:"HeightNumber ",type:"input"},
            {label:"跨区人数 ",prop:"Region ",type:"input"},
            {label:"移动人数 ",prop:"Move ",type:"input"},
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
          var data = JSON.parse(res.data)
          that.TableData.data = data.rows
          that.TableData.total = data.total
        },res =>{
          console.log("请求错误")
        })
      }
    }
  }
</script>

<style scoped>

</style>
