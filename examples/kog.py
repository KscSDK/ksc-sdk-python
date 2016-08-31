# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    client = s.create_client("kog", use_ssl=True)

    projects = client.get_project_list()

    project = client.add_project(name='123123', comment='123123')

    project.update(name="bcd")

    client.edit_project(**project)

    client.delete_project(id=project['id'])

    assert projects == client.get_project_list()
