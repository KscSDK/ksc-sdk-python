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
vip = "172.18.0.253" #改成您的本机内网 VIP
DestinationCidrBlock = '172.18.0.253/32' #修改为VIP 
thisInstanceId = '1cf963ff-7847-4859-8462-5405f0facc1d' #当前主机的Id
thatInstanceId = 'b141da5f-8e3e-44c0-ac0f-a0feccba78c7' #迁移前所在主机Id
interface = {"eth0":"172.18.0.13"} #当前机器主网卡和主IP
##################需修改部分End######################

log = open('/var/log/keepalived.log', 'a+')
state_file = open('/var/keepalived/state', 'r')

def get_now_time():
    return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time())) + '[pid' + str(os.getpid()) + ']' 

def log_write(message=''):
    log.write(get_now_time() + " " + str(message) + "\n")

def get_ip():
    f = os.popen('ip addr show dev %s | grep %s | awk \'{print $2}\' | awk -F/ \'{print $1}\'' % (interface.keys()[0] , interface.values()[0]))
    return f.read().strip()

def findRoute():
	for route in vpcClient.describe_routes()['RouteSet']:
		if route['DestinationCidrBlock'] == DestinationCidrBlock:
			print 'current route found'
			return route['RouteId']

        print 'route not found'
def migrateVip():
    params = {
        'vpcId': vpcId,             
        'privateIpAddress': vip,      
        'thatInstanceId': thatInstanceId, 
        'thisInstanceId': thisInstanceId 
    }

    log_write(" try set vip.")
    retry_times_when_mgr_ip_got = 4
    exceptimes = 0
    get_ip_times = 0
    time.sleep(0.5)
    r = findRoute()
    if r:
        vpcClient.delete_route(**{'RouteId':r})	
    log_write(" now change the nexthop of vip to this host." + get_ip())
    vpcClient.create_route(**{'VpcId':vpcId,'DestinationCidrBlock':DestinationCidrBlock,'RouteType':'Host','InstanceId':thisInstanceId})
    while get_ip_times < 5:
        log_write(" get_ip=" + get_ip())
        if get_ip()==interface.values()[0]:
            try:
                i = 0
                while i < retry_times_when_mgr_ip_got:
                    state_file.seek(0)
                    state = state_file.readline()
                    if state == 'MASTER':
                        break 
                    i = i + 1
                    time.sleep(2)
                if i >= retry_times_when_mgr_ip_got:
                    log_write(" set vip failed")
                break
            except Exception, e:
                log_write(' exception:' + str(e))
                exceptimes = exceptimes + 1
                if exceptimes > 3:
                    break
        time.sleep(0.5)
        get_ip_times = get_ip_times + 1

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

