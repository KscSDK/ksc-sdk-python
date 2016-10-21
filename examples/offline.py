# -*- encoding:utf-8 -*-
from kscore.session import get_session
import json

#初始化
s = get_session()
#注：参数不能改变
client = s.create_client("offline", "cn-beijing-6", use_ssl=False)

#创建模板接口调用示例 : preset  
presetname = 'testpreset'
description = 'just a demo'
presetType = 'avop'

#具体的格式请参考官网说明
param = {
    "preset": presetname,
    "description": description,
    "presettype": presetType,
    "param": {
        "f": "mp4",
        "AUDIO": {
            "acodec": "aac",
            "ar":"44100",
            "ab":"64k"
        },
        "VIDEO": {
            "vr": 25,
            "vb": "500k",
            "vcodec": "h264",
            "width": 640,
            "height": 360
        }
    }
}

#该接口需要输入json格式数据，并且在参数前面加上"**"
res = client.preset(**param)
print json.dumps(res)


#更新模板接口调用示例 : update_preset
#该接口需要输入json格式数据，并且在参数前面加上"**"
res = client.update_preset(**param)
print json.dumps(res)

#获取模板列表接口调用示例 : get_preset_list
res = client.get_preset_list()
print json.dumps(res)

#获取模板信息接口调用示例 : get_preset_detail
res = client.get_preset_detail(preset = presetname)
print json.dumps(res)

#删除模板接口调用示例 : del_preset
res = client.del_preset(preset = presetname)
print json.dumps(res)


#创建任务接口调用示例 : create_task
#具体参数请参考官方文档
task = {
    "dstDir": "",
    "dstObjectKey": "4.mp4",
    "dstBucket": "autotestoffline",
    "dstAcl": "public-read",
    "preset": presetname,
    "srcInfo": [
        {
            "path": "/autotestoffline/11.mp4",
            "type": "video",
            "index": 0
        }
    ],
    "cbMethod": "POST",
    "cbUrl": "http://10.4.2.38:19090/"
}

#该接口需要输入json格式数据，并且在参数前面加上"**"
res = client.create_task(**task)
print json.dumps(res)

#查看任务状态接口调用示例 : get_task_by_task_id
taskid = "40d309d3b2bf373cd3f08e5b5e1bddf720160816"
res = client.get_task_by_task_id(taskid = taskid)
print json.dumps(res)

#获取任务列表接口调用示例 : get_task_list
res = client.get_task_list()
print json.dumps(res)

#删除任务接口调用示例 : del_task_by_task_id
res = client.del_task_by_task_id(taskid = taskid)
print json.dumps(res)

#任务置顶接口调用示例 : top_task_by_task_id
res = client.top_task_by_task_id(taskid = taskid)
print json.dumps(res)

#查询任务META列表接口调用示例 : get_task_meta_info
res = client.get_task_meta_info(taskid = taskid)
print json.dumps(res)