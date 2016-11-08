# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":

    s = get_session()

    client = s.create_client("kog", use_ssl=True)

    projects = client.get_project_list()
