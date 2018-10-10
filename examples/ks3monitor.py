# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

if __name__ == "__main__":
    s = get_session()

    # 不同Region的bucket需要设置对应的参数去查询
    # 北京region cn-beijing-6
    # 上海region cn-shanghai-2
    # 杭州region cn-shanghai-2
    # 香港region cn-hongkong-2
    # 俄罗斯region eu-east-1

    #GetMetricStatistics
    client = s.create_client("monitor", "cn-beijing-6", use_ssl=True)

    #获取一天的标准存储量总量
    m=client.get_metric_statistics(InstanceID="test-wn",Namespace="KS3",MetricName="ks3.bucket.capacity.total.sd",StartTime="2018-07-03T00:00:05Z",EndTime="2018-07-04T00:00:05Z",Period="86400",Aggregate="Max")
    print json.dumps(m,sort_keys=True,indent=4)

'''
    #获取一天的标准存储量增量
    m=client.get_metric_statistics(InstanceID="test-wn",Namespace="ks3",MetricName="ks3.bucket.capacity.add.sd",StartTime="2018-03-18T00:00:00Z",EndTime="2018-03-19T00:00:00Z",Period="86400",Aggregate="Max")
    print json.dumps(m,sort_keys=True,indent=4)
    # 获取一天的标准存储量删除量
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.capacity.del.sd",StartTime="2018-03-18T00:00:00Z",EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
    # 获取一天的低频存储量总量
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.capacity.total.ia",StartTime="2018-03-18T00:00:00Z",EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
    # 获取一天的低频存储量增量
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.capacity.add.ia",StartTime="2018-03-18T00:00:00Z",EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
    # 获取一天的低频存储量增量
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.capacity.del.ia",StartTime="2018-03-18T00:00:00Z", EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
    # 获取一天的标准存储的下载流量
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.flow.down.sd",StartTime="2018-03-18T00:00:00Z", EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
    # 获取一天的低频存储的下载流量
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.flow.down.ia",StartTime="2018-03-18T00:00:00Z", EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
    # 获取一天的标准存储的get请求数
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.getcount.sd",StartTime="2018-03-18T00:00:00Z", EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
    # 获取一天的标准存储的put请求数
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.putcount.sd",StartTime="2018-03-18T00:00:00Z", EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
    # 获取一天的低频存储的get请求数
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.getcount.ia",StartTime="2018-03-18T00:00:00Z", EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
    # 获取一天的低频存储的put请求数
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.putcount.ia",StartTime="2018-03-18T00:00:00Z", EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
    # 获取一天的低频存储的数据取回量
    m = client.get_metric_statistics(InstanceID="test-wn", Namespace="ks3", MetricName="ks3.bucket.putcount.ia",StartTime="2018-03-18T00:00:00Z", EndTime="2018-03-19T00:00:00Z", Period="86400",Aggregate="Max")
    print json.dumps(m, sort_keys=True, indent=4)
'''
