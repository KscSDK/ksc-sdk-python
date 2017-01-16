# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":

    s = get_session()

    client = s.create_client("tag", region_name="cn-beijing-6", use_ssl=True)

    print client.describe_tags()
