#!/usr/bin/python

# -*- encoding:utf-8 -*-

from kscore.session import get_session
import sys

#inputfile format（csv）
#InstanceName,Vcpus,Memory,DataDiskSize,InstancePassword,PrivateIpAddress,SubnetId,SecurityGroupId,DedicatedHostId,ImageId

ak ='ak'
sk = 'sk'
region = 'cn-shanghai-2'




def createSdkClinet(service,region):
    s = get_session()
    s.set_credentials(ak,sk)
    client = s.create_client(service, region, use_ssl=True)
    return client

def createDedicatedVm(contents):
    try:
        client = createSdkClinet("kec", region)
        param = {
            "MaxCount": "1",
            "MinCount": "1",
            "ImageId": contents[9],
            "SubnetId": contents[6],
            "InstanceName": contents[0],
            "InstancePassword": contents[4],
            "SecurityGroupId": contents[7],
            "DataDiskGb": contents[3],
            "ChargeType": "Daily",
            "InstanceType": "DVM1.NONE",
            "PrivateIpAddress": contents[5],
            "PurchaseTime": "0",
            "DedicatedHostId": contents[8],
            "InstanceConfigure.VCPU": contents[1],
            "InstanceConfigure.MemoryGb": contents[2],
            "InstanceConfigure.DataDiskGb": contents[3]
        }
        client.run_instances(**param)
        print param["InstanceName"]+" create success "
    except Exception:
        print contents+" process error,please check"


def readConfigFileAndProcess():
    try:
        f = open(sys.argv[1])
        content = f.readline()
        while content:
            content = f.readline()
            if content != '':
                createDedicatedVm(content.split(','))
    except Exception:
        print 'File load Error'
        sys.exit(0)



if __name__ == '__main__':
    readConfigFileAndProcess()






