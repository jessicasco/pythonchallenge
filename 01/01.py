#!/usr/bin/env python
# coding=utf-8
# Title: What about making trans?

def main():
    def rotate_right_by_n(s, n):
        d = {}
        for c in (ord('A'), ord('a')):
            for i in range(26):
                d[chr(i+c)] = chr((i+n) % 26 + c)
        return "".join(d.get(c, c) for c in s)

    import string
    trans = string.maketrans(string.ascii_letters, rotate_right_by_n(string.ascii_letters, 2))

    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print s.translate(trans)
    # 打印出：i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
    
    # 继续对url进行处理
    url = "map"
    print url.translate(trans)
    # 打印出：ocr
    # 下一关地址为http://www.pythonchallenge.com/pc/def/ocr.html

if __name__ == '__main__':
    main()

    """
    学习使用了
    string的maketrans(frm, to) -> string
    和
    translate(table [,deletechars]) -> string
    函数，maketrans一般是为了配和translate使用，
    maketrans(frm, to)根据参数frm和to（两者的长度必须相等），
    构造一个ascii字母转化表table（一个256字节长的字符串），
    translate(table [,deletechars])使用转换表table时，
    将原字符串中的每个字符，根据转换表table转换成一个新字符，
    然后将转换成的字符串返回，
    转换的过程应该是：将原字符c，替换为table中ord（c）位置中的字符。
    """

    """
    题中移位的方法很常见，Python著名的"The Zen of Python"(by Time Peters)的
    源文件this.py就是用这种方式编码的，它向右偏移了13个位置，
    函数rotate_right_by_n(s, n）就是根据this.py而来。
    """

    """
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    """
