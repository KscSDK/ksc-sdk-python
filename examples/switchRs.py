#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session
def getCurrentRealserver(listenerId):
    param= {
                'Filter.1.Name': 'listener-id',
                'Filter.1.Value.1': listenerId
          }
    allServer=slbClient.describe_instances_with_listener(**param)
    #currentServer=allServer['RealServerSet'][0]['RegisterId']
    currentServer=allServer['RealServerSet'][0]
    return currentServer
def deregisterServer(registerId):
    slbClient.deregister_instances_from_listener(**{'RegisterId':registerId})
def registerServer(param):
    slbClient.register_instances_with_listener(**param)
def makeSwitch(listenerId,master,backup):
    target = master
    currentRealserver=getCurrentRealserver(listenerId)
    if master==currentRealserver['RealServerIp']:
       target=backup
    deregisterServer(currentRealserver['RegisterId'])
    param={
                'ListenerId': listenerId,
                'RealServerIp':target,
                'RealServerPort':'80',
                'RealServerType':'host',
                'Weight':10
          }
    registerServer(param)
 
if __name__ == "__main__":
    s = get_session()

    region='cn-shanghai-2'
    slbClient = s.create_client("slb", region, use_ssl=True)
    listenerId = 'e4faa0c6-3644-4f46-a2d0-d152c83d29f5'
    masterIp='10.0.2.2'
    backupIp='10.0.1.4'
    makeSwitch(listenerId,masterIp,backupIp)
