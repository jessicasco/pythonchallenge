# coding=utf-8
# Title: can you tell the difference?
# "it is more obvious that what you might think" -> brightness?
# goto: http://www.pythonchallenge.com/pc/return/brightness.html
# "maybe consider deltas.gz" 
import gzip
import difflib

def main():
    data = gzip.GzipFile('deltas.gz').read()
    data = data.splitlines()
    left, right, png = [], [], ['', '', '']
    for line in data:
        left.append(line[:53])
        right.append(line[56:])
    # 调用difflib模块的ndiff比较2个字符串列表，
    # 返回的每行开头为'- '或'+ '或'  '，
    # 分别表示对左唯一还是对右唯一还是两边都包涵。
    diff = list(difflib.ndiff(left, right))
    # print "\n".join(diff)

    for line in diff:
        chrs = [chr(int(byte, 16)) for byte in line[2:].split()]
        if line[0] == '+':
            png[0] += ''.join(chrs)
        elif line[0] == '-':
            png[1] += ''.join(chrs)
        elif line[0] == ' ':
            png[2] += ''.join(chrs)
    for i in range(3):
        open("output%s.png" % i, "wb").write(png[i])
    # 分别是butter, fly, ../hex/bin.html
    # 下一关：http://www.pythonchallenge.com/pc/hex/bin.html butter:fly

if __name__ == '__main__':
    main()
