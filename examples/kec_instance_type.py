# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    client = s.create_client("kec", "cn-beijing-6", use_ssl=False)

    #https://docs.ksyun.com/documents/5710
    result = client.describe_instance_type_configs()

    for item in result['InstanceTypeConfigSet']:
        print item['InstanceType']
        print item['AvailabilityZoneSet']

    # https://docs.ksyun.com/documents/5712
    result = client.describe_instance_familys()
    print result

    for item in result['InstanceFamilySet']:
        print item['InstanceFamilyName']
        if 'InstanceFamily' in item:
          print item['InstanceFamily']
