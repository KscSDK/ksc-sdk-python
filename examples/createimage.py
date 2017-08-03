# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    client = s.create_client("kec", "cn-shanghai-2", use_ssl=True)

    print client.describe_instances()
    client.create_image(InstanceId='ce09c927-12f1-44bc-8a73-30d0b2d275a5',Name='tm-04-25')
#    client.create_user(UserName="test22", RealName=u"刘一辰")

#    client.update_user(UserName="test22",)

#    client.delete_user(UserName="test22")
