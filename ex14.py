#组合运用
#input内可以加如相关提示信息
from sys import argv

#输入>>>argv>>>变量
script, user_name = argv

print(f'Hi {user_name}, I am the {script} script.')
print('I\'d like to ask you some questions.')

print(f'Do you like me, {user_name}?')
answer_1 = input('> ')

print(f'Where do you live, {user_name}?')
answer_2 = input('> ')

print('How old are you?')
age = int(input('> '))

print(f'Well,you are {age} old, and what kind of computer do you use?')
answer_3 = input('> ')

print(f'''
Alright, you said {answer_1} about liking me.
You live {answer_2}, Not sure where is.
And you have a {answer_3} computer, nice!
''')