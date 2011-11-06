# coding=utf-8
# Title: dealing evil

"""
evil1.jpg? so evil2.jpg?
evil2.jpg: not jpg -- .gfx
evil2.gfx
evil3.jpg: no more evils...
evil4.jpg
"""
def main():
    data = open("evil2.gfx", "rb").read()

    for i in range(5):
        open("%d.jpg" % i, "w").write(data[i::5])

    # 5幅图片分别显示dis, pro, port, ional, ity...其中ity用线划去了。。
    # 那答案就是disproportional
    # 下一关：http://www.pythonchallenge.com/pc/return/disproportional.html

if __name__ == '__main__':
    main()
