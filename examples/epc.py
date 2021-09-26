#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    region='cn-beijing-6'
    epcClient = s.create_client("epc", region, use_ssl=True)

    # 注:如果参数名中包含.请使用JSON格式数据，如参数名 HostId.N 、 Filter.N.Name 、 Filter.N.Value.1

    # ------------------CreateEpc（ 创建云物理主机）--------------------------
    # param = {
    #     'AvailabilityZone': 'cn-shanghai-3b',
    #     'ImageId': 'f38624d3-0719-4e5d-970f-cad32095a7cf',
    #     'HostName': 'test',
    #     'NetworkInterfaceMode': 'single',
    #     'SubnetId': '58c57698-4bf0-4af9-a984-fb152e54a866',
    #     'SecurityGroupId.1': '251905f6-1316-4533-a599-ac8481a9afae',
    #     'SecurityGroupId.2': 'fb76854b-f23a-4354-ac07-4a12aec29c71',
    #     'KeyId': '66182581-fe49-41d8-b2c4-1c59ba6d200a',
    #     'ChargeType': 'PostPaidByDay',
    #     'Password': 'Test@Password1234',
    #     'SecurityAgent': 'classic',
    #     'CloudMonitorAgent': 'classic',
    #     'Raid': 'Raid1',
    #     'HostType': 'CAL'
    # }
    # resp=epcClient.create_epc(**param)
    # print(resp)

    # ------------------DeleteEpc(删除云物理主机)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87'
    # }
    # resp = epcClient.delete_epc(**param)
    # # # 或者
    # # resp = epcClient.delete_epc(HostId='a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87')
    # print(resp)

    # ------------------ModifyEpc(更新云物理主机信息)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'HostName': 'test1'
    # }
    # # resp = epcClient.modify_epc(**param)
    # # # 或者
    # # resp = epcClient.modify_epc(HostId='a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',HostName='test2')
    # print(resp)

    # ------------------DescribeEpcs(获取云物理主机列表信息)--------------------------
    # 简单查询
    # resp=epcClient.describe_epcs(MaxResults=7,NextToken=1)
    # 复杂查询
    param = {
        'HostId.1': 'd25d1261-506b-427b-8637-2fc6f7fcc0e1',
        'HostId.2': 'f3207312-8be0-44d5-af1c-96f899751711',
        'Filter.1.Name': 'host-type',
        'Filter.1.Value.1': 'CAL',
        'Filter.1.Value.2': 'SSD',
        'MaxResults': 20,
        'NextToken': 1
    }
    resp=epcClient.describe_epcs(**param)
    print(resp)

    # ------------------StartEpc( 启动云物理主机)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87'
    # }
    # resp = epcClient.start_epc(**param)
    # print(resp)

    # ------------------StopEpc (关闭云物理主机)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87'
    # }
    # resp = epcClient.stop_epc(**param)
    # print(resp)

    # ------------------RebootEpc(重启云物理主机)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87'
    # }
    # resp = epcClient.reboot_epc(**param)
    # print(resp)

    # ------------------ReinstallEpc（重装云物理主机）--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'ImageId': '0b11b872-d8e6-11e8-803a-e8611f1450d8',
    #     'KeyId':'66182581 - fe49 - 41d8 - b2c4 - 1c59ba6d200a',
    #     'Password':'Test@Password1234',
    #     'NetworkInterfaceMode':'bond4',
    #     'SecurityAgent':'classic',
    #     'CloudMonitorAgent':'classic',
    #     'Raid':'Raid1'
    # }
    # resp = epcClient.reinstall_epc(**param)
    # print(resp)

    # ------------------ReinstallCustomerEpc（重装托管云物理主机）--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'ServerIp': '127.0.0.1',
    #     'Path': '/linux.0'
    # }
    # resp = epcClient.reinstall_customer_epc(**param)
    # print(resp)

    # ------------------ReinstallCustomerEpc（重装托管云物理主机）--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'ServerIp': '127.0.0.1',
    #     'Path': '/linux.0'
    # }
    # resp = epcClient.reinstall_customer_epc(**param)
    # print(resp)

    # ------------------CreateImage(创建自定义镜像)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'ImageName': 'image-test'
    # }
    # resp = epcClient.create_image(**param)
    # print(resp)

    # ------------------ModifyImage(修改自定义镜像信息)--------------------------
    # param = {
    #     'ImageId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'ImageName': 'image-update'
    # }
    # resp = epcClient.modify_image(**param)
    # print(resp)

    # ------------------DeleteImage(删除自定义镜像)--------------------------
    # param = {
    #     'ImageId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87'
    # }
    # resp = epcClient.delete_image(**param)
    # print(resp)

    # ------------------DescribeImages(查看云物理主机镜像信息)--------------------------
    # param = {
    #     'ImageId.1': '9841bf74-1503-11ec-8427-e8611f1450d8',
    #     'ImageId.2':'8747e162-1503-11ec-8427-e8611f1450d8',
    #     'ImageId.3':'prtba3010e4-b671-40d8-8252-2b77ae292d71',
    #     'Filter.1.Name': 'image-type',
    #     'Filter.1.Value.1': 'base',
    #     'Filter.1.Value.2': 'private',
    #     'Filter.2.Name': 'disk-type',
    #     'Filter.2.Value.1': 'local',
    # }
    # resp = epcClient.describe_images(**param)
    # print(resp)

    # ------------------ModifyNetworkInterfaceAttribute(修改网卡信息)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'NetworkInterfaceId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'SubnetId': '58c57698-4bf0-4af9-a984-fb152e54a866',
    #     'IpAddress':'10.10.10.10',
    #     'SecurityGroupId.1': '251905f6-1316-4533-a599-ac8481a9afae'
    # }
    # resp = epcClient.modify_network_interface_attribute(**param)
    # print(resp)

    # ------------------ModifyDns(修改网卡DNS信息)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'NetworkInterfaceId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'DNS1': '10.10.10.10',
    #     'DNS2': '10.10.10.10'
    # }
    # resp = epcClient.modify_dns(**param)
    # print(resp)

    # ------------------ModifySecurityGroup(修改网卡安全组信息)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'NetworkInterfaceId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'SecurityGroupId.1': '251905f6-1316-4533-a599-ac8481a9afae'
    # }
    # resp = epcClient.modify_security_group(**param)
    # print(resp)

    # ------------------DescribePhysicalMonitor(获取硬件监控信息)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87'
    # }
    # resp = epcClient.describe_physical_monitor(**param)
    # print(resp)

    # ------------------CreateRemoteManagement（创建带外管理)--------------------------
    # param = {
    #     'PhoneNumber': '12345678901',
    #     'Pin': '111111',
    #     'Name': 'test'
    # }
    # resp = epcClient.create_remote_management(**param)
    # print(resp)

    # ------------------ModifyRemoteManagement（修改带外管理)--------------------------
    # param = {
    #     'RemoteManagementId': 'b75c6797-5562-4af4-b96f-38aeb0b4329f',
    #     'Name': 'test2'
    # }
    # resp = epcClient.modify_remote_management(**param)
    # print(resp)

    # ------------------DeleteRemoteManagement（删除带外管理)--------------------------
    # param = {
    #     'RemoteManagementId': 'b75c6797-5562-4af4-b96f-38aeb0b4329f'
    # }
    # resp = epcClient.delete_remote_management(**param)
    # print(resp)

    # ------------------GetDynamicCode（获取验证码)--------------------------
    # param = {
    #     'RemoteManagementId': 'b75c6797-5562-4af4-b96f-38aeb0b4329f'
    # }
    # resp = epcClient.get_dynamic_code(**param)
    # print(resp)

    # ------------------DescribeRemoteManagements（查询带外管理信息)--------------------------
    # param = {
    #     'RemoteManagementId.1': '5d6620c1-6a23-40e4-bfd6-9be8ed7afc65'
    # }
    # resp = epcClient.describe_remote_managements(**param)
    # print(resp)

    # ------------------DescribeEpcManagements（查询ILO信息)--------------------------
    # param = {
    #     'RemoteManagementId': '5d6620c1-6a23-40e4-bfd6-9be8ed7afc65',
    #     'DynamicCode': '123456',
    #     'Pin': '111111',
    #     'MaxResults': 20,
    #     'NextToken': '1'
    # }
    # resp = epcClient.describe_epc_managements(**param)
    # print(resp)

    # ------------------DescribeVpns（查询VPN信息)--------------------------
    # param = {
    #     'RemoteManagementId': '5d6620c1-6a23-40e4-bfd6-9be8ed7afc65',
    #     'DynamicCode': '123456',
    #     'Pin': '111111'
    # }
    # resp = epcClient.describe_vpns(**param)
    # print(resp)

    # ------------------ModifyHyperThreading(修改超线程)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'HyperThreadingStatus': 'start'
    # }
    # resp = epcClient.modify_hyper_threading(**param)
    # print(resp)

    # ------------------ResetPassword(重置密码)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'Password': 'Test@Passwrod'
    # }
    # resp = epcClient.reset_password(**param)
    # print(resp)

    # ------------------DescribeEpcStocks(查询云物理主机的库存)--------------------------
    # param = {
    #     'Filter.1.Name': 'host-type',
    #     'Filter.1.Value.1': 'CAL',
    #     'Filter.1.Value.1': 'SSD'
    # }
    # resp = epcClient.describe_epc_stocks(**param)
    # print(resp)

    # ------------------DescribeEpcDeviceAttributes(获取云物理设备列表信息)--------------------------
    # param = {
    #     'Filter.1.Name': 'host-type',
    #     'Filter.1.Value.1': 'CAL',
    #     'Filter.1.Value.1': 'SSD'
    # }
    # resp = epcClient.describe_epc_device_attributes(**param)
    # print(resp)

    # ------------------DescribeProcesses(查询工单信息)--------------------------
    # param = {
    #     'OperationProcessId.1': '0a8b50f2-589a-445a-913a-b095fe60a726',
    #     'Filter.1.Name': 'sn',
    #     'Filter.1.Value.1': 'test-2-46',
    #     'MaxResults': 20,
    #     'NextToken': '1'
    # }
    # resp = epcClient.describe_processes(**param)
    # print(resp)

    # ------------------CreateProcess(创建故障替换工单)--------------------------
    # param = {
    #     'HostIdentificationType': 'sn',
    #     'Confirm': '0',
    #     'Content': 'test',
    #     'Type': 'fix',
    #     'AvailabilityZone': 'cn-shanghai-3b',
    #     'Title': 'test',
    #     'ProcessId': '79cd4aa4-8373-4387-a59f-ae5b31663671',
    #     'Sn': 'PC0KCJXS',
    #     'MachineCount': '1'
    # }
    # resp = epcClient.create_process(**param)
    # print(resp)

    # ------------------DeleteProcess(删除工单信息)--------------------------
    # param = {
    #     'OperationProcessId': '0a8b50f2-589a-445a-913a-b095fe60a726',
    # }
    # resp = epcClient.delete_process(**param)

    # print(resp)

    # ------------------ReplyProcess(回复工单信息)--------------------------
    # param = {
    #     'OperationProcessId': '0a8b50f2-589a-445a-913a-b095fe60a726',
    #     'Remarks': 'test'
    # }
    # resp = epcClient.reply_process(**param)
    # print(resp)

    # ------------------DescribeInspections(物理机巡检信息)--------------------------
    # param = {
    #     'MaxResults': 20,
    #     'NextToken': '1'
    # }
    # resp = epcClient.describe_inspections(**param)

    # print(resp)

    # ------------------CreateCabinet （创建机柜）-------------------------
    # param = {
    #     'CabinetName': 'test',
    #     'ChargeType': 'PostPaidByDay',
    #     'CabinetType': 'Reserved',
    #     'AvailabilityZone': 'cn-shanghai-3a'
    # }
    # resp = epcClient.create_cabinet(**param)
    # print(resp)

    # ------------------DescribeCabinets(获取云物理主机托管机柜列表信息)--------------------------
    # param = {
    #     'CabinetId.1': '597f7731-0359-4604-b2cd-08586d2bcaf4',
    #     'MaxResults': 20,
    #     'NextToken': '1'
    # }
    # resp = epcClient.describe_cabinets(**param)
    # print(resp)

    # ------------------ModifySecurityGroup(修改网卡安全组信息)--------------------------
    # param = {
    #     'HostId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'NetworkInterfaceId': 'a0e64a51-2fb9-4dd6-b5c4-0dcd8ff79b87',
    #     'SecurityGroupId.1': '251905f6-1316-4533-a599-ac8481a9afae'
    # }
    # resp = epcClient.modify_security_group(**param)
    # print(resp)