<template>
  <el-row>
    <el-col :span="24">
      <div class="page-title">
        <span style="margin-left: 10px;" class="text-size-normol">运维管理</span>
      </div>
      <div class="platformContainer">
        <el-form :inline="true">
          <el-form-item>
            <el-button type="primary" size="small" @click="add">新增</el-button>
          </el-form-item>
        </el-form>
        <el-table :data="TableData.data" border ref="multipleTable" @selection-change="handleSelectionChange">
          <el-table-column type="selection"></el-table-column>
          <el-table-column prop="EquipmentNo" label="设备编号"></el-table-column>
          <el-table-column prop="Name" label="人员姓名"></el-table-column>
          <el-table-column prop="Mail" label="邮箱账号"></el-table-column>
          <el-table-column prop="YunWeiTime" label="时间"></el-table-column>
          <el-table-column prop="Position" label="维护位置"></el-table-column>
          <el-table-column prop="WNumber" label="问题数量"></el-table-column>
          <el-table-column prop="Instructions" label="平台指令"></el-table-column>
          <el-table-column prop="Result" label="结果"></el-table-column>
          <el-table-column label="操作" fixed="right" width="160">
            <template slot-scope="scope">
              <el-button size="mini" type="primary" @click="edit(scope.$index, scope.row)">修改</el-button>
              <el-button size="mini" type="info" @click="del(scope.$index, scope.row)">删除</el-button>
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
            <el-form-item label="人员姓名">
              <el-input v-model="TableData.field.Name"></el-input>
            </el-form-item>
            <el-form-item label="邮箱账号">
              <el-input v-model="TableData.field.Mail"></el-input>
            </el-form-item>
            <el-form-item label="时间">
              <el-date-picker v-model="TableData.field.YunWeiTime" type="datetime" value-format="yyyy-MM-dd HH:mm:ss" placeholder="选择日期时间"></el-date-picker>
            </el-form-item>
            <el-form-item label="维护位置">
              <el-input v-model="TableData.field.Position"></el-input>
            </el-form-item>
            <el-form-item label="问题数量">
              <el-input v-model="TableData.field.WNumber"></el-input>
            </el-form-item>
            <el-form-item label="平台指令">
              <el-input v-model="TableData.field.Instructions"></el-input>
            </el-form-item>
            <el-form-item label="结果">
              <el-input v-model="TableData.field.Result"></el-input>
            </el-form-item>
          </el-form>
          <span slot="footer" class="dialog-footer">
            <el-button @click="TableData.dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="save">保存</el-button>
          </span>
        </el-dialog>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "YunWei",
    data(){
      return{
        TableData:{
          tableName:"YunWei",
          data:[],
          limit:5,
          offset:1,
          total:0,
          multipleSelection: [],
          dialogVisible: false,
          dialogTitle:'',
          field:{
            ID:"",
            EquipmentNo:"",
            Name:"",
            Mail:"",
            YunWeiTime:"",
            Position:"",
            WNumber:"",
            Instructions:"",
            Result:"",
          }
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
      },
      handleSizeChange(limit){
        this.TableData.limit = limit
        this.getTableData()
      },
      handleCurrentChange(offset){
        this.TableData.offset = offset
        this.getTableData()
      },
      handleSelectionChange(row){
        this.TableData.multipleSelection = row
      },
      add(){
        this.TableData.dialogVisible = true
        this.TableData.dialogTitle = "添加"
        this.TableData.field = {
          ID:"",
          EquipmentNo:"",
          Name:"",
          Mail:"",
          YunWeiTime:"",
          Position:"",
          WNumber:"",
          Instructions:"",
          Result:"",
        }
      },
      edit(index,row){
        this.TableData.dialogVisible = true
        this.TableData.dialogTitle = "修改"
        this.TableData.field = {
          ID:row.ID,
          EquipmentNo:row.EquipmentNo,
          Name:row.Name,
          Mail:row.Mail,
          YunWeiTime:row.YunWeiTime,
          Position:row.Position,
          WNumber:row.WNumber,
          Instructions:row.Instructions,
          Result:row.Result,
        }
      },
      del(index,row){
        var params = {tableName:this.TableData.tableName}
        var mulId = [{id:row.ID}]
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
            this.getTableData()
          },res =>{
            console.log("请求错误")
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      save(){
        let that = this
        if(this.fillType === "添加"){
          var params = {
            tableName:this.TableData.tableName,
            ID:this.TableData.field.ID,
            EquipmentNo:this.TableData.field.EquipmentNo,
            Name:this.TableData.field.Name,
            Mail:this.TableData.field.Mail,
            YunWeiTime:this.TableData.field.YunWeiTime,
            Position:this.TableData.field.Position,
            WNumber:this.TableData.field.WNumber,
            Instructions:this.TableData.field.Instructions,
            Result:this.TableData.field.Result,
          }
          this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
              this.getTableData()
              this.sendMail()
              this.TableData.dialogVisible = false
            }else{
              this.$message({
                type: 'info',
                message: res.data.message
              });
            }
          },res =>{
            console.log("请求错误")
          })
        }else if(this.fillType === "修改"){
          var params = {
            tableName:this.TableData.tableName,
            ID:this.TableData.field.ID,
            EquipmentNo:this.TableData.field.EquipmentNo,
            Name:this.TableData.field.Name,
            Mail:this.TableData.field.Mail,
            YunWeiTime:this.TableData.field.YunWeiTime,
            Position:this.TableData.field.Position,
            WNumber:this.TableData.field.WNumber,
            Instructions:this.TableData.field.Instructions,
            Result:this.TableData.field.Result,
          }
          this.axios.put("/api/CUID",this.qs.stringify(params)).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
              this.getTableData()
              this.sendMail()
              this.TableData.dialogVisible = false
            }else{
              this.$message({
                type: 'info',
                message: res.data.message
              });
            }
          },res =>{
            console.log("请求错误")
          })
        }
      },
      sendMail(){
        var mail = []
        mail.push(this.TableData.field.Mail)
        var params = {
          mail:JSON.stringify(mail)
        }
        this.axios.post("/api/send_mail",this.qs.stringify(params)).then(res =>{
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
        },res =>{
          console.log("请求错误")
        })
      }
    }
  }
</script>

<style scoped>

</style>
