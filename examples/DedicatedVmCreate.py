#!/usr/bin/python
#coding=utf-8

from kscore.session import get_session
from kscore.exceptions import ClientError
import sys


#使用方法
'''
专属宿主机批量创建
python python DedicatedVmCreate.py inputfile.csv
'''

#输入文件格式（csv文件）示例
'''
InstanceName,Vcpus,Memory,DataDiskSize,InstancePassword,PrivateIpAddress,SubnetId,SecurityGroupId,DedicatedHostId,ImageId
Vm-1,4,8,100,123@123,10.0.0.1,9c29fe3e-6a16-41d0-85e3-94c52ffb1038,2d0ab207-6fa5-451c-b0f5-34d7244fd424,ac5a9f97-ab38-40ce-b284-df14282e0916,3dc0a83e-2dbf-4fd4-99c4-e620fcf4d849
'''
#可以参考 DedicatedVmCreate.csv
#属性解释
'''
InstanceName 主机名称
Vcpus cpu数量
Memory 内存大小
DataDiskSize 数据盘大小
InstancePassword 主机密码
PrivateIpAddress 内网IP
SubnetId 子网ID
SecurityGroupId 安全组ID
DedicatedHostId 专属宿主机ID
ImageId 镜像ID
'''

ak ='ak'
sk = 'sk'
region = 'cn-shanghai-2'




def createSdkClinet(service,region):
    s = get_session()
    s.set_credentials(ak,sk)
    client = s.create_client(service, region, use_ssl=True)
    return client

def createDedicatedVm(contents,content):
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
    except ClientError, e:
      print content+" process error,please check error is "+str(e)


def readConfigFileAndProcess():
    try:
        f = open(sys.argv[1])
    except IOError:
        print 'File load Error'
        sys.exit(0)
    content = f.readline()
    content = content.replace("\n", "")
    while content:
        content = f.readline()
        content = content.replace("\n", "")
        if content != '':
            createDedicatedVm(content.split(','),content)



if __name__ == '__main__':
    readConfigFileAndProcess()






