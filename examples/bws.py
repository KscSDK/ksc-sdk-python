#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    region='cn-beijing-6'
    #region='cn-shanghai-2'
    eipClient = s.create_client("bws", region, use_ssl=True)

    #allInstances=kecClient.describe_instances()
    #allNics=vpcClient.describe_network_interfaces()
    #allEips=eipClient.describe_addresses(MaxResults=7,NextToken='OA==')
    allEips=eipClient.describe_band_width_shares(MaxResults=7)
    #allEips=eipClient.describe_addresses(**{'Filter.1.Name':'instance-type','Filter.1.Value.1':'Ipfwd'})
    #allEips=eipClient.describe_addresses(**{'Filter.1.Name':'instance-type','Filter.1.Value.1':'Slb'})

    #pprint.pprint(allEips)

    #prettyPrinter().pprint(allEips)
    #prettyPrinter().pprint(allNics)
    #prettyPrinter().pprint(allInstances)
    for item in allEips['BandWidthShareSet']:
       print item['BandWidthShareId']
       #print item['AllocationId']
    #eipClient.associate_address(**{'AllocationId':'1cd0da05-8a3e-4c8e-8230-e6d39b85331e','InstanceType':'Ipfwd','InstanceId':'bede9a1c-d3a7-4b31-82e6-6699790ad1a3', 'NetworkInterfaceId':'fec81567-a4c7-4460-a998-54f407e77c0a'})
    #eipClient.disassociate_address(**{'AllocationId':'1cd0da05-8a3e-4c8e-8230-e6d39b85331e'})
    #eipClient.modify_address(**{'AllocationId':'c054f87a-4508-4db2-bc10-f594b34a2ef3','BandWidth':1})
    #eipClient.modify_address(**{'AllocationId':'070a4af5-90ff-4953-a388-01a694ebdae5','BandWidth':1})
