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
    return self.client.create_record_task(**param)

  def CancelRecordTask(self,param):
    return self.client.cancel_record_task(**param)

  def StartStreamRecord(self,param):
    return self.client.start_stream_record(**param)

  def StopStreamRecord(self,param):
    return self.client.stop_stream_record(**param)

  def ListRecordingTasks(self,UniqueName="",App="",Pubdomain="",Stream="",RecType=0,Limit=1,Marker=1,OrderTime=0,RecStatusType=0):
    return self.client.list_recording_tasks(UniqueName = UniqueName,App=App,Pubdomain=Pubdomain,Stream=Stream,RecType=RecType,Limit=Limit,
            Marker=Marker,OrderTime=OrderTime,RecStatusType=RecStatusType)

  def ListHistoryRecordTasks(self,UniqueName="",App="",Pubdomain="",Stream="",RecType=0,Limit=1,Marker=1,OrderTime=0,StartUnixTime=0,EndUnixTime=0):
    return self.client.list_history_record_tasks(UniqueName = UniqueName,App=App,Pubdomain=Pubdomain,Stream=Stream,RecType=RecType,Limit=Limit,
            Marker=Marker,OrderTime=OrderTime,StartUnixTime=StartUnixTime,EndUnixTime=EndUnixTime)

  def GetRecordTask(self,RecID=0):
    return self.client.get_record_task(RecID = RecID)

  def ListRealtimePubStreamsInfo(self,UniqueName="",App="",Pubdomain="",Stream="",Limit=1,Marker=0,OrderTime=0):
    return self.client.list_realtime_pub_streams_info(UniqueName = UniqueName,App=App,Pubdomain=Pubdomain,Stream=Stream,Limit=Limit,
            Marker=Marker,OrderTime=OrderTime)

  def ListHistoryPubStreamsInfo(self,UniqueName="",App="",Pubdomain="",Stream="",Limit=1,Marker=0,OrderTime=0,StartUnixTime=0,EndUnixTime=0):
    return self.client.list_history_pub_streams_info(UniqueName = UniqueName,App=App,Pubdomain=Pubdomain,Stream=Stream,Limit=Limit,Marker=Marker,OrderTime=OrderTime,StartUnixTime=StartUnixTime,EndUnixTime=EndUnixTime)

  def ListHistoryPubStreamsErrInfo(self,UniqueName="",App="",Pubdomain="",Stream="",Limit=1,Marker=0,OrderTime=0,StartUnixTime=0,EndUnixTime=0):
    return self.client.list_history_pub_streams_err_info(UniqueName = UniqueName,App=App,Pubdomain=Pubdomain,Stream=Stream,Limit=Limit,
            Marker=Marker,OrderTime=OrderTime,StartUnixTime=StartUnixTime,EndUnixTime=EndUnixTime)

  def ListStreamDurations(self,UniqueName="",App="",Pubdomain="",Stream="",StartUnixTime=0,EndUnixTime=0):
    return self.client.list_stream_durations(UniqueName = UniqueName,App=App,Pubdomain=Pubdomain,Stream=Stream,StartUnixTime=StartUnixTime,EndUnixTime=EndUnixTime)

  def ForbidStream(self,param):
    return self.client.forbid_stream(**param)

  def ResumeStream(self,param):
    return self.client.resume_stream(**param)

  def GetBlacklist(self,UniqueName="",App="",Pubdomain=""):
    return self.client.get_blacklist(UniqueName = UniqueName,App = App, Pubdomain = Pubdomain)

  def CheckBlacklist(self,UniqueName="",App="",Pubdomain="",Stream=""):
    return self.client.check_blacklist(UniqueName = UniqueName,App = App, Pubdomain = Pubdomain,Stream = Stream)

  def ListRealtimeStreamsInfo(self,param):
    return self.client.list_realtime_streams_info(**param)

  def KillStreamCache(self,param):
    return self.client.kill_stream_cache(**param)

def getKlsClient(service_name,region_name,use_ssl=False,ks_access_key_id=None, ks_secret_access_key=None):
    return KlsClient(service_name,region_name,use_ssl,ks_access_key_id, ks_secret_access_key)
