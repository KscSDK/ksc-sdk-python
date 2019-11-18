#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    region='cn-beijing-6'
    #region='cn-shanghai-2'
    epcClient = s.create_client("epc", region, use_ssl=True)
    #query epc
    resp=epcClient.describe_epcs(MaxResults=7)
    #resp=epcClient.describe_epcs(**{'Filter.1.Name':'host-type','Filter.1.Value.1':'CAL'})
    prettyPrinter().pprint(resp)

