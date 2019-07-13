#打印字符串：直接使用print('字符串'，变量名)，实际上print()几乎可以打印所用值
my_name = 'chiu'
my_age = 24
my_height = 100
my_weight = 170
my_eye_color = 'black'
my_hair = 'black'

#另一种打印方式：f字符串格式化，print(f'字符串 {变量名}')
print(f"Let's talk aboub {my_name}.")
print(f"He's {my_height}cm. ")
print(f'He is {my_weight}kg.')
print(f'His hair is {my_hair}.')
print(f'His eyes is {my_eye_color}.')

total = my_name + str(my_age) + my_eye_color + my_hair
print(f'If add {my_age}, {my_name}, and {my_height} I get {total}.')