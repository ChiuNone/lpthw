#'{}'.format()格式化方法
print('I want to go to {} tonight.'.format('movie'))

#f'{}'格式化
favorite_food = 'chicken'
print(f'{favorite_food} is my favorite food.')

#end=''的用法，以' '结尾，而不是另起一行
a = 's'
b = 'u'
c = 'g'
d = 'a'
e = 'r'
f = 'm'
g = 'e'
h = 'a'
i = 't'

#输出自动换行
print(a + b + c + d + e)
print(f + g + h + i)
#end=' '空格，输出不换行
print(a + b + c + d + e, end=' ')
print(f + g + h + i)

#*号的使用，*另一个重要作用：解压序列
print('chiu' * 6)