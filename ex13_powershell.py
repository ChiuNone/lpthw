from sys import argv

#输入>>>argv>>>变量
#argv可接受很多类型的参数，例如字符串，数字，.txt，.py，.json，.csv等等
#注意这里的
script, first, second = argv
print('>>> argv=', repr(argv))

print('The script is called:', script)
print('Your first variable is:', first)
print('You second variable is:', second)
print('Your third varible is:', third)