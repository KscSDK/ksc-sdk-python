# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session
import json

if __name__ == "__main__":
	s = get_session()
	ak = "your AK"
	sk = "your SK"
	kis_client = s.create_client("kis", "cn-beijing-6", "2018-09-01", True, None, None, ak, sk)
	# 列出region
	regions = kis_client.list_region()
	# prettyPrinter().pprint(regions)

	# 列出Idc
	idcs = kis_client.list_idc()
	prettyPrinter().pprint(idcs)

	# 查询各机房内机柜
	for idc in idcs["Data"]:
		devices = kis_client.get_cabinet(Idc=idc["Name"], Limit=-1)
		if devices["Total"] > 0:
			prettyPrinter().pprint(devices)

	# 查询带宽
	instances = []
	for idc in idcs["Data"]:
		bds = kis_client.get_bandwidth(Idc=idc["Name"], Limit=-1)
		if bds["Total"] > 0:
			# prettyPrinter().pprint(bds)
			for bd in bds["Data"]:
				instances.append(bd["InstanceId"])

	# prettyPrinter().pprint(instances)

	# 比如带宽实例如下：
	# [edca6c2e-4826-4a7d-b14b-01aba8a109b8,6e8a010a-d498-4f46-9d70-ad71f1fdc3e3]
	# 查询流量：粒度60秒，从 2018-09-06 10:00:00 到 2018-09-06 12:00:00
	resp = kis_client.get_monitor_data(InstanceId="edca6c2e-4826-4a7d-b14b-01aba8a109b8", Step=60, StartTime="2018-09-06 10:00:00", EndTime="2018-09-06 12:00:00")
	prettyPrinter().pprint(resp)
