<template>
  <div>
    <el-form :inline="true">
      <el-form-item v-if="tableData.hasOwnProperty('searchProp') || tableData.hasOwnProperty('searchVal')">
        <el-select v-model="tableData.searchProp" placeholder="请选择搜索字段" size="small">
          <el-option v-for="(item,index) in tableData.column" :label="item.label" :value="item.prop" :key="index" v-if="item.searchProp != false"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item v-if="tableData.hasOwnProperty('searchProp') || tableData.hasOwnProperty('searchVal')">
        <el-input placeholder="请输入搜索内容" size="small" v-model="tableData.searchVal"></el-input>
      </el-form-item>
      <el-form-item v-if="tableData.hasOwnProperty('searchProp') || tableData.hasOwnProperty('searchVal')">
        <el-button type="success" icon="el-icon-search" size="small" @click="searchTab">搜索</el-button>
      </el-form-item>
      <el-form-item v-for="(item,index) in tableData.handleType" :key="index" v-if="item.hasOwnProperty('hasPermissions')" v-has="[item.hasPermissions]">
        <el-button :type="item.type" size="small" @click="tableClickHandleButton(item.label,item.clickEvent)">{{ item.label }}</el-button>
      </el-form-item>
      <el-form-item v-for="(item,index) in tableData.handleType" :key="index" v-if="!item.hasOwnProperty('hasPermissions')">
        <el-button :type="item.type" size="small" @click="tableClickHandleButton(item.label,item.clickEvent)" :icon='item.icon'>{{ item.label }}</el-button>
      </el-form-item>
    </el-form>
    <el-table :data="tableData.data" size="small" border ref="multipleTable" @selection-change="handleSelectionChange" @row-click="handleRowClick">
      <el-table-column type="selection" v-if="tableData.tableSelection"></el-table-column>
      <el-table-column v-for="(item,index) in tableData.column" :key="index" :prop="item.prop" :label="item.label" :width="item.width" v-if="item.showField != false">
        <template slot-scope="scope">
          <div v-for="spanItem in item.dataJudge" :key="spanItem.value" v-if="scope.row[item.prop] === spanItem.value">
            <span :style="{ color:spanItem.color }" v-if="spanItem.change" v-text="spanItem.change"></span>
            <span :style="{ color:spanItem.color }" v-if="!spanItem.change">{{ scope.row[item.prop] }}</span>
          </div>
          <span v-if="!item.hasOwnProperty('dataJudge') || item.dataJudge.length === 0">{{ scope.row[item.prop] }}</span>
        </template>
      </el-table-column>
    </el-table>
    <div class="paginationClass" v-if="tableData.hasOwnProperty('limit') || tableData.hasOwnProperty('offset')">
      <el-pagination background  layout="total, sizes, prev, pager, next, jumper"
       :total="tableData.total"
       :current-page="tableData.offset"
       :page-sizes="[5,10,20]"
       :page-size="tableData.limit"
       @size-change="handleSizeChange"
       @current-change="handleCurrentChange">
      </el-pagination>
    </div>
    <el-dialog :title="tableData.dialogTitle" :visible.sync="tableData.dialogVisible" :close-on-click-modal="false" :append-to-body="true" width="40%">
      <el-form label-width="110px">
        <el-form-item v-for="(item,index) in tableData.column" :key="index" :label="item.label" :prop="item.prop" v-if="item.canSubmit != false">
          <el-input v-if="item.type === 'input'" v-model="item.value" :disabled="item.disabled"></el-input>
          <el-select v-if="item.type === 'select' && !item.multiple" v-model="item.value" placeholder="请选择" @change="changeHandleChildSelect(item.value,item.prop)">
            <el-option v-for="(i,d) in item.DownData" :key="d" :label="i[item.showDownField]" :value="i[item.showDownField]"></el-option>
          </el-select>
          <el-select v-if="item.type === 'select' && item.multiple" multiple v-model="item.value" placeholder="请选择" @change="changeHandleChildSelect(item.value,item.prop)">
            <el-option v-for="(i,d) in item.DownData" :key="d" :label="i[item.showDownField]" :value="i[item.showDownField]"></el-option>
          </el-select>
          <el-date-picker v-if="item.type === 'datetime'" :disabled="item.disabled" v-model="item.value" type="datetime" value-format="yyyy-MM-dd HH:mm:ss" placeholder="选择日期时间"></el-date-picker>
          <el-date-picker v-if="item.type === 'date'" :disabled="item.disabled" v-model="item.value" type="date" value-format="yyyy-MM-dd" placeholder="选择日期"></el-date-picker>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="tableData.dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="save">保存</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    name: "CommonTable",
    props:['tableData','relatedTableData'],
    data(){
      return {

      }
    },
    created(){
      this.determineSubmitType()
    },
    methods:{
      handleSizeChange(limit){ //每页条数切换
        this.tableData.limit = limit
        this.$emit('getTableData')
      },
      handleCurrentChange(offset) { // 页码切换
        this.tableData.offset = offset
        this.$emit('getTableData')
      },
      handleSelectionChange(val){ //选择行数
        this.tableData.multipleSelection = val;
        if(val[0] != undefined){
          if(this.relatedTableData) { //关联子表
            this.relatedTableData.searchProp = this.tableData.relatedChildTableField
            this.relatedTableData.searchVal = val[0][this.tableData.relatedTableField]
            this.axios.get("/api/CUID",{
              params: {
                tableName: this.relatedTableData.tableName,
                field:this.relatedTableData.searchProp,
                fieldvalue:this.relatedTableData.searchVal,
                limit:this.relatedTableData.limit,
                offset:this.relatedTableData.offset - 1
              }
            }).then(res =>{
              if(res.data.code === '200'){
                var data = res.data.data
                this.relatedTableData.data = data.rows
                this.relatedTableData.total = data.total
              }
            },res =>{
              console.log("请求错误")
            })
          }
        }
      },
      handleRowClick(row){
        if(this.tableData.tableSelectionRadio){
          this.$refs.multipleTable.clearSelection();
          this.$refs.multipleTable.toggleRowSelection(row)
        }else{
          this.$refs.multipleTable.toggleRowSelection(row)
        }
        if(this.tableData.rowClick){
          this.tableData.rowClickData = row
          this.$emit(this.tableData.rowClick)
        }
      },
      searchTab(){
        this.tableData.offset = 1
        this.axios.get("/api/CUID",{
          params: {
            tableName: this.tableData.tableName,
            [this.tableData.searchProp]:this.tableData.searchVal,
            limit:this.tableData.limit,
            offset:this.tableData.offset - 1
          }
        }).then(res =>{
          if(res.data.code === '200'){
            var data = res.data.data
            this.tableData.data = data.rows
            this.tableData.total = data.total
          }
        },res =>{
          console.log("请求错误")
        })
      },
      tableClickHandleButton(label,event){
        this.tableData.dialogTitle = label
        if(label === "添加"){
          this.determineSubmitType()
          this.tableData.dialogVisible = true
          this.tableData.column.forEach(item =>{
            if(item.defaultValue){
              item.value = item.defaultValue
            }else{
              item.value = ""
            }
          })
        }else if(label === "修改"){
          this.determineSubmitType()
          if(this.tableData.multipleSelection.length == 1){
            this.tableData.dialogVisible = true
            this.tableData.column.forEach(item =>{
              if(item.defaultValue){
                item.value = item.defaultValue
              }else{
                item.value = this.tableData.multipleSelection[0][item.prop]
              }
            })
          }else{
            this.$message({
              type: 'info',
              message: '请单选一条数据 '
            })
          }
        }else if(label === "删除"){
          var params = {tableName:this.tableData.tableName}
          var mulId = []
          if(this.tableData.multipleSelection.length >= 1){
            this.tableData.multipleSelection.forEach(item =>{
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
                this.$emit('getTableData')
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
        }else{
          this.$emit(event)
        }
      },
      determineSubmitType(){  //判断表单提交的字段类型
        if(this.tableData.column){
          this.tableData.column.forEach(item =>{
            if(item.type === "select"){
              var params = {
                tableName: item.Downtable,
                limit:100000000,
                offset:0
              }
              this.axios.get("/api/CUID",{
                params: params
              }).then(res =>{
                if(res.data.code === "200"){
                  var data = res.data.data
                  item.DownData = data.rows
                }
              },res =>{
                console.log("请求错误")
              })
            }
          })
        }
      },
      changeHandleChildSelect(value,prop){
        if(this.tableData.column){
          this.tableData.column.forEach(item =>{
            if(item.prop === prop){  //判断点击的是当前字段的表单
              if(item.childProp){  //判断是否有联动的子字段表单
                this.tableData.column.forEach((childItem,index) =>{
                  if(childItem.prop === item.childProp){  //判断是否是点击项的子节点表单
                    this.axios.get("/api/CUID",{
                      params: {
                        tableName: childItem.Downtable,
                        [childItem.showDownField]:value,
                        limit:100000000,
                        offset:0
                      }
                    }).then(res =>{
                      if(res.data.code === "200"){
                        var data = res.data.data
                        childItem.DownData = data.rows
                        var childItemObj = childItem
                        this.tableData.column.splice(index,1,childItemObj) //将子节点表单按索引替换为修改后的数据
                      }
                    },res =>{
                      console.log("请求错误")
                    })
                  }
                })
              }
            }
          })
        }
      },
      save(){
        if(this.tableData.dialogTitle === "添加"){
          var params = {tableName:this.tableData.tableName}
          this.tableData.column.forEach(item =>{
            if(item.canSubmit != false){
              params[item.prop] = item.value
              if(Array.isArray(item.value)){
                params[item.prop] = JSON.stringify(item.value)
              }else {
                params[item.prop] = item.value
              }
            }
          })
          this.axios.post("/api/CUID",this.qs.stringify(params)).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
              this.$emit('getTableData')
            }else{
              this.$message({
                type: 'info',
                message: res.data.message
              });
            }
            this.tableData.dialogVisible = false
          },res =>{
            console.log("请求错误")
          })
        }else if(this.tableData.dialogTitle === "修改"){
          var params = {tableName:this.tableData.tableName}
          this.tableData.column.forEach(item =>{
            params[item.prop] = item.value
          })
          this.axios.put("/api/CUID",this.qs.stringify(params)).then(res =>{
            if(res.data.code === "200"){
              this.$message({
                type: 'success',
                message: res.data.message
              });
              this.$emit('getTableData')
            }else{
              this.$message({
                type: 'info',
                message: res.data.message
              });
            }
            this.tableData.dialogVisible = false
          },res =>{
            console.log("请求错误")
          })
        }
      }
    }
  }
</script>

<style scoped>

</style>
