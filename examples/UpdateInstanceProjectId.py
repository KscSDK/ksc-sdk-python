#!/usr/bin/python
#coding:utf-8
# -*- encoding:utf-8 -*-

#使用方法
'''
实例和项目绑定
python UpdateInstanceProjectId.py filename projectId
'''
#filename 的文件格式示例
'''
eda6c7ec-4ecf-4f5e-ac0d-8e9f5b8530cf
eda6c7ec-4ecf-4f5e-ac0d-8e9f5b8530c2
eda6c7ec-4ecf-4f5e-ac0d-8e9f5b8530c3
'''
#示例文件
'''
UpdateInstanceProjectId
'''

from kscore.session import get_session
import sys
from kscore.exceptions import ClientError

ks_access_key_id ='ak'
ks_secret_access_key = 'sk'
region = 'cn-shanghai-2'


if __name__ == "__main__":
    if len(sys.argv) == 3:
        fileName = sys.argv[1]
        projectId = sys.argv[2]
        s = get_session()
        s.set_credentials(ks_access_key_id, ks_secret_access_key)
        iamClient = s.create_client("iam", region, use_ssl=True)
        try:
            f = open(fileName)
        except IOError:
            print 'File load Error'
            sys.exit(0)
        instanceId = f.readline()
        while instanceId:
            instanceId = instanceId.replace("\n", "")
            try:
                result = iamClient.update_instance_project_id(InstanceId=instanceId,ProjectId=projectId)
                print '实例ID:'+instanceId+'绑定项目:'+projectId+'的结果为'+str(result)
            except ClientError, e:
                print ' UpdateInstanceProjectId by instanceId '+instanceId+' error '+str(e)
            instanceId = f.readline()
        f.close()
    else:
        print "Parameter Error Must Support action and file"
