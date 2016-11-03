# -*- coding: utf-8 -*-

p_id = 'uuid'  # Project ID

app_id = 'uuid'  # Application ID

temp_id = 'uuid'  # Deploy Template Settings ID

# ID for Server
s_id = 'uuid'

# Group ID
g_id = 'uuid'

# AssertServer ID
server_id = 'uuid'

# Role ID
r_id = 'uuid'

# Method ID
m_id = 'uuid'

# AssetRegion ID
ar_id = 'uuid'

# AssetServer ID
as_id = 'uuid'

# Variable ID
v_id = 'uuid'


def asset_region_test(client):
    """
        对 AssetRegion 进行测试
    """

    assert client.get_asset_region(id=ar_id)['id'] == ar_id  # 获取指定的AssetRegion

    # ======== 测试更新、创建、删除一个 AssetRegion ========

    data = {
        'name': 'test for delete', 'domain': 'kog.com',
        'username': 'xxx', 'password': '123',
        'proxy_minon': 'BJ6', 'verbose': '123456',
    }
    ar = client.create_asset_region(**data)  # 创建一个 AssetRegion
    n_ar = client.edit_asset_region(id=ar['id'], name='test edit')  # 更新一个 AssetRegion
    assert n_ar['name'] == 'test edit'
    client.delete_asset_region(id=ar['id'])  # 删除 AssetRegion

    # ======== 测试批量删除 AssetRegion ========
    data = {
        'name': 'test for batch delete', 'domain': 'kog.com',
        'username': 'wangchenguang', 'password': '123',
        'proxy_minon': 'BJ6', 'verbose': '123456',
    }
    ar = client.create_asset_region(**data)
    ret = client.batch_delete_asset_region(id=[ar['id']])  # 批量删除AssetRegion
    assert ret['count'] == 1


def asset_server_test(client):
    """
        对 AssetServer 进行测试
    """

    # ======== 测试更新、创建、删除 AssetServer ========

    data = {
        'name': 'test for delete', 'region_name': 'Region in bupt',
        'region': ar_id, 'private_ip': '127.0.0.1',
        'public_ip': '127.0.0.2', 'cpu': 8, 'os': 'ox',
        'mem_size': 100, 'disk_type': 'SSD', 'disk_size': 8,
    }
    aserver = client.create_asset_server(**data)  # 创建一个 AssetServer
    n_aserver = client.edit_asset_server(id=aserver['id'], name='test edit')  # 更新/编辑 AssetServer
    assert n_aserver['name'] == 'test edit'
    client.delete_asset_server(id=aserver['id'])  # 删除 AssetServer

    # ======== 测试批量删除 AssetServer ========

    data = {
        'name': 'test for batch delete', 'region_name': 'Region in bupt',
        'region': ar_id, 'private_ip': '127.0.0.1',
        'public_ip': '127.0.0.2', 'cpu': 8,
        'os': 'ox', 'mem_size': 100,
        'disk_type': 'SSD', 'disk_size': 8,
    }
    aserver = client.create_asset_server(**data)  # 创建一个 AssetServer
    ret = client.batch_delete_asset_server(id=[aserver['id']])
    assert ret['count'] == 1


def project_test(client):
    """
        对Project进行测试
    """
    projects = client.get_project_list()  # 获取项目列表
    for project in projects:
        print '项目名称: \'%s\'' % project['name']

    print '当前项目的数量为:', client.get_project_count()['count']  # 获取项目数量

    assert client.get_project(id=p_id)['id'] == p_id  # 获取指定的项目

    pro_servers = client.get_project_servers(id=p_id)  # 获取某个项目下的服务器
    for pro_server in pro_servers:
        print '\'%s\'' % client.get_project(id=p_id)['name'] + '项目下的服务器为:', '\'%s\'' \
                        % pro_server['name'], 'id: %s' % pro_server['id']

    p_groups = client.get_project_groups(id=p_id)  # 获取某个项目下的分组
    for p_group in p_groups:
        print '项目下分组的名称: %s' % p_group['name'], \
            '项目下分组的id: %s' % p_group['id']

    p_roles = client.get_project_roles(id=p_id)  # 获取某个项目下的角色
    for p_role in p_roles:
        print '项目下角色的名称: \'%s\'' % p_role['name'], \
            '项目下角色的id: %s' % p_role['id']

    p_applications = client.get_project_applications(id=p_id)  # 获取某个项目下的程序
    for p_application in p_applications:
        print '项目下的程序名称: %s' % p_application['name'], \
            '项目下的程序id: %s' % p_application['id']

    p_methods = client.get_project_methods(id=p_id)  # 获取某个项目下的操作方法
    for p_method in p_methods:
        print client.get_project(id=p_id)['name'] + '项目下的操作方法:\'%s\'' \
                                                  % p_method['name']

    g_servers = client.get_project_all_related_info(id=p_id)  # 获取该项目下分组服务器角色的相关信息
    for g_server in g_servers:
        print '\'%s\'' % client.get_project(id=p_id)['name']+'项目下分组服务器:\'%s\'' \
                                                  % g_server['groups']['name']

    p_templates = client.get_project_settings_template(id=p_id)  # 获取某个项目下的配置模板
    for p_template in p_templates:
        print '\'%s\'' % p_template['name'] + \
              '项目下的配置模板名: %s' % p_template['name'], '配置模板id: %s' % p_template['id']

    # ======== 测试更新、创建、删除一个项目 ========

    project = client.create_project(name='facebook')  # 创建一个项目
    n_project = client.edit_project(id=project['id'], comment='edit')  # 编辑/更新一个项目
    assert n_project['comment'] == 'edit'
    client.delete_project(id=project['id'])  # 删除一个项目
    assert client.get_project_list() == projects

    # ======== 测试删除项目下的服务器 ========

    p_server = client.create_project_servers(id=p_id, sid=[s_id])  # 添加项目下服务器
    assert p_server != []
    ret = client.delete_project_servers(id=p_id, sid=[s_id])  # 删除项目下的服务器
    assert ret['count'] == 1
    assert client.get_project_servers(id=p_id) == pro_servers

    # ========  检查某个项目下角色/分组/命令/模板/应用程序的名称不可重复 ========

    data = {
        "id": p_id,
        "scope": "application",
        "key": "name",
        "value": "project_variable",
    }
    client.check_project_sub_element_duplicate(**data)  # 检查某个项目下角色/分组/命令/模板/应用程序的名称不可重复

    # ======== 检查项目名不可重复 ========

    data = {
        "key": "name",
        "value": "project_test1"
    }
    client.check_project_element_duplicate(**data)  # 检查项目名不可重复


def role_test(client):
    """
        Role角色测试
    """

    r_tempates = client.get_role_settings_template(id=r_id)  # 获取角色中的配置模板
    for r_tempate in r_tempates:
        print '该角色下的配置模板', r_tempate['name']
        assert r_tempate['role'] == r_id

    r_apps = client.get_role_applications(id=r_id)  # 获取角色与程序关系
    for r_app in r_apps:
        print '该角色下的程序:', r_app['name']
        assert r_app['role'] == r_id

    r_methods = client.get_role_methods(id=r_id)  # 获取角色中的命令
    for r_method in r_methods:
        print '该角色下的命令:', r_method['name']
        assert r_method['role'] == r_id

    # ======== 修改/更新关联当前角色的服务器 ========

    ret = client.update_role_servers(id=r_id, servers=[s_id])
    assert ret != []

    # ====== 测试删除角色 ======
    data = {
        'name': 'a test role', 'project': p_id,
        'is_global': True,
    }
    role = client.create_role(**data)  # 创建一个角色
    n_role = client.edit_role(id=role['id'], name='edit test', comment='...')  # 更新角色
    assert n_role['name'] == 'edit test'
    client.delete_role(id=role['id'])  # 删除角色

    # ======== 测试批量删除角色 ======

    data = {
        'name': 'a test role', 'project': p_id,
        'is_global': True,
    }
    role = client.create_role(**data)
    ret = client.batch_delete_role(id=[role['id']])
    assert ret['count'] == 1


def method_test(client):

    # ======== 测试删除Method ========
    data = {
        'project': p_id, 'name': 'test',
        'comment': '批量删除测试', 'command': 'ls',
        'role': r_id,
    }
    method = client.create_method(**data)  # 创建一个命令

    data = {
        'id': method['id'], 'name': 'edit',
        'comment': '更新方法', 'command': 'ls',
        'role': r_id,
    }
    n_method = client.edit_method(**data)  # 更新一个命令
    assert n_method['name'] == 'edit'
    client.delete_method(id=n_method['id'])  # 删除一个命令

    # ======== 测试批量删除命令 ========

    data = {
        'project': p_id, 'name': 'test',
        'comment': '批量删除测试', 'command': 'ls',
        'role': r_id,
    }
    method = client.create_method(**data)  # 创建一个命令
    ret = client.batch_delete_method(id=[method['id']])
    assert ret['count'] == 1

    med_exec = client.method_execute(id=m_id, role=r_id, group=[g_id])  # 执行命令
    print '执行命令返回:', med_exec

    med_review = client.method_review(id=m_id, role=r_id, group=[g_id])  # 操作命令前预览
    print '操作命令前预览返回:', med_review


def group_test(client):

    """
        对Group进行测试, 创建分组先得添加一台已经认证的服务器
    """

    # ======== 测试获取不在分组中的服务器 ========

    no_servers = client.get_group_out_servers(id=g_id[0])
    for no_server in no_servers:
        print '不在分组中的服务器为:', '\'%s\'' % no_server['name'], \
            'id: {}'.format(no_server['id'])

    gp_servers = client.get_group_servers(id=g_id[0])
    for gp_server in gp_servers:
        print '\'%s\'中的服务器为:' % 'wcg group', '\'%s\'' % gp_server['name'], \
            'id: {}'.format(gp_server['id'])

    # ======== 测试删除项目下的分组 ========

    group = client.create_group(name='test delete', project=p_id, servers=[s_id])  # 创建项目下的分组
    n_group = client.edit_group(id=group['id'], name='wcg group edit', comment='have changed group2')  # 更新分组
    assert n_group['name'] == 'wcg group edit'
    client.delete_group(id=group['id'])  # 删除分组

    # ======== 测试批量删除项目下的分组 ========

    group = client.create_group(name='test batch delete', project=p_id, servers=[s_id])
    client.batch_delete_group(id=[group['id']])  # 批量删除分组

    # ======== 测试删除分组下面服务器 ========

    gp_servers = client.get_group_servers(id=g_id)  # 获取分组下面的服务器
    for gp_server in gp_servers:
        print '某个分组下面服务器为: \'%s\'' % gp_server['name'],\
            'id: %s' % gp_server['id']

    ret = client.create_group_servers(id=g_id, servers=[s_id])  # 添加服务器到当前分组
    assert ret['count'] == 1
    ret = client.delete_group_server(id=g_id, servers=[s_id])  # 删除分组下面服务器
    assert ret['count'] == 1
    assert client.get_group_servers(id=g_id) == gp_servers


def server_test(client):
    """
        对云主机进行测试, 需要已经认证的云主机
    """

    print client.get_server_count()  # 返回服务器数量

    servers = client.get_server_list()  # 获取服务器列表
    for server in servers:
        print '服务器列表中的服务器:', '\'%s\'' % server['name'], \
            'id: {}'.format(server['id'])

    print client.get_server_day_count(flag='private')  # 统计15天主机总数量

    assert 'wcg AssetServer for test' == \
           client.get_server(id='da711a14-b3be-4a04-a76c-cdae485f3625')['name']  # 获取某台主机的详细信息

    use_server = client.get_server_usage_list()[0]
    print '已经使用的服务器: \'%s\'' % use_server['name'], 'id: %s' % use_server['id']

    # ======== 测试开启、关闭、重启云主机、查询云主机状态 ======

    # 这几个方法参数为 region_server=[{region: server_id}]
    print client.start_server(
        region_server=[{'cn-beijing-6': 'da711a14-b3be-4a04-a76c-cdae485f3625'}]
    )  # 开启主机
    print client.stop_server(
        region_server=[{'cn-beijing-6': 'da711a14-b3be-4a04-a76c-cdae485f3625'}]
    )  # 关闭主机
    print client.reboot_server(
        region_server=[{'cn-beijing-6': 'da711a14-b3be-4a04-a76c-cdae485f3625'}]
    )  # 重启主机
    print client.get_server_status(
        region_server=[{'Region in bupt': '5b870cca-084e-4d2b-b9ea-0fa18b19377b'}]
    )

    print '\'%s\'' % client.get_server(id=s_id[3])['name'] + \
          '认证服务器agent返回: %s' % client.authentication_server_agent(id=[s_id])  # 认证服务器

    data = {
        'key': 'name',  # 待检查的字段
        'value': 'for test server'  # 检查字段的值
    }
    assert client.check_server_element_duplicate(**data)['data'] is True  # 检查主机名不可重复

    print '更新服务器名称:', client.edit_server(id=s_id, name='rename server')['name']  # 编辑/更新服务器


def version_test(client):

    versions = client.get_version_list()  # 获取程序包版本列表
    for version in versions:
        print '程序包版本名: %s' % version['name'], \
            '程序包版本id: %s' % version['id']

    version = client.get_version(id=v_id)
    assert version['id'] == v_id

    assert client.edit_version(
        id=v_id,
        comment='hahaha',
    )['comment'] == 'hahaha'  # 编译/更新应用版本

    client.delete_version(
        id=v_id
    )  # 测试删除程序版本通过

    client.batch_delete_version(
        id=[v_id]
    )  # 测试批量删除程序版本通过


def object_variables_test(client):
    """
        测试项目下的相关变量
    """

    variables = client.get_project_variable(pid=p_id)
    for variable in variables:
        print '当前项目下的变量名为: \'%s\'' % variable['name']

    client.get_diff_type_variable(
        pid=p_id, type='project',
        name='project_variable', varList=[p_id]
    )

    # ======== 测试根据变量的类型/名称删除相应的变量 ========

    variable = client.create_variable(
        pid=p_id, type='project', name='test for test',
        varList=[{'id': p_id, 'value': '1'}], comment='the first',
    )
    n_variable = client.edit_variable(
        type='project', name='test edit',
        varList=[{'tid': p_id, 'id': variable[0]['id'], 'value': '1'}]
    )
    assert n_variable[0]['name'] == 'test edit'
    ret = client.delete_variable(pid=p_id, type='project', name='test edit')
    assert ret['count'] == 1

    # ======== 测试根据变量的类型/批量删除变量 ========

    variable = client.create_variable(
        pid=p_id, type='project', name='test for batch delete',
        varList=[{'id': p_id, 'value': '1'}], comment='the first',
    )

    ret = client.batch_delete_variable(
        pid=p_id,
        varList=[{'type': 'project', 'name': variable[0]['name']}]
    )

    print '根据变量的类型/名称批量删除变量返回结果:', ret

    # ======== 检查某个项目下不同作用域的变量名称不可重复 ========

    ret = client.check_variable_sub_element_duplicate(
        pid=p_id, scope='project',
        key='name', value='project_variable'
    )
    assert ret['data'] is True


def application_test(client):

    for x in client.get_application_app_role(id=app_id):
        print '拆分规则名%s' % x['name'], \
            '拆分规则id: %s' % x['id'], '拆分规则对应的Role ID: %s' % x['role']

    # ====== 下发程序包/根据拆分规则下发程序包 ======

    print '下发程序包的包名: %s' % client.application_distribute(
        id=app_id, role=r_id,
        group=[g_id],
        version=v_id, split=True,
    )['name']

    # ====== 测试删除程序包拆分规则 ======

    app_role = client.create_application_app_role(
        id=app_id, name='create a app role',
        role=r_id, regex='haha', path='/tmp',
    )  # 创建程序包拆分规则

    app_role_id = app_role['id']
    n_app_role = client.edit_application_role(
        id=app_role_id, name='edit app role'
    )  # 编辑/更新应用拆分规则
    assert n_app_role['name'] == 'edit app role'

    ret = client.delete_application_app_role(
        id=app_id, app_role_id=[app_role_id]
    )  # 删除程序包拆分规则
    assert ret['count'] == 1

    print '操作前预览: %s' % client.application_review(
        id=app_id,
        role=r_id,
        group=[g_id],
    )  # 操作应用程序前预览

    print client.delete_application_versions(
        id=app_id,
        vid=[v_id]
    )  # 删除程序包版本测试通过

    app_versions = client.get_application_versions(id=app_id)  # 获取程序包版本测试通过
    for app_version in app_versions:
        print app_version['name']

    print client.batch_delete_application(
        id=[app_id]
    )  # 删除应用测试通过
    print client.delete_application(
        id=app_id
    )  # 批量删除应用测试通过
    print client.edit_application(
        id=app_id, name='wcg'
    )  # 测试编辑/更新应用测试通过


def deploy_settings_template_test(client):

    print client.deploy_settings_template_distribute(
        id=temp_id,
        role=r_id,
        group=[g_id],
    )  # 下发配置文件

    print client.deploy_settings_template_review(
        id=temp_id,
        role=r_id,
        group=[g_id],
    )  # 操作配置文件前预览

    client.delete_deploy_settings_template(
        id=temp_id
    )  # 删除配置文件测试通过

    print client.edit_deploy_settings_template(
        id=temp_id,
        rename='test eidt',
    )['rename']  # 更新配置文件测试通过

    client.batch_deploy_settings_template(
        id=[temp_id]
    )  # 批量删除配置文件测试通过


def package_test(client):

    packages = client.get_package_list()  # 获取Package列表
    for package in packages:
        print '程序包列表元素: %s' % package['name']

    print '已上传程序包容量及其占比: %s' % client.package_count()  # 已上传的程序包容量及其占比

    for package in client.package_day_count(day=1):
        print '15天程序包的总量: %s' % package  # 统计15天的程序包总量


def message_center_test(client):

    messages = client.get_message_center_list()  # 获取消息中心列表
    for message in messages:
        print '消息列表的元素id:', message['id']
        client.edit_message_center(id=message['id'], flag=False)

    print '把所有消息设置为已读:', client.batch_set_message_flag(set_all=True)

    print client.listen_message_center()  # 监听消息中心
