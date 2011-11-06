# coding=utf-8
# Title: re

def main():
    import re
    pattern = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
    match = pattern.findall(open("03.txt").read())
    print "".join(match)
    # 打印：linkedlist
    # 下一关：http://www.pythonchallenge.com/pc/def/linkedlist.html
    # 显示内容：linkedlist.php
    # 更改网址变为：http://www.pythonchallenge.com/pc/def/linkedlist.php

if __name__ == '__main__':
    main()
