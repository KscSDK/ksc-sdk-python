#!/usr/bin/python

# -*- encoding:utf-8 -*-

#使用方法
'''
专属宿主机批量挂盘
python Vm DedicatedVmAddDataDisk.py.py 50 filename
50 代表数据盘大小值
'''
#filename 的文件格式示例
'''
192.168.1.1
192.268.1.2
'''
#示例文件
'''
DedicatedVmAddDataDisk
'''

from kscore.session import get_session
import sys
import time
from kscore.exceptions import ClientError

ks_access_key_id ='ak'
ks_secret_access_key = 'sk'

def checkKecStateAndUpdate(ip,instanceId):
    check = 0

    while check == 0:
        time.sleep(20)
        try:
            kec = kecClient.describe_instances(**{'InstanceId.1': instanceId})
        except ClientError, e:
            print 'query vm by ip ' + ip + ' error '+str(e)
        else:
            for _kec in kec['InstancesSet']:
                status = _kec['InstanceState']['Name']
                if status == 'stopped':
                    check = 1
                    cpu = _kec['InstanceConfigure']['VCPU']
                    mem = _kec['InstanceConfigure']['MemoryGb']
    print ip + " is stop "
    modifyKec(ip,instanceId,diskSize,cpu,mem)
    check = 0
    while check == 0:
        time.sleep(20)
        try:
            kec = kecClient.describe_instances(**{'InstanceId.1': instanceId})
        except ClientError, e:
            print 'query vm by ip ' + ip + ' error '+str(e)
        else:
            for _kec in kec['InstancesSet']:
                status = _kec['InstanceState']['Name']
                if status == 'stopped':
                    check = 1
    print ip + " is complete modify "

    startKec(ip,instanceId)

def modifyKec(ip,instanceId,diskSize,cpu,mem):
    try:
        kecClient.modify_instance_type(**{'InstanceId': instanceId ,'InstanceConfigure.VCPU':cpu,'InstanceConfigure.DataDiskGb':diskSize,'InstanceConfigure.MemoryGb':mem})
    except ClientError, e:
        print 'modify vm by ip ' + ip + ' error '+str(e)
    else:
        print ip + ' modify !!!!'

def startKec(ip,instanceId):
    try:
        kecClient.start_instances(**{'InstanceId.1': instanceId})
    except ClientError, e:
        print 'start vm by ip ' + ip + ' error '+str(e)
    else:
        print ip + ' start !!!!'

if __name__ == "__main__":
    if len(sys.argv) == 3:
        diskSize = sys.argv[1]
        fileName = sys.argv[2];
        s = get_session()
        s.set_credentials(ks_access_key_id, ks_secret_access_key)
        region = 'cn-shanghai-2'
        vifClient = s.create_client("vpc", region, use_ssl=True)
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
                if size > 1:
                    print 'find ip '+ip+' have multi vif ,please check'
                else:
                    for item in vifs['NetworkInterfaceSet']:
                        instanceId = item['InstanceId']
                        kecClient = s.create_client("kec", region, use_ssl=True)
                        try:
                            kecClient.stop_instances(**{'InstanceId.1': instanceId})
                        except ClientError, e:
                            print 'shutdown vm by ip ' + ip + ' error '+str(e)
                        else:
                            print ip + ' shutdown !!!!'
                            checkKecStateAndUpdate(ip , instanceId)
            except ClientError, e:
                print ' query vm by ip '+ip+' error '+str(e)
            ip = f.readline()
        f.close()
    else:
        print "Parameter Error Must Support action and file"
