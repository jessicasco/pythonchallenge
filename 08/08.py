# coding=utf-8
# Title: working hard?
import bz2

def main():
    un = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
    pw = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

    print bz2.decompress(un)    # huge
    print bz2.decompress(pw)    # file
    # 点击图片，输入用户名和密码
    # 下一关：http://www.pythonchallenge.com/pc/return/good.html

if __name__ == '__main__':
    main()
