# coding=utf-8
# Title: let me get this straight
import Image, ImageChops

def main():
    im = Image.open("mozart.gif")
    print im.mode, im.format, im.size
    
    # 用GIMP查看，随便获得一个粉红色点的位置（312,2）
    pixel = im.getpixel((312,2))
    print pixel # 值为195
    
    pink = chr(195)

    for y in range(im.size[1]):
        box = (0, y, im.size[0], y+1)   #截取一小行的区域位置
        row = im.crop(box)      #截取图片内容
        rowstring = row.tostring()  #转化成字符串
        offset = rowstring.index(pink)  #获得第一个粉红点像素的偏移量
        row = ImageChops.offset(row, -offset, 0) #向左移
        im.paste(row, box)      #粘贴到原区域
    im.save("output.gif")
    # 图上看出romance
    # 下一关：http://www.pythonchallenge.com/pc/return/romance.html

if __name__ == '__main__':
    main()
