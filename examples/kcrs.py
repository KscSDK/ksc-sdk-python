# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()

    client = s.create_client("kcrs", "cn-beijing-6", use_ssl=True)
    # 查询镜像实例列表
    param = {
        "ProjectId.1": "0",
        "MaxResults": 20,
        "Marker": 0,
    }
    m = client.describe_instance(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''
    
    # 创建镜像实例
    param = {
        "InstanceName": "xxxxx2",
        "ChargeType":   "HourlyInstantSettlement",
        "InstanceType": "basic",
        "PurchaseTime": "1",
        "ProjectId":    "0",
    }
    m = client.create_instance(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''
    '''
    m = client.delete_instance(InstanceId="d11bbbc9-xxx")
    print json.dumps(m, sort_keys=True, indent=4)
    '''
    '''
    # 创建镜像实例访问凭证
    param = {
        "InstanceId": "c3fdd2ac-xxxx",
        "TokenType": "Hour",
        "TokenTime": "24",
    }
    m = client.create_instance_token(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''
