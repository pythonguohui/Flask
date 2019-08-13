# def getcontent():
#     while True:
#         url= yield "I have url"
#         print("url from content:%s"%url)
#
# def content(g):
#     url_list=["url1","url2","url3","url4","url5",]
#     for i in url_list:
#         g.send(i)
#         print("+++++++++++++++")
#
# if __name__ == '__main__':
#     g = getcontent()
#     print(next(g))
#     content(g)


# def hello():
#     for i in (1,10,23):
#         key=yield i
#         print(key)
#         print("hello word")
#
# h=hello()
# print(next(h))
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print(h.send(3))
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print(h.send(66))

import gevent
from gevent.lock import Semaphore

sem=Semaphore(1)

def fun1():
    for i in range(5):
        sem.acquire()
        print(i)
        sem.release()

def fun2():
    for i in range(5):
        sem.acquire()
        print(i)
        sem.release()

t1=gevent.spawn(fun1)
t2=gevent.spawn(fun2)

gevent.joinall([t1,t2])