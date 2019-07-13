#练习
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = '''
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explannation
\n\twhere there is none.
'''

print('--------------------')
print(poem)
print('--------------------')

#格式化
five = 10 - 2 + 3 - 6
print(f'This should be five:{five}')

print('With a starting point of:{}'.format(10000))

#函数
def secret_fornumla(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 100000
beans, jars, crates = secret_fornumla(start_point)
print(f'We have {beans} beans, {jars} jars, and {crates} crates.')

start_point = start_point / 50
second_points = secret_fornumla(start_point)
print('>>>> second_points=', second_points)