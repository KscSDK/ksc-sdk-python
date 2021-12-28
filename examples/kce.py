# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()

    # 创建集群

    client = s.create_client("kce", "cn-beijing-6", use_ssl=True)
    client2 = s.create_client("kcev2", "cn-beijing-6", use_ssl=True)
    '''
    #创建集群（老版2019-08-06不推荐）
    param = {
        "ClusterName": "xxxxx",
        "ClusterManageMode": "DedicatedCluster",
        "VpcId": "15552848-026b-4ad6-a3e3-xxxxx",
        "PodCidr": "10.32.0.0/14",
        "ServiceCidr": "10.254.0.0/16",
        "NetworkType": "Flannel",
        "K8sVersion": "v1.13.4",
        "ReserveSubnetId": "9729f4c0-93ee-4e2a-9b2a-xxxxx",
        "PublicApiServer": "{\"LineId\":\"5fc2595f-1bfd-481b-bf64-2d08f116d800\",\"BandWidth\": \"10\",\"ChargeType\": \"PostPaidByDay\"}",
        "InstanceSet.0.NodeRole": "Master_Etcd",
        "InstanceSet.0.NodePara.0": "{\"MaxCount\":3,\"MinCount\":3,\"ImageId\":\"a0699172-76c6-4885-a4e9-0799a9cb811d\",\"SubnetId\":\"4a077fa8-a239-47bf-a18f-xxxxx\",\"InstancePassword\":\"Root23123\",\"SecurityGroupId\":\"0dcd8356-9e7e-43ae-897b-xxxxx\",\"DataDiskGb\":0,\"ChargeType\":\"Daily\",\"InstanceType\":\"I3.2A\",\"PurchaseTime\":0,\"InstanceName\":\"kce-py\",\"InstanceNameSuffix\":1}",
        "InstanceSet.1.NodeRole": "Worker",
        "InstanceSet.1.NodePara.0": "{\"MaxCount\":1,\"MinCount\":1,\"ImageId\":\"a0699172-76c6-4885-a4e9-0799a9cb811d\",\"SubnetId\":\"4a077fa8-a239-47bf-a18f-xxxxx\",\"InstancePassword\":\"Root23123\",\"SecurityGroupId\":\"0dcd8356-9e7e-43ae-897b-xxxxx\",\"DataDiskGb\":0,\"ChargeType\":\"Daily\",\"InstanceType\":\"I3.2A\",\"PurchaseTime\":0,\"InstanceName\":\"kce-py\",\"InstanceNameSuffix\":1}",
    }

    m = client.create_cluster(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''

    #创建集群（新版2020-12-31推荐）
    param = {
        "ClusterName": "xxxxx",
        "ClusterManageMode": "DedicatedCluster",
        "VpcId": "15552848-026b-4ad6-a3e3-xxxxx",
        "PodCidr": "10.32.0.0/14",
        "ServiceCidr": "10.254.0.0/16",
        "NetworkType": "Flannel",
        "K8sVersion": "v1.19.3",
        "ReserveSubnetId": "9729f4c0-93ee-4e2a-9b2a-xxxxx",
        "PublicApiServer": "{\"LineId\":\"5fc2595f-1bfd-481b-bf64-2d08f116d800\",\"BandWidth\": \"10\",\"ChargeType\": \"PostPaidByDay\"}",
        "InstanceForNode.1.NodeRole": "Master_Etcd",
        "InstanceForNode.1.NodeConfig.1.Para": "{\"MaxCount\":3,\"MinCount\":3,\"ImageId\":\"a0699172-76c6-4885-a4e9-0799a9cb811d\",\"SubnetId\":\"4a077fa8-a239-47bf-a18f-xxxxx\",\"InstancePassword\":\"Root23123\",\"SecurityGroupId\":\"0dcd8356-9e7e-43ae-897b-xxxxx\",\"DataDiskGb\":0,\"ChargeType\":\"Daily\",\"InstanceType\":\"I3.2A\",\"PurchaseTime\":0,\"InstanceName\":\"kce-py\",\"InstanceNameSuffix\":1}",
        "InstanceForNode.1.NodeConfig.1.AdvancedSetting.DockerPath": "/data1/docker",
        "InstanceForNode.1.NodeConfig.1.AdvancedSetting.DataDisk.FileSystem": "ext3",
        "InstanceForNode.1.NodeConfig.1.AdvancedSetting.DataDisk.MountTarget": "/data1",
        "InstanceForNode.2.NodeRole": "Worker",
        "InstanceForNode.2.NodeConfig.1.Para": "{\"MaxCount\":1,\"MinCount\":1,\"ImageId\":\"a0699172-76c6-4885-a4e9-0799a9cb811d\",\"SubnetId\":\"4a077fa8-a239-47bf-a18f-xxxxx\",\"InstancePassword\":\"Root23123\",\"SecurityGroupId\":\"0dcd8356-9e7e-43ae-897b-xxxxx\",\"DataDiskGb\":0,\"ChargeType\":\"Daily\",\"InstanceType\":\"I3.2A\",\"PurchaseTime\":0,\"InstanceName\":\"kce-py\",\"InstanceNameSuffix\":1}",
        "InstanceForNode.2.NodeConfig.1.AdvancedSetting.DockerPath": "/data1/docker",
        "InstanceForNode.2.NodeConfig.1.AdvancedSetting.Label.1.Key": "label",
        "InstanceForNode.2.NodeConfig.1.AdvancedSetting.Label.1.Value": "worker",
        "InstanceForNode.2.NodeConfig.1.AdvancedSetting.DataDisk.FileSystem": "ext4",
        "InstanceForNode.2.NodeConfig.1.AdvancedSetting.DataDisk.MountTarget": "/data1",
    }

    m = client2.create_cluster(**param)
    print json.dumps(m, sort_keys=True, indent=4)

    '''
    #  查询集群列表
    m = client.describe_cluster()
    print json.dumps(m, sort_keys=True, indent=4)
    # 查询集群节点列表
    m = client.describe_cluster_instance(ClusterId="a77b437f-07c9-4ae7-ac8d-xxxxx")
    print json.dumps(m, sort_keys=True, indent=4)
    '''
    '''
    # 新增节点
    param = {
        "ClusterId": "a77b437f-07c9-4ae7-ac8d-xxxxx",
        "InstanceSet.0.NodeRole": "Worker",
        "InstanceSet.0.NodePara.0": "{\"MaxCount\":1,\"MinCount\":1,\"ImageId\":\"a0699172-76c6-4885-a4e9-0799a9cb811d\",\"SubnetId\":\"4a077fa8-a239-47bf-a18f-xxxxx\",\"InstancePassword\":\"Root23123\",\"SecurityGroupId\":\"0dcd8356-9e7e-43ae-897b-xxxxx\",\"DataDiskGb\":0,\"ChargeType\":\"Daily\",\"InstanceType\":\"I3.2A\",\"PurchaseTime\":0,\"InstanceName\":\"kce-py\",\"InstanceNameSuffix\":1}",

    }
    m = client.add_cluster_instances(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''
    '''
    # 删除集群中的节点
    param = {
        "ClusterId": "a77b437f-07c9-4ae7-ac8d-xxxxx",
        "InstanceId.1": "0253d503-485e-4adc-8859-xxxxx",
    }
    m = client.delete_cluster_instances(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    
    #   强制移除节点,该接口必须在delete_cluster_instances后执行
    param = {
        "ClusterId": "a77b437f-07c9-4ae7-ac8d-xxxxx",
        "InstanceId.1": "0253d503-485e-4adc-8859-xxxxx",
        "InstanceId.2": "0253d503-485e-4adc-8860-xxxxx",
    }
    m = client.force_remove_cluster_instance(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    # 修改集群基本信息

    
    m = client.modify_cluster_info(ClusterId="6f7f35d4-5c91-42f2-bab8-xxxxx", ClusterName="xxxxx",
                                   ClusterDesc="xxxxx")
    print json.dumps(m, sort_keys=True, indent=4)
    '''

    # 下载集群配置文件
    '''
    m = client.download_cluster_config(ClusterId="6f7f35d4-5c91-42f2-bab8-xxxxx")
    print json.dumps(m, sort_keys=True, indent=4)
    ''' \
 \
    '''
    # 删除集群
    m = client.delete_cluster(ClusterId="715d3352-e401-4994-bd2b-xxxxx")
    print json.dumps(m, sort_keys=True, indent=4)
    '''

    # 获取容器服务支持的节点操作系统
    '''
    param = {}
    m = client.describe_instance_image(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    ''' \
 \
    '''
    # 获取支持移入物理机集群的epc列表
    m = client.describe_epc_for_cluster(ClusterId="a77b437f-07c9-4ae7-ac8d-xxxxx")
    print json.dumps(m, sort_keys=True, indent=4)
    ''' \
 \
    '''
    # 移入物理机服务器至物理机集群
    param = {
        "ClusterId": "a77b437f-07c9-4ae7-ac8d-xxxxx",
        "InstanceId.1": "0253d503-485e-4adc-8859-xxxxx",
        "InstanceId.2": "0253d503-485e-4adc-8860-xxxxx",
        "AdvancedSetting.ExtraArgs.Kubelet.1.CustomArg": "--feature-gates=EphemeralContainers=true",
        "AdvancedSetting.ExtraArgs.Kubelet.2.CustomArg": "--read-only-port=0",
        "AdvancedSetting.ExtraArgs.Kubelet.3.CustomArg": "--cluster-dns=127.0.0.1"
    }
    m = client.add_cluster_epc_instances(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''
    #查询已经存在的云服务器
    '''
    param = {
        "ClusterId": "84d89f76-xxxx-47a2-b37e-xxxxx",
        "InstanceId.1": "8d1cae6a-xxxx-47f6-8fe6-xxxxx"
    }
    m = client.describe_existed_instances(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    
    #添加已有的服务器
    param = {
        "ClusterId": "84d89f76-xxxx-47a2-b37e-xxxxx",
        "ExistedInstanceKecSet.1.NodeRole": "worker",
        "ExistedInstanceKecSet.1.KecPara.1": "{\"InstanceId\":\"8d1cae6a-23c3-47f6-8fe6-xxxxx\",\"ImageId\":\"81cc01c3-4d64-40fa-89af-xxxxx\",\"InstancePassword\":\"xxxxx\"}"
    }

    m = client.add_existed_instances(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''

    #获取裸金属服务器支持的节点操作系统
    param = {
        # "ImageId": "84d89f76-xxxx-47a2-b37e-xxxxx",
    }

    m = client.describe_epc_image(**param)
    print json.dumps(m, sort_keys=True, indent=4)

    ''' 
    #创建节点池
    param = {
        "NodePoolName": "xuan-create",
        "ClusterId": "d9a0adf0-a8f3-xxx-xxxxx",
        "EnableAutoScale": True,
        "MinSize": 0,
        "DesiredCapacity": 0,
        "MaxSize": 2,
        "Label.0.Key": "labelk",
        "Label.0.Value": "labelv",
        "Taint.0.Key": "taintk",
        "Taint.0.Value": "taintv",
        "Taint.0.Effect": "NoSchedule",
        "NodeTemplate.ImageId": "13107fc5-0dd8-xxx-xxxxx",
        # "NodeTemplate.KeyId.1":"c409d431-xxx-xxx-9834-xxxxx",
        "NodeTemplate.DataDiskGb": 0,
        "NodeTemplate.SubnetId.1": "2c83f2d6-8160-xxx-xxxxx",
        "NodeTemplate.InstanceType": "E1.4B",
        "NodeTemplate.SecurityGroupId": "8728f772-6186-xxx-xxxxx",
        "NodeTemplate.ChargeType": "HourlyInstantSettlement",
        "NodeTemplate.SystemDisk.DiskType": "Local_SSD",
        "NodeTemplate.SubnetStrategy": "balanced-distribution",
        "NodeTemplate.AdvancedSetting.DockerPath": "/data/docker",
        "NodeTemplate.AdvancedSetting.Schedulable": True,
        "NodeTemplate.AdvancedSetting.UserScript": "ZWNobyAicG9zIiA+cG9z",
        "NodeTemplate.AdvancedSetting.PreUserScript": "ZWNobyAicHJlIiA+cHJl",
        "NodeTemplate.AdvancedSetting.ContainerLogMaxSize": 100,
        "NodeTemplate.AdvancedSetting.ContainerLogMaxFiles": 10,
        "NodeTemplate.SystemDisk.DiskSize": 20,
        "NodeTemplate.ProjectId": 0,
        "NodeTemplate.Password": "Xuanxxx",
        "NodeTemplate.DataDisk.1.Type": "EHDD",
        "NodeTemplate.DataDisk.1.Size": 30
    }
    m = client.create_node_pool(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    
    #查询节点池
    param = {
        "ClusterId": "d9a0adf0-a8f3-xxx-xxxxx",
        "NodePoolId.1": "64xxxxxxxx"
    }
    m = client.describe_node_pool(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    #修改节点池
    param = {
        "NodePoolId": "64xxxxxxxxx",
        "ClusterId": "d9a0adf0-a8f3-xxx-xxxxx",
        "NodePoolName": "xuan-update",
        "EnableAutoScale": False,
        "MinSize": 1,
        "DesiredCapacity": 0,
        "MaxSize": 3,
        "Label.0.Key": "labelkupdate",
        "Label.0.Value": "labelvupdate",
        "Taint.0.Key": "taintkupdate",
        "Taint.0.Value": "taintvupdate",
        "Taint.0.Effect": "NoSchedule",
        "UpdateExistingNodes": True
    }
    m = client.modify_node_pool(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    
    #删除节点池
    param = {
        "ClusterId": "d9a0adf0-a8f3-xxx-xxxxx",
        "NodePoolId.1": "64xxxxxxxxx"
    }
    m = client.delete_node_pool(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    # 修改节点池模板
    param = {
        "ClusterId": "d9a0adf0-a8f3-xxx-xxxxx",
        "NodePoolId": "64xxxxxxxxx",
        "NodeTemplate.ImageId": "13107fc5-0dd8-xxx-xxxxx",
        # "NodeTemplate.KeyId.1":"c409d431-xxx-xxx-9834-xxxxx",
        "NodeTemplate.DataDiskGb": 0,
        "NodeTemplate.SubnetId.1": "2c83f2d6-8160-xxx-xxxxx",
        "NodeTemplate.InstanceType": "E1.2B",
        "NodeTemplate.SecurityGroupId": "8728f772-6186-xxx-xxxxx",
        "NodeTemplate.ChargeType": "HourlyInstantSettlement",
        "NodeTemplate.SystemDisk.DiskType": "Local_SSD",
        "NodeTemplate.SubnetStrategy": "balanced-distribution",
        "NodeTemplate.AdvancedSetting.DockerPath": "/data/docker/xuan",
        "NodeTemplate.AdvancedSetting.Schedulable": True,
        "NodeTemplate.AdvancedSetting.UserScript": "ZWNobyAicG9zIiA+cG9z",
        "NodeTemplate.AdvancedSetting.PreUserScript": "ZWNobyAicHJlIiA+cHJl",
        "NodeTemplate.AdvancedSetting.ContainerLogMaxSize": 110,
        "NodeTemplate.AdvancedSetting.ContainerLogMaxFiles": 11,
        "NodeTemplate.SystemDisk.DiskSize": 20,
        "NodeTemplate.ProjectId": 0,
        "NodeTemplate.Password": "Xuanxxx",
        "NodeTemplate.DataDisk.1.Type": "EHDD",
        "NodeTemplate.DataDisk.1.Size": 30
    }
    m = client.modify_node_template(**param)
    print json.dumps(m, sort_keys=True, indent=4)

    #修改节点池扩容策略
    param = {
        "ClusterId": "d9a0adf0-a8f3-xxx-xxxxx",
        "ScaleUpPolicy": "most-pods"
    }
    m = client.modify_node_pool_scale_up_policy(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    #修改节点池缩容策略
    param = {
        "ClusterId": "d9a0adf0-a8f3-xxx-xxxxx",
        "MaxEmptyBulkDelete": 1,
        "ScaleDownDelayAfterAdd": 1,
        "ScaleDownEnabled": True,
        "ScaleDownUnneededTime": 1,
        "ScaleDownUtilizationThreshold": 60

    }
    m = client.modify_node_pool_scale_down_policy(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    
    #将集群内节点移入节点池
    param = {
        "ClusterId": "d9a0adf0-a8f3-xxx-xxxxx",
        "NodePoolId": "64xxxxxxxxx",
        "InstanceIds.1": "7654649f-bbc4-xxx-xxxxx"
    }
    m = client.add_cluster_instance_to_node_pool(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    #节点池节点设置缩容保护
    param = {
        "ClusterId": "d9a0adf0-a8f3-xxx-xxxxx",
        "NodePoolId": "64xxxxxxxxx",
        "InstanceIds.1": "7654649f-bbc4-xxx-xxxxx",
        "ProtectedFromScaleDown": True
    }
    m = client.protected_from_scale_down(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    
    #移除节点池节点
    param = {
        "ClusterId": "d9a0adf0-a8f3-xxx-xxxxx",
        "NodePoolId": "64xxxxxxxxx",
        "InstanceIds.1": "40b1fee5-5d0d-xxx-xxxxx",
        "InstanceDeleteMode": "Terminate"
    }
    m = client.delete_cluster_instances_from_node_pool(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''