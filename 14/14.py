# coding=utf-8
# Title: walk around
import Image

def main():
    im = Image.open("wire.png")

    print im.size # (10000, 1) 刚好是100×100

    output = Image.new(im.mode, (100, 100))
    
    # 100*100 = (100+99+99+98) + (...
    # 100*100 = 100 + (99+98+...+1)*2
    # 按顺时针绕
    for i in range(100):
        pixel = im.getpixel((i,0))
        output.putpixel((i,0), pixel)

    x = 99
    y = 0
    index = 100
    for count in range(99, 0, -1):
        if count % 2:
            for i in range(count):
                y += 1 
                pixel = im.getpixel((index, 0))
                index += 1
                output.putpixel((x, y), pixel)
            for i in range(count):
                x -= 1
                pixel = im.getpixel((index, 0))
                index += 1
                output.putpixel((x, y), pixel)
        else:
            for i in range(count):
                y -= 1
                pixel = im.getpixel((index, 0))
                index += 1
                output.putpixel((x, y), pixel)
            for i in range(count):
                x += 1
                pixel = im.getpixel((index, 0))
                index += 1
                output.putpixel((x, y), pixel)

    output.save(open("output.png", "w"))
    # 显示一只可爱的猫
    # http://www.pythonchallenge.com/pc/return/cat.html
    # "and its name is uzi. you'll hear from him later."..
    # uzi被加粗了。。而且这个网页的图片上没有显示题号。继续把cat改成uzi
    # 下一关：http://www.pythonchallenge.com/pc/return/uzi.html

if __name__ == '__main__':
    main()
