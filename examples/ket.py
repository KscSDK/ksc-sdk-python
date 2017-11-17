#!/usr/bin/python
# -*- coding: UTF-8 -*-
from kscore.ket import getKetClient
import time
import json

if __name__ == "__main__":
    client = getKetClient("ket", "cn-beijing-6",use_ssl=False)

    uniqname = 'xxxx'
    presetname = 'xxxx'
    appname = 'xxxx'
    description = 'xxxx'
    presettype = 4
    streamid = 'xxxx'
    taskid = 'xxxx'
    outpull = 1
    srcurl = "xxxx"

    # 删除模板
    #res = client.DelPreset(App=appname, UniqName=uniqname, Preset=presetname)
    #print json.dumps(res)

    # 创建模板
    param = {
       "UniqName": uniqname,
       "Preset": presetname,
       "PresetType": presettype,
       "Description": description,
       "App": appname,
       "Output": [
         {
           "Idx": 0,
           "Overlay":[
               {
                  "inputIdx": 0,
               }
           ],
           "Amix":[
               {
                  "inputIdx": 0,
               }
           ]
         },
         {
           "Idx": 1,
           "Overlay":
           {
              "inputIdx": 0,
           },
           "Amix":
           {
              "inputIdx": 0,
           }
         },
         {
           "Idx": 2,
           "Video":
           {
              "codec": "copy",
           },
           "Audio":
           {
              "codec": "copy",
           }
         }
       ]
    }
    res = client.Preset(param)
    print json.dumps(res)

    # 更新模板
    res = client.UpdatePreset(param)
    print json.dumps(res)

    # 获取模板详情
    res = client.GetPresetDetail(App=appname, UniqName=uniqname, Preset=presetname)
    print json.dumps(res)

    # 获取用户模板列表
    res = client.GetPresetList(App=appname, UniqName=uniqname)
    print json.dumps(res)

    # 启动外网拉流
    param1 = {
       "UniqName": uniqname,
       "StreamID": streamid,
       "SrcUrl": srcurl,
       "App": appname,
       "Params": "a",
    }
    res = client.StartStreamPull(param1)
    print json.dumps(res)

    # 停止外网拉流
    param2 = {
       "UniqName": uniqname,
       "StreamID": streamid,
       "App": appname,
    }
    res = client.StopStreamPull(param2)
    print json.dumps(res)

    # 获取转码任务列表
    res = client.GetStreamTranList(App=appname, UniqName=uniqname, StreamID=streamid, OutPull=outpull)
    print json.dumps(res)

    # 获取用户已占用配额
    res = client.GetQuotaUsed(UniqName=uniqname)
    print json.dumps(res)
    
    # 发起轮播任务
    param3 = {
       "UniqName": uniqname,
       "App": appname,
       "StreamID": streamid,
       "Preset": presetname,
       "PubDomain": "xxxx",
       "DurationHour":168,
       "SrcInfo": [
         {
            "Path": "xxxx",
            "Index": 0
         }
       ]
    }
    res = client.StartLoop(param3)
    print json.dumps(res)
    
    # 更新轮播时长
    param5 = {
       "UniqName": uniqname,
       "App": appname,
       "StreamID": streamid,
       "DurationHour":100,
    }
    res = client.UpdateLoop(param5)
    print json.dumps(res)
    
    # 查询轮播列表
    res = client.GetLoopList(App=appname, UniqName=uniqname, StreamID=streamid)
    print json.dumps(res)
    
    # 停止轮播任务
    param4 = {
       "UniqName": uniqname,
       "App": appname,
       "StreamID": streamid,
    }
    res = client.StopLoop(param4)
    print json.dumps(res)
    
    #查询直播转码时长统计数据接口调用示例 : GetLiveTransDuration
    #参数
    # StartUnixTime:查询起始时间戳秒数
    # EndUnixTime:查询截止时间戳秒数
    # Granularity:统计时间粒度
    # ResultType:返回结果类型
    start = "2017-06-16 00:00:00"
    end = "2017-06-20 00:00:00"
    t0 = time.strptime(start, "%Y-%m-%d %H:%M:%S")
    t1 = time.strptime(end, "%Y-%m-%d %H:%M:%S")
    startunixtime = int(time.mktime(t0))
    endunixtime = int(time.mktime(t1))
    granularity = 5
    resulttype = 1
    res = client.GetLiveTransDuration(startunixtime, endunixtime, uniqname, granularity, resulttype)
    print json.dumps(res)
    
    # 创建选流任务
    param4 = {
       "UniqName": uniqname,
       "App": appname,
       "Preset": presetname,
       "SrcInfo": [
         {
            "Url": "rtmp://host/app/outernetStreamForSwitch",
            "Idx": 0
         },
         {
            "Streamid": "streamForSwitch",
            "Idx": 1
         }
       ],
       "DstInfo": [
         {
            "Streamid":"stream0ForMonitor",
            "Idx": 0
         },
         {
            "Streamid": "stream1ForSwitch",
            "Idx": 1
         },
         {
            "Streamid": "stream2ForSwitch",
            "Idx": 2
         }
       ]
    }
    res = client.CreateDirectorTask(param4)
    print json.dumps(res)
    
    #更新选流任务
    param4["TaskID"] = taskid
    res = client.UpdateDirectorTask(param4)
    print json.dumps(res)
    
    #查询选流任务
    res = client.QueryDirectorTask(App=appname, UniqName=uniqname, TaskID=taskid)
    print json.dumps(res)
    
    #删除选流任务
    res = client.DelDirectorTask(App=appname, UniqName=uniqname, TaskID=taskid)
    print json.dumps(res)
