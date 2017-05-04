#!/usr/bin/python
# -*- coding: UTF-8 -*-
from kscore.ket import getKetClient
import json

if __name__ == "__main__":
    client = getKetClient("ket", "cn-beijing-6",use_ssl=False)

    uniqname = 'mytest'
    presetname = 'testpreset00'
    appname = 'live'
    description = 'just a demo'
    presetType = 'avop'
    streamid = 'myteststreamid'
    outpull = 1
    srcurl = "rtmp://qa-ws.test-rtmplive.ks-cdn.com/live/20160819"

    # 删除模板
    res = client.DelPreset(App=appname, UniqName=uniqname, Preset=presetname)
    print json.dumps(res)

    # 创建模板
    param = {
       "UniqName": uniqname,
       "Preset": presetname,
       "Description": description,
       "App": appname,
       "Output": [
         {
           "format": 
           {
              "output_format": 257,
              "abr": 70000,
              "vbr": 700000,
              "fr": 23
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
       "PubDomain": "test.uplive.ksyun.com",
       "DurationHour":168,
       "SrcInfo": [
         {
            "Path": "http://wangshuai9.ks3-cn-beijing.ksyun.com/ksyun.flv",
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
    
