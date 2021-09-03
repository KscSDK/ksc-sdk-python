# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()
    '''
    通用产品线，不包含容器（docker）
    '''
    #ListMetrics
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.list_metrics(InstanceID="3f092bb4-7461-4dac-9ee5-xxxxx",
                            Namespace="kec",
                            PageIndex="1",
                            PageSize="10")
    print(json.dumps(m, sort_keys=True, indent=4))

    #GetMetricStatistics
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.get_metric_statistics(
        InstanceID="227d550e-88d4-428e-8b90-xxxxx",
        Namespace="eip",
        MetricName="eip.bps.in",
        StartTime="2019-11-27T20:09:00Z",
        EndTime="2019-11-27T20:19:00Z",
        Period="60",
        Aggregate="Average,Max,Min")
    print(json.dumps(m, sort_keys=True, indent=4))

    #GetMetricStatisticsBatch      version=2018-11-14
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    param = {
        "Namespace":
        "kec",
        "StartTime":
        "2019-11-27T14:00:00Z",
        "EndTime":
        "2019-11-27T14:09:00Z",
        "Period":
        "180",
        "Aggregate": ["Max", "Min", "Avg"],
        "Metrics": [{
            "InstanceID": "3f092bb4-7461-4dac-9ee5-xxxxx",
            "MetricName": "net.if.in"
        }, {
            "InstanceID": "3f092bb4-7461-4dac-9ee5-xxxxx",
            "MetricName": "cpu.utilizition.total"
        }, {
            "InstanceID": "ee321b50-1d9b-474c-92d0-xxxxx",
            "MetricName": "net.if.out"
        }]
    }
    m = client.get_metric_statistics_batch_v2(**param)
    print(json.dumps(m, sort_keys=True, indent=4))
    '''
    只支持容器docker（kce），其余产品线不支持。
    '''
    #ListMetrics
    paraml = {
        "Action": "ListMetrics",
        "Version": "2019-08-12",
        "Namespace": "kce",
        "PageIndex": "1",
        "PageSize": "10",
        "Dimensions.0.Name": "ClusterId",
        "Dimensions.0.Value": "807a4149-b7e2-4e05-8a35-xxxxx",
        "Dimensions.1.Name": "NamespaceName",
        "Dimensions.1.Value": "xxxxx",
        "Dimensions.2.Name": "WorkloadType",
        "Dimensions.2.Value": "deployment",
        "Dimensions.3.Name": "WorkloadName",
        "Dimensions.3.Value": "xxxxx",
        "Dimensions.4.Name": "PodName",
        "Dimensions.4.Value": "xxxxx-xxxxx-xxxxx",
        # "Dimensions.5.Name":"ContainerName",
        # "Dimensions.5.Value":"kxxxxx"
    }

    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.list_metrics_v3(**paraml)
    print(json.dumps(m, sort_keys=True, indent=4))

    #GetMetricStatistics
    paramg = {
        "Action": "GetMetricStatistics",
        "Version": "2019-08-12",
        "Namespace": "kce",
        "MetricName": "pod.network.rx",
        "StartTime": "2019-11-26T17:09:00Z",
        "EndTime": "2019-11-26T17:19:00Z",
        "Period": "60",
        "Aggregate": "Average,Max,Min",
        "Dimensions.0.Name": "ClusterId",
        "Dimensions.0.Value": "807a4149-b7e2-4e05-8a35-xxxxx",
        "Dimensions.1.Name": "NamespaceName",
        "Dimensions.1.Value": "xxxxx",
        "Dimensions.2.Name": "WorkloadType",
        "Dimensions.2.Value": "deployment",
        "Dimensions.3.Name": "WorkloadName",
        "Dimensions.3.Value": "xxxxx",
        "Dimensions.4.Name": "PodName",
        "Dimensions.4.Value": "xxxxx",
        # "Dimensions.5.Name":"ContainerName",
        # "Dimensions.5.Value":"xxxxx"
    }

    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.get_metric_statistics_v3(**paramg)
    print(json.dumps(m, sort_keys=True, indent=4))

    #ListAlarmPolicy
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.list_alarm_policy(PageIndex=1, PageSize=1)
    print(json.dumps(m, sort_keys=True, indent=4))

    #DescribeAlarmPolicy
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.describe_alarm_policy(PolicyId=25232)
    print(json.dumps(m, sort_keys=True, indent=4))

    #DescribePolicyObject
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.describe_policy_object(PolicyId=25232, PageIndex=1, PageSize=10)
    print(json.dumps(m, sort_keys=True, indent=4))

    #DescribeAlarmReceives
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.describe_alarm_receives(PolicyId=25232)
    print(json.dumps(m, sort_keys=True, indent=4))

    #AddAlarmReceives
    paraml = {
        "PolicyId": 25232,
        "ContactFlag": 2,
        "ContactWay": 3,
        "ContactId": [1985, 3607],
    }

    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.add_alarm_receives(**paraml)
    print(json.dumps(m, sort_keys=True, indent=4))

    #DeleteAlarmReceives
    paraml = {
        "PolicyId": 25232,
        "ContactFlag": 2,
        "ContactId": [1985, 3607],
    }

    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.delete_alarm_receives(**paraml)
    print(json.dumps(m, sort_keys=True, indent=4))

    #GetUserGroup
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.get_user_group()
    print(json.dumps(m, sort_keys=True, indent=4))

    #GetAlertUser
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.get_alert_user(UserGrpId=[879, 1484])
    print(json.dumps(m, sort_keys=True, indent=4))

    #UpdateAlertUserStatus
    paraml = {
        "UserId": [1985, 3607],
        "UserStatus": 1,
    }
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m = client.update_alert_user_status(**paraml)
    print(json.dumps(m, sort_keys=True, indent=4))
