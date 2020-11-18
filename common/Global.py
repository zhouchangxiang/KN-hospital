from enum import Enum, IntEnum, unique

#连接WMS接口URL
WMSurl = "http://192.168.20.68:8090/"#192.168.20.68 192.168.20.55

GLOBAL_PLANSTARTTIME= "08:30:00"
GLOBAL_PLANENDTIME= "08:29:59"

#与WMS单据状态
class OrderStatus(Enum):
    New = '0'#备料
    RUN = '5'#执行
    finished = '10'#完成

#计划planmanager
class PlanStatus(Enum):
    NEW = "新增"
    Confirm = "待审核"
    UnCheck = "审核未通过"
    WaitRealse = "待下发"
    Realse = "已下发"
    Recall = "撤回"
    PreRUN = "待执行"
    PreMaterial = "待备料"
    FSMWMSed = "已发送投料计划"
    RUN = "执行"
    FINISH = "已完成"

#计划ZYPlan
class ZYPlanStatus(Enum):
    Produced = "待确认"
    EquipmentCheck = "待审核"
    EquipmentReview = "待复核"
    Feeding = "开始投料"
    FeedingFinish = "投料完成"
    Produncting = "执行"
    Finshed = "完成"
#任务ZYTask
class TASKSTATUS(Enum):
    Confirm = "已选设备"#任务选择设备
    NEW = "新增"#新增
    START = "开始"#开始
    RUN = "进行"#进行
    END = "结束"#结束

#计划状态
class AuditStatus(Enum):
    Unaudited = "10"#未审核
    Checked = "20"#审核
    Realse = "30"#下发
    Recall = "40"#撤回
    ClearField = "50"#清场
    Recheck = "60"#清场复核
    ReviewPass = "70"#QA审核通过
    BatchEndPass = "80"#QA批次结束放行

#WorkFlowEventPlan的type
class Type(Enum):
    NEW = "10"#生产部门制定计划
    Checked = "11"#生产部分复核计划
    Realse = "20"#下发计划
    Recall = "21"# 生产部门撤回计划
    Control = "30"#中控操作确认
    ControlChecked = "31"#中控操作复核
    COMFIRM = "40"  # 任务确认
    QAChecked = "32"#QA复核
    RUN = "50"#执行计划
    FINISH = "60"#完成计划
    AgainControl = "61"  #中控确认生产结束清场
    AgainControlChecked = "62"  #中控复核生产结束清场
    AgainQAChecked = "63"  #QA清场复核
    QApass = "70"#QA放行

#WorkFlowEventZYPlan的TypeZY
class TypeZY(Enum):
    NEW = "10"#下发生成计划
    Control = "30"#中控操作确认
    ControlChecked = "31"#中控操作复核
    QAChecked = "32"#QA复核
    COMFIRM = "40"#任务确认
    RUN = "50"#执行计划
    FINISH = "60"#完成计划
    AgainControl = "61"  # 中控确认生产结束清场
    AgainControlChecked = "62"  # 中控复核生产结束清场
    AgainQAChecked = "63"  # QA清场复核

#处理状态
class Handle(Enum):
    Untreated = "0"#未处理
    Treated = "1"#已处理

class TASKLOCKSTATUS(Enum):
    LOCKED = "10"
    UNLOCK = "0"


class SCHEDULETYPE(Enum):
    DAY = "日计划"
    MONTH = "月计划"
    YEAR = "年计划"


class PLANTYPE(Enum):
    SCHEDULE = "调度计划"

class SchedulingStatus(Enum):
    Locl = "1" #排产表批次已经生产则为锁定状态
    Unlock = "0" #批次还未生产

WeightUnit = 'kg'


