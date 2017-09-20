# -*- encoding:utf-8 -*-
from kscore.session import get_session
import time
class KlsClient:
    def __init__(self,service_name,region_name,use_ssl,ks_access_key_id,ks_secret_access_key):
        s = get_session()
        if ks_access_key_id != None and  ks_secret_access_key != None:
            self.client = s.create_client(service_name, region_name, use_ssl = use_ssl,
            ks_access_key_id=ks_access_key_id, ks_secret_access_key=ks_secret_access_key)
        else:
            self.client = s.create_client(service_name, region_name, use_ssl = use_ssl)

    def CreateRecordTask(self,param):
        return self.client.CreateRecordTask(**param)

    def CancelRecordTask(self,param):
        return self.client.CancelRecordTask(**param)

    def GetRecordTask(self,recID):
        return self.client.GetRecordTask(RecID = recID)

    def ListHistoryRecordTasks(self,uniqueName,app,pubdomain,stream,recType,limit,marker,orderTime,startUnixTime,endUnixTime):
        return self.client.ListHistoryRecordTasks(UniqueName = uniqueName,App=app,Pubdomain=pubdomain,Stream=stream,RecType=recType,Limit=limit,
            Marker=marker,OrderTime=orderTime,StartUnixTime=startUnixTime,EndUnixTime=endUnixTime)

    def StartStreamRecord(self,param):
        return self.client.StartStreamRecord(**param)

    def StopStreamRecord(self,param):
        return self.client.StopStreamRecord(**param)

    def ListRecordingTasks(self,uniqueName,app,pubdomain,stream,recType,limit,marker,orderTime,recStatusType):
        return self.client.ListRecordingTasks(UniqueName = uniqueName,App=app,Pubdomain=pubdomain,Stream=stream,RecType=recType,Limit=limit,
            Marker=marker,OrderTime=orderTime,RecStatusType=recStatusType)

     def ListStreamDurations(self,uniqueName,app,pubdomain,stream,startUnixTime,endUnixTime):
        return self.client.ListStreamDurations(UniqueName = uniqueName,App=app,Pubdomain=pubdomain,Stream=stream,StartUnixTime=startUnixTime,EndUnixTime=endUnixTime)

    def ListRealtimePubStreamsInfo(self,uniqueName,app,pubdomain,stream,limit,marker,orderTime):
        return self.client.ListRealtimePubStreamsInfo(UniqueName = uniqueName,App=app,Pubdomain=pubdomain,Stream=stream,Limit=limit,
            Marker=marker,OrderTime=orderTime)

    def ListHistoryPubStreamsInfo(self,uniqueName,app,pubdomain,stream,limit,marker,orderTime,startUnixTime,endUnixTime):
        return self.client.ListHistoryPubStreamsInfo(UniqueName = uniqueName,App=app,Pubdomain=pubdomain,Stream=stream,Limit=limit,
            Marker=marker,OrderTime=orderTime,StartUnixTime=startUnixTime,EndUnixTime=endUnixTime)

    def ListHistoryPubStreamsErrInfo(self,uniqueName,app,pubdomain,stream,limit,marker,orderTime,startUnixTime,endUnixTime):
        return self.client.ListHistoryPubStreamsErrInfo(UniqueName = uniqueName,App=app,Pubdomain=pubdomain,Stream=stream,Limit=limit,
            Marker=marker,OrderTime=orderTime,StartUnixTime=startUnixTime,EndUnixTime=endUnixTime)

    def ForbidStream(self,param):
        return self.client.ForbidStream(**param)

    def ResumeStream(self,param):
        return self.client.ResumeStream(**param)

    def GetBlacklist(self,uniqueName,app,pubdomain):
        return self.client.GetBlacklist(UniqueName = uniqueName,App = app, Pubdomain = pubdomain)

    def CheckBlacklist(self,uniqueName,app,pubdomain,stream):
        return self.client.CheckBlacklist(UniqueName = uniqueName,App = app, Pubdomain = pubdomain,Stream = stream)

    def listRelayStreamsInfo(self,uniqueName,app,limit,marker):
        return self.client.listRelayStreamsInfo(uniquename = uniqueName,app = app, marker = marker,limit = limit)

    def listRelayErrInfo(self,uniqueName,app,limit,marker,starttime,duration):
        return self.client.listRelayErrInfo(uniquename = uniqueName,app = app, marker = marker,limit = limit,starttime=starttime,duration=duration)

    def KillStreamCache(self,param):
        return self.client.KillStreamCache(**param)

def getKlsClient(service_name,region_name,use_ssl=False,ks_access_key_id=None, ks_secret_access_key=None):
    return KlsClient(service_name,region_name,use_ssl,ks_access_key_id, ks_secret_access_key)
