#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    vpcClient = s.create_client("vpc", "cn-shanghai-2", use_ssl=False)
    #eipClient = s.create_client("eip", "cn-beijing-6", use_ssl=False)
    eipClient = s.create_client("eip", "cn-shanghai-2", use_ssl=False)
    slbClient = s.create_client("slb", "cn-shanghai-2", use_ssl=False)
    kecClient = s.create_client("kec", "cn-shanghai-2", use_ssl=False)

    #allVpcs=vpcClient.describe_vpcs()
    #allNics=vpcClient.describe_network_interfaces()
    #allEips=eipClient.describe_addresses(MaxResults=7,NextToken='OA==')
    #allEips=eipClient.describe_addresses(MaxResults=7)
    #allEips=eipClient.describe_addresses(**{'Filter.1.Name':'instance-type','Filter.1.Value.1':'Ipfwd'})
    allInstances=kecClient.describe_instances()
    allEips=eipClient.describe_addresses(**{'Filter.1.Name':'instance-type','Filter.1.Value.1':'Slb'})
    allListeners=slbClient.describe_listeners(**{'Filter.1.Name':'load-balancer-id','Filter.1.Value.1':'5acac037-531c-414e-bb6f-c639c8948a57'}) 
    #slbClient.register_instances_with_listener(**{'ListenerId':'9b465945-5214-4038-8436-c1764b8298f5','RealServerIp':'10.0.0.2','RealServerPort':'80','RealServerType':'host'}) 
    givenListeners=slbClient.describe_listeners(**{'ListenerId.1':'9b465945-5214-4038-8436-c1764b8298f5'}) 
    prettyPrinter().pprint(givenListeners)
    #slbClient.deregister_instances_from_listener(**{'RegisterId':'cf0245b2-b847-462a-a777-7f680f6e48b8'}) 

    #pprint.pprint(allEips)

    #prettyPrinter().pprint(allVpcs)
    #prettyPrinter().pprint(allEips)
    #prettyPrinter().pprint(allNics)
    #prettyPrinter().pprint(allInstances)
    for item in allEips['AddressesSet']:
       print item['PublicIp']
       print item['AllocationId']
    #eipClient.associate_address(**{'AllocationId':'1cd0da05-8a3e-4c8e-8230-e6d39b85331e','InstanceType':'Ipfwd','InstanceId':'bede9a1c-d3a7-4b31-82e6-6699790ad1a3', 'NetworkInterfaceId':'fec81567-a4c7-4460-a998-54f407e77c0a'})
    #eipClient.disassociate_address(**{'AllocationId':'1cd0da05-8a3e-4c8e-8230-e6d39b85331e'})
    for item in allListeners['ListenerSet']:
       print item['ListenerName']
       print item['ListenerId']
    #availableIps=vpcClient.describe_subnet_available_addresses()
    #availableIps=vpcClient.describe_subnet_available_addresses(**{'Filter.1.Name':'subnet-id','Filter.1.Value.1':'0d238ac1-69b0-4602-893b-8da5862069e0'})
