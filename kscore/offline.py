# -*- encoding:utf-8 -*-
from kscore.session import get_session
import time
class OfflineClient:
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

	def DelPreset(self,presetName):
		return self.client.del_preset(preset = presetName)

	def GetPresetList(self,withDetail=0,presettype='',presets=''):
		return self.client.get_preset_list(withDetail = withDetail,presettype=presettype,presets=presets)

	def GetPresetDetail(self,presetName):
		return self.client.get_preset_detail(preset = presetName)

	def CreateTask(self,task):
		return self.client.create_task(**task)

	def GetTaskByTaskID(self,taskid):
		return self.client.get_task_by_task_id(taskid = taskid)

	def GetTaskList(self,startdate=0,enddate=0,marker=0,limit=100):
		if startdate == 0:
			startdate = int(time.strftime('%Y%m',time.localtime(time.time()))+"01")
		if enddate == 0:
			return self.client.get_task_list(startdate=startdate,marker=marker,limit=limit)
		else:
			return self.client.get_task_list(startdate=startdate,enddate=enddate,marker=marker,limit=limit)

	def DelTaskByTaskID(self,taskid):
		return self.client.del_task_by_task_id(taskid = taskid)

	def TopTaskByTaskID(self,taskid):
		return self.client.top_task_by_task_id(taskid = taskid)

	def GetTaskMetaInfo(self,taskid = "",startdate=0,enddate=0,marker=0,limit=0):
		if taskid == "":
			if startdate == 0:
				startdate = int(time.strftime('%Y%m',time.localtime(time.time()))+"01")
			if enddate == 0:
				return self.client.get_task_list(startdate=startdate,marker=marker,limit=limit)
			else:
				return self.client.get_task_list(startdate=startdate,enddate=enddate,marker=marker,limit=limit)
		else:
			return self.client.get_task_meta_info(taskid = taskid)

def getOfflineClient(service_name,region_name,use_ssl=False,ks_access_key_id=None, ks_secret_access_key=None):
	return OfflineClient(service_name,region_name,use_ssl,ks_access_key_id,	ks_secret_access_key)
