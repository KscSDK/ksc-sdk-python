# -*- encoding:utf-8 -*-
from kscore.exceptions import ClientError
from kscore.session import get_session
from pprint import pprint

if __name__ == "__main__":
    s = get_session()
    client = s.create_client("kec", "cn-beijing-6", use_ssl=False)

    # https://docs.ksyun.com/documents/816?type=3
    client.describe_instances()

    # https://docs.ksyun.com/documents/806?type=3
    client.run_instances(
        MaxCount=50, MinCount=20, ImageId="3f3bddcf-4982-4ab4-a63d-795e8d74e9d5",
        SubnetId="f1bd236b-7fd3-44d3-aef9-2d673a65466e", InstancePassword="Ksyun2017",
        SecurityGroupId="2f43a9e4-1a3c-448e-b661-efa6d04b82fc", DataDiskGb=50, ChargeType="Monthly",
        InstanceType="C1.1A", PurchaseTime=1, InstanceName="test", InstanceNameSuffix="1")

    # https://docs.ksyun.com/documents/809?type=3
    instances = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]

    instances = dict(("InstanceId.{}".format(index), instance) for index, instance in enumerate(instances, 1))

    client.terminate_instances(**instances)

    # 用户查询竞价实例历史价格列表
    # pprint("-------------------------------用户查询竞价实例历史价格列表---------------------------------")
    # _spot_price = client.describe_spot_price_history(InstanceType="E1.1A", AvailabilityZone="cn-shanghai-3a")
    # pprint(_spot_price)

    # 查看主机价格
    # pprint("-------------------------------查看主机价格---------------------------------")
    # _instance_price = client.describe_price(InstanceType="N3.1A", ImageId="IMG-5a7cb0e5-d297-4259-9944-38b3c053a7dc", ChargeType="Daily", SriovNetSupport=True)
    # pprint(_instance_price)

    # 创建实例启动模板
    # pprint("-------------------------------创建实例启动模板---------------------------------")
    # _instance_model = client.create_model(ImageId="IMG-5a7cb0e5-d297-4259-9944-38b3c053a7dc",
    #                                       SubnetId="afa859fc-65ea-410d-99f2-d686cf9da1d9",
    #                                       ChargeType="Daily", ModelName="wyn_test_model",
    #                                       SecurityGroupId="18523073-c6c0-44ba-9858-1c0f92cb453d", PurchaseTime=0,
    #                                       InstanceType="N3.1A")
    # pprint(_instance_model)

    # 删除实例启动模板
    # pprint("-------------------------------删除实例启动模板---------------------------------")
    # models = ["0565ffc5-55e3-44e9-b242-5ed3de725ee0"]
    # models = dict(("ModelId.{}".format(index), model) for index, model in enumerate(models, 1))
    # _del_model = client.terminate_models(**models)
    # pprint(_del_model)

    # 查看实例启动模板
    # pprint("-------------------------------查看实例启动模板---------------------------------")
    # _des_models = client.describe_models()
    # pprint(_des_models)

    # 云主机迁入容灾组
    # pprint("-------------------------------云主机迁入容灾组-------------------------------")
    # instances = ["5e78a001-e472-44f5-9aa4-c822a8121319"]
    # instances = dict(("InstanceId.{}".format(index), instance) for index, instance in enumerate(instances, 1))
    # add_vm_into_data_guard = client.add_vm_into_data_guard(DataGuardId="ec148c88-5958-49dc-97a2-76fc21c4552a", **instances)
    # pprint(add_vm_into_data_guard)

    # 修改容灾分组名称
    # pprint("-------------------------------修改容灾分组名称--------------------------------")
    # mod_data_guard_group_name = client.modify_data_guard_groups(DataGuardId="ec148c88-5958-49dc-97a2-76fc21c4552a", DataGuardName="wyn_test")
    # pprint(mod_data_guard_group_name)

    # 查询用户某区域的容灾分组容量
    # pprint("-------------------------------查询用户某区域的容灾分组容量--------------------------------")
    # des_data_guard_capacity = client.describe_data_guard_capacity()
    # pprint(des_data_guard_capacity)

    # 创建容灾分组
    # pprint("-------------------------------创建容灾分组---------------------------------")
    # cre_data_guard_group = client.create_data_guard_group(DataGuardName="my_dataguard_test")
    # pprint(cre_data_guard_group)

    # 删除容灾分组
    # pprint("-------------------------------删除容灾分组---------------------------------")
    # data_guards = ["ec148c88-5958-49dc-97a2-76fc21c4552a"]
    # data_guards = dict(("DataGuardId.{}".format(index), data_guard) for index, data_guard in enumerate(data_guards, 1))
    # del_data_guard_groups = client.delete_data_guard_groups(**data_guards)
    # pprint(del_data_guard_groups)

    # 查询容灾组信息
    # pprint("-------------------------------查询容灾组信息---------------------------------")
    # des_data_guard_group = client.describe_data_guard_group()
    # pprint(des_data_guard_group)

    # 云主机从容灾组中移除
    # pprint("-------------------------------云主机从容灾组中移除---------------------------------")
    # instances = ["5e78a001-e472-44f5-9aa4-c822a8121319"]
    # instances = dict(("InstanceId.{}".format(index), instance) for index, instance in enumerate(instances, 1))
    # remove_vm_from_data_guard = client.remove_vm_from_data_guard(DataGuardId="ec148c88-5958-49dc-97a2-76fc21c4552a", **instances)
    # pprint(remove_vm_from_data_guard)

    # #镜像导入
    # client.import_image(ImageName="", Architecture="", Platform="", ImageUrl="", ImageFormat="")

    # 镜像复制
    # pprint("-------------------------------镜像复制---------------------------------")
    # param = {
    #     "ImageId.1": "432eb1f8-72f3-4320-a0f7-572b33b32431",
    #     "DestinationRegion.1": "cn-shanghai-3"
    # }
    # copy_image = client.copy_image(**param)
    # pprint(copy_image)

    # 查看镜像分享信息
    # pprint("-------------------------------查看镜像分享信息---------------------------------")
    # describe_image_share_permission = client.describe_image_share_permission(ImageId="e5b7d077-021c-4fb2-9d0e-fa4700f99b58")
    # pprint(describe_image_share_permission)

    # 修改镜像分享信息
    # pprint("-------------------------------修改镜像分享信息---------------------------------")
    # accounts = ["73403544"]
    # accounts = dict(("AccountId.{}".format(index), account) for index, account in enumerate(accounts, 1))
    # modify_image_share_permission = client.modify_image_share_permission(ImageId="e5b7d077-021c-4fb2-9d0e-fa4700f99b58", Permission="share", **accounts)
    # pprint(modify_image_share_permission)

    # 镜像预热
    # pprint("-------------------------------镜像预热---------------------------------")
    # enable_image_caching = client.enable_image_caching(ImageId="432eb1f8-72f3-4320-a0f7-572b33b32431")
    # pprint(enable_image_caching)

    # 取消镜像预热
    # pprint("-------------------------------取消镜像预热---------------------------------")
    # disable_image_caching = client.disable_image_caching(ImageId="432eb1f8-72f3-4320-a0f7-572b33b32431")
    # pprint(disable_image_caching)

    # 创建本地盘快照
    # pprint("-------------------------------创建本地盘快照---------------------------------")
    # create_local_volume_snapshot = client.create_local_volume_snapshot(LocalVolumeId="58ce95e4-0e8f-44e1-8134-dca14697c103-a", LocalVolumeSnapshotName="wyn_test")
    # pprint(create_local_volume_snapshot)

    # 回滚快照
    # pprint("-------------------------------回滚快照---------------------------------")
    # rollback_local_volume = client.rollback_local_volume(LocalVolumeSnapshotId="6c08b3ff-34c2-4948-b81d-4c8cc9b7a084")
    # pprint(rollback_local_volume)

    # 删除快照
    # pprint("-------------------------------删除快照---------------------------------")
    # local_volume_snapshots = ["6c08b3ff-34c2-4948-b81d-4c8cc9b7a084"]
    # local_volume_snapshots = dict(("LocalVolumeSnapshotId.{}".format(index), local_volume_snapshot) for index, local_volume_snapshot in enumerate(local_volume_snapshots, 1))
    # delete_local_volume_snapshot = client.delete_local_volume_snapshot(**local_volume_snapshots)
    # pprint(delete_local_volume_snapshot)

    # 主机绑定密钥
    # pprint("-------------------------------主机绑定密钥---------------------------------")
    # param = {
    #     "InstanceId.1": "5e78a001-e472-44f5-9aa4-c822a8121319",
    #     "KeyId.1": "c079a41f-beb4-4b73-a68c-69f25b9c8819"
    # }
    # attach_key = client.attach_key(**param)
    # pprint(attach_key)

    # 主机解绑密钥
    # pprint("-------------------------------主机解绑密钥---------------------------------")
    # param = {
    #     "InstanceId.1": "5e78a001-e472-44f5-9aa4-c822a8121319",
    #     "KeyId.1": "c079a41f-beb4-4b73-a68c-69f25b9c8819"
    # }
    # detach_key = client.detach_key(**param)
    # pprint(detach_key)

    # 获取弹性伸缩配置
    # pprint("-------------------------------获取弹性伸缩配置---------------------------------")
    # list = client.describe_scaling_configuration()
    # print(list)

    # 创建弹性伸缩配置
    # pprint("-------------------------------创建弹性伸缩配置---------------------------------")
    # # API参数参见: https://docs.ksyun.com/documents/28246
    # res = client.create_scaling_configuration(**{
    #     "ScalingConfigurationName": "test-scaling-configuration",
    #     "ImageId": "IMG-5465174a-6d71-4770-b8e1-917a0dd92466",
    #     "InstanceType": "N3.4B",
    #     "ChargeType": "HourlyInstantSettlement",
    #     "ProjectId": 0,
    #     "KeyId.1": "71c17c37-c9cb-4faf-a86e-d76d35f3c4d9",
    #     "DataDisk.1.Type": "SSD3.0",
    #     "DataDisk.1.Size": 50,
    #     "DataDisk.1.deleteWithInstance": True,
    #     "SystemDisk.DiskType": "SSD3.0",
    #     "SystemDisk.DiskSize": 40,
    # })
    # print(res)

    # 编辑弹性伸缩配置
    # pprint("-------------------------------编辑弹性伸缩配置---------------------------------")
    # # API参数参见: https://docs.ksyun.com/documents/28247
    # res = client.modify_scaling_configuration(**{
    #     "ScalingConfigurationId": res["ScalingConfigurationId"],
    #     "ScalingConfigurationName": "test-scaling-configuration123",
    # })
    # print(res)

    # 删除弹性伸缩配置
    # pprint("-------------------------------删除弹性伸缩配置---------------------------------")
    # res = client.delete_scaling_configuration(**{
    #     "ScalingConfigurationId.1": res["ScalingConfigurationId"]
    # })
    # print(res)
