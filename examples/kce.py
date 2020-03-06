# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()

    # 创建集群

    client = s.create_client("kce", "cn-shanghai-3", use_ssl=False)

    param = {
        "ClusterName": "fdgfh-test",
        "ClusterManageMode": "DedicatedCluster",
        "VpcId": "15552848-026b-4ad6-a3e3-cad873fbabe5",
        "PodCidr": "10.32.0.0/14",
        "ServiceCidr": "10.254.0.0/16",
        "NetworkType": "Calico",
        "K8sVersion": "v1.13.4",
        "ReserveSubnetId": "9729f4c0-93ee-4e2a-9b2a-5e2bfdf3f3fg",
        "PublicApiServer": {
            "LineId": "fc52d881-8942-4118-bdc6-e9f3a158329d",
            "BandWidth": "1000",
            "ChargeType": "PostpaidByTime"
        },
        "InstanceSet.0.NodeRole": "Master_Etcd",

        "InstanceSet.0.NodePara.0": "{\"MaxCount\":3,\"MinCount\":3,\"ImageId\":\"3c504d3e-babf-4a40-85bd-c20537214eb7\",\"SubnetId\":\"4a077fa8-a239-47bf-a18f-df597f759ba6\",\"InstancePassword\":\"Root23123\",\"SecurityGroupId\":\"0dcd8356-9e7e-43ae-897b-a8dac8914e62\",\"DataDiskGb\":0,\"ChargeType\":\"Daily\",\"InstanceType\":\"I3.2A\",\"PurchaseTime\":0,\"InstanceName\":\"kce-py\",\"InstanceNameSuffix\":1}",
        "InstanceSet.1.NodeRole": "Worker",
        "InstanceSet.1.NodePara.0": "{\"MaxCount\":1,\"MinCount\":1,\"ImageId\":\"3c504d3e-babf-4a40-85bd-c20537214eb7\",\"SubnetId\":\"4a077fa8-a239-47bf-a18f-df597f759ba6\",\"InstancePassword\":\"Root23123\",\"SecurityGroupId\":\"0dcd8356-9e7e-43ae-897b-a8dac8914e62\",\"DataDiskGb\":0,\"ChargeType\":\"Daily\",\"InstanceType\":\"I3.2A\",\"PurchaseTime\":0,\"InstanceName\":\"kce-py\",\"InstanceNameSuffix\":1}",
    }

    m = client.create_cluster(**param)
    print json.dumps(m, sort_keys=True, indent=4)

    '''
    #  查询集群列表
    m = client.describe_cluster()
    print json.dumps(m, sort_keys=True, indent=4)
    # 查询集群节点列表
    m = client.describe_cluster_instance(ClusterId="a77b437f-07c9-4ae7-ac8d-33ae33c811db")
    print json.dumps(m, sort_keys=True, indent=4)
    '''

    # 新增节点
    param = {
        "ClusterId": "a77b437f-07c9-4ae7-ac8d-33ae33c811dc",
        "InstanceSet.0.NodeRole": "Worker",
        "InstanceSet.0.NodePara.0": "{\"MaxCount\":1,\"MinCount\":1,\"ImageId\":\"3c504d3e-babf-4a40-85bd-c20537214eb7\",\"SubnetId\":\"4a077fa8-a239-47bf-a18f-df597f759ba6\",\"InstancePassword\":\"Root23123\",\"SecurityGroupId\":\"0dcd8356-9e7e-43ae-897b-a8dac8914e62\",\"DataDiskGb\":0,\"ChargeType\":\"Daily\",\"InstanceType\":\"I3.2A\",\"PurchaseTime\":0,\"InstanceName\":\"kce-py\",\"InstanceNameSuffix\":1}",

    }
    m = client.add_cluster_instances(**param)
    print json.dumps(m, sort_keys=True, indent=4)

    '''
    # 删除集群中的节点
    param = {
        "ClusterId": "a77b437f-07c9-4ae7-ac8d-33ae33c811db",
        "InstanceId.1": "0253d503-485e-4adc-8859-0f0fb8c41639",
    }
    m = client.delete_cluster_instances(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''

    # 修改集群基本信息

    '''
    m = client.modify_cluster_info(ClusterId="6f7f35d4-5c91-42f2-bab8-4af8dd2bf53d", ClusterName="cluster-pyupdate",
                                   ClusterDesc="kec")
    print json.dumps(m, sort_keys=True, indent=4)
    '''

    # 下载集群配置文件
    '''
    m = client.download_cluster_config(ClusterId="6f7f35d4-5c91-42f2-bab8-4af8dd2bf53d")
    print json.dumps(m, sort_keys=True, indent=4)
    ''' \
 \
    '''
    # 删除集群
    m = client.delete_cluster(ClusterId="715d3352-e401-4994-bd2b-01e1e1fe035b")
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
    m = client.describe_epc_for_cluster(ClusterId="a77b437f-07c9-4ae7-ac8d-33ae33c811db")
    print json.dumps(m, sort_keys=True, indent=4)
    ''' \
 \
    '''
    # 移入物理机服务器至物理机集群
    m = client.add_cluster_epc_instances(**param)
    print json.dumps(m, sort_keys=True, indent=4)
    '''
