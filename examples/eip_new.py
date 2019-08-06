#!/usr/bin/python
# -*- encoding:utf-8 -*-
# example for eip

import pprint
from kscore.session import get_session

#设置相关参数
service = "eip"
region = '####'
api = '####'
ssl = '####'
param_verify = '####'
endpoint = '####'
access_key = '####'
secret_key = '####'
session_token = '####'
param_config = '####'

#获取连接
def test_get_client():
    session = get_session()
    client = session.create_client(
        service_name = service,
        region_name = region,
        api_version = api,
        use_ssl = ssl,
        verify = param_verify,
        endpoint_url = endpoint,
        ks_access_key_id = access_key,
        ks_secret_access_key = secret_key,
        ks_session_token = session_token,
        param_config = param_config
    )
    return client

#查看链路信息
def test_getlines_eip(client):
    result = client.get_lines()
    pprint.pprint(result)
    return result

#创建EIP
def test_create_eip(client):
    param = {
        "LineId" : "####",
        "BandWidth" : "####",
        "ChargeType" : "####",
        "PurchaseTime" : "####",
        "ProjectId" : "####"
    }
    print "Param Of Create Eip Is", str(param)
    result = client.allocate_address(**param)
    pprint.pprint(result)
    return result

# 删除EIP
def test_release_eip(client):
    param = {
        "AllocationId" : "####"
    }
    print "Param Of Release Eip Is", str(param)
    result = client.release_address(**param)
    pprint.pprint(result)
    return result

# 绑定EIP
def test_associate_eip(client):
    param = {
        "AllocationId" : "####",
        "InstanceType" : "####",
        "InstanceId" : "####",
        "NetworkInterfaceId" : "####"
    }
    print "Param Of Associate Eip Is", str(param)
    result = client.associate_address(**param)
    pprint.pprint(result)
    return result

# 解绑EIP
def test_disassociate_eip(client):
    param = {
        "AllocationId" : "####"
    }
    print "Param Of Disassociate Eip Is", str(param)
    result = client.disassociate_address(**param)
    pprint.pprint(result)
    return result

#查询EIP信息
def test_describe_eip(client):
    param = {
        "AllocationId.N" : "####",
        "ProjectId.N" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value.1" : "####",
        "MaxResults" : 9 ,
        "NextToken" : "####"
    }
    print "Param Of Describe Eip Is", str(param)
    result = client.describe_addresses(**param)
    pprint.pprint(result)
    return result

#更新EIP
def test_modify_eip(client):
    param = {
        "AllocationId" : "####",
        "BandWidth" : "####"
    }
    print "Param Of Modify Eip Is", str(param)
    result = client.modify_address(**param)
    pprint.pprint(result)
    return result


if __name__ == "__main__":

    # 获取链接
    client = test_get_client()
    # 查看链路
    test_getlines_eip(client)
    # 创建EIP
    test_create_eip(client)
    # 更新
    test_modify_eip(client)
    # 绑定
    test_associate_eip(client)
    # 解绑
    test_disassociate_eip(client)
    # 删除
    test_release_eip(client)
    # 查询
    test_describe_eip(client)