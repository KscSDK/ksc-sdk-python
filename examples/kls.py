#!/usr/bin/python
# -*- coding: UTF-8 -*-
from kscore.kls import getKlsClient
import json

if __name__ == "__main__":
	client = getKlsClient("kls", "cn-beijing-6",use_ssl=False)
	
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

	# 查询推流实时信息接口: ListRealtimePubStreamsInfo
	res = client.ListRealtimePubStreamsInfo(UniqueName="test",App="live",Pubdomain="yangfan21.cn")
	print json.dumps(res)
	

	#定时录制接口需要输入json格式数据
	res = client.CreateRecordTask(param)
	print json.dumps(res)

	#定时录制取消接口需要输入json格式数据
	res = client.CancelRecordTask(param)
	print json.dumps(res)

	#查询录像任务状态接口(GetRecordTask)
	res = client.GetRecordTask(RecID = 2017)
	print json.dumps(res)

	#查询历史录制任务接口 ListHistoryRecordTasks
	res = client.ListHistoryRecordTasks(UniqueName="test",App="live",Pubdomain="yangfan21.cn",Stream="yangfan21",RecType=1,Limit=10,Marker=10,OrderTime=1,StartUnixTime=1489485300,EndUnixTime=1489485480)
	print json.dumps(res)

	#短视频开始录制接口 : StartStreamRecord
	res = client.StartStreamRecord(param)
	print json.dumps(res)

	#短视频开始录制接口 : StopStreamRecord
	res = client.StopStreamRecord(param)
	print json.dumps(res)

	#查询在线录制任务接口 : ListRecordingTasks
	res = client.ListRecordingTasks(UniqueName="test",App="live",Pubdomain="yangfan21.cn",Stream="yangfan21",RecType=1,Limit=10,Marker=10,OrderTime=1,RecStatusType=1)
	print json.dumps(res)

	#查询主播流时长接口 : ListStreamDurations
	res = client.ListStreamDurations(UniqueName="test",App="live",Pubdomain="yangfan21.cn",Stream="yangfan21",StartUnixTime=1489485300,EndUnixTime=1489485480)
	print json.dumps(res)

	#查询流历史信息接口 : ListHistoryPubStreamsInfo
	res = client.ListHistoryPubStreamsInfo(UniqueName="test",App="live",Pubdomain="yangfan21.cn",Stream="yangfan21",Limit=10,Marker=10,OrderTime=1,StartUnixTime=1489485300,EndUnixTime=1489485480)
	print json.dumps(res)

	#查询流历史错误信息接口 : ListHistoryPubStreamsErrInfo
	res = client.ListHistoryPubStreamsErrInfo(UniqueName="test",App="live",Pubdomain="yangfan21.cn",Stream="yangfan21",Limit=10,Marker=10,OrderTime=1,StartUnixTime=1489485300,endUnixTime=1489485480)
	print json.dumps(res)

	#禁止单路直播流推送 : ForbidStream
	res = client.ForbidStream(param)
	print json.dumps(res)

	#恢复单路直播流推送 : ResumeStream
	res = client.ResumeStream(param)
	print json.dumps(res)

	#查询黑名单列表 : GetBlacklist
	res = client.GetBlacklist(UniqueName="test",App="live",Pubdomain="yangfan21.cn")
	print json.dumps(res)

	#踢拉流接口 : KillStreamCache
	res = client.KillStreamCache(param)
	print json.dumps(res)

