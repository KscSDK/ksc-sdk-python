#!/usr/bin/python
#coding=utf-8

#属性解释
'''
InstanceName 主机名称
DataDiskSize 数据盘大小 注意和快照大小一致
LocalVolumeSnapshotId 本地盘快照ID
InstancePassword 主机密码
SubnetId 子网ID
SecurityGroupId 安全组ID
ImageId 镜像ID
InstanceType 机型信息 必须是本地数据盘支持的机型
'''

from kscore.session import get_session

ak ='ak'
sk = 'sk'
region = 'cn-beijing-6'

if __name__ == '__main__':
    s = get_session()
    s.set_credentials(ak, sk)
    client = s.create_client("kec", region, use_ssl=True)

    param = {
        "MaxCount": "1",
        "MinCount": "1",
        "ImageId": "d3290df6-3597-4f83-b5ae-48356e91ad46",
        "SubnetId": "d72361fe-837b-4676-85ff-faa3b0b4ef73",
        "InstanceName": "TEST",
        "InstancePassword": "Aa123456",
        "SecurityGroupId": "e470911a-6ae7-481e-adc6-299ce3c932bc",
        "DataDiskGb": "20",
        "ChargeType": "Daily",
        "InstanceType": "S3.1A",
        "LocalVolumeSnapshotId": "e4189c4e-0a92-43a1-9b04-26a25184f3b7"
    }
    client.run_instances(**param)