#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    region='cn-beijing-6'
    # region='cn-shanghai-2'
    sksClient = s.create_client("epc", region, use_ssl=True)
    #query
    allKeys=sksClient.describe_keys()
    prettyPrinter().pprint(allKeys)
    #create
    # createKey = sksClient.create_key(**{"KeyName":"j-test-1"})
    # prettyPrinter().pprint(createKey)
     #import
    # importKey = sksClient.import_key(**{"KeyName":"j-test-3","PublicKey":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQCcHn2MLBZ8qVpa/eBY/k6YR7pPNgqBqznZ6PBu818PXkcHYq4KrYAOmMwQG4rZgqLp9lGnYdX7WVGpmG0ulO+maDjt7CKViOGHDzXQt4d/G0mi0LKzn0xUMXr9Jcgjn9hkrDoXzg9ztfyxvBrnicd/t/12nah6CPJGyY5Fna4tpQ== root"})
    # prettyPrinter().pprint(importKey)

     #delete
    # deleteKey = sksClient.delete_key(**{"KeyId":"d1805cdf-f98e-4580-a74d-88481c2fb5b7"})
    # prettyPrinter().pprint(deleteKey)

