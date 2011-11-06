# coding=utf-8
# Title: peak hell
# "pronounce it"
# "peak hell sounds familiar ?" 
#  peak hell -> pickle

import pickle
def main():
    L = pickle.load(open("banner.p"))
    print L
    # len(L) 值为1,其实load出的结果只有一个list。
    # 观察发现，最底层的子list中的tuple里的数字成员和都为95,根据这个尝试按行打印出内容

    print "\n".join(["".join([a[0] * a[1] for a in l]) for l in L])
    # 观察结果，原来是用空格和#打印出channel这个单词
    # 下一关：http://www.pythonchallenge.com/pc/def/channel.html

if __name__ == '__main__':
    main()
