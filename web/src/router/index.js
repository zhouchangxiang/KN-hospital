import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import board from '@/components/board'
import Home from '@/views/home'
import floorData from '@/views/energy/floorData'
import IntelligentMaintenance from '@/views/energy/IntelligentMaintenance'
import ServiceDiagnosis from '@/views/energy/ServiceDiagnosis'
import DataReport from '@/views/energy/DataReport'
import ControlMode from '@/views/energy/ControlMode'
import ControlRoom from '@/views/energy/ControlRoom'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Index',
      name: 'Index',
      component: Index,
      redirect:'/floorData', //index主页默认加载home页面
      children:[
        {path:'/home',name:'home',meta:{ title:'工作台'},component:Home},
        {path:'/IntelligentMaintenance',name:'IntelligentMaintenance',meta:{ title:'智能维保'},component:IntelligentMaintenance},
        {path:'/ServiceDiagnosis',name:'ServiceDiagnosis',meta:{ title:'服务诊断'},component:ServiceDiagnosis},
        {path:'/floorData',name:'floorData',meta:{ title:'楼层选择'},component:floorData},
        {path:'/DataReport',name:'DataReport',meta:{ title:'数据报表'},component:DataReport},
        {path:'/ControlMode',name:'ControlMode',meta:{ title:'总控模式'},component:ControlMode},
        {path:'/ControlRoom',name:'ControlRoom',meta:{ title:'房间控制'},component:ControlRoom},
      ]
    },
    {
      path:"/",
      name:"board",
      component:board,
    }
  ]
})
