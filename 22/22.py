# coding=utf-8
# Title: emulate
import Image, ImageDraw

def main():
    f = Image.open('white.gif')   # 一幅多帧的gif图
    print f.mode, f.size, f.format
    my = Image.new('RGB', (640, 480))
    draw = ImageDraw.Draw(my)
    curpoint = [50, 50]
    pointlist = [tuple(curpoint)]
    frameno = 0
    d = {
            '98-98' :(-5,-5), '100-98':(0, -5), '102-98' :(5, -5), 
            '98-100':(-5, 0), '100-100':(0, 0), '102-100':(5, 0), 
            '98-102':(-5, 5), '100-102':(0, 5), '102-102':(5, 5)
            }
    while True:
        try:
            for y in range(98, 103, 2):
                for x in range(98, 103, 2):
                    if f.getpixel((x,y)) != 0:  
                    # 打印每帧发现，每帧里面都有调色板索引为8的像素，
                    # 坐标范围为（98,98）-（102,102）
                    # 其坐标为偶数，刚好是3×3的九宫格。。其他的调色板都为0
                        print '%d: %d, %d = %d' % (frameno, x, y, f.getpixel((x, y)))
                        # 网页中的游戏摇杆图片暗示九宫格的点是用矢量方法记录的，可以按照这个画图。
                        k = '%d-%d' % (x, y)
                        if d[k] == (0, 0):
                            print u'回到原点，开始画新字符'
                            if len(pointlist) > 1:
                                draw.line(pointlist)
                                del pointlist[:]
                                # 开始画新字符，向右下方移
                                curpoint[0] += 50
                                curpoint[1] += 50
                                pointlist.append(tuple(curpoint))
                            continue
                        curpoint[0] += d[k][0]
                        curpoint[1] += d[k][1]
                        pointlist.append(tuple(curpoint))
            f.seek(f.tell() + 1)
            frameno += 1
        except EOFError:
            print 'end of frame.'
            draw.line(pointlist)
            my.save(ur'output.png', 'png')
            break
        # 显示: bonus
        # 下一关：http://www.pythonchallenge.com/pc/hex/bonus.html

if __name__ == '__main__':
    main()
