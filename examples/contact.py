# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    client = s.create_client("contact", "cn-beijing-6", use_ssl=False)

    param = {
        "StartTime": "2021-07-01",
        "EndTime": "2021-07-20",
        "PageNumber": 1,
        "PageSize": 10,
    }
    item = client.query_in_mail_list(**param)

    print(item)
