# coding=utf-8
# Title: what is this module?

"""
<!--
TODO: do you owe someone an apology? now it is a good time to
tell him that you are sorry. Please show good manners although
it has nothing to do with this level.
-->
"""

"""
<!--    it can't find it. this is an undocumented module. -->
"""
def main():
    def rotate_right_by_n(s, n):
        d = {}
        for c in (ord('A'), ord('a')):
            for i in range(26):
                d[chr(i+c)] = chr((i+n) % 26 + c)
        return "".join([d.get(c, c) for c in s])

    import string
    trans = string.maketrans(string.ascii_letters, rotate_right_by_n(string.ascii_letters, 13)) 
    # 尝试其他都不行，13刚好是this.py的向右偏移量

    s = "va gur snpr bs jung?"
    print s.translate(trans)
    # 打印出：in the face of what?
    # import this: In the face of ambiguity, refuse the temptation to guess.
    # 答案就是ambiguity
    # 下一关:http://www.pythonchallenge.com/pc/hex/ambiguity.html

if __name__ == '__main__':
    main()

    """
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    """
