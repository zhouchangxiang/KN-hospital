<template>
  <div class="boardContent">
    <div class="main">
			<div id="header">
				<div class="header_left header_div pingfang white font48">
					{{weather.date}}
					<span class="address">{{weather.city}}</span>
				</div>
				<div class="header_title header_div semibold">
					HSTL能源管控平台
				</div>
				<div class="header_right header_div pingfang white font48">
					天气:<span>{{weather.wea}}</span>温度:<span>{{weather.tem}}</span>空气质量:<span>{{weather.air_level}}</span>
				</div>
			</div>

			<div class="content">
				<div class="left">
					<!-- 绿色医院等级 -->
					<div class="left_1">
						<p class="white font72 pingfang" style="line-height: 120px;">绿色医院能源管控系统已正常运行 <span class="font72">{{usingDay}}</span> 天</p>
						<!-- <p class="white font48 pingfang">单位面积综合能耗低于深圳市医疗卫生建筑平均水平<span>{{companyEnergyEfficiency.ranking * 100}} %</span>,能耗水平达到<span>{{energy_level}}</span></p> -->
					</div>
					<!-- 康宁医院能效展示 -->
					<div class="left_2">
						<header class="white semibold">深圳市康宁医院能效展示</header>
						<ul>
							<li>
								<div>
									<div class="icon">
                    <i class="fa fa-bolt white font72"></i>
									</div>
									<div class="txt white">
										<p class="pingfang">今日预估能耗(tce)</p>
										<strong class="fzhz" v-if="yesterday_energy != 0">{{Math.floor(today_energy * yesterday_total_energy/yesterday_energy)}}</strong>
										<strong class="fzhz" v-else>未知</strong>
									</div>
								</div>
							</li>
							<li>
								<div>
									<div class="icon">
                    <i class="el-icon-s-opportunity white font72"></i>
									</div>
									<div class="txt white">
										<p class="pingfang">综合节能(tce)</p>
										<strong class="fzhz">{{Math.floor(companyEnergyEfficiency.energyConservationAmount * 100)/100}}</strong>
									</div>
								</div>
							</li>
							<li>
								<div>
									<div class="icon">
                    <i class="fa fa-fire white font72"></i>
									</div>
									<div class="txt white">
										<p class="pingfang">碳排放总值(t)</p>
										<strong class="fzhz">{{Math.floor(companyEnergyEfficiency.carbonEmissionAmount * 100)/100}}</strong>
									</div>
								</div>
							</li>
							<li>
								<div>
									<div class="icon">
                    <i class="fa fa-tree white font72"></i>
									</div>
									<div class="txt white">
										<p class="pingfang">相当于种植树(棵)</p>
										<strong class="fzhz">{{Math.floor(companyEnergyEfficiency.convertOfPlantingAmount * 100)/100}}</strong>
									</div>
								</div>
							</li>
							<li>
								<div>
									<div class="icon">
                    <i class="el-icon-cloudy white font72"></i>
									</div>
									<div class="txt white">
										<p class="pingfang">降低碳粉尘(t)</p>
										<strong class="fzhz">{{Math.floor(companyEnergyEfficiency.reducePm25Amount * 100)/100}}</strong>
									</div>
								</div>
							</li>
						</ul>
					</div>
					<!-- 能效对比 -->
					<div class="left_3">
						<header class="white font60 pingfang">能效对比</header>
            <ul style="margin-top: 150px;">
              <li style="margin-bottom: 80px;">
                <span class="pingfang white font60">本日能耗：{{ Math.floor(today_energy) }}</span>
              </li>
              <li style="margin-bottom: 80px;">
                <span class="pingfang white font60">昨日同期能耗：{{ Math.floor(yesterday_energy) }}</span>
              </li>
              <li style="margin-bottom: 80px;">
                <span class="pingfang white font60">昨日总能耗：{{ Math.floor(yesterday_total_energy) }}</span>
              </li>
              <li style="margin-bottom: 80px;">
                <span class="pingfang white font60">对比：</span><span class="pingfang font60" :class="today_energy-yesterday_energy>0?'danger':'success'">{{ compareYesterday }}</span>
              </li>
            </ul>
					</div>
				</div>
				<div class="middle">
					<!-- bim -->
					<div class="middle_1">
						<video muted="muted" width="100%" height="100%" autoplay loop="loop">
						    <source src="http://cdn.szhostiy.com/%E5%BA%B7%E5%AE%81%E5%8C%BB%E9%99%A2%E6%A0%87%E5%87%86%E5%B1%824.9.mp4" type="video/mp4">
						    您的浏览器不支持 video 标签。
						</video>
					</div>
					<!-- 能源总况 -->
					<div class="middle_2">
						<header>能耗实时趋势</header>
						<div class="item_main" :style="{ marginLeft: ((nyzk_index == -1)?0:'-100%') }">
							<div class="middle_item">
								<div id="nyzk_echarts"></div>
							</div>
							<div class="middle_item">
                <ul class="header_btn">
                    <li v-for="(item,index) in type" v-bind:class="{active:nyzk_index == item}" @click="energyActiveChange(item)">{{item}}</li>
                </ul>
								<!-- 能源总况能效分析 -->
								<div class="nyzknxfx">
									<header>{{ nyzk_index }}实时总量{{ energyTotal }}</header>
									<div class="nyzk">
										<ve-line :data="chartData" :extend="ChartExtend" height="900px"></ve-line>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="right">
					<!-- 资产管理 -->
					<div class="right_1">
						<header class="white font60 pingfang">
							资产管理
						</header>
						<div class="bhgl right_item">
							<p><img src="img/ring.png" alt="">
								<span class="pingfang white font48">病患管理</span></p>
							<div id="bhgl_echart"></div>
							<ul>
								<li v-for="illnes in illness">
									{{illnes.name}} <span>{{illnes.data}} </span>人
								</li>
							</ul>
						</div>
						<div class="ywds right_item">
							<p><img src="img/ring.png" alt="">
								<span class="pingfang white font48">运维大师</span></p>
							<table border="2" v-if="operations.length">
								<tr>
									<th width="200">人员编号</th>
									<th width="180">时间</th>
									<th width="200">维护位置</th>
									<th width="200">问题数量</th>
									<th width="200">平台指令</th>
									<th width="180">结果</th>
								</tr>
								<tr v-for="operation in operations">
									<td>{{operation.pollingUserId}}</td>
									<td>{{operation.pollingTime.split(' ')[1]}}</td>
									<td>{{operation.areaName}}</td>
									<td>{{operation.questionCount}}</td>
									<td>{{operation.processMethodStr}}</td>
									<td>{{operation.processStatusStr}}</td>
								</tr>
							</table>

							<table border="2" v-else>
								<tr>
									<th width="200">人员编号</th>
									<th width="180">时间</th>
									<th width="200">维护位置</th>
									<th width="200">问题数量</th>
									<th width="200">平台指令</th>
									<th width="180">结果</th>
								</tr>
								<tr>
									<td colspan="6" rowspan="2">暂无数据</td>
								</tr>
							</table>
						</div>
						<div class="right_item">
							<div id="sbgz_echart"></div>
						</div>
					</div>
					<!-- 今日管控情况 -->
					<div class="right_2">
						<header class="white font60 pingfang">
							今日管控情况
						</header>
            <ul style="margin-top: 150px;">
              <li style="margin-bottom: 50px;">
                <span class="pingfang white font48">websocket服务：</span><span class="pingfang font60 floatRight" :class="websocket_status === '执行成功'?'success':'danger'">{{ websocket_status }}</span>
              </li>
              <li style="margin-bottom: 50px;">
                <span class="pingfang white font48">OPC服务：</span><span class="pingfang font60 floatRight" :class="Stutus === '执行正常'?'success':'danger'">{{ Stutus }}</span>
              </li>
              <li style="margin-bottom: 50px;">
                <span class="pingfang white font48">历史数据采集服务：</span><span class="pingfang font60 floatRight" :class="History_Stutus === '执行正常'?'success':'danger'">{{ History_Stutus }}</span>
              </li>
              <li style="margin-bottom: 50px;">
                <span class="pingfang white font48">运行成功次数：</span><span class="pingfang success font60 floatRight">{{ Successcount }}</span>
              </li>
              <li style="margin-bottom: 50px;">
                <span class="pingfang white font48">运行总次数：</span><span class="pingfang success font60 floatRight">{{ Totalcount }}</span>
              </li>
            </ul>
						<div class="ksynsj right_item" style="text-align: center;">
               <el-button type="primary" class="button" style="margin-top: 100px;" @click="$router.push('/Index')">空调照明管理系统</el-button>
						</div>
					</div>
				</div>
			</div>
		</div>
  </div>
</template>
<script>
  var moment = require('moment');
  export default {
    name: "board",
    data(){
      return {
        websockVarData:{},
        websocket_status:"",
        Stutus:"",
        History_Stutus:"",
        Successcount:"",
        Totalcount:"",
        chartSettings:{},
        ChartExtend: {
          tooltip:{
              show:false
                },
                legend:{
            show:false
                },
                xAxis:{
              splitLine:{
                  show:false
                    },
                    axisLabel: {
                       show: true,
                        textStyle: {
                          color: '#c3dbff',  //更改坐标轴文字颜色
                          fontSize : 56      //更改坐标轴文字大小
                        }
                     },
                },
                yAxis:{
              splitLine:{
                  show:false
                    }
                },
              grid:{
                left:'2%',
                right:'2%',
                bottom:'2%',
                top:'2%'
              },
              series:{
                barMaxWidth : 50,
                smooth: false,
                label:{
                  show: false,
                  position: "top",
                  fontSize:56
                },
                  lineStyle:{
                    width:5
                  }
              }
            },
        chartData: {
          columns: ['时间', '能耗量'],
          rows: [
              { '时间': moment().subtract(40, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(38, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(36, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(34, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(32, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(30, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(28, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(26, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(24, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(22, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(20, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(18, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(16, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(14, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(12, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(10, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(8, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(6, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(4, 's').format("HH:mm:ss"), '能耗量': null},
            { '时间': moment().subtract(2, 's').format("HH:mm:ss"), '能耗量': null}
          ]
        },
        energyTotal:0,
        tagListData:[
            {name:"空调智能电表1F",tag:"COM2.KT1F.总有功电量",type:"电",tier:"1楼"},
            {name:"空调智能电表2F",tag:"COM2.KT2F.总有功电量",type:"电",tier:"2楼"},
            {name:"空调智能电表3F",tag:"COM2.KT3F.总有功电量",type:"电",tier:"3楼"},
            {name:"空调智能电表4F",tag:"COM2.KT4F.总有功电量",type:"电",tier:"4楼"},
            {name:"空调智能电表5F",tag:"COM2.KT5F.总有功电量",type:"电",tier:"5楼"},
            {name:"空调智能电表6F",tag:"COM2.KT6F.总有功电量",type:"电",tier:"6楼"},
            {name:"空调智能电表7F",tag:"COM2.KT7F.总有功电量",type:"电",tier:"7楼"},
            {name:"空调智能电表8F",tag:"COM2.KT8F.总有功电量",type:"电",tier:"8楼"},
            {name:"空调智能电表9F",tag:"COM2.KT9F.总有功电量",type:"电",tier:"9楼"},
            {name:"空调智能电表10F",tag:"COM2.KT10F.总有功电量",type:"电",tier:"10楼"},
            {name:"空调智能电表11F",tag:"COM2.KT11F.总有功电量",type:"电",tier:"11楼"},
            {name:"空调智能电表12F",tag:"COM2.KT12F.总有功电量",type:"电",tier:"12楼"},
            {name:"照明智能电表1F",tag:"COM2.LIGHT1F.总有功电量",type:"电",tier:"1楼"},
            {name:"照明智能电表2F",tag:"COM2.LIGHT2F.总有功电量",type:"电",tier:"2楼"},
            {name:"照明智能电表3F",tag:"COM2.LIGHT3F.总有功电量",type:"电",tier:"3楼"},
            {name:"照明智能电表4F",tag:"COM2.LIGHT4F.总有功电量",type:"电",tier:"4楼"},
            {name:"照明智能电表5F",tag:"COM2.LIGHT5F.总有功电量",type:"电",tier:"5楼"},
            {name:"照明智能电表6F",tag:"COM2.LIGHT6F.总有功电量",type:"电",tier:"6楼"},
            {name:"照明智能电表7F",tag:"COM2.LIGHT7F.总有功电量",type:"电",tier:"7楼"},
            {name:"照明智能电表8F",tag:"COM2.LIGHT8F.总有功电量",type:"电",tier:"8楼"},
            {name:"照明智能电表9F",tag:"COM2.LIGHT9F.总有功电量",type:"电",tier:"9楼"},
            {name:"照明智能电表10F",tag:"COM2.LIGHT10F.总有功电量",type:"电",tier:"10楼"},
            {name:"照明智能电表11F",tag:"COM2.LIGHT11F.总有功电量",type:"电",tier:"11楼"},
            {name:"照明智能电表12F",tag:"COM2.LIGHT12F.总有功电量",type:"电",tier:"12楼"},
            {name:"中央空调智能电表1",tag:"COM2.KTCTR1.总有功电量",type:"电"},
            {name:"中央空调智能电表2",tag:"COM2.KTCTR2.总有功电量",type:"电"},
            {name:"辅助设备智能电表",tag:"COM2.KTCTRADD.总有功电量",type:"电"},
            {name:"8楼水表",tag:"COM1.WATER8F.今日累积流量",type:"水",tier:"8楼"},
            {name:"9楼水表",tag:"COM1.WATER9F.今日累积流量",type:"水",tier:"9楼"},
        ],
        usingDay:moment(moment().format("YYYY-MM-DD")).diff("2020-11-28", 'day'),
        today_energy:"", //今天已经运行小时数的能耗
        yesterday_energy:"", //昨天相同时间小时数的能耗
        yesterday_total_energy:"", //昨天的总能耗
        companyEnergyEfficiency:{
            'energyLevel':0, //节能等级
            'ranking':0, //节能排名
            'usingDate':0, //系统启用时间
            'usingDay':0, //已使用时间
            'energyConservationAmount':0, //综合节能
            'carbonEmissionAmount':0, //碳排放总量
            'convertOfPlantingAmount':0, //转换种植树木
            'reduceForestCarbonAmount':0, //减少森林碳能
            'reducePm25Amount':0, //降低PM2.5
            'reduceElectricalLoadAmount':0, //减少电力负荷值
            'energyConsumptionIndex':0, //耗能指数
        },
        hnzs:0,//耗能指数
        hnzs_left:0,
        energy_level:'',//能耗水平
        nyzk_index: "电",//水电冷暖气到哪个了
        nyzk_title_son:'',
        type: [ '电','水' ],
        types: ["t","kW·h","kW·h","kW·h","m³"],
        operations: [

        ],
        illness: [],
        weather: {},
        energy:[],
        energyCount:0,//总耗能量
        economyEnergyTotal:0,//总节能量
      }
    },
    created(){
      document.body.style.zoom = document.documentElement.clientWidth / 5760;
      window.onresize = function () {
        document.body.style.zoom = document.documentElement.clientWidth / 5760;
      }
    },
    mounted() {
      this.initWebSocket()
      this.getWeather();
      this.getNotice();
      //this.getCompanyEnergyEfficiency();
      this.getPatient();
    },
    computed:{
      compareYesterday(){
        if(this.today_energy > 0){
          var compare = (this.today_energy - this.yesterday_energy) / this.today_energy * 100
          if(this.today_energy - this.yesterday_energy > 0){
            return "+" + compare.toFixed(2) + "%"
          }else{
            return compare.toFixed(2) + "%"
          }
        }else{
          if(this.yesterday_energy > 0){
            return "-" + 100 + "%"
          }else{
            return 0 + "%"
          }
        }
      },
    },
    methods: {
      //获取能效展示等数据
      getCompanyEnergyEfficiency(){
        var that = this;
        axios.get(baseUrl + '/operation/main/companyEnergyEfficiency/'+that.companyId)
        .then(function (response) {
          that.companyEnergyEfficiency = response.data.data;
          that.indicator = response.data.data.companyEnergyEfficiencyDetailList;
          that.companyEnergyEfficiency.energyConsumptionIndex = (that.companyEnergyEfficiency.energyConsumptionIndex > 0.9) ? 0.81 : that.companyEnergyEfficiency.energyConsumptionIndex;
          var enery = that.indicator[that.indicator.length-1].companyIndicatorValue;
          var hnzs = that.indicator[1].companyIndicatorValue;
          if(enery > 25){
            that.energy_level = '不达标'
          }else if(enery > 16){
            that.energy_level = '达标'
          }else if(enery > 6){
            that.energy_level = '先进'
          }else{
            that.energy_level = '领先'
          }
          hnzs = hnzs/90/365;
          console.log(hnzs);
          if(hnzs < 0.001){
            that.hnzs = '优'
            that.hnzs_left = '80%';
          }else if(hnzs < 0.0012){
            that.hnzs = '良'
            that.hnzs_left = '40%';
          }else{
            that.hnzs = '差'
            that.hnzs_left = '10%';
          }
        })
        .catch(function (error) {
          console.log(error);
        });
      },
      getNotice(){ //通知栏
        var that = this;
      },
      //获取病患管理
      getPatient() {
        var that = this;
        //axios.get(baseUrl + '/operation/main/patient/'+that.companyId)
        //.then(function (response) {
          //if(response.data.code === 0){
              var response = {
                  data:{
                      data:{}
                              }
              }
              response.data.data.transRegionPerson = "212"
              response.data.data.unusualPerson = "121"
              response.data.data.patientDetailList = [
                              {areaName:"aaaa",patientDegreeEasy:1231,patientDegreeMedium:4123,patientDegreeSerious:5324},
                              {areaName:"bbb",patientDegreeEasy:456,patientDegreeMedium:2334,patientDegreeSerious:3522},
                          ]
            that.illness = [ {
              name: '跨区移动',
              data: response.data.data.transRegionPerson,
            }, {
              name: '异常人员',
              data: response.data.data.unusualPerson,
            }]
            var yAxis = [];
            var patientDegreeEasy = [];
            var patientDegreeMedium = [];
            var patientDegreeSerious = [];
            response.data.data.patientDetailList.forEach((item)=>{
              yAxis.push(item.areaName);
              patientDegreeEasy.push(item.patientDegreeEasy)
              patientDegreeMedium.push(item.patientDegreeMedium)
              patientDegreeSerious.push(item.patientDegreeSerious)
            })
          //}
        //})
        //.catch(function (error) {
          //console.log(error);
        //});

      },
      getWeather() {
        var that = this;
      },
      initWebSocket(){ //初始化weosocket
        // this.websock = new WebSocket('ws://' + location.host + '/socket');
        this.websock = new WebSocket('ws://127.0.0.1:5002/socket');
        this.websock.onmessage = this.websocketonmessage;
        this.websock.onopen = this.websocketonopen;
        this.websock.onerror = this.websocketonerror;
        this.websock.onclose = this.websocketclose;
      },
      websocketonopen(){ //连接建立之后执行send方法发送数据
        this.websocketsend();
      },
      websocketonerror(){//连接建立失败重连
        console.log("websocket连接失败")
      },
      websocketonmessage(e){ //数据接收
        var that = this
        this.websockVarData = JSON.parse(e.data)
        this.websocket_status = this.websockVarData.websocket_status
        this.Stutus = this.websockVarData.Stutus
        this.History_Stutus = this.websockVarData.History_Stutus
        this.Successcount = this.websockVarData.Successcount
        this.Totalcount = this.websockVarData.Totalcount
        this.today_energy = this.websockVarData.today_energy
        this.yesterday_energy = this.websockVarData.yesterday_energy
        this.yesterday_total_energy = this.websockVarData.yesterday_total_energy
        this.energyTotal = 0
        for(var key in this.websockVarData){
            this.tagListData.forEach(item =>{
                if(item.tag === key ){
                    if(item.type === this.nyzk_index){
                        that.energyTotal += Number(this.websockVarData[key])
                    }
                }
            })
        }
        that.chartData.rows.push({
          "时间": moment().format("HH:mm:ss"),
          "能耗量": that.energyTotal
        })
        that.chartData.rows.shift()
      },
      websocketsend(Data){//数据发送
        this.websock.send(Data);
      },
      websocketclose(e){  //关闭
        console.log("websocket关闭")
      },
      closesocket(){
        this.websock.close()
      },
      energyActiveChange(index){
        this.nyzk_index = index
          this.chartData = {
            columns: ['时间', '能耗量'],
            rows: [
                { '时间': moment().subtract(40, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(38, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(36, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(34, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(32, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(30, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(28, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(26, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(24, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(22, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(20, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(18, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(16, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(14, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(12, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(10, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(8, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(6, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(4, 's').format("HH:mm:ss"), '能耗量': null},
              { '时间': moment().subtract(2, 's').format("HH:mm:ss"), '能耗量': null}
            ]
          }
      }
    }
  }
</script>

<style scoped>
  @import "../assets/board.css";
  .boardContent{
    width: 5760px;
	  height: 3240px;
    background: url("../assets/img/bg.png");
    background-repeat: no-repeat;
    background-size: 100% 100%;
  }
</style>
