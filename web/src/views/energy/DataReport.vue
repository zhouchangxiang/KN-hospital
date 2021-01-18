<template>
  <el-row>
    <el-col :span="24">
      <TabControl :TabControl="TabControl"></TabControl>
      <el-row :gutter="15" v-if="TabControl.TabControlCurrent === '电能报表'">
        <el-col :span="24">
          <el-form :inline="true" :model="formParameters">
            <el-form-item>
              <el-date-picker type="datetime" v-model="formParameters.startDate" :picker-options="pickerOptions" size="small" format="yyyy-MM-dd HH:mm:ss"  style="width: 200px;" :clearable="false"></el-date-picker> ~
              <el-date-picker type="datetime" v-model="formParameters.endDate" :picker-options="pickerOptions" size="small" format="yyyy-MM-dd HH:mm:ss" style="width: 200px;" :clearable="false"></el-date-picker>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="searchElcetricityTime" size="small">查询</el-button>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col :span="24">
          <div class="tableContainer text-size-large color-grayblack" style="margin-bottom:2px;">
            <span>电能报表</span>
            <el-button type="primary" size="mini" style="float: right;" @click="exportExcel">导出报表</el-button>
          </div>
          <div class="tableContainer">
            <el-table :data="tableData" border tooltip-effect="dark" v-loading="loading" size="small">
              <el-table-column prop="AreaName" label="区域"></el-table-column>
              <el-table-column prop="Address" label="设备"></el-table-column>
              <el-table-column prop="Value" label="能耗值"></el-table-column>
              <el-table-column prop="Unit" label="单位"></el-table-column>
              <el-table-column prop="StartTime" label="开始时间" width="200"></el-table-column>
              <el-table-column prop="EndTime" label="结束时间" width="200"></el-table-column>
            </el-table>
          </div>
        </el-col>
      </el-row>
      <el-row :gutter="15" v-if="TabControl.TabControlCurrent === '水能报表'">
        <el-col :span="24">
          <el-form :inline="true" :model="formParameters">
            <el-form-item>
              <el-date-picker type="datetime" v-model="formParameters.startDate" :picker-options="pickerOptions" size="small" format="yyyy-MM-dd HH:mm:ss"  style="width: 200px;" :clearable="false"></el-date-picker> ~
              <el-date-picker type="datetime" v-model="formParameters.endDate" :picker-options="pickerOptions" size="small" format="yyyy-MM-dd HH:mm:ss" style="width: 200px;" :clearable="false"></el-date-picker>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="searchWaterTime" size="small">查询</el-button>
            </el-form-item>
          </el-form>
        </el-col>
        <el-col :span="24">
          <div class="tableContainer text-size-large color-grayblack" style="margin-bottom:2px;">
            <span>水能报表</span>
            <el-button type="primary" size="mini" style="float: right;" @click="exportWaterExcel">导出报表</el-button>
          </div>
          <div class="tableContainer">
            <el-table :data="tableWaterData" border tooltip-effect="dark" v-loading="loading" size="small">
              <el-table-column prop="AreaName" label="区域"></el-table-column>
              <el-table-column prop="Address" label="设备"></el-table-column>
              <el-table-column prop="Value" label="能耗值"></el-table-column>
              <el-table-column prop="Unit" label="单位"></el-table-column>
              <el-table-column prop="StartTime" label="开始时间" width="200"></el-table-column>
              <el-table-column prop="EndTime" label="结束时间" width="200"></el-table-column>
            </el-table>
          </div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
  var moment = require('moment');
  import TabControl from '@/components/TabControl'
  export default {
    name: "DataReport",
    components:{TabControl},
    data(){
      return{
        TabControl:{
          TabControlCurrent:"",
          TabControlOptions:[
            {name:"电能报表"},
            {name:"水能报表"},
          ],
        },
        formParameters:{
          startDate:moment().day(moment().day() - 1).format('YYYY-MM-DD') + " 07:00",
          endDate:moment().day(moment().day() - 1).format('YYYY-MM-DD') + " 19:00"
        },
        pickerOptions:{
          disabledDate(time) {
            return time.getTime() > moment();
          }
        },
        tableData:[],
        tableWaterData:[],
        loading:false,
      }
    },
    created(){
      this.searchElcetricityTime()
    },
    methods:{
      exportExcel(){
        var startTime = moment(this.formParameters.startDate).format("YYYY-MM-DD HH:mm:ss")
        var endTime = moment(this.formParameters.endDate).format("YYYY-MM-DD HH:mm:ss")
        this.$confirm('确定导出' +startTime+'至'+endTime+'的电能详细记录？', '提示', {
          type: 'warning'
        }).then(()  => {
          window.location.href = "/api/exports?start_time="+startTime+"&end_time="+endTime+"&energy_type=电"
        });
      },
      exportWaterExcel(){
        var startTime = moment(this.formParameters.startDate).format("YYYY-MM-DD HH:mm:ss")
        var endTime = moment(this.formParameters.endDate).format("YYYY-MM-DD HH:mm:ss")
        this.$confirm('确定导出' +startTime+'至'+endTime+'的水能详细记录？', '提示', {
          type: 'warning'
        }).then(()  => {
          window.location.href = "/api/exports?start_time="+startTime+"&end_time="+endTime+"&energy_type=水"
        });
      },
      searchElcetricityTime(){
        this.loading = true
        this.axios.get("/api/energy",{
          params: {
            energy_type:"电",
            start_time:moment(this.formParameters.startDate).format("YYYY-MM-DD HH:mm:ss"),
            end_time:moment(this.formParameters.endDate).format("YYYY-MM-DD HH:mm:ss"),
          }
        }).then(res =>{
          if(res.data.code === "200"){
            var data = res.data
            this.tableData = data.data
            this.loading = false
          }
        })
      },
      searchWaterTime(){
        this.loading = true
        this.axios.get("/api/energy",{
          params: {
            energy_type:"水",
            start_time:moment(this.formParameters.startDate).format("YYYY-MM-DD HH:mm:ss"),
            end_time:moment(this.formParameters.endDate).format("YYYY-MM-DD HH:mm:ss"),
          }
        }).then(res =>{
          if(res.data.code === "200"){
            var data = res.data
            this.tableWaterData = data.data
            this.loading = false
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
