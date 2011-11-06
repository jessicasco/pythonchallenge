# coding=utf-8
# Title: whom?
import calendar
# 图片显示January，看到February有29天，年份为1XX6

def main():
    output = []
    for i in range(1006, 2006, 10):
        if calendar.weekday(i, 1, 26) == 0 and i%4 == 0:
            output.append(i)
    print output
    
    # "he ain't the youngest, he is the second"
    print "The second: ", output[-2]
    # 1756年
    # "todo: buy flowers for tomorrow"
    # 明天是指1756年的1月27日，这天发生了什么重大事呢？标题是whom，跟谁有关呢？Google了下，原来是mozart。
    # 下一关：http://www.pythonchallenge.com/pc/return/mozart.html

if __name__ == '__main__':
    main()
