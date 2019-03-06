# -*- encoding:utf-8 -*-
from kscore.session import get_session
import time
class KvsClient:
	def __init__(self,service_name,region_name,use_ssl,ks_access_key_id,ks_secret_access_key):
		s = get_session()
		if ks_access_key_id != None and  ks_secret_access_key != None:
			self.client = s.create_client(service_name, region_name, use_ssl = use_ssl,
			ks_access_key_id=ks_access_key_id, ks_secret_access_key=ks_secret_access_key)
		else:
			self.client = s.create_client(service_name, region_name, use_ssl = use_ssl)

	def Preset(self,param):
		return self.client.preset(**param)

	def UpdatePreset(self,param):
		return self.client.update_preset(**param)

	def DelPreset(self,Preset=''):
		return self.client.del_preset(Preset=Preset)

	def GetPresetList(self,WithDetail=0,PresetType='',Presets=''):
		return self.client.get_preset_list(WithDetail=WithDetail,PresetType=PresetType,Presets=Presets)

	def GetPresetDetail(self,Preset=''):
		return self.client.get_preset_detail(Preset=Preset)

	def CreateTask(self,task):
		return self.client.create_task(**task)

	def FetchMetaInfo(self,task):
		return self.client.fetch_meta_info(**task)

	def CreateFlowTask(self,task):
		return self.client.create_flow_task(**task)

	def FetchObjectMediaProcess(self,task):
		return self.client.fetch_object_media_process(**task)

	def GetTaskByTaskID(self,TaskID=''):
		return self.client.get_task_by_task_id(TaskID=TaskID)

	def GetTaskList(self,StartDate=0,EndDate=0,Marker=0,Limit=100,StartTime=0,EndTime=0,ErrorCode='',TaskStatus=''):
		if StartDate == 0:
			StartDate = int(time.strftime('%Y%m',time.localtime(time.time()))+"01")
		if EndDate == 0:
			return self.client.get_task_list(StartDate=StartDate,Marker=Marker,Limit=Limit,StartTime=StartTime,EndTime=EndTime,ErrorCode=ErrorCode,TaskStatus=TaskStatus)
		else:
			return self.client.get_task_list(StartDate=StartDate,EndDate=EndDate,Marker=Marker,Limit=Limit,StartTime=StartTime,EndTime=EndTime,ErrorCode=ErrorCode,TaskStatus=TaskStatus)

	def DelTaskByTaskID(self,TaskID = ''):
		return self.client.del_task_by_task_id(TaskID = TaskID)

	def TopTaskByTaskID(self,TaskID = ''):
		return self.client.top_task_by_task_id(TaskID = TaskID)

	def GetTaskMetaInfo(self,TaskID = '',StartDate=0,EndDate=0,Marker=0,Limit=100):
		if TaskID == "":
			if StartDate == 0:
				StartDate = int(time.strftime('%Y%m',time.localtime(time.time()))+"01")
			if EndDate == 0:
				return self.client.get_task_list(StartDate=StartDate,Marker=Marker,Limit=Limit)
			else:
				return self.client.get_task_list(StartDate=StartDate,EndDate=EndDate,Marker=Marker,Limit=Limit)
		else:
			return self.client.get_task_meta_info(TaskID = TaskID)

	def UpdatePipeline(self,param):
		return self.client.update_pipeline(**param)

	def QueryPipeline(self,PipelineName="usual"):
		return self.client.query_pipeline(PipelineName=PipelineName)

	def GetInterfaceNumber(self,StartUnixTime,EndUnixTime,Granularity=5,ResultType=1):
		return self.client.get_interface_number(StartUnixTime=StartUnixTime,EndUnixTime=EndUnixTime,Granularity=Granularity,ResultType=ResultType)

	def GetMediaTransDuration(self,StartUnixTime=0,EndUnixTime=0,Granularity=5,ResultType=1):
		return self.client.get_media_trans_duration(StartUnixTime=StartUnixTime,EndUnixTime=EndUnixTime,Granularity=Granularity,ResultType=ResultType)

	def GetScreenshotNumber(self,StartUnixTime,EndUnixTime,Granularity=5,ResultType=1):
		return self.client.get_screenshot_number(StartUnixTime=StartUnixTime,EndUnixTime=EndUnixTime,Granularity=Granularity,ResultType=ResultType)

def getKvsClient(service_name,region_name,use_ssl=False,ks_access_key_id=None, ks_secret_access_key=None):
	return KvsClient(service_name,region_name,use_ssl,ks_access_key_id,	ks_secret_access_key)
