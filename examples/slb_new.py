#!/usr/bin/python
# -*- encoding:utf-8 -*-
# example for eip

import pprint
from kscore.session import get_session

#设置相关参数
service = "slb"
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

#创建负载均衡
def test_create_load_balancer(client):
    param = {
        "VpcId" : "####",
        "LoadBalancerName" : "####",
        "Type" : "####",
        "SubnetId" : "####",
        "PrivateIpAddress" : "####"
    }
    result = client.create_load_balancer(**param)
    pprint.pprint(result)
    return result


#删除负载均衡
def test_delete_load_balancer(client):
    param = {
        "LoadBalancerId" : "####"
    }
    result = client.delete_load_balancer(**param)
    pprint.pprint(result)
    return result

#修改负载均衡
def test_modify_load_balancer(client):
    param = {
        "LoadBalancerId" : "####",
        "LoadBalancerName" : "####",
        "LoadBalancerState" : "####"
    }
    result = client.modify_load_balancer(**param)
    pprint.pprint(result)
    return result

#查询负载均衡
def test_describe_load_balancers(client):
    param = {
        "LoadBalancerId.1" : "####",
        "State" : "####",
        "ProjectId.N" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value.1" : "####"
    }
    result = client.describe_load_balancer(**param)
    pprint.pprint(result)
    return result

#创建监听器
def test_create_listeners(client):
    param = {
        "LoadBalancerId" : "####",
        "ListenerState" : "####",
        "ListenerName" : "####",
        "ListenerProtocol" : "####",
        "CertificateId" : "####",
        "ListenerPort" : "####",
        "Method" : "####",
        "SessionState" : "####",
        "SessionPersistencePeriod" : "####",
        "CookieType" : "####",
        "CookieName" : "####"
    }
    result = client.create_listeners(**param)
    pprint.pprint(result)
    return result

#更改监听器
def test_modify_listeners(client):
    param = {
        "ListenerId" : "####",
        "CertificateId" : "####",
        "ListenerName" : "####",
        "ListenerState" : "####",
        "SessionState" : "####",
        "Method" : "####",
        "SessionPersistencePeriod" : "####",
        "CookieType" : "####",
        "CookieName" : "####"
    }
    result = client.modify_listeners(**param)
    pprint.pprint(result)
    return result

#删除监听器
def test_delete_listeners(client):
    param = {
        "ListenerId" : "####"
    }
    result = client.delete_listeners(**param)
    pprint.pprint(result)
    return result

#查询监听器
def test_describe_listeners(client):
    param = {
        "ListenerId.1" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value" : "####"
    }
    result = client.describe_listeners(**param)
    pprint.pprint(result)
    return result

#创建健康检查
def test_configure_health_check(client):
    param = {
        "ListenerId" : "####",
        "HealthCheckState" : "####",
        "HealthyThreshold" : "####",
        "Interval" : "####",
        "Timeout" : "####",
        "UnhealthyThreshold" : "####",
        "UrlPath" : "####",
        "isDefaultHostName" : "####",
        "HostName" : "####"
    }
    result = client.configure_health_check(**param)
    pprint.pprint(result)
    return result

#修改健康检查
def test_modify_health_check(client):
    param = {
        "HealthCheckId" : "####",
        "HealthCheckState" : "####",
        "HealthyThreshold" : "####",
        "Interval" : "####",
        "Timeout" : "####",
        "UnhealthyThreshold" : "####",
        "UrlPath" : "####",
        "isDefaultHostName" : "####",
        "HostName" : "####"
    }
    result = client.modify_health_check(**param)
    pprint.pprint(result)
    return result

#删除健康检查
def test_delete_health_check(client):
    param = {
        "HealthCheckId" : "####"
    }
    result = client.delete_health_check(**param)
    pprint.pprint(result)
    return result

#查询健康检查
def test_describe_health_checks(client):
    param = {
        "HealthCheckId.1" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value.1" : "####"
    }
    result = client.describe_health_check(**param)
    pprint.pprint(result)
    return result

#添加后端服务
#绑定真实服务器
def test_register_instances_with_listener(client):
    param = {
        "ListenerId" : "####",
        "RealServerIp" : "####",
        "RealServerPort" : "####",
        "RealServerType" : "####",
        "InstanceId" : "####",
        "Weight" : "####"
    }
    result = client.register_instances_with_listener(**param)
    pprint.pprint(result)
    return result

#修改后端服务
def test_modify_instances_with_listener(client):
    param = {
        "RegisterId" : "####",
        "RealServerPort" : "####",
        "Weight" : "####"
    }
    result = client.modify_instances_with_listener(**param)
    pprint.pprint(result)
    return result

#解绑后端服务
def test_deregister_instances_from_listener(client):
    param = {
        "RegisterId" : "####"
    }
    result = client.deregister_instances_from_listener(**param)
    pprint.pprint(result)
    return result

#描述后端服务
def test_describe_instances_with_listener(client):
    param = {
        "RegisterId.N" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value.1" : "####"
    }
    result = client.describe_instances_with_listener(**param)
    pprint.pprint(result)
    return result

#创建证书
def test_create_certificate(client):
    param = {
        "CertificateName" : "####",
        "PrivateKey" : "####",
        "PublicKey" : "####"
    }
    result = client.create_certificate(**param)
    pprint.pprint(result)
    return result

#删除证书
def test_delete_certificate(client):
    param = {
        "CertificateId" : "####"
    }
    result = client.delete_certificate(**param)
    pprint.pprint(result)
    return result

#更新证书
def test_modify_certificate(client):
    param = {
        "CertificateId" : "####",
        "CertificateName" : "####"
    }
    result = client.modify_certificate(**param)
    pprint.pprint(result)
    return result

#描述证书
def test_describe_certificates(client):
    param = {
        "CertificateId.N" : "####"
    }
    result = client.describe_cerfificates(**param)
    pprint.pprint(result)
    return result

if __name__ == "__main__":

    pass