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

