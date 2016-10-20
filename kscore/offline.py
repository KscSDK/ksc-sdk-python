# -*- encoding:utf-8 -*-
from kscore.session import get_session
class OfflineClient:
	def __init__(self,service_name,region_name,use_ssl,env_vars):
		s = get_session()
		self.client = s.create_client(service_name, region_name, use_ssl = use_ssl)

	def Preset(self,param):
		return self.client.preset(**param)

	def UpdatePreset(self,param):
		return self.client.update_preset(**param)

	def DelPreset(self,presetName):
		return self.client.del_preset(preset = presetName)

	def GetPresetList(self,withDetail = 0):
		return self.client.get_preset_list(withDetail = withDetail)

	def GetPresetDetail(self,presetName):
		return self.client.get_preset_detail(preset = presetName)

	def CreateTask(self,task):
		return self.client.create_task(**task)

	def GetTaskByTaskID(self,taskID):
		return self.client.get_task_by_task_id(taskid = taskID)

	def GetTaskList(self):
		return self.client.get_task_list()

	def DelTaskByTaskID(self,taskID):
		return self.client.del_task_by_task_id(taskid = taskID)

	def TopTaskByTaskID(self,taskID):
		return self.client.top_task_by_task_id(taskid = taskID)

	def GetTaskMetaInfo(self,taskID = ""):
		if taskID == "":
			return self.client.get_task_meta_info()
		else:
			return self.client.get_task_meta_info(taskid = taskID)

def getOfflineClient(service_name,region_name,use_ssl=True,env_vars=None):
	return OfflineClient(service_name,region_name,use_ssl,env_vars)
