import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import board from '@/components/board'
import Home from '@/views/home'
import Login from '@/components/Login'
import floorData from '@/views/energy/floorData'
import IntelligentMaintenance from '@/views/energy/IntelligentMaintenance'
import eqMaintenance from '@/views/energy/eqMaintenance'
import ServiceDiagnosis from '@/views/energy/ServiceDiagnosis'
import DataReport from '@/views/energy/DataReport'
import ControlMode from '@/views/energy/ControlMode'
import ControlRoom from '@/views/energy/ControlRoom'
import Disease from '@/views/energy/Disease'
import EqDetails from '@/views/energy/EqDetails'

import Organization from '@/views/system/Organization'
import Personnel from '@/views/system/Personnel'
import Role from '@/views/system/Role'
import Permission from '@/views/system/Permission'
import log from '@/views/system/log'

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
        {path:'/IntelligentMaintenance',name:'IntelligentMaintenance',meta:{ title:'资产管理'},component:IntelligentMaintenance},
        {path:'/eqMaintenance',name:'eqMaintenance',meta:{ title:'智能维保'},component:eqMaintenance},
        {path:'/ServiceDiagnosis',name:'ServiceDiagnosis',meta:{ title:'服务诊断'},component:ServiceDiagnosis},
        {path:'/floorData',name:'floorData',meta:{ title:'楼层选择'},component:floorData},
        {path:'/DataReport',name:'DataReport',meta:{ title:'数据报表'},component:DataReport},
        {path:'/ControlMode',name:'ControlMode',meta:{ title:'总控模式'},component:ControlMode},
        {path:'/ControlRoom',name:'ControlRoom',meta:{ title:'房间控制'},component:ControlRoom},
        {path:'/Disease',name:'Disease',meta:{ title:'病患管理'},component:Disease},
        {path:'/EqDetails',name:'EqDetails',meta:{ title:'按需配能'},component:EqDetails},

        {path:'/Organization',name:'Organization',meta:{ title:'用户架构'},component:Organization},
        {path:'/Personnel',name:'Personnel',meta:{ title:'人员管理'},component:Personnel},
        {path:'/Role',name:'Role',meta:{ title:'角色管理'},component:Role},
        {path:'/Permission',name:'Permission',meta:{ title:'权限维护'},component:Permission},
        {path:'/log',name:'log',meta:{ title:'权限维护'},component:log},
      ]
    },
    {
      path:"/",
      name:"board",
      component:board,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
  ]
})
