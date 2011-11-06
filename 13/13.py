# coding=utf-8
# Title: call him
# "phone that evil"
# 12/evil4.jpg: Bert is evil! go back!
import xmlrpclib
import httplib

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

def main():
    #p = ProxiedTransport()
    #p.set_proxy('127.0.0.1:8000') # Gapproxy
    #server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php", transport=p)

    server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")

    print server.system.listMethods()   # 发现有phone方法
    print "#" * 20
    print server.system.methodSignature('phone')
    print "#" * 20
    print server.system.methodHelp('phone')
    print "#" * 20
    print server.phone('Bert')      # call Bert
    # 555-ITALY
    # 下一关：http://www.pythonchallenge.com/pc/return/italy.html
    print "#" * 20

if __name__ == '__main__':
    main()
