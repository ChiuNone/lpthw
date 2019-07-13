#列表的操作
from pprint import pprint

ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print('Wait there are not 10 things in that list. let\'s fix that.')

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Corn', 'Banana', 'Girl', 'Boy', 'Song']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print('Adding: ', next_one)
    stuff.append(next_one)
    pprint(stuff)#美化打印
    print(f'There are {len(stuff)} items now.')

print('There we go:', stuff)

print('Let\'s do some things with stuff.')

print(stuff[-1])
print(stuff[1])
print(stuff.pop())

#join()的设计思路：告诉一个对象使用自己连接列表中所有的元素
#错误写法：stuff.join(' ')
print(' '.join(stuff))
print('#'.join(stuff[2:4]))