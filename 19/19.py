# coding=utf-8
# Title: please!
import urllib
import re
import email
import wave
import array

def main():
    # proxies = {'http':'http://127.0.0.1:8000'}
    proxies = None
    data = urllib.urlopen("http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html", proxies=proxies).read()
    m = re.search(r'<!--\n(.*)-->', data, re.M|re.S)
    mail = email.message_from_string(m.group(1))
    for part in mail.walk():
        if part.get_content_maintype() == 'audio':
            audio = part.get_payload(decode=1)
            open(ur'indian.wav', 'w').write(audio)
    
    # 'sorry'
    # 进入：http://www.pythonchallenge.com/pc/hex/sorry.html
    # '- "what are you apologizing for?"'
    # 此路不通
    # 'Maybe my computer is out of order.'
    # 还有地图上的印度是反的（很难看出来），'inverted India'->'inverted endian'...大小端转换

    wi = wave.open(ur'indian.wav', 'rb')
    wo = wave.open(ur'indian_inv.wav', 'wb')
    wo.setparams(wi.getparams())    # 两个wave文件的参数设成一样的
    a = array.array('i')
    a.fromstring(wi.readframes(wi.getnframes()))
    a.byteswap()    # 两两交换字节，大小端转换
    wo.writeframes(a.tostring())
    wi.close()
    wo.close()
    # 'you are an idiot.aaaaaaa'
    # 进入:http://www.pythonchallenge.com/pc/hex/idiot.html
    # 点击：Continue to the next level
    # 下一关：http://www.pythonchallenge.com/pc/hex/idiot2.html

if __name__ == '__main__':
    main()
