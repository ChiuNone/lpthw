#.format()
formatter = '{} {} {} {}'

#格式化数字，加减.format()里的元素不会引发异常
print(formatter.format(1, 2, 3, 4, 5))

#格式化字符串，加减只会打印出对应formatter的元素个数
print(formatter.format('one', 'two', 'three', 'four', 'five'))

#格式化自身
print(formatter.format(formatter, formatter, formatter, formatter))

#格式化其他数据
print(formatter.format(True, False, True, TabError))

#格式化长字符串
print(formatter.format(
    'Try your',
    'Own text here',
    'Maybe a poem',
    'Or a song about fear',
))
#长字符串赋值给变量，导入变量
lines = (
    'Try your',
    'Own text here',
    'Maybe a poem',
    'Or a song about fear',
)
print('>>>lines', repr(lines))
# *变量名(魔法)，解压可迭代序列中的每个元素赋值给变量名
print(formatter.format(*lines))