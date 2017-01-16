#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    region='cn-beijing-6'
    #region='cn-shanghai-2'
    vpcClient = s.create_client("vpc", region, use_ssl=True)

    allVpcs=vpcClient.describe_vpcs()
    #allNics=vpcClient.describe_network_interfaces()


    prettyPrinter().pprint(allVpcs)
