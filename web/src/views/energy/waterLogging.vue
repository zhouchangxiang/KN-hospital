<template>
  <el-row>
    <el-col :span="24">
      <div class="page-title">
        <span style="margin-left: 10px;" class="text-size-normol">水处理工作记录</span>
      </div>
      <el-form :inline="true" v-if="!isFill">
        <el-form-item label="记录日期：">
          <el-date-picker v-model="searchDate" type="date" value-format="yyyy-MM-dd" placeholder="选择日期" size="small"></el-date-picker>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" size="mini" @click="add">添加</el-button>
        </el-form-item>
      </el-form>
      <div class="platformContainer" v-if="!isFill">
        <el-table :data="tableData.data" size="small" border ref="multipleTable" @selection-change="handleSelectionChange">
          <el-table-column type="selection"></el-table-column>
          <el-table-column prop="ID" label="ID"></el-table-column>
          <el-table-column prop="A15" label="日期"></el-table-column>
          <el-table-column label="操作" fixed="right" width="160">
            <template slot-scope="scope">
              <el-button size="mini" type="info" @click="edit(scope.$index, scope.row)">修改</el-button>
              <el-button size="mini" type="danger" @click="del(scope.$index, scope.row)">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="paginationClass">
          <el-pagination background  layout="total, sizes, prev, pager, next, jumper"
           :total="tableData.total"
           :current-page="tableData.offset"
           :page-sizes="[5,10,20]"
           :page-size="tableData.limit"
           @size-change="handleSizeChange"
           @current-change="handleCurrentChange">
          </el-pagination>
        </div>
      </div>
      <div class="platformContainer" v-if="isFill">
        <el-button size="mini" @click="isFill = false">返回列表</el-button>
        <el-divider>水处理工作记录单</el-divider>
        <el-form :model="fieldList">
          <el-form-item>
            <p><label class="floatLeft marginRight">甲方单位名称</label><el-input class="floatLeft" style="width: auto;" v-model="fieldList.A1" size="small"></el-input></p>
          </el-form-item>
          <el-form-item>
            <p>1.冷却水系统</p>
            <p>（1）水处理工作内容<el-input v-model="fieldList.A2"></el-input></p>
          </el-form-item>
          <el-form-item>
            <p>（2）水处理药剂投加</p>
            <table class="orderTable">
              <tr>
                <td>NF系列</td>
                <td>7001</td>
                <td>8002</td>
                <td>8005</td>
                <td>8006</td>
                <td>8010</td>
                <td>8020</td>
                <td>8022</td>
                <td>8026</td>
                <td>8036</td>
              </tr>
              <tr>
                <td>投加</td>
                <td><el-input v-model="fieldList.A3"></el-input></td>
                <td><el-input v-model="fieldList.B3"></el-input></td>
                <td><el-input v-model="fieldList.C3"></el-input></td>
                <td><el-input v-model="fieldList.D3"></el-input></td>
                <td><el-input v-model="fieldList.E3"></el-input></td>
                <td><el-input v-model="fieldList.F3"></el-input></td>
                <td><el-input v-model="fieldList.G3"></el-input></td>
                <td><el-input v-model="fieldList.H3"></el-input></td>
                <td><el-input v-model="fieldList.I3"></el-input></td>
              </tr>
              <tr>
                <td>NF系列</td>
                <td>9002</td>
                <td>9008</td>
                <td>9016</td>
                <td>9017</td>
                <td>9009</td>
                <td>9010</td>
                <td>9004B</td>
                <td>9004A</td>
                <td>9005</td>
              </tr>
              <tr>
                <td>投加</td>
                <td><el-input v-model="fieldList.A4"></el-input></td>
                <td><el-input v-model="fieldList.B4"></el-input></td>
                <td><el-input v-model="fieldList.C4"></el-input></td>
                <td><el-input v-model="fieldList.D4"></el-input></td>
                <td><el-input v-model="fieldList.E4"></el-input></td>
                <td><el-input v-model="fieldList.F4"></el-input></td>
                <td><el-input v-model="fieldList.G4"></el-input></td>
                <td><el-input v-model="fieldList.H4"></el-input></td>
                <td><el-input v-model="fieldList.I4"></el-input></td>
              </tr>
            </table>
          </el-form-item>
          <el-form-item>
            <p>
              <label class="floatLeft marginRight">（3）清洗冷却塔盘</label>
              <el-input v-model="fieldList.A5" style="width: auto;float: left;"></el-input>
              <label class="floatLeft marginRight">，</label>
              <label class="floatLeft marginRight">取冷却水样</label>
              <el-input v-model="fieldList.B5" style="width: auto;float: left;"></el-input>
              <label class="floatLeft marginRight">，冷凝器单台清洗</label>
              <el-input v-model="fieldList.C5" style="width: auto;float: left;"></el-input>
            </p>
          </el-form-item>
          <el-form-item>
            <p>
              <label class="floatLeft marginRight">（4）冬季湿保：通炮</label>
              <el-input v-model="fieldList.A6" style="width: auto;float: left;"></el-input>
              <label class="floatLeft marginRight">，折Y隔，端盖保养</label>
              <el-input v-model="fieldList.B6" style="width: auto;float: left;"></el-input>
              <label class="floatLeft marginRight">，冷却系统湿保</label>
              <el-input v-model="fieldList.C6" style="width: auto;float: left;"></el-input>
            </p>
          </el-form-item>
          <el-form-item>
            <p>2.冷冻水系统</p>
            <p>（1）水处理工作内容<el-input v-model="fieldList.A8"></el-input></p>
          </el-form-item>
          <el-form-item>
            <p>（2）水处理药剂投加</p>
            <table class="orderTable">
              <tr>
                <td>NF系列</td>
                <td>7001</td>
                <td>8002</td>
                <td>8010</td>
                <td>9004B</td>
                <td>9004A</td>
                <td>9010</td>
                <td>9015</td>
                <td>9005</td>
                <td>9007</td>
              </tr>
              <tr>
                <td>投加</td>
                <td><el-input v-model="fieldList.A9"></el-input></td>
                <td><el-input v-model="fieldList.B9"></el-input></td>
                <td><el-input v-model="fieldList.C9"></el-input></td>
                <td><el-input v-model="fieldList.D9"></el-input></td>
                <td><el-input v-model="fieldList.E9"></el-input></td>
                <td><el-input v-model="fieldList.F9"></el-input></td>
                <td><el-input v-model="fieldList.G9"></el-input></td>
                <td><el-input v-model="fieldList.H9"></el-input></td>
                <td><el-input v-model="fieldList.I9"></el-input></td>
              </tr>
            </table>
          </el-form-item>
          <el-form-item>
            <p>
              <label class="floatLeft marginRight">（3）取冷冻水样</label>
              <el-input v-model="fieldList.A10" style="width: auto;float: left;"></el-input>
              <label class="floatLeft marginRight">，测冷冻水PH</label>
              <el-input v-model="fieldList.B10" style="width: auto;float: left;"></el-input>
            </p>
          </el-form-item>
          <el-form-item>
            <p>
              <label class="floatLeft marginRight">放冷冻水排气</label>
              <el-input v-model="fieldList.A11" style="width: auto;float: left;"></el-input>
              <label class="floatLeft marginRight">，折Y隔</label>
              <el-input v-model="fieldList.B11" style="width: auto;float: left;"></el-input>
            </p>
          </el-form-item>
          <el-form-item>
            <p>
              <label class="floatLeft marginRight">3、其他工作内容：送水样报告单</label>
              <el-input v-model="fieldList.A12" style="width: auto;float: left;"></el-input>
            </p>
          </el-form-item>
          <el-form-item>
            <p>
              <label class="floatLeft marginRight">甲方意见</label>
              <el-input v-model="fieldList.A13" style="width: auto;float: left;"></el-input>
              <label class="floatLeft marginRight"> 现场评价</label>
              <el-input v-model="fieldList.B13" style="width: auto;float: left;"></el-input>
              <label class="floatLeft marginRight"> 甲方人员</label>
              <el-input v-model="fieldList.C13" style="width: auto;float: left;"></el-input>
            </p>
          </el-form-item>
          <el-form-item>
            <p>
              <label class="floatLeft marginRight">乙方施工人员</label>
              <el-input v-model="fieldList.A14" style="width: auto;float: left;"></el-input>
            </p>
          </el-form-item>
          <el-form-item>
            <p>
              <label class="floatLeft marginRight">日期</label>
              <el-input v-model="fieldList.A15" style="width: auto;float: left;"></el-input>
            </p>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" size="small" @click="save">保存</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: "waterLogging",
    data(){
      return{
        searchDate:"",
        tableData:{
          data:[],
          limit:5,
          offset:1,
          total:0,
          multipleSelection: [],
        },
        isFill:false,
        fillType:"",
        row:"",
        fieldList:{
          A1:"",
          A2:"",
          A3:"",B3:"", C3:"", D3:"", E3:"", F3:"", G3:"", H3:"", I3:"",
          A4:"",B4:"", C4:"", D4:"", E4:"", F4:"", G4:"", H4:"", I4:"",
          A5:"",B5:"",C5:"",
          A6:"",B6:"",C6:"",
          A8:"",
          A9:"",B9:"", C9:"", D9:"", E9:"", F9:"", G9:"", H9:"", I9:"",
          A10:"",B10:"",
          A11:"",B11:"",
          A12:"",
          A13:"",B13:"",C13:"",
          A14:"",
          A15:"",
        }
      }
    },
    created(){
      this.getTableData()
    },
    methods:{
      getTableData(){
        var that = this
        var params = {
          tableName:"WaterOperation",
          A15: this.searchDate,
          limit:this.tableData.limit,
          offset:this.tableData.offset - 1
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res =>{
            if(res.data.code === "200"){
              that.tableData.data = res.data.data.rows
              that.tableData.total = res.data.data.total
            }
        },res =>{
          console.log("请求错误")
        })
      },
      handleSizeChange(limit){ //每页条数切换
        this.tableData.limit = limit
        this.getTableData()
      },
      handleCurrentChange(offset) { // 页码切换
        this.tableData.offset = offset
        this.getTableData()
      },
      handleSelectionChange(val){ //选择行数
        this.tableData.multipleSelection = val;
      },
      add(){
        this.isFill = true
        this.fillType = "添加"
      },
      edit(index,row){
        this.isFill = true
        this.fillType = "修改"
        this.row = row
      },
      save(){
        let that = this
        if(this.fillType === "添加"){
          var params = {
            tableName:"WaterOperation",
          }
          for(var i in that.fieldList){
            params[i] = that.fieldList[i]
          }
          this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
              this.getTableData()
              this.isFill = false
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
        }else if(this.fillType === "修改"){
          var params = {
            tableName:"WaterOperation",
            ID:that.row.ID,
          }
          for(var i in that.fieldList){
            params[i] = that.fieldList[i]
          }
          this.axios.put("/api/CUID",this.qs.stringify(params)).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
              this.getTableData()
              this.isFill = false
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
      del(index,row){
        var params = {tableName:"WaterOperation"}
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
      }
    }
  }
</script>

<style scoped>
  .orderTable {
    width: 100%;
    border-width: 1px;
    border-color: #666666;
    border-collapse: collapse;
  }
  .orderTable th {
    border-width: 1px;
    padding: 0 5px;
    border-style: solid;
    border-color: #666666;
    background-color: #dedede;
  }
  .orderTable td {
    border-width: 1px;
    padding: 0 5px;
    white-space: nowrap;
    border-style: solid;
    border-color: #666666;
    background-color: #ffffff;
  }
</style>
