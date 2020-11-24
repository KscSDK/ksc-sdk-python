# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()

    # 创建集群

    client = s.create_client("kce", "cn-beijing-6", use_ssl=True)

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
    #  查询集群列表
    m = client.describe_cluster()
    print json.dumps(m, sort_keys=True, indent=4)
    # 查询集群节点列表
    m = client.describe_cluster_instance(ClusterId="a77b437f-07c9-4ae7-ac8d-xxxxx")
    print json.dumps(m, sort_keys=True, indent=4)
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
    # 删除集群中的节点
    param = {
        "ClusterId": "a77b437f-07c9-4ae7-ac8d-xxxxx",
        "InstanceId.1": "0253d503-485e-4adc-8859-xxxxx",
    }
    m = client.delete_cluster_instances(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''

    # 修改集群基本信息

    '''
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
    m = client.add_cluster_epc_instances(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''
    #查询已经存在的云服务器
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