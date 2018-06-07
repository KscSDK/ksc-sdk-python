#!/usr/bin/python
# -*- coding: utf-8 -*-
#/etc/keepalived/nexthop.py

import os
import time
import json
import sys
from kscore.session import get_session

##################需修改部分Begin####################
region='cn-beijing-6'   #region code
vpcId = '1858a08a-6cc9-4278-8d0c-d536f441fe8e'  #vpcId
ks_access_key_id = '您的ak'
ks_secret_access_key = '您的sk'
DestinationCidrBlock = '172.18.0.253/32' #修改为VIP 
thisInstanceId = '1cf963ff-7847-4859-8462-5405f0facc1d' #当前主机的Id
##################需修改部分End######################

log = open('/var/log/keepalived.log', 'a+')
#state_file = open('/var/keepalived/state', 'r')

def get_now_time():
    return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time())) + '[pid' + str(os.getpid()) + ']' 

def log_write(message=''):
    log.write(get_now_time() + " " + str(message) + "\n")


def findRoute():
	for route in vpcClient.describe_routes()['RouteSet']:
		if route['DestinationCidrBlock'] == DestinationCidrBlock:
			log_write('an existing route found')
			return route['RouteId']
        log_write('route not found')
def migrateVip():
    param={'VpcId':vpcId,
            'DestinationCidrBlock':DestinationCidrBlock,
            'RouteType':'Host',
            'InstanceId':thisInstanceId}
    log_write("migrating vip to another host.")
    time.sleep(0.5)
    r = findRoute()
    if r:
        print vpcClient.delete_route(RouteId=r)
    log_write(" now change the nexthop of vip to this host." + thisInstanceId)
    if vpcClient.create_route(**param):
                log_write('migrating vip success')

def print_help():
    log_write(
            '''
            ./nexthop.py migrate
                migrate your vip
            ''')

if __name__ == '__main__':
    s = get_session()
    s.set_credentials(ks_access_key_id,ks_secret_access_key)
    vpcClient = s.create_client("vpc", region, use_ssl=True)
    if len(sys.argv) == 1:
        log_write("nexthop.py: parameter num is 0")
        print_help()
    elif sys.argv[1] == 'migrate':
        migrateVip()   
        log_write()
    else:
        log_write("nexthop.py: misMatched parameter")
        print_help()

