#!/usr/bin/python
# -*- encoding:utf-8 -*-
# example for eip

import pprint
from kscore.session import get_session

#设置相关参数
service = "bws"
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

#创建共享带宽
def test_create_band_width_share(client):
    param = {
        "LineId":"####",
        "BandWidthShareName":"####",
        "BandWidth":"####",
        "Charge":"####"
    }
    result = client.create_band_width_share(**param)
    pprint.pprint(result)
    return result

#删除共享带宽
def test_delete_band_width_share(client):
    param = {
        "BandWidthShareId":"####"
    }
    result = client.create_band_width_share(**param)
    pprint.pprint(result)
    return result

#绑定共享带宽
def test_associate_band_width_share(client):
    param = {
        "BandWidthShareId":"####",
        "AllocationId":"####"
    }
    result = client.associate_band_width_share(**param)
    pprint.pprint(result)
    return result

#解绑共享带宽
def test_disassociate_band_width_share(client):
    param = {
        "BandWidthShareId":"####",
        "AllocationId":"####",
        "BandWidth":"N"
    }
    result = client.disassociate_band_width_share(**param)
    pprint.pprint(result)
    return result

#查询共享带宽
def test_describe_band_width_shares(client):
    param = {
        "BandWidthShareId.N":"####",
        "Filter.1.Name":"####",
        "Filter.1.Value.1":"####"
    }
    result = client.describe_band_width_shares(**param)
    pprint.pprint(result)
    return result

#更新共享带宽
def test_modify_band_width_share(client):
    param = {
        "BandWidthShareId":"####",
        "BandWidth":"N"
    }
    result = client.modify_band_width_share(**param)
    pprint.pprint(result)
    return result

if __name__ == "__main__":

    # 获取链接
    client = test_get_client()
    # 创建
    test_create_band_width_share(client)
    # 查询
    test_describe_band_width_shares(client)
    # 绑定
    test_associate_band_width_share(client)
    #解绑
    test_disassociate_band_width_share(client)
    # 更新
    test_modify_band_width_share(client)
    # 查询
    test_describe_band_width_shares(client)