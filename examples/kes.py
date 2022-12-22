# -*- encoding:utf-8 -*-
from kscore.exceptions import ClientError
from kscore.session import get_session
from pprint import pprint

if __name__ == "__main__":
    s = get_session()  # 创建会话

    client = s.create_client("kes", "cn-shanghai-3", use_ssl=False)  # 一个 kscore 客户端实例（kes）
    param = {
        "ChargeType": "HourlyInstantSettlement",
        "AvailabilityZone": "cn-shanghai-3a",
        "MainVersion": "7.4.2",
        "InstanceGroups": [
            {
                "InstanceGroupType": "DATA",
                "InstanceCount": 3,
                "InstanceType": "ES.ssd.3C3G",
                "VolumeType": "Local_SSD",
                "VolumeSize": 20
            }
        ],
        "VpcDomainId": "XXXXXXXXXXXXXXXXXXXXX",
        "VpcSubnetId": "XXXXXXXXXXXXXXXXXXXXX"
    }
    resp = client.launch_cluster(**param)
    print(resp)

''' 
   ListClusters 查看所有集群的信息

   Parameters:
       Marker        string    分页信息,示例limit=10&offset=0 
   Returns:
       <type json>
   '''
# param = {
#     "Marker": "limit=50&offset=0"
# }
# resp = client.list_clusters(**param)
# print(resp)


''' 
   LaunchCluster 创建集群

   Parameters:
       VpcSubnetId        string    账号下同数据中心同可用区可用云服务器子网（云服务器网络，节点资源有KEC资源则必填）
       VpcEpcSubnetId     string    账号下同数据中心同可用区可用裸金属服务器子网（云物理机网络，节点资源有裸金属资源则必填）
       VpcDomainId        string    账号下同数据中心可用VPC网络（VPC网络）
       SecurityGroupId    string    账号下KES产品线可用安全组。标准UUID格式，形如[1]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$（安全组ID，若不填则默认创建新的安全组）
       PurchaseTime       int       1-36（购买时长，当计费类型为Monthly（包年包月）时，需要传此参数，其他计费类型时不需要）
       ProjectId          long      账号有权限的所有项目ID，0为默认项目（项目ID）
       MainVersion        string    7.4.2，6.8.4，5.6.16（ES版本）
       EipLineId          string    UUID（EIP链路，购买弹性IP时必填）
       InstanceGroups     object [] 节点组列表标识（）
       EnableEip          boolean	true，false（是否开启EIP，不传默认为false）
       EipId                        绑定，EIPID（）
       ClusterName        string    长度限制为1-25个字符，支持数字、大小写字母、减号和下划线（集群名称，如果未指定，则自动生成）
       ...
   Returns:
       <type json>
   '''

# param = {
#     "ChargeType":"HourlyInstantSettlement",
#     "AvailabilityZone":"cn-shanghai-3a",
#     "MainVersion":"7.4.2",
#     "InstanceGroups":[
#         {
#             "InstanceGroupType":"DATA",
#             "InstanceCount":3,
#             "InstanceType":"ES.ssd.3C3G",
#             "VolumeType":"Local_SSD",
#             "VolumeSize":20
#         }
#     ],
#     "VpcDomainId":"XXXXXXXXXXXXXXXXXXXXX",
#     "VpcSubnetId":"XXXXXXXXXXXXXXXXXXXXX"
# }
# resp = client.launch_cluster(**param)
# print(resp)


''' 
   DescribeCluster 查看指定集群详情信息

   Parameters:
       ClusterId        string    集群ID 
   Returns:
       <type json>
   '''
# param = {
#     "ClusterId":"XXXXXXXXXXXXXXXXXXXXX"
# }
# resp = client.describe_cluster(**param)
# print(resp)


''' 
   RestartCluster 重启指定的金山云KES集群

   Parameters:
       ClusterId        string    集群ID
       Rolling          boolean   为1时，滚动重启，为0时强制启动
       RollingInterval   	      节点重启间隔时间	
   Returns:
       <type json>
   '''
# param = {
#     "ClusterId":"XXXXXXXXXXXXXXXXXXXXX"
# }
# resp = client.restart_cluster(**param)
# print(resp)


''' 
   ScaleOutInstanceGroups 完成现有集群扩容操作

   Parameters:
       ClusterId            string    集群ID
       InstanceGroups       string[]  扩容节点组标识	
       InstanceGroupType 	boolean   是否新开节点组
       InstanceType         string    节点组套餐code，已有节点组扩容该参数无效，新开节点组必填
       InstanceCount        int       扩容数量，若已有节点组为新增数量，新开节点组为节点组内节点数量
       VolumeType           string    磁盘类型
       VolumeSize           int       数据盘大小
       ProjectId            long      账号有权限的所有项目ID，0为默认项目
   Returns:
       <type json>
   '''
# param = {
#     "ClusterId":"XXXXXXXXXXXXXXXXXXXXX",
#     "InstanceGroups":[
#         {
#             "InstanceGroupType":"DATA",
#             "InstanceCount":1
#         }
#     ]
# }
# resp = client.scale_out_instance_groups(**param)
# print(resp)
