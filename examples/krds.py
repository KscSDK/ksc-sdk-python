# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()
    # 确定服务名称以及机房
    krdsClient = s.create_client("krds", "cn-beijing-6", use_ssl=False, ks_access_key_id="AKLT9rO-ssiXT3GGmdqhM3YVvw",
                                 ks_secret_access_key="OI+1Ra/Tgu53Q0iqzhD5TtXlzqJ1430rNTtFP6z6Be9ggowUr4HKYCkSxzOlVWh8xw==")

    # 查询KRDS服务列表
    # https://docs.ksyun.com/documents/330
    print(krdsClient.describe_db_instances(**{'Marker': 0, 'MaxRecords': 10}))
    print(krdsClient.create_db_instance_read_replica(**{'DBInstanceIdentifier': "fd6ab4e8-07d9-4784-8876-6f943ae0a667", 'DBInstanceName': "wws", "DBInstanceClass":"db.ram.5|db.disk.10"}))

