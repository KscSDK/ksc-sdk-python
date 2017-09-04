#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    region='cn-beijing-6'
    dnsClient = s.create_client("dns", region, use_ssl=True)

    allZones=dnsClient.describe_hosted_zones(**{'HostedZoneId':'319076f8-15cb-4e2a-b784-9d18fbaf95ca'})
    allRecords = dnsClient.describe_resource_records(**{'HostedZoneId':'319076f8-15cb-4e2a-b784-9d18fbaf95ca'})


    prettyPrinter().pprint(allZones)
    prettyPrinter().pprint(allRecords)
