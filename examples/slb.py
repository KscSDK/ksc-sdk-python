#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    region='cn-beijing-6'
    #region='cn-shanghai-2'
    slbClient = s.create_client("slb", region, use_ssl=True)
    #kecClient = s.create_client("kec", region, use_ssl=True)

    #allInstances=kecClient.describe_instances()
    #allListeners=slbClient.describe_listeners(**{'Filter.1.Name':'load-balancer-id','Filter.1.Value.1':'89befb57-095a-4329-ae2a-fdfe81959f8c'}) 
    allListeners=slbClient.describe_listeners()
    #slbClient.register_instances_with_listener(**{'ListenerId':'9b465945-5214-4038-8436-c1764b8298f5','RealServerIp':'10.0.0.2','RealServerPort':'80','RealServerType':'host'}) 
    #givenListeners=slbClient.describe_listeners(**{'ListenerId.1':'d94b6af0-61bd-4b15-ab2c-c6758a3367bc'}) 
    prettyPrinter().pprint(allListeners)
    #slbClient.deregister_instances_from_listener(**{'RegisterId':'cf0245b2-b847-462a-a777-7f680f6e48b8'}) 
    #slbClient.delete_load_balancer(**{'LoadBalancerId':'b5a2fac6-7cd0-40ee-abb5-dbcc59cbb4b7'}) 

    #prettyPrinter().pprint(allInstances)
    for item in allListeners['ListenerSet']:
       print item['ListenerName']
       print item['ListenerId']
