#开始函数学习
#星号参数法
def print_two(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')

def print_two_again(arg1, arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')

def print_one(arg1):
    print(f'arg1: {arg1}')

def print_none():
    print('I got nothing.')

print_two('chiu', 'gaozheng')
print_two_again('chiu', 'gz')
print_one('chiu')
print_none()