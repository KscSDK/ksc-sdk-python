#!/usr/bin/python
# -*- encoding:utf-8 -*-

from kscore.session import get_session

def get_data(region):

    projects = []
    s = get_session()

    iam = s.create_client("iam", use_ssl=False)
    resp = iam.get_account_all_project_list()

    for item in resp["ListProjectResult"]["ProjectList"]:
       projects.append(item['ProjectId'])



    # param = {"MaxResults": 1000, "Marker": 0}
    # count = 1
    # for i in projects:
    #     key = "ProjectId."+str(count)
    #     param.update({key: str(i)})
    #     count=count+1

    param = {}
    count = 1
    for i in projects:
        key = "ProjectId."+str(count)
        param.update({key: str(i)})
        count=count+1


    kec = s.create_client("kec",region,use_ssl=False)
    kecParam = {"MaxResults": 1000, "Marker": 0}
    kecParam.update(param)
    print "kecParam"+str(kecParam)
    result = kec.describe_instances(**kecParam)
    for item in  result['InstancesSet']:
        for networkInterface in item["NetworkInterfaceSet"]:
            eipClient = s.create_client("eip", region, use_ssl=False)
            eipParam = {"Filter.1.Name":"network-interface-id","Filter.1.Value.1":networkInterface["NetworkInterfaceId"]}
            eipParam.update(param)
            print "eipparam"+str(eipParam)
            eipResp = eipClient.describe_addresses(**eipParam)
            print item, {"Filter.1.Name":"network-interface-id","Filter.1.Value.1":networkInterface["NetworkInterfaceId"]},  eipResp
            for eip in eipResp["AddressesSet"]:
                print "------"+str(eip)

if __name__ == "__main__":
    get_data("cn-beijing-6")
