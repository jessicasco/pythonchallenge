# coding=utf-8
# Title: eat?
# 图片是饼干，cookie？跟cookie值有关
import urllib
import urllib2
import re
import bz2
import xmlrpclib
import httplib

def func1():
    # 回到问题4，查看headers，
    # Cookie内容为：info=you+should+have+followed+busynothing...
    # Gapproxy, 使用Gapproxy有时有问题，响应头的Set-Cookie可能获得不到，具体，可能缓存的缘故吧,运行到f.info().getheaders('set-cookie')[0]时会出现问题
    # print f.info() 会看到x-google-cache-control的值为remote-cache-hit
    # 而一般情况下会是remote-fetch
    # 所以如果使用Gapproxy，则最好隔长一点时间，（时间不会太长，10分钟左右吧）运行脚本，否则。。。
    # 最好不使用Gapproxy，直接访问，不会出现问题。
    # 具体原因，Gapproxy做了相关的缓存吧。。还得多学点东西才能明白吧。
    # proxies = {'http':'http://127.0.0.1:8000'}
    proxies = None
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
    busynothing="12345"
    # cookie info
    info = ""
    index = 0

    while True:
        old_busynothing = busynothing
        f = urllib.urlopen(url + busynothing, proxies=proxies)
        print f.info()
        t = f.info().getheaders('set-cookie')[0]
        info += t.split(';')[0][5:]
        for line in f.readlines():
            print "Page index: ", index, " ", line
            m = re.search("the next busynothing is ([0-9]*)", line)
            if m != None:
                busynothing = m.groups()[0]
                print "next busynothing is: ", busynothing
                break
        if busynothing == old_busynothing:
            break
        index += 1
    print info

def func2():
    info = "BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
    # BZh开头，跟第8关一样，用bz2模块,可是直接解压有错误，查看攻略原来这个info是经过url的quote处理过的，怪不得都是%，而且看上去和第8关很不一样。
    # 试了下urllib.unquote()还是不行，还得用urllib.unquote_plus()
    # 观察发现，urllib.unquote_plus()是先用urllib.unquote()处理，然后将处理后的结果里面的‘+’换成' '。想必urllib.quote_plus()也是先将空格换成'+'，然后用urllib.quote()处理吧。
    info = urllib.unquote_plus(info)
    info = bz2.decompress(info)
    print info
    # 'is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.'
    # 26号，这不是第15关里面日历的日子么？。。his father，那就是mozart的父亲咯Leopold，call his father。。call。。用第13关的方式打电话给Leopold..
    # 'inform him that "the flowers are on their way"...这个不知道怎么做，还是先打电话吧。。

class ProxiedTransport(xmlrpclib.Transport):
    def set_proxy(self, proxy):
        self.proxy = proxy
    def make_connection(self, host):
        self.realhost = host
        h = httplib.HTTP(self.proxy)
        return h
    def send_request(self, connection, handler, request_body):
        connection.putrequest("POST", 'http://%s%s' % (self.realhost, handler))
    def send_host(self, connection, host):
        connection.putheader('Host', self.realhost)

def func3():
    # p = ProxiedTransport()
    # p.set_proxy('127.0.0.1:8000')
    # server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php", transport=p)

    server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

    print server.system.listMethods()
    print '#' * 20
    print server.system.methodSignature('phone')
    print '#' * 20
    print server.system.methodHelp('phone')
    print '#' * 20
    # print server.phone('leopold') 失败
    print server.phone('Leopold')
    # 555-VIOLIN
    # 进入：http://www.pythonchallenge.com/pc/return/violin.html
    # 显示：no! i mean yes! but ../stuff/violin.php
    # 进入：http://www.pythonchallenge.com/pc/stuff/violin.php
    # 看到了leopold.jpg，title是it's me. what do you want?..
    # 是mozart老爸leopold的画像。。
    # 找到了leopold了。。。接下来就是inform him that "the flowers are on their way"
    # 可是怎么inform呢？把这句话放到请求头里去，发送到这个php文件。

def func4():
    # proxy_handler = urllib2.ProxyHandler({'http':'http://127.0.0.1:8000'})
    # opener = urllib2.build_opener(proxy_handler)
    # urllib2.install_opener(opener)
    req = urllib2.Request('http://www.pythonchallenge.com/pc/stuff/violin.php')
    req.add_header('cookie', 'info=' + urllib.quote_plus('the flowers are on their way'))
    print urllib2.urlopen(req).read()
    # 'oh well, don't you dare to forget the balloons.'
    # 访问http://www.pythonchallenge.com/pc/stuff/balloons.html
    # 跳转到http://www.pythonchallenge.com/pc/return/balloons.html
    # 下一关：http://www.pythonchallenge.com/pc/return/balloons.html

def main():
    func1()
    func2()
    func3()
    func4()

if __name__ == '__main__':
    main()

