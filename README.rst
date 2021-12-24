SDK 使用文档
========

A low-level interface to a growing number of KSC Web Services.


----------------
Install 安装
----------------

+ github 安装
    + 通过 `GitHub <https://github.com/KscSDK/ksc-sdk-python>`__ 下载
    + 通过命令 python setup.py install 安装

----------------
Config 配置
----------------

+ 申请安全凭证：

    在第一次使用云API之前，用户首先需要在金山云控制台申请安全凭证，安全凭证包括access_key_id和secret_access_key,access_key_id 是用于标识API调用者的身份，secret_access_key是用于加密签名字符串和服务器端验证签名字符串的密钥。secret_access_key 必须严格保管，避免泄露。

+ 获取安全凭证方法：

参见金山云文档： https://docs.ksyun.com/documents/40311

+ 通过文件配置及管理密钥，参考examples内示例：

    + 所在位置: '/etc/kscore.cfg' 或 './.kscore.cfg' 或 'C:\\kscore.cfg'

    + 注意: 使用相对路径时，需与运行目录保持一致。
::

    [Credentials]
    ks_access_key_id=your ak
    ks_secret_access_key=your sk

+ 或在程序运行时配置：

::

    from kscore.session import get_session
    # 密钥
    ACCESS_KEY_ID = "your ak"
    SECRET_ACCESS_KEY = "your sk"

    s = get_session()
    client = s.create_client("iam", ks_access_key_id=ACCESS_KEY_ID, ks_secret_access_key=SECRET_ACCESS_KEY)

----------------
接口输出自定义 SDK版本 >=1.3.46
----------------
+ 通过自定义映射yaml文件，文件名称必须为customer.yaml

+ customer.yaml必须放置在 您的路径/service名称/官网服务版本号 的路径下

+ 以EIP为例 需要放在 您的路径/eip/2016-03-04/customer.yaml

+ customer.yaml示例

::

  DescribeAddresses:
    PublicIp: address
    AllocationId: uuid
    AddressesSet: ips


+ 使用示例

::

eipClient = s.create_client("eip", region, use_ssl=True,customer_path='your path')



----------------
金山云-私有云域名配置 SDK版本 >1.3.32
----------------

+ 通过文件配置及管理密钥，参考examples内示例：

    + 所在位置: '/etc/kscore.cfg' 或 './.kscore.cfg' 或 'C:\\kscore.cfg'

    + 注意: 使用相对路径时，需与运行目录保持一致。

    + 注意 域名不要带引号 示例 ks_domain = api.ksyun.com
::

    [Domain]
    ks_domain = your domain

+ 或在程序运行时配置：

::

    from kscore.session import get_session
    # 密钥
    ks_domain = "your domain"


    s = get_session()
    s.set_domain(ks_domain)


----------------
日志级别配置方法
----------------
    from kscore.utils import set_logger_level
    
    import logging

    set_logger_level(logging.WARNING)

----------------
Service 服务
----------------

+ 已支持大区 region_name

    +---------------------+--------------+
    | region_name         | 大区         |
    +=====================+==============+
    | cn-beijing-6        | 北京6区      |
    +---------------------+--------------+
    | cn-shanghai-2       | 上海2区      |
    +---------------------+--------------+
    | cn-guangzhou-1      | 广州1区      |
    +---------------------+--------------+
    | cn-hongkong-2       | 香港2区      |
    +---------------------+--------------+
    | cn-taipei-1         | 台北1区      |
    +---------------------+--------------+
    | ap-singapore-1      | 新加坡1区    |
    +---------------------+--------------+
    | eu-east-1           | 俄罗斯1区    |
    +---------------------+--------------+
    | cn-beijing-fin      | 北京金融     |
    +---------------------+--------------+
    | cn-shanghai-fin     | 上海金融     |
    +---------------------+--------------+
    
+ 已支持服务列表 service_name，具体方法与API的Action对应,如kec服务RunInstances对应为run_instances方法。 `详情参考API手册 <http://docs.ksyun.com>`__

    +-------------------+----------------+
    | service           | 服务名         |
    +===================+================+
    | iam               | 身份与访问控制 |
    +-------------------+----------------+
    | eip               | 弹性IP         |
    +-------------------+----------------+
    | bws               | 共享带宽       |
    +-------------------+----------------+
    | slb               | 负载均衡       |
    +-------------------+----------------+
    | kec               | 云服务器       |
    +-------------------+----------------+
    | epc               | 云物理机       |
    +-------------------+----------------+
    | kce               | 容服           |
    +-------------------+----------------+
    | tag               | 标签服务       |
    +-------------------+----------------+
    | slb               | 负载均衡       |
    +-------------------+----------------+
    | kcs               | REDIS          |
    +-------------------+----------------+
    | vpc               | 虚拟私有网络   |
    +-------------------+----------------+
    | cdn               | 内容分发网络   |
    +-------------------+----------------+
    | monitor           | 云监控         |
    +-------------------+----------------+
    | offline           | 视频转码       |
    +-------------------+----------------+


----------------
Method 方法
----------------

+ 常用方法

    + get_session

    +---------------------------+---------------------------------------+
    | 参数                       | 说明                                 |
    +===========================+=======================================+
    | env_vars                  | 环境变量                              |
    +---------------------------+---------------------------------------+

    + create_client

    +---------------------------+---------------------------------------+
    | 参数                       | 说明                                 |
    +===========================+=======================================+
    | service_name              | 服务，必须参数，例：iam               |
    +---------------------------+---------------------------------------+
    | region_name=None          | 大区，必须参数，全局服务可以为None    |
    +---------------------------+---------------------------------------+
    | api_version=None          | API 版本，默认使用最近版本            |
    +---------------------------+---------------------------------------+
    | use_ssl=True              | 是否使用HTTPS，优先使用               |
    +---------------------------+---------------------------------------+
    | verify=None               | 是否验证SSL证书                       |
    +---------------------------+---------------------------------------+
    | endpoint_url=None         |                                       |
    +---------------------------+---------------------------------------+
    | ks_access_key_id=None     |                                       |
    +---------------------------+---------------------------------------+
    | ks_secret_access_key=None |                                       |
    +---------------------------+---------------------------------------+
    | ks_session_token=None     |                                       |
    +---------------------------+---------------------------------------+


----------------
Examples 示例
----------------

+ IAM

::

    from kscore.session import get_session

    if __name__ == "__main__":
        s = get_session()

        client = s.create_client("iam", use_ssl=False)

        users = client.list_users()

+ KEC

::

    from kscore.session import get_session

    if __name__ == "__main__":
        s = get_session()

        client = s.create_client("kec", "cn-beijing-6", use_ssl=False)

        client.[your method]()

+ MONITOR

::

    from kscore.session import get_session

    if __name__ == "__main__":
        s = get_session()

        client = s.create_client("monitor", "cn-beijing-5", use_ssl=True)

        m=client.get_metric_statistics(InstanceID="6f582c78-5d49-438e-bf2d-db4345daf503",Namespace="eip",MetricName="qos.bps_in",StartTime="2016-08-16T17:09:00Z",EndTime="2016-08-16T23:56:00Z",Period="600",Aggregate="Average")

        print json.dumps(m,sort_keys=True,indent=4)

+ OFFLINE

::

    from kscore.session import get_session
    import json

    if __name__=="__main__":

        #初始化
        s = get_session()
        client = s.create_client("offline", "cn-beijing-6", use_ssl=False)

        #创建模板接口调用示例 : preset
        presetname = 'testpreset'
        description = 'just a demo'
        presetType = 'avop'
        param = {
           "preset": presetname,
           "description": description,
           "presettype": presetType,
           "param": {
               "f": "mp4",
               "AUDIO": {
                   "acodec": "aac",
                   "ar":"44100",
                   "ab":"64k"
               },
               "VIDEO": {
                   "vr": 25,
                   "vb": "500k",
                   "vcodec": "h264",
                   "width": 640,
                   "height": 360
               }
           }
        }
        res = client.preset(**param)
        print json.dumps(res)

        #获取模板信息接口调用示例 : get_preset_detail
        res = client.get_preset_detail(preset = presetname)
        print json.dumps(res)

+ CDN

::

    from kscore.session import get_session

    if __name__ == "__main__":
        # CDN API调用 详细示例位于 ./examples/cdn.py
        s = get_session()

        client = s.create_client("cdn", use_ssl=False)

        res = client.get_cdn_domains(PageSize=20,PageNumber=0,DomainStatus='online',CdnType='download')

        print res

+ 更多

--------------------
BUG FIXED 问题修正
--------------------

+ CERTIFICATE_VERIFY_FAILED
::

    requests.exceptions.SSLError: [Errno 1] _ssl.c:504: error:14090086:SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed

 + 参考 `InsecurePlatformWarning <https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings>`__ 解决方法如下
::

    pip install requests[security]

 + 如 `build/temp.linux-x86_64-2.7/_openssl.c:433:30: fatal error: openssl/opensslv.h: No such file or directory` 解决方法如下
::

    yum install openssl-devel

 + 如 `build/temp.linux-x86_64-2.7/_openssl.c:12:24: fatal error: pyconfig.h: No such file or directory`解决方法如下
::

    yum install python-devel
