#!/usr/bin/python

# -*- encoding:utf-8 -*-

import json,pprint
from prettyprinter import prettyPrinter
from kscore.session import get_session

if __name__ == "__main__":
    s = get_session()

    region='cn-beijing-6'
    # region='cn-shanghai-2'
    sksClient = s.create_client("sks", region, use_ssl=True)
    #query
    allKeys=sksClient.describe_keys()
    prettyPrinter().pprint(allKeys)
    #create
    # createKey = sksClient.create_key(**{"KeyName":"j-test-3"})
    # prettyPrinter().pprint(createKey)
     #import
    # importKey = sksClient.import_key(**{"KeyName":"j-test-5","PublicKey":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQCcbmgQsS4zM43iFsCo31GtUfp1/cdTXhFha4MkvWnSQaz4Z7ehDHqx9nT2fadY1f0hBD4aNDO3bf+3zUSejOcJw15xlTtiNQ57ttH4LsG+6CP03h9WYYwcCtsnlaPfVr0LldSpLSiHa2UrhuAVItGe6v54+6e8ncueiA6fUW1jUw== root"})
    # prettyPrinter().pprint(importKey)

    #modify
    # modifyKey = sksClient.modify_key(**{"KeyId":"005d19f6-774d-4631-9eda-3dbbd34100d1","KeyName":"modify-test"})
    # prettyPrinter().pprint(modifyKey)

     #delete
    # deleteKey = sksClient.delete_key(**{"KeyId":"a748558d-8994-4f5e-add1-9c4230115608"})
    # prettyPrinter().pprint(deleteKey)

