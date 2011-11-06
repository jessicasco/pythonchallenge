# coding=utf-8
# Title: what are you looking at?

def main():
    a = [1, 11, 21, 1211, 111221]

    for i in range(5, 31):
        pre = str(a[i-1])
        prelen = len(pre)
        l = 0
        nex = ""
        while l <= prelen-1:
            m = l + 1
            while m <= prelen-1:
                if pre[m] != pre[l]:
                    break
                m += 1
            nex += str(m-l) + pre[l]
            l = m
        a.append(int(nex))
    print len(str(a[30]))
    # 5808
    # 下一关：http://www.pythonchallenge.com/pc/return/5808.html

if __name__ == '__main__':
    main()  
