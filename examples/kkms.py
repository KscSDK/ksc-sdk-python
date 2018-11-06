# -*- encoding:utf-8 -*-

from kscore.session import get_session
import json

# 打印一个 对象 （可忽略该函数）
def printObj(Obj = None,level = 0):
    ObjType = type(Obj).__name__;
    for key in Obj:
        Value = None;
        PrintStr = "  " * level;
        # 判断是否字典
        if( ObjType == 'dict' ):
            Value = Obj[key];
            PrintStr += "[%s]-" % (key);
        else:
            Value = key;
        # 判断当前要打印的变量类型
        TmpType = type(Value).__name__;   
        if( TmpType == 'dict' or TmpType == 'list' or TmpType == 'set' ):
            PrintStr += "[%s]:" % ( TmpType , );
            print PrintStr;
            printObj(Value,level + 1);
        else:
            PrintStr += "[%s]\n" % ( Value, );
            print PrintStr;

# 样例文件入口
if __name__ == "__main__":
    s = get_session()

    # 设置链接基本参数
    client = s.create_client(service_name="kkms",
        region_name = "cn-beijing-6",
        use_ssl=False,
        ks_access_key_id = "Your AK",
        ks_secret_access_key="Your SK"
    );r
    
    # 参数配置方法
    # client.[接口]([参数])
    # 如创建kms 的主Key 需要参数 
    #   { 
    #       "KeyUsage" : "EncryptDecrypt",
    #       "Origin"   : "kms",
    #       "KeyName"  : "NoName"
    #   }
    # 则调用
    # client.create_key(KeyUsage = "EncryptDecrypt",Origin = "kms",KeyName = "NoName");
    # 参数错误，将抛出异常，请查看对应的异常信息，获取正确的参数使用方法
    # 也可以参照KMS文档，来设定具体的参数
    
    
    try:
        # 查询 kms 的主Key列表
        printObj( client.describe_keys() );
        # 创建kms 的主Key
        printObj( client.create_key() );
        # 修改kms 的主Key
        printObj( client.modify_key() );
        # 修改kms 的主Key状态
        printObj( client.modify_key_state() );
        # 删除kms 的主Key
        printObj( client.delete_key() );
        # 加密
        printObj( client.encrypt() );
        # 解密
        printObj( client.decrypt() );
        # 生成数据密钥
        printObj( client.generate_data_key());
    except BaseException as e:
        print e.message;
    
    # 实际调用时，请按照以下方式单独使用 try except 来捕获异常
    '''
    try:
        # 查询 kms 的主Key列表
        printObj( client.describe_keys() );
    except BaseException as e:
        print e.message;
    try:
        # 创建kms 的主Key
        printObj( client.create_key() );
    except BaseException as e:
        print e.message;
    try:
        # 修改kms 的主Key
        printObj( client.modify_key(KeyId = "Your KeyID") );
    except BaseException as e:
        print e.message;
    try:
        # 修改kms 的主Key状态
        printObj( client.modify_key_state(KeyId = "Your KeyID") );
    except BaseException as e:
        print e.message;
    try:
        # 删除kms 的主Key
        printObj( client.delete_key(KeyId = "Your KeyID") );
    except BaseException as e:
        print e.message;
    try:
        # 加密
        printObj( client.encrypt(KeyId = "Your KeyID") );
    except BaseException as e:
        print e.message;
    try:
        # 解密
        printObj( client.decrypt(KeyId = "Your KeyID") );
    except BaseException as e:
        print e.message;
    try:
        # 生成数据密钥
        printObj( client.generate_data_key(KeyId = "Your KeyID"));
    except BaseException as e:
        print e.message;
    '''