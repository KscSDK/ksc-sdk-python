# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()


    #ListMetrics

    # client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    # m=client.list_metrics(InstanceID="e564f8b3-f120-42cd-8b0e-084e66e73161",Namespace="kec",PageIndex="1",PageSize="10")
    # print json.dumps(m,sort_keys=True,indent=4)



    #GetMetricStatistics
    client = s.create_client("monitor", "cn-beijing-5", use_ssl=True)
    m=client.get_metric_statistics(InstanceID="6f582c78-5d49-438e-bf2d-db4345daf503",Namespace="eip",MetricName="qos.bps_in",StartTime="2016-08-16T17:09:00Z",EndTime="2016-08-16T23:56:00Z",Period="600",Aggregate="Average,Max,Min,Count,Sum")
    print json.dumps(m,sort_keys=True,indent=4)

    '''
    #GetMetricStatisticsBatch
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    param={
           "Namespace": "eip",
           "StartTime": "2018-09-21T14:00:00Z",
           "EndTime": "2018-09-21T014:59:00Z",
           "Period": "1800",
           "Aggregate": ["Max","Min","Avg"],
           "Metrics": [
                       {
                        "InstanceID": "2cdb3797-3a6b-4ff1-ad87-6038fd606dd7",
                        "MetricName":"eip.bps.in"
                       },
                       {
                        "InstanceID": "62033090-9298-4d28-a413-1d6a08cf7270",
                        "MetricName":"eip.bps.out"
                       },
                       {
                        "InstanceID": "611d617b-5d94-474f-8346-a2c5032a488b",
                        "MetricName":"eip.pps.in"
                       }
                     ]
          }
    m=client.get_metric_statistics_batch(**param)
    print json.dumps(m,sort_keys=True,indent=4)
    '''

    '''
    docker（kce） 没有InstanceId，需要设置Dimensions。且Dimensions只支持docker（kce）产品线，其余产品线不支持。
    '''
    '''
    dimensions={
        "ClusterId": "1f0dc90a-b639-43e8-8448-a0aa29fbc4df",
        "NamespaceName": "kube-system",
        "DeploymentName": "heapster-85f77cbfb9",
        "PodName": "heapster-85f77cbfb9-cl5x8"
}


    #ListMetrics

    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m=client.list_metrics(Namespace="kce",PageIndex="1",PageSize="10",Dimensions=dimensions)
    print json.dumps(m,sort_keys=True,indent=4)



    #GetMetricStatistics

    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)
    m=client.get_metric_statistics(Namespace="kce",MetricName="cpu.utilizition.total",StartTime="2018-06-16T17:09:00Z",EndTime="2018-07-13T23:56:00Z",Period="600",Aggregate="Average,Max,Min,Count,Sum",Dimensions=dimensions)
    '''
