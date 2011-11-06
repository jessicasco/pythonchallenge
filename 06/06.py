# coding=utf-8
# Title: now there are pairs
import re
import zipfile

def main():
    # channel.zip -> readme.txt
    """
    welcome to my zipped list.

    hint1: start from 90052
    hint2: answer is inside the zip
    """

    nothing = "90052"
    z = zipfile.ZipFile("channel.zip")
    comments = ""

    i = 0
    while True:
        f = z.open(nothing + ".txt")
        old_nothing = nothing
        comments += z.getinfo(nothing + ".txt").comment
        for line in f:
            print "index: ", i, " ", line
            m = re.search("Next nothing is ([0-9]*)", line)
            if m != None:
                nothing = m.groups()[0]
                print "Next nothing is: ", nothing
                print
        i += 1
        if old_nothing == nothing:
            break
    print comments
    """
    index:  908   Collect the comments.
    """

    """
    ****************************************************************
    ****************************************************************
    **                                                            **
    **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
    **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
    **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
    **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
    **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
    **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
    **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
    **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
    **                                                            **
    ****************************************************************
     **************************************************************
    """
    # 下一关:http://www.pythonchallenge.com/pc/def/hockey.html ?
    # No! "it's in the air. look at the letters."
    # So, next level is: http://www.pythonchallenge.com/pc/def/oxygen.html

if __name__ == '__main__':
    main()
