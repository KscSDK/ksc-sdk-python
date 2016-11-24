#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    region='cn-beijing-6'
    #region='cn-shanghai-2'
    #vpcClient = s.create_client("vpc", region, use_ssl=True)
    #vpcClient = s.create_client("vpc", region, use_ssl=True)
    #vpcClient = s.create_client("vpc", region, use_ssl=True,verify=False)
    #eipClient = s.create_client("eip", region, use_ssl=True)
    slbClient = s.create_client("slb", region, use_ssl=True)
    #kecClient = s.create_client("kec", region, use_ssl=True)

    #allVpcs=vpcClient.describe_vpcs()
    #allInstances=kecClient.describe_instances()
    #allNics=vpcClient.describe_network_interfaces()
    #allEips=eipClient.describe_addresses(MaxResults=7,NextToken='OA==')
    #allEips=eipClient.describe_addresses(MaxResults=7)
    #allEips=eipClient.describe_addresses(**{'Filter.1.Name':'instance-type','Filter.1.Value.1':'Ipfwd'})
    #allEips=eipClient.describe_addresses(**{'Filter.1.Name':'instance-type','Filter.1.Value.1':'Slb'})
    #allListeners=slbClient.describe_listeners(**{'Filter.1.Name':'load-balancer-id','Filter.1.Value.1':'89befb57-095a-4329-ae2a-fdfe81959f8c'}) 
    #allListeners=slbClient.describe_listeners()
    #slbClient.register_instances_with_listener(**{'ListenerId':'9b465945-5214-4038-8436-c1764b8298f5','RealServerIp':'10.0.0.2','RealServerPort':'80','RealServerType':'host'}) 
    #slbClient.register_instances_with_listener(**{'ListenerId':'c1b03c98-9252-44fe-94e8-ece92767f76e','RealServerIp':'120.92.44.206','RealServerPort':'80','RealServerType':'Ipfwd'}) 
    slbClient.register_instances_with_listener(**{'ListenerId':'9156f303-65fb-4f90-86cb-52dc25721031','RealServerIp':'120.92.33.46','RealServerPort':'4431','RealServerType':'Ipfwd','Weight':10}) 
    slbClient.register_instances_with_listener(**{'ListenerId':'9156f303-65fb-4f90-86cb-52dc25721031','RealServerIp':'120.92.42.4','RealServerPort':'4431','RealServerType':'Ipfwd','Weight':10}) 
    slbClient.register_instances_with_listener(**{'ListenerId':'9156f303-65fb-4f90-86cb-52dc25721031','RealServerIp':'120.92.9.75','RealServerPort':'4431','RealServerType':'Ipfwd','Weight':10}) 
    #eipClient.associate_address_portfwd(**{'AllocationId':'981ad9c1-329e-4096-a25b-0684a908a164','InstanceId':'9cbf64e0-b974-43e9-9d9c-18ed96101041','Protocol':'UDP','PublicIpPort':'8080','InstancePort':'8090'})
    #eipClient.associate_address_portfwd(**{'AllocationId':'981ad9c1-329e-4096-a25b-0684a908a164','InstanceId':'9cbf64e0-b974-43e9-9d9c-18ed96101041','Protocol':'TCP','PublicIpPort':'9080','InstancePort':'9090'})
    #givenListeners=slbClient.describe_listeners(**{'ListenerId.1':'d94b6af0-61bd-4b15-ab2c-c6758a3367bc'}) 
    #prettyPrinter().pprint(givenListeners)
    #slbClient.deregister_instances_from_listener(**{'RegisterId':'cf0245b2-b847-462a-a777-7f680f6e48b8'}) 
    #slbClient.delete_load_balancer(**{'LoadBalancerId':'b5a2fac6-7cd0-40ee-abb5-dbcc59cbb4b7'}) 

    #pprint.pprint(allEips)
    #pprint.pprint(allVpcs)

    #prettyPrinter().pprint(allVpcs)
    #prettyPrinter().pprint(allEips)
    #prettyPrinter().pprint(allNics)
    #prettyPrinter().pprint(allInstances)
'''
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
    #pprint.pprint(dir(vpcClient)) 
    #eipClient.modify_address(**{'AllocationId':'c054f87a-4508-4db2-bc10-f594b34a2ef3','BandWidth':1})
    #eipClient.modify_address(**{'AllocationId':'070a4af5-90ff-4953-a388-01a694ebdae5','BandWidth':1})
'''
