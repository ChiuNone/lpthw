#函数与文件组合
from sys import argv

script, input_file = argv

def print_all(f):
    print('>>> print_all f:', f)
    print(f.read())
    print('>>> f:', f)
def rewind(f):
    f.seek(0)

def print_line(count_line, f):
    print('>>> f:', f)
    print(count_line, f.readline())
    print('>>> f:', f)

current_file = open(input_file)

print('First we print the whole file:')
print_all(current_file)

print('Let\'s rewind, kind of like a tape.')
rewind(current_file)

print('Then, we print three line in this file:')
count_line = 1
print_line(count_line, current_file)

count_line += 1
print_line(count_line, current_file)

count_line += 1
print_line(count_line, current_file)
