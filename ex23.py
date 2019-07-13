#自然语言：每个国家都有自己的语言，例如英语，日语，中文，西班牙语...
#计算机语言:二进制语言，0和1，只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。

#位(bit)：表示以二进制0或1，计算机储存处理信息的最基本单位
#字节(byte)：1个字节由8个位组成
#字(word)：1个字由2个字节即16个位组成

#编码：将自然语言转换成计算机语言。各国有各国的标准，比如：
#美国：ASCII
#日本：Shift_JIS
#韩国：Euc-kr
#中国：GB2312
#在实际中不可避免发生冲突导致乱码
#因而产生了Unicode，Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了

#字母'A'用ASCII编码是十进制的65，二进制的01000001；
#字符'0'用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；
#汉字'中'已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101
#如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001，
#如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算

#因而又出现了把Unicode编码转化为“可变长编码”的UTF-8编码
#UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，
#只有很生僻的字符才会被编码成4-6个字节

#Python的字符串
#在pythohn3中字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
z = ord('中')
print(" >>> ord('中')=", repr(z))

b = ord('B')
print(">>> ord('B')=", repr(b))

print(">>> chr(66)=", chr(66))
print(">>> chr(25991)=", chr(25991))

#对于字符串(多个字符)，在内存中以Unicode表示，一个字符对应若干个字节
#如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
#Python对bytes类型的数据用带b前缀的单引号或双引号表示
#转换：encode(编码格式)>>>bytes，decode(编码格式)>>>str

#以Unicode表示的str通过encode()方法可以编码为utf-8的bytes
#反过来就是用方法decode()将utf-8的bytes变为str
bytes_1 = '我爱你'.encode()
print(" >>> 'abc'>", bytes_1)

str_1 = b'\xe4\xb8\xad\xe6\x96\x87'.decode()
print(" >>> \xe4\xb8\xad\xe6\x96\x87 >", str_1)

s = 'python-中文'
print(s)
print(s.encode())

#写一个函数，读取文件，编码解码
from sys import argv

script, language_file, input_encoding, errors = argv

def main(file, encoding, errors):
    for line in language_file.readlines():
        line = line.strip()
        raw_bytes = line.encode(encoding, errors = errors)
        cooked_string = raw_bytes.decode(encoding, errors =errors)

        print(raw_bytes, '>>>', cooked_string)

languages = open(language_file, encoding = 'utf-8')

main(languages, input_encoding, errors = errors) 

