# coding=utf-8
# Title: smarty

import Image
def main():
    im = Image.open("oxygen.png")
    print im.mode           # RGBA
    box = (0, 43, 608, 52)  
    # 用GIMP获得灰度条的区域位置,每条灰色带的宽为7个像素，高为9个像素（9 = 52-43）
    belt = im.crop(box)     # 截图灰度条
    pixels = belt.getdata()     
    # 获得像素数据,打印发现对于每个像素RGB值相等，
    # A值都为255,不同的灰色带的R（GB）值不一样。

    # 尝试将各个灰色带的颜色值转化为字符
    data = [chr(pixels[i][0]) for i in range(0, len(pixels)/9, 7)]
    print ''.join(data)
    # smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
    # 网页title的smarty原来出自这里

    print "Next level: "
    level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    level = [chr(x) for x in level]
    print "".join(level)
    # 打印integrity
    # 下一关：http://www.pythonchallenge.com/pc/def/integrity.html

if __name__ == '__main__':
    main()
