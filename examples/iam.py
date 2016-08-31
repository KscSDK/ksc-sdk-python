# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    client = s.create_client("iam", use_ssl=False)

    users = client.list_users()

    client.create_user(UserName="test22", RealName=u"刘一辰")

    client.update_user(UserName="test22",)

    client.delete_user(UserName="test22")
