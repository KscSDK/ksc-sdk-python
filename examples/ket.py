#!/usr/bin/python
# -*- coding: UTF-8 -*-
from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()
    client = s.create_client("ket", "cn-beijing-6", use_ssl=False)

    uniqname = 'mytest'
    presetname = 'testpreset00'
    appname = 'live'
    description = 'just a demo'
    presetType = 'avop'
    streamid = 'myteststreamid'
    outpull = 1
    srcurl = "rtmp://qa-ws.test-rtmplive.ks-cdn.com/live/20160819"

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
    res = client.preset(**param)
    print json.dumps(res)

    # 更新模板
    res = client.update_preset(**param)
    print json.dumps(res)

    # 获取模板详情
    res = client.get_preset_detail(App=appname, UniqName=uniqname, Preset=presetname)
    print json.dumps(res)

    # 获取用户模板列表
    res = client.get_preset_list(App=appname, UniqName=uniqname)
    print json.dumps(res)

    # 删除模板
    res = client.del_preset(App=appname, UniqName=uniqname, Preset=presetname)
    print json.dumps(res)

    # 启动外网拉流
    param1 = {
       "UniqName": uniqname,
       "StreamID": streamid,
       "SrcUrl": srcurl,
       "App": appname,
       "Params": "a",
    }
    res = client.start_stream_pull(**param1)
    print json.dumps(res)

    # 停止外网拉流
    param2 = {
       "UniqName": uniqname,
       "StreamID": streamid,
       "App": appname,
    }
    res = client.stop_stream_pull(**param2)
    print json.dumps(res)

    # 获取转码任务列表
    res = client.get_stream_tran_list(App=appname, UniqName=uniqname, StreamID=streamid, OutPull=outpull)
    print json.dumps(res)

    # 获取用户已占用配额
    res = client.get_quota_used(UniqName=uniqname)
    print json.dumps(res)
