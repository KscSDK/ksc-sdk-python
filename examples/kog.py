# -*- encoding:utf-8 -*-

from kscore.session import get_session
from test import *

if __name__ == "__main__":

    s = get_session()

    client = s.create_client("kog", use_ssl=True)

    # asset_server_test(client)

    # project_test(client)

    # group_test(client)
    #
    # method_test(client)
    #

    #
    # role_test(client)
    #
    # version_test(client)
    #
    # server_test(client)
    #
    # message_center_test(client)
    #
    # asset_region_test(client)
    #
    # object_variables_test(client)
    #
    for task in client.get_deploy_history_last():
        print '最近不同任务列表的元素:', task

    for diff_kind_task in client.get_history_last():
        print '最近不同类型任务列表的元素:', diff_kind_task

    # application_test(client)

    # package_test(client)

    # deploy_settings_template_test(client)
    #
    # version_test(client)
