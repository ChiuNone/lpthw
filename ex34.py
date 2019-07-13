#访问列表元素，索引，切片
#注意：差一错误
animals = ['bear', 'tiger', 'penguin', 'zebra']
bear = animals[0]

two = animals[:2]
print(two)

l1 = animals[1:3:2]
print(l1)

print(animals[-0])
print(animals[-1])

word = 'hello how are you this day?'
words = word.split()

word_3 = word.split()[2]

print(words)
print(word_3)