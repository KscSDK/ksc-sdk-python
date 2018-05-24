# -*- encoding:utf-8 -*-
from kscore.kvs import getKvsClient
import json
import time

#没有配置kscore.cfg调用方式
#ks_access_key_id='xxxxxxxxxxxxxxxxxxxx'
#ks_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxx'
# 参数：服务service_name,大区region_name 
#client = getKvsClient("offline", "cn-beijing-6",use_ssl=False,ks_access_key_id=ks_access_key_id,ks_secret_access_key=ks_secret_access_key)

#配置kscore.cfg调用方式

client = getKvsClient("kvs", "cn-beijing-6",use_ssl=False)

#创建模板接口调用示例 : preset  
presetname = 'xxxx'
description = 'just a demo'
presetType = 'avop'

#具体的格式请参考官网说明
param = {
    "Preset": presetname,
    "Description": description,
    "PresetType": presetType,
    "Param": {
        "f": "mp4",
        "AUDIO": {
            "acodec": "aac"
        },
        "VIDEO": {
            "vcodec": "h264"
        }
    }
}

#该接口需要输入json格式数据
res = client.Preset(param)
print json.dumps(res)

#更新模板接口调用示例 : UpdatePreset
#该接口需要输入json格式数据
res = client.UpdatePreset(param)
print json.dumps(res)

#获取模板列表接口调用示例 : GetPresetList
#参数
# WithDetail:是否查询模板详情，1-是 0-否
# PresetType:模板类型，多种模板类型以逗号隔开
# Presets:模板名称，多个模板名称以逗号隔开
res = client.GetPresetList(WithDetail=1,PresetType="xxxx")
print json.dumps(res)

#获取模板信息接口调用示例 : GetPresetDetail
# Preset:模板名称
res = client.GetPresetDetail(Preset=presetname)
print json.dumps(res)

#删除模板接口调用示例 : DelPreset
# Preset:模板名称
res = client.DelPreset(Preset=presetname)
print json.dumps(res)

#修改任务队列接口调用示例 : UpdatePipeline
# 该接口需要输入json格式数据
pipeinfo = {
    "PipelineName": "usual",
    "Description": "test pipeline",
    "State": "Active",
    "RegularStart": "01:00:00",
    "RegularDuration":7200
}
res = client.UpdatePipeline(pipeinfo)
print json.dumps(res)

#查询任务队列接口调用示例 : QueryPipeline
# PipelineName:队列名称
res = client.QueryPipeline(PipelineName="usual")
print json.dumps(res)


#创建任务接口调用示例 : CreateTask
#具体参数请参考官方文档
task = {
    "DstDir": "",
    "DstObjectKey": "xxxx",
    "DstBucket": "xxxx",
    "DstAcl": "public-read",
    "Preset": presetname,
    "SrcInfo": [
        {
            "path": "/xxxxx/xxxxx",
            "type": "video",
            "index": 0
        }
    ],
    "CbMethod": "POST",
    "CbUrl": "xxxxx"
}

#该接口需要输入json格式数据
res = client.CreateTask(task)
print json.dumps(res)

#该接口需要输入json格式数据
res = client.CreateFlowTask(task)
print json.dumps(res)

#查看任务状态接口调用示例 : GetTaskByTaskID
taskid = "xxxxxx"
# TaskID:任务ID
res = client.GetTaskByTaskID(TaskID = taskid)
print json.dumps(res)

#获取任务列表接口调用示例 : GetTaskList
#参数
# StartDate:开始时间，默认为当前月的第一天；格式：20160919
# EndDate:截止时间，默认为开始时间加30天；若大于当前时间，则默认为当前时间；格式：20160930
# Marker:请求起始游标，默认为0    
# Limit:单次请求的记录数，默认为100，最大值为100
# StartTime:起始时间戳
# EndTime:结束时间戳
# 错误码:ErrorCode
# 任务状态:TaskStatus
res = client.GetTaskList(StartDate=20170100,EndDate=20170112,Marker=0,Limit=50)
print json.dumps(res)

#删除任务接口调用示例 : DelTaskByTaskID
# TaskID:任务ID
res = client.DelTaskByTaskID(TaskID = taskid)
print json.dumps(res)

#任务置顶接口调用示例 : TopTaskByTaskID
# TaskID:任务ID
res = client.TopTaskByTaskID(TaskID = taskid)
print json.dumps(res)

#查询任务META列表接口调用示例 : GetTaskMetaInfo
#参数
# TaskID:任务ID
# StartDate:开始时间，默认为当前月的第一天；格式：20160919
# EndDate:截止时间，默认为开始时间加30天；若大于当前时间，则默认为当前时间；格式：20160930
# Marker:请求起始游标，默认为0    
# Limit:单次请求的记录数，默认为100，最大值为100
res = client.GetTaskMetaInfo(StartDate=20170100,EndDate=20170112,Marker=0,Limit=50)
print json.dumps(res)

#查询转码时长统计数据接口调用示例 : GetMediaTransDuration
#查询转码API调用次数统计数据接口调用示例 : GetInterfaceNumber
#查询转码截图统计数据接口调用示例 : GetScreenshotNumber
#参数
# StartUnixTime:查询起始时间戳秒数
# EndUnixTime:查询截止时间戳秒数
# Granularity:统计时间粒度
# ResultType:返回结果类型
start = "2017-06-16 00:00:00"
end = "2017-06-20 00:00:00"
t0 = time.strptime(start, "%Y-%m-%d %H:%M:%S")
t1 = time.strptime(end, "%Y-%m-%d %H:%M:%S")
StartUnixTime = int(time.mktime(t0))
EndUnixTime = int(time.mktime(t1))
Granularity = 5
ResultType = 1
res = client.GetMediaTransDuration(StartUnixTime, EndUnixTime, Granularity, ResultType)
print json.dumps(res)

res = client.GetInterfaceNumber(StartUnixTime, EndUnixTime, Granularity, ResultType)
print json.dumps(res)

res = client.GetScreenshotNumber(StartUnixTime, EndUnixTime, Granularity, ResultType)
print json.dumps(res)

#控制台专用
#发起媒体转码
res = client.FetchObjectMediaProcess(task)
print json.dumps(res)

#查询任务列表
res = client.ListFetchObjectMediaProcess(StartUnixTime=StartUnixTime,EndUnixTime=EndUnixTime)
print json.dumps(res)

#查询单个任务详情
res = client.GetFetchObjectMediaProcess(ProcessTaskId="12121212")
print json.dumps(res)