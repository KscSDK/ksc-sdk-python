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
    allEpcs=epcClient.describe_epcs()

    prettyPrinter().pprint(allEpcs)

