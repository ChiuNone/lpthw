#更多文件操作
from sys import argv
from os.path import exists

#输入>>>argv>>>变量
script, from_file, to_file = argv

print(f'Copying from {from_file} to {to_file}')
#只读打开from_file
in_file = open(from_file)
indate = in_file.read()

print(f'The input file is {len(indate)} bytes long')

#检测是否已经创建copy_file
print(f'Does the output file exist?{exists(to_file)}')
print('Ready, hit RETURN to continue, CTRL-C to abort.')
input()

#没有copy.txt，copy并创建它
out_file = open(to_file, 'w')
out_file.write(indate)

print('Alright, all done.')

#关闭文件
in_file.close()
out_file.close()