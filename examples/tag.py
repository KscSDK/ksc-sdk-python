# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":

    s = get_session()

    client = s.create_client("tag", region_name="cn-beijing-6", use_ssl=True)

    print client.describe_tags()

    # https://docs.ksyun.com/documents/1327
    # 根据资源id查询tag
    print client.describe_tags(**{
        "Filter.1.Name": "resource-id",
        "Filter.1.Value.1": "fc175f56-d29d-497f-9f57-xxxxxxxxxxxx",
    })