# coding=utf-8
# Title: go away!
import httplib, base64

# GET unreal.jpg(unreal?)的响应头里面
# Content-Range：bytes 0-30202/2123456789
# 看来并不完整，分块下载？应该跟下载工具的断点续传类似吧。。
# 请求头里面将不同的Range(HTTP协议的协议头）发送过去，查看返回的数据
base64_login = base64.encodestring('%s:%s' % ("butter", "fly"))[:-1]
headers = {"Authorization": "Basic %s" % base64_login}
conn = httplib.HTTPConnection("www.pythonchallenge.com")

def func1():
    n = 30203
    while True:
        headers["Range"] = "bytes=%s-%s" % (n, n + 1)
        conn.request("GET", "/pc/hex/unreal.jpg", "", headers)
        response = conn.getresponse()
        data = response.read()
        if data:
            print response.getheader('content-range')
            print data
            n = int(response.getheader('content-range').split('/')[0].split('-')[-1])
        n += 1
    """
    bytes 30203-30236/2123456789
    Why don't you respect my privacy?

    bytes 30237-30283/2123456789
    we can go on in this way for really long time.

    bytes 30284-30294/2123456789
    stop this!

    bytes 30295-30312/2123456789
    invader! invader!

    bytes 30313-30346/2123456789
    ok, invader. you are inside now.
    """
    # 后面很长一段时间没有结果。
    # 打开http://www.pythonchallenge.com/pc/hex/invader.html--"Yes! that's you!"
    # 获得新的nickname: "invader"，后面有用
    
    # 由'we can go on in this way for really long time.'尝试反着进行

def func2():
    n = 2123456788
    while True:
        headers["Range"] = "bytes=%s-%s" % (n, n + 1)
        conn.request("GET", "/pc/hex/unreal.jpg", "", headers)
        response = conn.getresponse()
        data = response.read()
        if data:
            print response.getheader('content-range')
            print data
            n = int(response.getheader('content-range').split('/')[0].split()[1].split('-')[0])
        n -= 1
        """
        bytes 2123456744-2123456788/2123456789
        esrever ni emankcin wen ruoy si drowssap eht
        """
        # 倒过来就是: "the password is your new nickname in reverse
        # 所以密码是; 'invader' --> 'redavni'
        """
        bytes 2123456712-2123456743/2123456789
        and it is hiding at 1152983631.
        """
        # 好，下一步在1152983631出寻找

def func3():
    n = 1152983631
    headers["Range"] = "bytes=%s-%s" % (n, n + 1)
    conn.request("GET", "/pc/hex/unreal.jpg", "", headers)
    response = conn.getresponse()
    data = response.read()
    print response.getheader('content-range')
    """
    bytes 1152983631-1153223363/2123456789
    """
    # print data  # PK开头，是zip格式的，
    h = open("20.zip", "wb")
    h.write(data)
    h.close()
    # 解压得到的readme.txt里 "Yes! This is really level 21 in here.
    # 本关结束

if __name__ == '__main__':
    #func1()
    #func2()
    func3()

