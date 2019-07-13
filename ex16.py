#写入文件，截断文件，倒带
from sys import argv

#输入>>>argv>>>变量名filename
script, filename = argv

print(f'We are going to erase {filename}.')
print('If you don\'t want that, hit CTRL-C(^C).')
print('If you do want that, hit RETURN.')

input(' ')

#以写入的方式打开文件。注意：文件若是不存在，将会自动创建
print('Opening the file...')
target = open(filename, 'w')

#截断：移到开始位置，然后擦除所有数据
print('Truncating the file. Goodbye!')
target.truncate()

#请求用户输入3行信息
print('Now I\'m going to ask you for three lines:')
line1 = input('line 1:')
line2 = input('line 2:')
line3 = input('line 3:')

#将三行信息写入文件
print('I\'m going to write these to the file...')
lines = line1 + '\n' + line2 + '\n' + line3
target.write(lines)
print('Done, We write three new lines into the file.')

#关闭文件
print('Finally, We close the file')
target.close()