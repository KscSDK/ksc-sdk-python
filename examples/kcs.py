# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    #确定服务名称以及机房
    kcsClient = s.create_client("kcs", "cn-shanghai-3", use_ssl=False)

    # 创建缓存服务
    #print(kcsClient.create_cache_cluster(**{'Action': 'CreateCacheCluster', 'Version': '2016-07-01', 'Name': 'pjl_sdk_test0921', 'Capacity': 1, 'NetType': 2, 'VpcId': '3c12ccdf-9b8f-4d9b-8aa6-a523897e97a1', 'VnetId': '293c16a5-c757-405c-a693-3b2a3adead50'}))

    # 查询缓存服务列表
    #print(kcsClient.describe_cache_clusters(**{'Action': 'DescribeCacheClusters', 'Version': '2016-07-01', 'Offset': 0, 'Limit': 5, 'OrderBy': 'created,desc'}))

    # 查询缓存服务详情
    #print(kcsClient.describe_cache_cluster(**{'Action': 'DescribeCacheCluster', 'Version': '2016-07-01', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 重命名缓存服务
    #print(kcsClient.rename_cache_cluster(**{'Action': 'RenameCacheCluster', 'Version': '2016-07-01', 'Name': 'pjl_test_sdk', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 清空缓存服务
    #print(kcsClient.flush_cache_cluster(**{'Action': 'FlushCacheCluster', 'Version': '2016-07-01', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 锁定缓存服务
    #print(kcsClient.lock_cache_cluster(**{'Action': 'LockCacheCluster', 'Version': '2016-07-01', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 解锁缓存服务
    #print(kcsClient.unlock_cache_cluster(**{'Action': 'UnlockCacheCluster', 'Version': '2016-07-01', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 更配缓存服务
    #print(kcsClient.resize_cache_cluster(**{'Action': 'ResizeCacheCluster', 'Version': '2016-07-01', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb', 'Capacity': 2}))

    # 删除缓存服务
    #print(kcsClient.delete_cache_cluster(**{'Action': 'DeleteCacheCluster', 'Version': '2016-07-01', 'CacheId': 'b80ef266-dd52-47b2-9377-6a4a73626c19'}))

    # 查询缓存服务参数
    #print(kcsClient.describe_cache_parameters(**{'Action': 'DescribeCacheParameters', 'Version': '2016-07-01', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 设置缓存服务参数
    #print(kcsClient.set_cache_parameters(**{'Action': 'SetCacheParameters', 'Version': '2016-07-01', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb', 'Parameters.ParameterName.1': 'maxmemory-policy', 'Parameters.ParameterValue.1': 'allkeys-lru', 'ResetAllParameters': 'true'}))

    # 查询缓存服务安全规则
    #print(kcsClient.describe_cache_security_rules(**{'Action': 'DescribeCacheSecurityRules', 'Version': '2016-07-01', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb'}))

    # 设置缓存服务安全规则
    #print(kcsClient.set_cache_security_rules(**{'Action': 'SetCacheSecurityRules', 'Version': '2016-07-01', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb', 'SecurityRules.Cidr.1': '192.168.18.17/21'}))

    # 删除缓存服务安全规则
    #print(kcsClient.delete_cache_security_rule(**{'Action': 'DeleteCacheSecurityRule', 'Version': '2016-07-01', 'CacheId': '01988fc0-6041-49d2-b6b5-e2385e5d5edb', 'SecurityRuleId': 105}))