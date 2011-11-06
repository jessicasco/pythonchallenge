# coding=utf-8
# Title: follow the chain
import urllib
import re

def follow_nothing(nothing):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

    old_nothing = None
    i = 0
    while True:
        f = urllib.urlopen(url + str(nothing))
        for line in f.readlines():
            print "Page index: ", i,  line
            m = re.search("the next nothing is ([0-9]*)", line)
            if m != None:
                nothing = m.groups()[0]
                print "next nothing is: ", nothing
        if nothing == old_nothing:
            break
        old_nothing = nothing
        i += 1

def main():
    follow_nothing(12345)
    # 观察到打印出下面的内容时停下来，92118/2是46059,换个参数给follow_nothing()函数，继续follow the chain

    """
    Page index:  197 and the next nothing is 92118
    next nothing is:  92118
    Page index:  198 Yes. Divide by two and keep going.
    """
    
    print '*'*25
    
    follow_nothing(46059)
    # 观察到打印出下面的内容，下一关网址就是http://www.pythonchallenge.com/pc/def/peak.html

    """
    Page index:  9 and the next nothing is 65667
    next nothing is:  65667
    Page index:  10 peak.html
    """

if __name__ == '__main__':
    main()
