# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()
    # 确定服务名称以及机房
    krdsClient = s.create_client("krds", "cn-beijing-6", use_ssl=False, ks_access_key_id="",
                                 ks_secret_access_key="")

    # 查询缓存服务列表
    # https://docs.ksyun.com/documents/330
    print(krdsClient.describe_db_instances(**{'Marker': 0, 'MaxRecords': 10}))

