# coding=utf-8
# Title: odd even
import Image
def main():
    im = Image.open("cave.jpg")

    w = im.size[0]
    h = im.size[1]

    odd = Image.new(im.mode, (w, h))
    even = Image.new(im.mode, (w, h))

    for i in range(w):
        for j in range(h):
            pixel = im.getpixel((i, j))
            if i%2 == 0 and j%2 == 0:
                even.putpixel((i, j), pixel)
            elif i%2 == 1 and j%2 == 1:
                even.putpixel((i, j), pixel)
            elif i%2 == 0 and j%2 == 1:
                odd.putpixel((i, j), pixel)
            else:
                odd.putpixel((i, j), pixel)

    odd.save(open("odd.jpg", "w"))
    even.save(open("even.jpg", "w"))
    # even.jpg中看的evil。。。
    # 下一关：http://www.pythonchallenge.com/pc/return/evil.html

if __name__ == '__main__':
    main()
