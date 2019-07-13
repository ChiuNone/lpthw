#用组合的方式写函数
#cheese_count和boxes_of_crackers是形参
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print('>>> cheese_count=',cheese_count, 'boxes_of_crackers=', boxes_of_crackers)
    print(f'You have {cheese_count} cheeses!')
    print(f'You have {boxes_of_crackers} boxes of crackers!')
    print('Man that\'s enough for a party!')
    print('Get a blanket.')
    print('>>> This function is over.\n')

#传递实参,调用函数
print('We can just give the function numbers directly:')
cheese_and_crackers(15, 20)

print('Or we can use variables from our script:')
amount_of_cheese = 20
amount_of_crackers = 45
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print('Also we can even do math inside too:')
cheese_and_crackers(30 - 10, 5 + 20)

print('We can combine the two, variables and math:')
cheese_and_crackers(amount_of_cheese + 6, amount_of_crackers - 7)