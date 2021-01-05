# -*- encoding:utf-8 -*-

from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    client = s.create_client("kec", "cn-beijing-6", use_ssl=False)

    # https://docs.ksyun.com/read/latest/52/_book/oaDescribeInstances.html
    client.describe_instances()

    # https://docs.ksyun.com/read/latest/52/_book/oaRunInstances.html
    client.run_instances(
        MaxCount=50, MinCount=20, ImageId="3f3bddcf-4982-4ab4-a63d-795e8d74e9d5",
        SubnetId="f1bd236b-7fd3-44d3-aef9-2d673a65466e", InstancePassword="Ksyun2017",
        SecurityGroupId="2f43a9e4-1a3c-448e-b661-efa6d04b82fc", DataDiskGb=50, ChargeType="Monthly",
        InstanceType="C1.1A", PurchaseTime=1, InstanceName="test", InstanceNameSuffix="1")
    
    # https://docs.ksyun.com/read/latest/52/_book/oaTerminateInstances.html
    instances = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]

    instances = dict(("InstanceId.{}".format(index), instance) for index, instance in enumerate(instances, 1))

    client.terminate_instances(**instances)

    #用户查询竞价实例历史价格列表
    client.describe_spot_price_history(InstanceType="E1.1A", AvailabilityZone="cn-shanghai-3a")

    #查看主机价格
    client.describe_price(InstanceType="I1.8B", ImageId="e00e5b9a-0914-4611-8730-3768bf08e035", ChargeType="Daily", SriovNetSupport=True)

    #创建实例启动模板
    client.create_model(ImageId="", SubnetId="", ChargeType="Daily", ModelName="", SecurityGroupId="", PurchaseTime=0)

    #删除实例启动模板
    models = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    models = dict(("ModelId.{}".format(index), model) for index, model in enumerate(models, 1))
    client.terminate_models(**models)

    #查看实例启动模板
    client.describe_models()

    #云主机迁入容灾组
    instances = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    instances = dict(("InstanceId.{}".format(index), instance) for index, instance in enumerate(instances, 1))
    client.add_vm_into_data_guard(DataGuardId="", **instances)

    #修改容灾分组名称
    client.modify_data_guard_groups(DataGuardId="", DataGuardName="")

    #查询用户某区域的容灾分组容量
    client.describe_data_guard_capacity()

    #创建容灾分组
    client.create_data_guard_group(DataGuardName="my_dataguard_test")

    #删除容灾分组
    data_guards = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    data_guards = dict(("DataGuardId.{}".format(index), data_guard) for index, data_guard in enumerate(data_guards, 1))
    client.delete_data_guard_groups(**data_guards)

    #查询容灾组信息
    client.describe_data_guard_group()

    #云主机从容灾组中移除
    instances = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    instances = dict(("InstanceId.{}".format(index), instance) for index, instance in enumerate(instances, 1))
    client.remove_vm_from_data_guard(DataGuardId="", **instances)

    #镜像导入
    client.import_image(ImageName="", Architecture="", Platform="", ImageUrl="", ImageFormat="")

    #镜像复制
    images = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    images = dict(("ImageId.{}".format(index), image) for index, image in enumerate(images, 1))
    destination_regions = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    destination_regions = dict(("DestinationRegion.{}".format(index), destination_region) for index, destination_region in enumerate(destination_regions, 1))
    client.copy_image(**images, **destination_regions)

    #查看镜像分享信息
    client.describe_image_share_permission(ImageId="", RequestId="", SharePermissionSet="")

    #修改镜像分享信息
    accounts = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    accounts = dict(("AccountId.{}".format(index), account) for index, account in enumerate(accounts, 1))
    client.modify_image_share_permission(ImageId="", Permission="", **accounts)

    #查询云市场镜像信息
    client.query_image_list(Region="")

    #镜像预热
    client.enable_image_caching(ImageId="")

    #取消镜像预热
    client.disable_image_caching(ImageId="")

    #创建本地盘快照
    client.create_local_volume_snapshot(LocalVolumeId="", LocalVolumeSnapshotName="")

    #回滚快照
    client.rollback_local_volume(LocalVolumeId="", LocalVolumeSnapshotId="")

    #删除快照
    local_volume_snapshots = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    local_volume_snapshots = dict(("LocalVolumeSnapshotId.{}".format(index), local_volume_snapshot) for index, local_volume_snapshot in enumerate(local_volume_snapshots, 1))
    client.delete_local_volume_snapshot(**local_volume_snapshots)

    #创建弹性网卡
    security_groups = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    security_groups = dict(("SecurityGroupId.{}".format(index), security_group) for index, security_group in enumerate(security_groups, 1))
    client.create_network_interface(SubnetId="", **security_groups)

    #删除弹性网卡
    client.delete_network_interface(NetworkInterfaceId="")

    #描述网卡信息
    client.describe_network_interfaces()

    #创建密钥
    client.create_key()

    #导入密钥
    client.import_key(KeyName="", PublicKey="")

    #删除密钥
    client.delete_key(KeyId="")

    #主机绑定密钥
    instances = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    instances = dict(("InstanceId.{}".format(index), instance) for index, instance in enumerate(instances, 1))
    keys = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    keys = dict(("KeyId.{}".format(index), key) for index, key in enumerate(keys, 1))
    client.attach_key(**instances, **keys)

    #主机解绑密钥
    instances = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    instances = dict(("InstanceId.{}".format(index), instance) for index, instance in enumerate(instances, 1))
    keys = ["2f43a9e4-1a3c-448e-b661-efa6d04b82fc", "2f43a9e4-1a3c-448e-b661-efa6d04b82fc"]
    keys = dict(("KeyId.{}".format(index), key) for index, key in enumerate(keys, 1))
    client.detach_key(**instances, **keys)