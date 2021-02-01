import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import board from '@/components/board'
import Home from '@/views/home'
import Login from '@/components/Login'
import IntelligentMaintenance from '@/views/energy/IntelligentMaintenance'
import eqMaintenance from '@/views/energy/eqMaintenance'
import ServiceDiagnosis from '@/views/energy/ServiceDiagnosis'
import DataReport from '@/views/energy/DataReport'
import ControlMode from '@/views/energy/ControlMode'
import KTmaintenance from '@/views/energy/KTmaintenance'
import waterLogging from '@/views/energy/waterLogging'
import YunWei from '@/views/energy/YunWei'
import EqDetails from '@/views/energy/EqDetails'
import Notice from '@/views/energy/Notice'

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
      redirect:'/home', //index主页默认加载home页面
      children:[
        {path:'/home',name:'home',meta:{ title:'工作台'},component:Home},
        {path:'/IntelligentMaintenance',name:'IntelligentMaintenance',meta:{ title:'资产列表'},component:IntelligentMaintenance},
        {path:'/eqMaintenance',name:'eqMaintenance',meta:{ title:'智能维保'},component:eqMaintenance},
        {path:'/ServiceDiagnosis',name:'ServiceDiagnosis',meta:{ title:'服务诊断'},component:ServiceDiagnosis},
        {path:'/DataReport',name:'DataReport',meta:{ title:'数据报表'},component:DataReport},
        {path:'/ControlMode',name:'ControlMode',meta:{ title:'总控模式'},component:ControlMode},
        {path:'/YunWei',name:'YunWei',meta:{ title:'设备运行管理'},component:YunWei},
        {path:'/KTmaintenance',name:'KTmaintenance',meta:{ title:'空调维保'},component:KTmaintenance},
        {path:'/waterLogging',name:'waterLogging',meta:{ title:'水处理工作记录'},component:waterLogging},
        {path:'/EqDetails',name:'EqDetails',meta:{ title:'按需配能'},component:EqDetails},
        {path:'/Notice',name:'Notice',meta:{ title:'公告管理'},component:Notice},

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
