#for循环和列表
the_numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pear', 'apricot']
change =  [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_numbers:
    print(f'This is count {number}')

for fruit in fruits:
    print(f'A fruit of type: {fruit}')

for i in change:
    print(f'I got {i}')

elements = []

for i in range(0,6):
    print(f'Adding {i} to the list.')
    elements.append(i)
#在循环外打印i的值，显示的是列表最后的值
print('>>> i=', i)

for element in elements:
    print(f'Element was: {element}')
