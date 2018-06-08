#!/usr/bin/python
#coding=utf-8

#使用方法
'''
虚机批量重启 关机 删除
python Vm VmOperateStatus.py action filename
action 可选值
restart 重启
shutdown 关机
remove 删除
'''
#filename 的文件格式示例
'''
192.168.1.1
192.268.1.2
'''
#示例文件
'''
VmOperateStatus
'''

from kscore.exceptions import ClientError
from kscore.session import get_session
import sys

ks_access_key_id ='ak'
ks_secret_access_key = 'sk'

region = 'cn-shanghai-2'

if __name__ == "__main__":
    if len(sys.argv) == 3:
        action = sys.argv[1]
        fileName = sys.argv[2];
        s = get_session()
        s.set_credentials(ks_access_key_id, ks_secret_access_key)
        vifClient = s.create_client("vpc", region, use_ssl=True)
        kecClient = s.create_client("kec", region, use_ssl=True)
        eipClient = s.create_client("eip", region, use_ssl=True)
        slbClient = s.create_client("slb", region, use_ssl=True)
        try:
            f = open(fileName)
        except IOError:
            print 'File load Error'
            sys.exit(0)
        ip = f.readline()
        while ip:
            ip = ip.replace("\n", "")
            try:
                vifs = vifClient.describe_network_interfaces(**{'Filter.1.Name':'private-ip-address','Filter.1.Value.1': ip})
                size = len(vifs['NetworkInterfaceSet'])
                if size == 0:
                    print 'not find ip ' + ip + ' have multi vif ,please check'
                if size > 1:
                    print 'find ip '+ip+' have multi vif ,please check'
                else:
                    for item in vifs['NetworkInterfaceSet']:
                        instanceId = item['InstanceId']
                        deviceId = item['NetworkInterfaceId']
                        if action == 'restart':
                            try:
                                kecClient.reboot_instances(**{'InstanceId.1': instanceId})
                            except ClientError, e:
                                print 'restart vm by ip ' + ip + ' error '+str(e)
                            else:
                                print ip + ' ' + instanceId +' restart!!!!'
                        if action == 'shutdown':
                            try:
                                kecClient.stop_instances(**{'InstanceId.1': instanceId})
                            except ClientError, e:
                                print 'shutdown vm by ip ' + ip + ' error '+str(e)
                            else:
                                print ip + ' shutdown !!!!'
                        if action == 'remove':
                            try:
                                eipList = eipClient.describe_addresses(**{'Filter.1.Name': 'network-interface-id', 'Filter.1.Value.1': deviceId})
                                for eip in eipList['AddressesSet']:
                                    eipId = eip['AllocationId']
                                    eipClient.disassociate_address(AllocationId=eipId)
                                try:
                                    rsList = slbClient.describe_instances_with_listener(**{'Filter.1.Name':'instance-id','Filter.1.Value.1':instanceId})
                                    for rs in rsList['RealServerSet']:
                                        rsId = rs['RegisterId']
                                        slbClient.deregister_instances_from_listener(RegisterId=rsId)
                                    try:
                                        kecClient.terminate_instances(**{'InstanceId.1':instanceId})
                                        print 'remove vm by ip ' + ip + ' success '
                                    except ClientError, e:
                                        print 'remove vm by ip ' + ip + ' error '+str(e)
                                except ClientError, e:
                                    print 'DeregisterInstancesFromListener vm by ip ' + ip + ' error '+str(e)
                            except ClientError, e:
                                print 'DisassociateAddress vm by ip ' + ip + ' error '+str(e)
            except ClientError, e:
                print ' query vm by ip '+ip+' error '
            ip = f.readline()
        f.close()
    else:
        print "Parameter Error Must Support action and file"
