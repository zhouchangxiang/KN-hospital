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
					天气:<span>{{weather.wea}}</span>温度:<span>{{weather.tem}}℃</span>风向:<span>{{weather.air_level}}</span>
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
										<p class="pingfang">今日预估能耗(KWH)</p>
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
										<strong class="fzhz">{{ Math.floor(save_energy * 0.3619) }}</strong>
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
										<strong class="fzhz">{{ Math.floor(save_energy * 0.6379) }}</strong>
									</div>
								</div>
							</li>
							<li>
								<div>
									<div class="icon">
                    <i class="fa fa-leaf white font72"></i>
									</div>
									<div class="txt white">
										<p class="pingfang">减排二氧化碳(kg)</p>
										<strong class="fzhz">{{ Math.floor(save_energy * 0.997) }}</strong>
									</div>
								</div>
							</li>
							<li>
								<div>
									<div class="icon">
                    <i class="el-icon-cloudy white font72"></i>
									</div>
									<div class="txt white">
										<p class="pingfang">降低碳粉尘(kg)</p>
										<strong class="fzhz">{{ Math.floor(save_energy * 0.272) }}</strong>
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
										<strong class="fzhz">{{ Math.floor(save_energy * 0.6379 / 5.023) }}</strong>
									</div>
								</div>
							</li>
						</ul>
					</div>
					<!-- 能效对比 -->
					<div class="left_3">
						<header class="white font60 pingfang">能效对比</header>
            <table border="2" style="width: 1200px;margin-left: -20px;">
              <tr>
                <th width="400">指标名称</th>
                <th width="160">改造前<br/>指标</th>
                <th width="130">本院<br/>指标</th>
                <th width="200">节能效果</th>
              </tr>
              <tr v-for="(energy,index) in indicator">
                <td>{{ energy.Desc }}</td>
                <td>{{ energy.beforeValue }}</td>
                <td>{{ energy.companyValue }}</td>
                <td>
                  {{ energy.companyValue == 0 ? 0 : (Math.floor((Number(energy.beforeValue) - Number(energy.companyValue)) / Number(energy.companyValue) * 10000) / 100) }}%
                  <span class="el-icon-top" style="color: #11f6e7;" v-if="Number(energy.companyValue) < Number(energy.beforeValue)"></span>
                  <span class="el-icon-bottom" style="color: #d84a27;" v-else></span>
                </td>
              </tr>
            </table>
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
						<header>{{ middle_title }}</header>
						<div class="item_main" v-bind:style="{marginLeft: ((nyzk_index) != -1) ? 0:'-100%' }">
							<div class="middle_item">
                <ul class="header_btn">
                    <li v-for="(item,index) in type" v-bind:class="{active:nyzk_index == index}" @click="energyActiveChange(index)">{{item}}</li>
                </ul>
								<!-- 能源总况能效分析 -->
								<div class="nyzknxfx">
                  <header>能源总况</header>
									<div class="nyzk">
										<ul v-for="(tp,i) in type" v-if="i === nyzk_index">
                      <li>今年用{{ tp }}总量：{{ energy.year_total_energy }}{{ types[i] }}</li>
                      <li>本月用{{ tp }}总量：{{ energy.month_total_energy }}{{ types[i] }}</li>
                      <li>今年月均{{ tp }}总量：{{ energy.year_avg_month }}{{ types[i] }}</li>
                      <li>今年日均{{ tp }}总量：{{ energy.year_avg_day }}{{ types[i] }}</li>
                      <li>今日用{{ tp }}总量：{{ energy.today_energy }}{{ types[i] }}</li>
                    </ul>
									</div>
                  <!--<ve-line :data="chartData" :extend="ChartExtend" height="980px" width="100%"></ve-line>-->
								</div>
                <div class="nyzknxfx" style="margin-top: 10px">
                  <header>能源趋势</header>
                  <div style="margin-top: 20px;">
                    <ve-histogram :data="chartData" :extend="ChartExtend" height="520px"></ve-histogram>
                  </div>
                </div>
							</div>
              <div class="middle_item">
                <ve-pie :data="ringChartData" :settings="ringChartSettings" :extend="ringChartExtend" height="1000px"></ve-pie>
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
							<div>
                <div style="float: left;">
                  <img src="img/ring.png" alt="">
                  <span class="pingfang white font48"><span style="color: #11f6e7;margin-right: 20px;" class="el-icon-collection-tag"></span>资产统计</span>
                </div>
                <div style="float: right;color: #fff;font-size: 42px;margin: 10px 0;">
                  <i style="display: inline-block;width: 60px;height: 30px;background: #024576;border-radius: 8px;margin-right: 10px;"></i>水表
                  <i style="display: inline-block;width: 60px;height: 30px;background: #f1a726;border-radius: 8px;margin-right: 10px;"></i>电表
                  <i style="display: inline-block;width: 60px;height: 30px;background: #1E9FFF;border-radius: 8px;margin-right: 10px;"></i>制冷设备
                  <i style="display: inline-block;width: 60px;height: 30px;background: #e24e26;border-radius: 8px;margin-right: 10px;"></i>照明设备
                </div>
              </div>
              <div style="height: 400px;width: 100%;overflow: hidden;position: relative;margin-bottom: 10px;">
                <ve-bar style="position: absolute;width:100%;left:0;z-index:1;" v-bind:style="{ top: bhgl_margin + 'px' }" :data="barChartData" :extend="barChartExtend" :colors="barColor" :settings="barChartSettings" height="1000px"></ve-bar>
              </div>
							<ul>
								<li v-for="illnes in illness">
									{{illnes.name}} <span>{{illnes.data}} </span>
								</li>
							</ul>
						</div>
						<div class="ywds right_item">
							<p><img src="img/ring.png" alt="">
								<span class="pingfang white font48"><span style="color: #11f6e7;margin-right: 20px;" class="el-icon-collection-tag"></span>运维大师</span>
                <a href="javascript:;" class="pingfang white font48" style="float:right; text-decoration: none;" @click="$router.push('/Index')">去维护</a>
              </p>
						  <table border="2" v-if="operations.length">
                <tr>
                  <th width="150">人员编号</th>
                  <th width="250">时间</th>
                  <th width="300">维护位置</th>
                  <th width="80">问题数量</th>
                  <th width="100">平台指令</th>
                  <th width="100">结果</th>
                </tr>
                <tr v-for="(item,index) in operations">
                  <td>{{ item.UserNo }}</td>
                  <td>{{ item.YunWeiTime }}</td>
                  <td>{{ item.Position }}</td>
                  <td>{{ item.WNumber }}</td>
                  <td>{{ item.Instructions }}</td>
                  <td>{{ item.Result }}</td>
                </tr>
              </table>
              <table border="2" v-else>
                <tr>
                  <th width="200">人员编号</th>
                  <th width="100">时间</th>
                  <th width="200">维护位置</th>
                  <th width="200">问题数量</th>
                  <th width="200">平台指令</th>
                  <th width="100">结果</th>
                </tr>
                <tr>
                  <td colspan="6" rowspan="2">暂无数据</td>
                </tr>
              </table>
            </div>
            <div class="right_item">

            </div>
					</div>
					<!-- 今日管控情况 -->
					<div class="right_2">
						<header class="white font60 pingfang">
							今日管控情况
						</header>
            <div class="ksynsj right_item">
              <div>
                <span class="pingfang white font48"><span style="color: #11f6e7;margin-right: 20px;" class="el-icon-collection-tag"></span>楼层实时用能数据</span>
              </div>
              <div class="ksynsj_left">
                <ul v-for="(item,index) in ksynsj" v-bind:style="{ marginTop:ksynsj_margin + 'px' }">
                  <li v-bind:class="{active:ksyns_index === index}">{{ item.areaName }}</li>
                </ul>
              </div>
              <div class="ksynsj_right">
                <ul>
                  <li>
                    <p>耗电(kW·h)</p>
                    <strong v-if="ksynsj.length > 0">{{ ksynsj[ksyns_index].electricity }}</strong>
                  </li>
                  <li>
                    <p>耗水(t)</p>
                    <strong v-if="ksynsj.length > 0">{{ ksynsj[ksyns_index].water }}</strong>
                  </li>
                  <li>
                    <p>耗冷(kW·h)</p>
                    <strong>0</strong>
                  </li>
                  <li>
                    <p>耗暖(kj)</p>
                    <strong>0</strong>
                  </li>
                  <li>
                    <p>耗气(m³)</p>
                    <strong>0</strong>
                  </li>
                </ul>
              </div>
            </div>
            <div class="kshnjndb right_item">
              <div>
                <span class="pingfang white font48"><span style="color: #11f6e7;margin-right: 20px;" class="el-icon-collection-tag"></span>楼层耗能综合对比</span>
              </div>
              <div class="kshnjndb_item">
                <ul v-bind:style="{ marginTop: kshnjndb_margin + 'px' }">
                  <li v-for="item in ksynsj">
                    <div class="kshnjndb_bar">
                      <div class="kshnjndb_bar_active" v-bind:style="{ width:Number(item.ratio) + '%' }"></div>
                    </div>
                    <div class="txt">{{ item.areaName }}</div>
                  </li>
                </ul>
              </div>
            </div>
            <div class="message">
              <marquee behavior="" direction="up" scrollamount="2">
                <div class="item" v-for="item in notice">
                  <p class="pingfang white font48 center">{{ item.Title }}</p>
                  <p class="pingfang white font32" v-html="item.Content"></p>
                </div>
              </marquee>
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
        websock:null,
        chartSettings:{},
        ChartExtend: {
          tooltip:{
            show:false
          },
          legend:{
            show:true,
            right:50,
            textStyle:{
              color:"#ffffff",
              fontSize:32
            }
          },
          xAxis:{
            show:true,
            type: 'category',
            axisLabel: {
              margin:30,
              color: '#ffffff',  //更改坐标轴文字颜色
              fontSize : 48      //更改坐标轴文字大小
            },
            axisTick:{
              show:true,
              length:10,
              lineStyle:{
                width:5,
                color:"#fff"
              }
            },
            axisLine:{
              show:true,
              lineStyle: {
                width:5,
                color: '#c3dbff',
              }
            },
            splitLine:{
              show:false
            }
          },
          yAxis:{
            show:false,
          },
          grid:{
            left:'0',
            right:'2%',
            bottom:'1%',
            top:'6%'
          },
          series:{
            smooth: false,
            barMaxWidth:"100",
            label:{
              show:true,
              position:"top",
              color:"#ffffff",
              fontSize:48,
            },
            lineStyle:{
              width:8
            }
          }
        },
        chartData: {
          columns: ['月份', '已使用', '额定', '预估', '去年同比'],
          rows: []
        },
        ringChartSettings:{
          radius:300,
          offsetY:500
        },
        ringChartExtend:{
          legend:{
            show:false
          },
          series:{
            label:{
              color:"#ffffff",
              fontSize:48
            },
            labelLine:{
              length:30,
              legnth2:50,
              lineStyle:{
                width:3
              }
            }
          }
        },
        ringChartData:{
          columns: ['能源', '能耗'],
          rows: []
        },
        barChartSettings:{
          stack: {
            'xxx': ['水表', '电表' , '制冷设备', '照明设备']
          }
        },
        barChartExtend: {
          tooltip:{
            show:false
          },
          legend:{
            show:false,
          },
          xAxis:{
            show:false,
          },
          yAxis:{
            axisLabel: {
              margin:30,
              color: '#ffffff',  //更改坐标轴文字颜色
              fontSize : 42     //更改坐标轴文字大小
            },
            axisTick:{
              show:true,
              length:10,
              lineStyle:{
                width:5,
                color:"#fff"
              }
            },
            axisLine:{
              show:true,
              lineStyle: {
                width:5,
                color: '#c3dbff',
              }
            },
          },
          grid:{
            left:'0',
            right:'2%',
            bottom:'0',
            top:'0'
          },
          series:{
            smooth: false,
            barMaxWidth:"50",
            lineStyle:{
              width:8
            }
          },
        },
        barColor:["#024576","#f1a726","#1E9FFF","#e24e26"],
        barChartData:{
          columns: ['楼层', '水表', '电表', '制冷设备', '照明设备'],
          rows: []
        },
        energyTotal:0,
        usingDay:moment(moment().format("YYYY-MM-DD")).diff("2019-03-30", 'day'),
        today_energy:"", //今天已经运行小时数的能耗
        yesterday_energy:"", //昨天相同时间小时数的能耗
        yesterday_total_energy:"", //昨天的总能耗
        save_energy:"", //已节约能耗
        indicator:[],
        nyzk_index: -1,//水电冷暖气到哪个了
        nyzk_index_son:0,
        type: ["电","水","冷","暖","汽"],
        types: ["kW·h","t","kW·h","kW·h","m³"],
        middle_title:"年耗能占比分析",
        bhgl_margin:0,
        ksynsj_margin:0,
        ksyns_index:0,
        ksynsj:[],
        kshnjndb_margin:0,
        notice:[],
        operations: [], //运维大师数据
        illness: [],
        weather: {}, //天气
        energy:{
          year_total_energy:0,
          month_total_energy:0,
          year_avg_day:0,
          year_avg_month:0,
          total_energy:0,
        },
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
      var that = this
      this.nyzkInterVal()
      this.setksynsj_margin()
      this.setkshnjndb_margin()
      this.initWebSocket()
      that.getWeather();
      setInterval(function(){
        that.getWeather();
      },1000 * 60 * 60)
      this.getNotice();
      this.getIndexEquipment();
      this.setbhgl_margin()
      this.getYunWeiData()
    },
    computed:{

    },
    destroyed() {
      if(this.websock){
        this.websock.close() //离开路由之后断开websocket连接
      }
    },
    watch:{
      nyzk_index:function(val){
        if(val == 0){
          this.energy = {
            year_total_energy:Number(this.websockVarData.year_total_energy).toFixed(2),
            month_total_energy:Number(this.websockVarData.month_total_energy).toFixed(2),
            year_avg_day:Number(this.websockVarData.year_avg_day).toFixed(2),
            year_avg_month:Number(this.websockVarData.year_avg_month).toFixed(2),
            today_energy:Number(this.websockVarData.today_energy).toFixed(2),
          }
        }else if(val == 1){
          this.energy = {
            year_total_energy:Number(this.websockVarData.water_year_total).toFixed(2),
            month_total_energy:Number(this.websockVarData.water_month_total).toFixed(2),
            year_avg_day:Number(this.websockVarData.water_avg_day).toFixed(2),
            year_avg_month:Number(this.websockVarData.water_avg_month).toFixed(2),
            today_energy:Number(this.websockVarData.water_day_total).toFixed(2),
          }
        }else{
          this.energy = {
            year_total_energy:0,
            month_total_energy:0,
            year_avg_day:0,
            year_avg_month:0,
            today_energy:0,
          }
        }
      }
    },
    methods: {
      //能源总况定时器
      nyzkInterVal(){
        var that = this
        setInterval(function(){
          if(that.nyzk_index < 4){
            that.nyzk_index++
            that.middle_title = "能源总况/能耗趋势"
          }else{
            that.nyzk_index = -1
            that.middle_title = "年耗能占比分析"
          }
        },10000)
      },
      //楼层滚动
      setksynsj_margin(){
        var that = this
        setInterval(function(){
          if(that.ksyns_index + 1 === that.ksynsj.length){
            that.ksyns_index = 0
            that.ksynsj_margin = 0
          }else{
            that.ksyns_index++
            var top = (that.ksynsj.length - 3 > 0) ? (that.ksynsj.length - 3) : 0
            if(that.ksynsj_margin + (top * 84) != 0){
              that.ksynsj_margin -= 84
            }
          }
        },3000)
      },
      //楼层进度条滚动
      setkshnjndb_margin(){
        var that = this
        setInterval(function(){
          var top = (that.ksynsj.length - 3 > 0) ? (that.ksynsj.length - 3) : 0
          if(that.kshnjndb_margin + (top * 60) == 0){
            that.kshnjndb_margin = 0
          }else{
            that.kshnjndb_margin -= 60
          }
        },3000)
      },
      //资产管理图表滚动
      setbhgl_margin(){
        var that = this
        setInterval(function(){
          if(that.bhgl_margin + (8 * 75) == 0){
            that.bhgl_margin = 0
          }else{
            that.bhgl_margin -= 75
          }
        },3000)
      },
      getNotice(){ //通知栏
        var that = this
        var params = {
          tableName: "Notice",
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res =>{
          if(res.data.code === "200"){
            that.notice = res.data.data.rows
          }
        },res =>{
          console.log("请求错误")
        })
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
        this.websockVarData = JSON.parse(e.data)
        this.today_energy = this.websockVarData.today_energy
        this.yesterday_energy = this.websockVarData.yesterday_energy
        this.yesterday_total_energy = this.websockVarData.yesterday_total_energy
        this.save_energy = this.websockVarData.save_energy
        this.indicator = JSON.parse(this.websockVarData.indicator)
        var month_total_energy = 0
        if(this.nyzk_index == 0){
            month_total_energy = this.websockVarData.month_total_energy
        }else if(this.nyzk_index == 1){
            month_total_energy = this.websockVarData.water_month_total
        }
        this.chartData.rows = [
          {'月份':"1月",'已使用':month_total_energy,"额定":0,"预估":0,"去年同比":0},
          {'月份':"2月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
          {'月份':"3月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
          {'月份':"4月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
          {'月份':"5月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
          {'月份':"6月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
          {'月份':"7月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
          {'月份':"8月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
          {'月份':"9月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
          {'月份':"10月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
          {'月份':"11月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
          {'月份':"12月",'已使用':0,"额定":0,"预估":0,"去年同比":0},
        ]
        this.ringChartData.rows = [
          { '能源': '电', '能耗': this.websockVarData.year_total_energy*0.1229},
          { '能源': '水', '能耗': this.websockVarData.water_year_total },
          { '能源': '冷', '能耗': 0 },
          { '能源': '暖', '能耗': 0 },
          { '能源': '汽', '能耗': 0 },
        ]
        this.ksynsj = JSON.parse(this.websockVarData.floorData)
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
      },
      //获取天气
      getWeather(){
        var that = this
        this.axios.get("http://wthrcdn.etouch.cn/weather_mini",{
          params:{
            city:"深圳"
          }
        }).then(res =>{
          that.weather = {
            date:moment().format("YYYY-MM-DD"),
            wea:res.data.data.forecast[0].type,
            tem:res.data.data.wendu,
            air_level:res.data.data.forecast[0].fengxiang,
            city:"深圳"
          }
        },res =>{
          console.log("请求错误")
        })
      },
      getIndexEquipment(){
        var that = this
        this.axios.get("/api/IndexEquipment",).then(res =>{
          if(res.data.code === "200"){
            that.barChartData.rows = []
            var Num1 = 0
            var Num2 = 0
            var Num3 = 0
            var Num4 = 0
            res.data.data.forEach(item =>{
              Num1 += item['水表']
              Num2 += item['电表']
              Num3 += item['制冷设备']
              Num4 += item['照明设备']
            })
            that.barChartData.rows = res.data.data
            that.barChartData.rows.forEach(item =>{
              if(item['制冷设备'] == 39){
                item['制冷设备'] = 7
              }
              if(item['照明设备'] == 45){
                item['照明设备'] = 8
              }
            })
            that.illness =  [
              {name:"水表",data:Num1},
              {name:"电表",data:Num2},
              {name:"制冷设备",data:Num3},
              {name:"照明设备",data:Num4},
            ]
          }
        },res =>{
          console.log("请求错误")
        })
      },
      getYunWeiData(){
        var that = this
        var params = {
          tableName: "YunWei",
        }
        this.axios.get("/api/CUID",{
          params: params
        }).then(res =>{
          if(res.data.code === "200"){
            that.operations = []
            res.data.data.rows.forEach(item =>{
              that.operations.push({
                UserNo:item.UserNo,
                YunWeiTime:moment(item.YunWeiTime).format("YYYY-MM-DD"),
                Position:item.Position,
                WNumber:item.WNumber,
                Instructions:item.Instructions,
                Result:item.Result,
              })
            })
          }
        },res =>{
          console.log("请求错误")
        })
      },
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
