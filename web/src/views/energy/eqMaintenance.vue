<template>
  <el-row>
    <el-col :span="24">
      <div class="tableContainer">
        <el-form :inline="true">
          <el-form-item>
            <el-button type="primary" @click="KeepOK" v-has="['设备保养工作']">保养完成</el-button>
          </el-form-item>
        </el-form>
        <el-table :data="KeepTaskTableData.data" border ref="multipleTableKeepTask" @selection-change="handleKeepTaskSelectionChange" @row-click="handleKeepTaskRowClick">
          <el-table-column type="selection"></el-table-column>
          <el-table-column v-for="(item,index) in KeepTaskTableData.column" :key="index" :prop="item.prop" :label="item.label"></el-table-column>
        </el-table>
        <div class="paginationClass">
          <el-pagination background  layout="total, sizes, prev, pager, next, jumper"
           :total="KeepTaskTableData.total"
           :current-page="KeepTaskTableData.offset"
           :page-sizes="[5,10,20]"
           :page-size="KeepTaskTableData.limit"
           @size-change="handleKeepTaskSizeChange"
           @current-change="handleKeepTaskCurrentChange">
          </el-pagination>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "eqMaintenance",
    data(){
      return {
        KeepTaskTableData:{ //保养任务表参数
          column:[
            {prop:"Status",label:"工单状态"},
            {prop:"No",label:"工单号"},
            {prop:"EquipmentCode",label:"设备编码"},
            {prop:"Worker",label:"制定计划人"},
            {prop:"ApplyTime",label:"制定计划时间"},
            {prop:"StartTime",label:"任务开始时间"},
            {prop:"WorkTime",label:"工作截止时间"},
            {prop:"Describe",label:"计划描述"},
            {prop:"Content",label:"保养内容"},
            {prop:"WeekTime",label:"工作周期"},
          ],
          data:[],
          limit:5,
          offset:1,
          total:0,
          multipleSelection:[],
        },
      }
    },
    created(){
      this.getKeepTaskTable()
    },
    methods:{
      getKeepTaskTable(){ //获取保养任务表
        var that = this
        var params = {
          limit:this.KeepTaskTableData.limit,
          offset:this.KeepTaskTableData.offset
        }
        this.axios.get("/api/keep_task",{
          params: params
        }).then(res =>{
          if(res.data.code === "10001"){
            this.KeepTaskTableData.data = res.data.data.rows
            this.KeepTaskTableData.total = res.data.data.total
          }
        },res =>{
          console.log("请求错误")
        })
      },
      handleKeepTaskSelectionChange(val){ //选中保养任务
        this.KeepTaskTableData.multipleSelection = val;
      },
      handleKeepTaskRowClick(row){ //点击保养任务行
        this.$refs.multipleTableKeepTask.clearSelection();
        this.$refs.multipleTableKeepTask.toggleRowSelection(row)
      },
      handleKeepTaskSizeChange(limit){
        this.KeepTaskTableData.limit = limit
        this.getKeepTaskTable()
      },
      handleKeepTaskCurrentChange(offset){
        this.KeepTaskTableData.offset = offset
        this.getKeepTaskTable()
      },
      KeepOK(){ //保养完成
        if(this.KeepTaskTableData.multipleSelection.length === 1){
          this.$prompt('确定完成此保养任务？请输入保养内容', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
          }).then(({value})  => {
            var params = {
                No:this.KeepTaskTableData.multipleSelection[0].No,
                EndTime:moment().format("YYYY-MM-DD HH:mm:ss"),
                Content:value
              }
            this.axios.post("/api/keep_task",this.qs.stringify(params)).then(res =>{
              if(res.data.code === "10001"){
                this.$message({
                  type: 'success',
                  message: res.data.message
                });
                this.getEQTable()
                this.getKeepTaskTable()
              }else{
                this.$message({
                  type: 'info',
                  message: res.data.message
                });
              }
            },res =>{
              console.log("请求错误")
            })
          }).catch(() => {
            this.$message({
              type: 'info',
              message: '已取消完成操作'
            });
          });
        }else{
          this.$message({
            type: 'info',
            message: '请选择一项保养任务'
          });
        }
      },
    }
  }
</script>

<style scoped>

</style>
