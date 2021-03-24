# -*- encoding:utf-8 -*-
from kscore.exceptions import ClientError
from kscore.session import get_session
from pprint import pprint

if __name__ == "__main__":
    s = get_session()
    client = s.create_client("ebs", "cn-beijing-6", use_ssl=False)

    result = client.describe_volumes()

    print(result)
