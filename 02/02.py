# coding=utf-8
# Title: ocr
# The meaning may be: Optical Character Recognition

def main():
    print "".join(filter(lambda x: x.isalpha(), open("02.txt").read()))
    # 打印：equality
    # 下一关：http://www.pythonchallenge.com/pc/def/equality.html

if __name__ == "__main__":
    main()
