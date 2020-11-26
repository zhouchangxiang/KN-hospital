import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import board from '@/components/board'
import Home from '@/views/home'
import SystemMonitor from '@/views/energy/SystemMonitor'
import IntelligentAnalysis from '@/views/energy/IntelligentAnalysis'
import IntelligentMaintenance from '@/views/energy/IntelligentMaintenance'
import ServiceDiagnosis from '@/views/energy/ServiceDiagnosis'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Index',
      name: 'Index',
      component: Index,
      redirect:'/SystemMonitor', //index主页默认加载home页面
      children:[
        {path:'/home',name:'home',meta:{ title:'工作台'},component:Home},
        {path:'/SystemMonitor',name:'SystemMonitor',meta:{ title:'系统监控'},component:SystemMonitor},
        {path:'/IntelligentAnalysis',name:'IntelligentAnalysis',meta:{ title:'智能分析'},component:IntelligentAnalysis},
        {path:'/IntelligentMaintenance',name:'IntelligentMaintenance',meta:{ title:'智能维保'},component:IntelligentMaintenance},
        {path:'/ServiceDiagnosis',name:'ServiceDiagnosis',meta:{ title:'服务诊断'},component:ServiceDiagnosis},
      ]
    },
    {
      path:"/",
      name:"board",
      component:board,
    }
  ]
})
