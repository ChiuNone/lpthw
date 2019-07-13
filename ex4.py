#变量和命名：驼峰命名法
#命名不能以数字开头，字符之间不能有空格，可以加下划线
cars = 88
sapce_in_a_car = 5.0
drivers = 33
passengers = 40
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * sapce_in_a_car
avg_passengers_per_car = passengers / cars_driven

#使用变量
print('There are', cars, 'cars available.')
print('There are only', drivers, 'drivers available.')
print('We will be', cars_not_driven, 'empty cars today.')
print('We can transport', carpool_capacity, 'people today.')
print('We have', passengers, 'to carpool today.')
print('We need to put about', avg_passengers_per_car, 'in each car.')