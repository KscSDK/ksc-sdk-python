#coding:utf-8
#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()
    vpcClient = s.create_client("vpc", "cn-beijing-6", use_ssl=True)
    # 获取物理专线列表，创建，修改和删除物理专线请联系售前或者销售
    vpcClient.describe_direct_connects()


    #创建专线通道 这里只是最简单参数，其他请按需添加
    param_dict = {
        "DirectConnectId": "物理专线ID",
        "DirectConnectInterfaceName": "ceshi"
    }
    #vpcClient.create_direct_connect_interface(**param_dict)

    #创建专线网关
    param_dict = {
        "VpcId": "虚拟私有网络id",
        "DirectConnectGatewayName": "ceshi-gw"
    }
    #vpcClient.create_direct_connect_gateway(**param_dict)

    #绑定专线网关
    param_dict = {
        "DirectConnectGatewayId": "专线网关id",
        "DirectConnectInterfaceId": "专线通道id"
    }
    #vpcClient.attach_direct_connect_gateway(**param_dict)

    #解绑专线网关
    param_dict = {
        "DirectConnectGatewayId": "专线网关id",
        "DirectConnectInterfaceId": "专线通道id"
    }
    #vpcClient.detach_direct_connect_gateway(**param_dict)

    #专线网关列表
    vpcClient.describe_direct_connect_gateways()

    #专线通道列表
    vpcClient.describe_direct_connect_interfaces()

    #删除专线网关
    param_dict={
        "DirectConnectGatewayId": "专线网关id"
    }
    #vpcClient.delete_direct_connect_gateway(**param_dict)

    #删除专线通道
    param_dict = {
        "DirectConnectInterfaceId": "专线通道id"
    }
    vpcClient.delete_direct_connect_interface(**param_dict)
