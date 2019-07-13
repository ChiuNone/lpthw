#打开文本文件，函数open()
from sys import argv

#输入>>>argv>>>变量
script, filename = argv

#打开文件，函数open()在需要时打开文件，不需要时使用方法.close()关闭
#with open()自动关闭文件，不用方法.close()
txt = open(filename)

print(f'Here are your file {filename}:')
print(txt.read())

print('Type the filename again:')
#input可以当作文件
filename_again = input('> ')
txt_again = open(filename_again)

print(txt_again.read())