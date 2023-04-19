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

    # 注:如果参数名中包含.请使用JSON格式数据，如参数名 KeyId.N 、 Filter.N.Name 、 Filter.N.Value.1
    # ------------------DescribeKeys(获取密钥列表信息)--------------------------
    param = {
        'KeyId.1': '89e84941-41fb-43e3-8426-43676ac11b0b',
        'MaxResults': 20,
        'NextToken': 1
    }
    resp=sksClient.describe_keys(**param)
    print(resp)

    # ------------------CreateKey(创建密钥)--------------------------
    # param = {
    #     'KeyName': 'test'
    # }
    # resp = sksClient.create_key(**param)
    # print(resp)

    # ------------------ImportKey(导入密钥)--------------------------
    # param = {
    #     'KeyName': 'test-import',
    #     "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQCcbmgQsS4zM43iFsCo31GtUfp1/cdTXhFha4MkvWnSQaz4Z7ehDHqx9nT2fadY1f0hBD4aNDO3bf+3zUSejOcJw15xlTtiNQ57ttH4LsG+6CP03h9WYYwcCtsnlaPfVr0LldSpLSiHa2UrhuAVItGe6v54+6e8ncueiA6fUW1jUw== root"
    # }
    # resp = sksClient.import_key(**param)
    # print(resp)

    # ------------------ModifyKey(修改密钥信息)--------------------------
    # param = {
    #     'KeyId': 'f3a5e823-2713-4ffc-920c-f0b57dffd8f8',
    #     "KeyName": "test-update"
    # }
    # resp = sksClient.modify_key(**param)
    # print(resp)

    # ------------------DeleteKey(删除密钥)--------------------------
    # param = {
    #     'KeyId': 'f3a5e823-2713-4ffc-920c-f0b57dffd8f8'
    # }
    # resp = sksClient.delete_key(**param)
    # print(resp)

