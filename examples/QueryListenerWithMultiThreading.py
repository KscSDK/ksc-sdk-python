#!/usr/bin/python
#coding=utf-8

import threading
import time
import queue
from kscore.session import get_session
from threading import Lock

'''
当含有大量监听器真实服务器的时候
可以使用这个脚本示例，来规避全量直接查询全量监听器列表过慢的问题
流程：
项目制获取项目->查询负载均衡->并发按照负载均衡ID查询监听器

使用信号量Semaphore做并发量控制
使用queue做多线程排队并发操作
'''

sem = threading.Semaphore(20)
lock = Lock()
results = []

class SlbThread (threading.Thread):
    def __init__(self, lbid, q):
        threading.Thread.__init__(self)
        self.lbid = lbid
        self.q = q

    def run(self):
        try:
            __hasNextPage = True
            __nextToken = 1
            __maxResults = 50
            while __hasNextPage:
                __param = {
                    'NextToken': __nextToken,
                    'MaxResults': __maxResults,
                    'Filter.1.Name': 'load-balancer-id',
                    'Filter.1.Value.1': self.lbid
                }
                __allListeners = slbClient.describe_listeners(**__param)
                '''
                整合每页的获取结果
                '''
                lock.acquire(True)
                try:
                    results.extend(__allListeners['ListenerSet'])
                finally:
                    lock.release()

                if "NextToken" in __allListeners:
                    '''
                    设置下一页
                    '''
                    __nextToken = __allListeners["NextToken"]
                else:
                    '''
                    没有NextToken下自动跳出循环
                    '''
                    __hasNextPage = False
        finally:
            sem.release()
            self.q.task_done()

if __name__ == "__main__":
    s = get_session()
    region = 'cn-shanghai-2'
    slbClient = s.create_client("slb", region, use_ssl=True)
    '''
        获取项目制
    '''
    # IAM
    projects = []
    iam = s.create_client("iam", use_ssl=False)
    resp = iam.get_account_all_project_list()
    for item in resp["ListProjectResult"]["ProjectList"]:
        projects.append(item['ProjectId'])
    _param = {}
    count = 1
    for i in projects:
        key = "ProjectId." + str(count)
        _param.update({key: str(i)})
        count = count + 1
    print(count)
    '''
    获取负载均衡
    '''
    allLbs = slbClient.describe_load_balancers(**_param)
    count = 0
    q = queue.Queue(len(allLbs["LoadBalancerDescriptions"]))
    old = time.time()
    for lb in allLbs["LoadBalancerDescriptions"]:
        q.put(lb["LoadBalancerId"])
    for lb in allLbs["LoadBalancerDescriptions"]:
        lb_id = lb["LoadBalancerId"]
        sem.acquire()
        print(lb_id, q)
        thread = SlbThread(lb_id, q)
        thread.start()
    q.join()
    print(time.time()-old)
    print(len(results))
    # for item in results:
    #    print item['ListenerName']
    #    print item['ListenerId']