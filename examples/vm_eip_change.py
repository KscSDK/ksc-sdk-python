#!/usr/bin/python
#coding=utf-8

from kscore.session import get_session
from kscore.exceptions import ClientError
import sys

#使用方法
'''
VM_EIP批量切换
python python vm_eip_change.py vm_eip_change.csv
'''

#输入文件格式（csv文件）示例
'''
InstanceID,NewEIP
5e7f65c5-d338-4ccd-8ce9-f196be5fc7e3,192.168.1.1
'''

#属性解释
'''
InstanceID 主机或者原EIP实例
NewEIP 新的EIP的IP
'''

ak ='ak'
sk = 'sk'
region = 'cn-beijing-6'

def createSdkClinet(service,region):
    s = get_session()
    s.set_credentials(ak,sk)
    client = s.create_client(service, region, use_ssl=True)
    return client


if __name__ == "__main__":
    # 是否实例是EIP实例
    instance_is_eip = True
    try:
        f = open(sys.argv[1])
    except IOError:
        print 'File load Error'
        sys.exit(0)
    print 'InstanceID,NewEIPIp,NewEIpId,OldEIPIp,OldEIPId'
    kec_client = createSdkClinet("kec",region)
    eip_client = createSdkClinet("eip",region)
    content = f.readline()
    content = content.replace("\n", "")
    while content:
        content = f.readline()
        content = content.replace("\n", "")
        if content != '':
            contents = content.split(',')
            vm_id = content[0]
            if instance_is_eip:
                # 查询EIP信息
                param_eip = {
                    "AllocationId.1": contents[0]
                }
                eip_result = eip_client.describe_addresses(**param_eip)
                for item in eip_result['AddressesSet']:
                    old_eip_ip = item['PublicIp']
                    old_eip_id = item['AllocationId']
                    vif_id = item['NetworkInterfaceId']

                # 查询主机信息
                param_kec = {
                      "Filter.1.Name": 'network-interface.network-interface-id',
                      'Filter.1.Value.1': vif_id
                }
                kec_result = kec_client.describe_instances(**param_kec)
                vm_id = kec_result["InstancesSet"][0]["InstanceId"]
            else:
                # 查询主机的网卡信息
                param_kec = {
                    'InstanceId.1': contents[0]
                }
                kec_result = kec_client.describe_instances(**param_kec)
                vif_id = kec_result["InstancesSet"][0]["NetworkInterfaceSet"][0]["NetworkInterfaceId"]
                # 根据网卡信息查询原先绑定的EIP信息
                param_eip = {
                    "Filter.1.Name": 'network-interface-id',
                    'Filter.1.Value.1': vif_id
                }
                eip_result = eip_client.describe_addresses(**param_eip)
                for item in eip_result['AddressesSet']:
                    old_eip_ip = item['PublicIp']
                    old_eip_id = item['AllocationId']

            # 解绑EIP
            if old_eip_id:
                param_eip_dis = {
                    'AllocationId': old_eip_id
                }
                print param_eip_dis
                eip_client.disassociate_address(**param_eip_dis)

            # 查询新EIP
            param_new_eip = {
                "Filter.1.Name": "public-ip",
                "Filter.1.Value.1" : contents[1]
            }
            new_eip_result = eip_client.describe_addresses(**param_new_eip)
            for item in new_eip_result['AddressesSet']:
                new_eip_id = item['AllocationId']
                new_eip_ip = item['PublicIp']
            # 绑定EIP
            if new_eip_id:
                param_eip_ass = {
                    'AllocationId': new_eip_id,
                    'InstanceType': 'Ipfwd',
                    'InstanceId': vm_id,
                    'NetworkInterfaceId': vif_id
                }
                print param_eip_ass
                eip_client.associate_address(**param_eip_ass)
            # 输出结果
            print vm_id+','+new_eip_ip+','+new_eip_id+','+old_eip_ip+','+old_eip_id