# -*- encoding:utf-8 -*-
from kscore.kls import getKlsClient
import json


client = getOfflineClient("kls", "cn-beijing-6",use_ssl=False)

param = {
    "UniqueName":"test",
    "App":"live",
    "Pubdomain":"test.uplive.ks-cdn.com",
    "Stream":"yangfan21",
    "Mp4VodEnable":1,
    "Ks3FileNameM3u8":"a23{Pubdomain}23sf{AppName}",
    "Ks3FullPathMP4":"record-1/{UniqueName}/{AppName}/{Pubdomain}/{StreamName}/mp4/{StreamName}-{UnixTimestamp}-activity",
    "StartUnixtime":1489485300,
    "EndUnixtime":1489485480
}

#定时录制接口需要输入json格式数据
res = client.CreateRecordTask(param)
print json.dumps(res)

#定时录制取消接口需要输入json格式数据
res = client.CancelRecordTask(param)
print json.dumps(res)

#查询录像任务状态接口(GetRecordTask)
#参数
# RecID:录制任务ID
res = client.GetRecordTask(recID = 2017)
print json.dumps(res)

#查询历史录制任务接口 ListHistoryRecordTasks
res = client.ListHistoryRecordTasks(uniqueName="test",app="live",pubdomain="yangfan21.cn",stream="yangfan21",recType=1,limit=10,marker=10,orderTime=1,startUnixTime=123,endUnixTime=321)
print json.dumps(res)

#短视频开始录制接口 : StartStreamRecord
res = client.StartStreamRecord(param)
print json.dumps(res)

#短视频开始录制接口 : StopStreamRecord
res = client.StopStreamRecord(param)
print json.dumps(res)

#查询在线录制任务接口 : ListRecordingTasks
res = client.ListRecordingTasks(uniqueName="test",app="live",pubdomain="yangfan21.cn",stream="yangfan21",recType=1,limit=10,marker=10,orderTime=1,recStatusType=1)
print json.dumps(res)

#查询主播流时长接口 : ListStreamDurations
res = client.ListStreamDurations(uniqueName="test",app="live",pubdomain="yangfan21.cn",stream="yangfan21",startUnixTime=123,endUnixTime=321)
print json.dumps(res)

#查询流历史信息接口 : ListHistoryPubStreamsInfo
res = client.ListHistoryPubStreamsInfo(uniqueName="test",app="live",pubdomain="yangfan21.cn",stream="yangfan21",limit=10,marker=10,orderTime=1,startUnixTime=123,endUnixTime=321)
print json.dumps(res)

#查询流历史错误信息接口 : ListHistoryPubStreamsErrInfo
res = client.ListHistoryPubStreamsErrInfo(uniqueName="test",app="live",pubdomain="yangfan21.cn",stream="yangfan21",limit=10,marker=10,orderTime=1,startUnixTime=123,endUnixTime=321)
print json.dumps(res)

#禁止单路直播流推送 : ForbidStream
res = client.ForbidStream(param)
print json.dumps(res)

#恢复单路直播流推送 : ResumeStream
res = client.ResumeStream(param)
print json.dumps(res)

#查询黑名单列表 : GetBlacklist
res = client.GetBlacklist(uniqueName="test",app="live",pubdomain="yangfan21.cn")
print json.dumps(res)

#转推实时信息查询接口 : listRelayStreamsInfo
res = client.listRelayStreamsInfo(uniqueName="test",app="live",limit=10,marker=10)
print json.dumps(res)

#转推历史错误统计接口 : listRelayErrInfo
res = client.listRelayErrInfo(uniqueName="test",app="live",marker=10,startUnixTime=123,duration=120)
print json.dumps(res)

#踢拉流接口 : KillStreamCache
res = client.KillStreamCache(param)
print json.dumps(res)

