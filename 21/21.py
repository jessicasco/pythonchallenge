# coding=utf-8
import zlib, bz2

def main():
    data = open(r'21.pack', 'rb').read()
    result = ""
    # print data
    while True:
        if data.startswith('x\x9c'):
            data = zlib.decompress(data)
            result += ' '
        elif data.startswith('BZh'):
            data = bz2.decompress(data)
            result += '#'
        elif data.endswith('\x9cx'):
            data = data[::-1]
            result += '\n'
        else:
            print 'data:', data
            # 'sgol ruoy ta kool' ---> 'look at your logs'
            # 用result记录log。
            print 'result:'
            print result
            # copper
            # 下一关：http://www.pythonchallenge.com/pc/hex/copper.html
            break

if __name__ == '__main__':
    main()
