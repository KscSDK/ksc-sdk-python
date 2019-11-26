# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()
    #确定服务名称以及机房
    mongoClient = s.create_client("mongodb", "cn-shanghai-3", use_ssl=False)
    # 创建MongoDB实例
    #print(mongoClient.create_mongo_db_instance(**{'Name': 'pjl_sdk_test0921', 'Capacity': 1, 'NetType': 2, 'VpcId': '3c12ccdf-9b8f-4d9b-8aa6-a523897e97a1', 'VnetId': '293c16a5-c757-405c-a693-3b2a3adead50'}))

    # 删除mongo实例
    #print(mongoClient.delete_mongo_db_instance(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 查询mongodb实例列表
    #print(mongoClient.describe_mongo_db_instances(**{}))

    # 查看MongoDB实例详情
    #print(mongoClient.describe_mongo_db_instance(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 重命名MongoDB实例
    #print(mongoClient.rename_mongo_db_instance(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb', 'Name':'xxdfdsdf'}))

    # 重启MongoDB实例
    #print(mongoClient.restart_mongo_db_instance(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 查询副本集实例节点信息
    #print(mongoClient.describe_mongo_db_instance_node(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 查看服务安全规则
    #print(mongoClient.list_security_group_rules(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 删除安全组规则
    #print(mongoClient.delete_security_group_rules(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb', 'Cidrs': '0.0.0.0/16'}))

    # 添加安全组规则
    #print(mongoClient.add_security_group_rule(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb', 'Cidrs': '0.0.0.0/16'}))

    # 创建手动备份
    #print(mongoClient.create_mongo_db_snapshot(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb', 'Name': 'xxxxx'}))

    # 创建自动备份
    #print(mongoClient.set_mongo_db_timing_snapshot(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb', 'TimingSwitch': 'Off', 'Timezone': '8:00-9:00', 'TimeCycle': 1}))

    # 删除实例备份
    #print(mongoClient.delete_mongo_db_snapshot(**{'SnapshotId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 查看实例备份列表
    #print(mongoClient.describe_mongo_db_snapshot(**{'InstanceId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # mongodb重命名备份
    #print(mongoClient.rename_mongo_db_snapshot(**{'SnapshotId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb', 'Name': "123123"}))

    # 查询机房
    #print(mongoClient.describe_regions(**{}))

    # 查询mongodb分片节点
    #print(mongoClient.describe_mongo_db_shard_node(**{'InstanceId': 'pjl_sdk_test0921'}))

    # 副本集添加secondary节点
    #print(mongoClient.add_secondary_instance(**{'InstanceId': 'pjl_sdk_test0921', 'NodeNum': 5}))

    # 创建MongoDB分片实例
    #print(mongoClient.create_mongo_db_shard_instance(**{'Name': 'pjl_sdk_test0921', 'Capacity': 1, 'NetType': 2, 'VpcId': '3c12ccdf-9b8f-4d9b-8aa6-a523897e97a1', 'VnetId': '293c16a5-c757-405c-a693-3b2a3adead50'}))
