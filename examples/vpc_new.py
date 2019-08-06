#!/usr/bin/python
# -*- encoding:utf-8 -*-
# example for eip

import pprint
from kscore.session import get_session

#设置相关参数
service = 'vpc'
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

#查看可用区信息
def test_describe_availability_zones(client):
    result = client.describe_availability_zones()
    pprint.pprint(result)
    return result

#描述网卡信息
def test_describe_network_interfaces(client):
    param = {
        "NetworkInterfaceId.N" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value.1" : "####"
    }
    result = client.describe_network_interfaces(**param)
    pprint.pprint(result)
    return result

#创建vpc
def test_create_vpc(client):
    param = {
        "VpcName" : "####",
        "CidrBlock" : "####",
        "IsDefault" : "####"
    }
    result = client.create_vpc(**param)
    pprint.pprint(result)
    return result

#删除vpc
def test_delete_vpc(client):
    param = {
        "VpcId" : "####",
    }
    result = client.delete_vpc(**param)
    pprint.pprint(result)
    return result

#修改vpc
def test_modify_vpc(client):
    param = {
        "VpcId" : "####",
        "VpcName" : "####"
    }
    result = client.modify_vpc(**param)
    pprint.pprint(result)
    return result

#查询vpc
def test_describe_vpcs(client):
    param = {
        "VpcId.N" : "####"
    }
    result = client.describe_vpcs(**param)
    pprint.pprint(result)
    return result

#创建子网
def test_create_subnet(client):
    param = {
        "AvailabilityZone" : "####",
        "SubnetName" : "####",
        "CidrBlock" : "####",
        "SubnetType" : "####",
        "DhcpIpFrom" : "####",
        "DhcpIpTo" : "####",
        "GatewayIp" : "####",
        "VpcId" : "####",
        "Dns1": "####",
        "Dns2": "####"
    }
    result = client.create_subnet(**param)
    pprint.pprint(result)
    return result

#删除子网
def test_delete_subnet(client):
    param = {
        "SubnetId" : "####"
    }
    result = client.delete_subnet(**param)
    pprint.pprint(result)
    return result

#修改子网
def test_modify_subnet(client):
    param = {
        "SubnetId" : "####",
        "SubnetName" : "####",
        "Dns1" : "####",
        "Dns2" : "####"
    }
    result = client.modify_subnet(**param)
    pprint.pprint(result)
    return result

#查询子网
def test_describe_subnets(client):
    param = {
        "SubnetId.N" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value.1" : "####"
    }
    result = client.describe_subnets(**param)
    pprint.pprint(result)
    return result

#查询子网可用IP信息
def test_describe_subnets_available_addresses(client):
    param = {
        "Filter.1.Name" : "subnet-id",
        "Filter.1.Value.1" : "####"
    }
    result = client.describe_subnets_available_addresses(**param)
    pprint.pprint(result)
    return result

#查询子网已用IP信息
def test_describe_subnet_allocated_ip_addresses(client):
    param = {
        "Filter.1.Name" : "subnet-id",
        "MaxResults": "####",
        "NextToken" : "####"
    }
    result = client.describe_subnet_allocated_ip_addresses(**param)
    pprint.pprint(result)
    return result

#创建路由
def test_create_route(client):
    param = {
        "VpcId" : "####",
        "DestinationCidrBlock" : "####",
        "RouteType" : "####",
        "TunnelId" : "####",
        "InstanceId" : "####",
        "VpcPeeringConnectionId" : "####",
        "DirectConnectGatewayId" : "####",
        "VpnTunnelId" : "####"
    }
    result = client.create_route(**param)
    pprint.pprint(result)
    return result

#删除路由
def test_delete_route(client):
    param =  {
        "RouteId" : "####"
    }
    result = client.delete_route(**param)
    pprint.pprint(result)
    return result

#查询路由信息
def test_describe_routes(client):
    param = {
        "RouteId.N" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value.1" : "####"
    }
    result = client.describe_routes(**param)
    pprint.pprint(result)
    return result

#创建ACL
def test_create_network_acl(client):
    param = {
        "VpcId" : "####",
        "NetworkAclName" : "####"
    }
    result = client.create_network_acl(**param)
    pprint.pprint(result)
    return result

#删除ACL
def test_delete_network_acl(client):
    param = {
        "NetworkAclId" : "####"
    }
    result = client.delete_network_acl(**param)
    pprint.pprint(result)
    return result

#修改ACL
def test_modify_network_acl(client):
    param = {
        "NetworkAclId" : "####",
        "NetworkAclName" : "####"
    }
    result = client.modify_network_acl(**param)
    pprint.pprint(result)
    return result

#关联ACL
def test_associate_network_acl(client):
    param = {
        "NetworkAclId" : "####",
        "SubnetId" : "####"
    }
    result = client.associate_network_acl(**param)
    pprint.pprint(result)
    return result

#解绑ACL
def test_disassociate_network_acl(client):
    param = {
        "NetworkAclId" : "####",
        "SubnetId" : "####"
    }
    result = client.disassociate_network_acl(**param)
    pprint.pprint(result)
    return result

#创建ACL规则
def test_create_network_acl_entry(client):
    param = {
        "Description" : "####",
        "NetworkAclId" : "####",
        "CidrBlock" : "####",
        "RuleNumber" : "####",
        "Direction" : "####",
        "RuleAction" : "####",
        "Protocol" : "####",
        "IcmpType" : "####",
        "IcmpCode" : "####",
        "PortRangeFrom" : "####",
        "PortRangeTo" : "####"
    }
    result = client.create_network_acl_entry(**param)
    pprint.pprint(result)
    return result

#删除ACL规则
def test_delete_network_acl_entry(client):
    param = {
        "NetworkAclId" : "####",
        "NetworkAclEntryId" : "####"
    }
    result = client.delete_network_acl_entry(**param)
    pprint.pprint(result)
    return result

#描述ACL信息
def test_describe_network_acls(client):
    param = {
        "NetworkAclId.N" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value.1": "####"
    }
    result = client.describe_network_acls(**param)
    pprint.pprint(result)
    return result

#创建安全组
def test_create_security_group(client):
    param = {
        "VpcId" : "####",
        "SecurityGroupName" : "####"
    }
    result = client.create_security_group(**param)
    pprint.pprint(result)
    return result

#删除安全组
def test_delete_security_group(client):
    param = {
        "SecurityGroupId" : "####",
    }
    result = client.delete_security_group(**param)
    pprint.pprint(result)
    return result

#修改安全组
def test_modify_security_group(client):
    param = {
        "SecurityGroupId" : "####",
        "SecurityGroupName" : "####"
    }
    result = client.modify_security_group(**param)
    pprint.pprint(result)
    return result

#创建安全组规则
def test_authorize_security_group_entry(client):
    param = {
        "Description" : "####",
        "SecurityGroupId" : "####",
        "CidrBlock": "####",
        "Direction": "####",
        "Protocol: "####",
        "IcmpType": "####",
        "IcmpCode": "####",
        "PortRangeFrom": "####",
        "PortRangeTo": "####",
    }
    result = client.authorize_security_group_entry(**param)
    pprint.pprint(result)
    return result

#删除安全组规则
def test_revoke_security_group_entry(client):
    param = {
        "SecurityGroupId" : "####",
        "SecurityGroupEntryId" : "####"
    }
    result = client.revoke_security_group_entry(**param)
    pprint.pprint(result)
    return result

#描述安全组信息
def test_describe_security_groups(client):
    param = {
        "SecurityGroupId.N" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value.1": "####"
    }
    result = client.describe_security_groups(**param)
    pprint.pprint(result)
    return result

#创建NAT
def test_create_nat(client):
    param = {
        "VpcId" : "####",
        "NatName" : "####",
        "NatMode" : "####",
        "NatType" : "####",
        "NatIpNumber" : "####",
        "BandWidth" : "####",
        "ChargeType" : "####",
        "PurchaseTime" : "####"
    }
    result = client.create_nat(**param)
    pprint.pprint(result)
    return result

#删除NAT
def test_delete_nat(client):
    param = {
        "NatId" : "####"
    }
    result = client.delete_nat(**param)
    pprint.pprint(result)
    return result

#修改NAT
def test_modify_nat(client):
    param = {
        "NatId" : "####",
        "BandWidth" : "####",
        "NatName" : "####"
    }
    result = client.modify_nat(**param)
    pprint.pprint(result)
    return result

#描述NAT
def test_describe_nats(client):
    param = {
        "NatId" : "####",
        "Filter.1.Name" : "####",
        "Filter.1.Value.l" : "####"
    }
    result = client.describe_nats(**param)
    pprint.pprint(result)
    return result

#绑定子网
def test_associate_nat(client):
    param = {
        "SubnetId" : "####",
        "NatId" : "####"
    }
    result = client.associate_network_nat(**param)
    pprint.pprint(result)
    return result

#解绑子网
def test_disassociate_nat(client):
    param = {
        "SubnetId" : "####",
        "NatId" : "####"
    }
    result = client.disassociate_nat(**param)
    pprint.pprint(result)
    return result

if __name__ == "__main__":
    pass