# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    clientv2 = s.create_client("monitorv2", "cn-beijing-6", use_ssl=True)

    '''
    通用产品线，不包含容器（docker）
    '''
    #ListMetrics
    m = client.list_metrics(InstanceID="293bbbc1-6c27-4567-89fc-xxxxx",
                            Namespace="kec",
                            PageIndex="1",
                            PageSize="10")
    print(json.dumps(m, sort_keys=True, indent=4))

    #GetMetricStatistics
    #m = client.get_metric_statistics(
    #    InstanceID="ef6eaa98-8e2b-4629-98e0-xxxxx",
    #    Namespace="eip",
    #    MetricName="eip.bps.in",
    #    StartTime="2021-09-15T10:09:00Z",
    #    EndTime="2021-09-15T10:19:00Z",
    #    Period="60",
    #    Aggregate="Average,Max,Min")
    #print(json.dumps(m, sort_keys=True, indent=4))

    #GetMetricStatisticsBatch      version=2018-11-14
    param = {
        "Namespace":
        "kec",
        "StartTime":
        "2021-09-15T10:00:00Z",
        "EndTime":
        "2021-09-15T10:09:00Z",
        "Period":
        "180",
        "Aggregate": ["Max", "Min", "Avg"],
        "Metrics": [{
            "InstanceID": "293bbbc1-6c27-4567-89fc-xxxxx",
            "MetricName": "net.if.in"
        }, {
            "InstanceID": "293bbbc1-6c27-4567-89fc-xxxxx",
            "MetricName": "cpu.utilizition.total"
        }, {
            "InstanceID": "6a725f27-1c7e-4704-95c8-xxxxx",
            "MetricName": "net.if.out"
        }]
    }
    #m = client.get_metric_statistics_batch_v2(**param)
    #print(json.dumps(m, sort_keys=True, indent=4))
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
        # "Dimensions.5.Value":"xxxxx"
    }

    #m = client.list_metrics_v3(**paraml)
    #print(json.dumps(m, sort_keys=True, indent=4))

    #GetMetricStatistics
    paramg = {
        "Action": "GetMetricStatistics",
        "Version": "2019-08-12",
        "Namespace": "kce",
        "MetricName": "pod.network.rx",
        "StartTime": "2021-09-15T10:09:00Z",
        "EndTime": "2021-09-15T10:19:00Z",
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

    #m = client.get_metric_statistics_v3(**paramg)
    #print(json.dumps(m, sort_keys=True, indent=4))

    #ListAlarmPolicy
    #m = clientv2.list_alarm_policy(PageIndex=1, PageSize=10)
    #print(json.dumps(m, sort_keys=True, indent=4))

    #DescribeAlarmPolicy
    #m = clientv2.describe_alarm_policy(PolicyId=25232)
    #print(json.dumps(m, sort_keys=True, indent=4))

    #DescribePolicyObject
    #m = clientv2.describe_policy_object(PolicyId=25232, PageIndex=1, PageSize=10)
    #print(json.dumps(m, sort_keys=True, indent=4))

    #DescribeAlarmReceives
    #m = clientv2.describe_alarm_receives(PolicyId=25232)
    #print(json.dumps(m, sort_keys=True, indent=4))

    #AddAlarmReceives
    paraml = {
        "PolicyId": 25232,
        "ContactFlag": 2,
        "ContactWay": 3,
        "ContactId": [1985, 3607],
    }

    #m = clientv2.add_alarm_receives(**paraml)
    #print(json.dumps(m, sort_keys=True, indent=4))

    #DeleteAlarmReceives
    paraml = {
        "PolicyId": 25232,
        "ContactFlag": 2,
        "ContactId": [1985, 3607],
    }

    #m = clientv2.delete_alarm_receives(**paraml)
    #print(json.dumps(m, sort_keys=True, indent=4))

    #GetUserGroup
    #m = clientv2.get_user_group()
    #print(json.dumps(m, sort_keys=True, indent=4))

    #GetAlertUser
    #m = clientv2.get_alert_user(UserGrpId=[879, 1484])
    #print(json.dumps(m, sort_keys=True, indent=4))

    #UpdateAlertUserStatus
    paraml = {
        "UserId": [1985, 3607],
        "UserStatus": 1,
    }
    #m = clientv2.update_alert_user_status(**paraml)
    #print(json.dumps(m, sort_keys=True, indent=4))
