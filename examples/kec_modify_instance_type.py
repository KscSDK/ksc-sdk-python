
import time
from kscore.session import get_session

##################需修改部分Begin####################
region = 'cn-beijing-6'  # region code
ks_access_key_id = "ak"
ks_secret_access_key = "sk"
instanceId = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' # 主机的Id
##################需修改部分End######################

session = get_session()
session.set_credentials(ks_access_key_id, ks_secret_access_key)
kec_cli = session.create_client("kec", region, use_ssl=True)

# 更配成功的状态
success_need_reboot = [
    'migrating_success',
]
success_need_start = [
    'migrating_success_off_line',
    'resize_success_local',
    'cross_finish',
]

# 更配失败的状态
error_status = [
    'pre_migrating_error',
    'migrating_error',
    'drg_migrating_error',
    'migrating_error_off_line',
    'resize_error_local',
    'power_on_error',
    'cross_error'
]

############### 调用变更配置的接口 ###############
# 升配
modify_resp = kec_cli.modify_instance_type(**{
    'InstanceId': instanceId,
    'InstanceType': 'N3.2B',
})

# # 降配（实例应为关机状态）
# modify_resp = kec_cli.modify_instance_type(**{
#     'InstanceId': instanceId,
#     'InstanceType': 'N3.1B',
# })

# # 变更实例类型（实例应为关机状态）
# # 支持变更实例类型的机型列表：https://docs.ksyun.com/documents/6666
# modify_resp = kec_cli.modify_instance_type(**{
#     'InstanceId': instanceId,
#     'InstanceType': 'S6.1B',
#     'CrossInstanceMigrate': True
# })

############### 更配是异步操作，接口成功后，可以轮询查询实例，待实例状态为变更成功后，执行启动或重启，配置会生效 ###############
if modify_resp['Return']:
    # 接口成功，开始轮询实例状态
    while True:
        describe_resp = kec_cli.describe_instances(**{
            'InstanceId.1': instanceId,
        })
        current_state = describe_resp['InstancesSet'][0]['InstanceState']['Name']

        if current_state in success_need_reboot:
            ## 更配成功，需要重启，新配置才会生效（如果需要自动重启，可以将下面这段代码的注释去掉）
            # kec_cli.reboot_instances(**{
            #     'InstanceId.1': instanceId,
            # })
            print('success:', current_state)
            break
        elif current_state in success_need_start:
            # 更配成功，启动实例后新配置即生效（如果需要自动启动，可以将下面这段代码的注释去掉）
            # kec_cli.start_instances(**{
            #     'InstanceId.1': instanceId,
            # })
            print('success:', current_state)
            break
        elif current_state in error_status:
            # 更配失败
            print('error:', current_state)
            break

        print('waiting...')
        time.sleep(5)


