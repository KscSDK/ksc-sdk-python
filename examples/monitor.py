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

