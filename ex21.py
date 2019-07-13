#函数返回
def add(a, b):
    print(f'ADDING {a} + {b}')
    return a + b

def subtract(a, b):
    print(f'SUBTRACT {a} - {b}')
    return a - b

def mult(a, b):
    print(f'MULT {a} * {b}')
    return a * b

def divide(a, b):
    print(f'DIVIDE {a} / {b}')
    return a / b

print('Let\'s do some math with just function!')

age = add(25, 10)
apple = subtract(50, 26)
water = mult(10, 6)
sheep = divide(100, 4)

print('We just use these functions do some math, here are results:')
print(f'''
{age}, 
{apple}, 
{water}, 
{sheep}
''')

#函数套用或者说函数嵌套？
#函数互相调用
print('Here is a puzzle.')
what = add(age, mult(apple, subtract(water, divide(sheep, 2))))
print('>>> what=', what)