#字典dict，可爱的字典

#如果要用到顺序，就是用list
#如果用到键对应的值，就用dict

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksnoville',
}

cities['NY'] = 'New York'
cities['OR'] = 'Portlan'

print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

print('-' * 10)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])

print('-' * 10)
print('Michigan has:', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

print('-' * 10)
for state, abbrev in states.items():
    print(f'{state} is abbreviated {abbrev}.')

print('-' * 10)
for abbrev, city in cities.items():
    print('%s has the city %s.' % (abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
    print(f'{state} state is abbreviated {abbrev} and has city {cities[abbrev]}.')

#字典中get()的用法，接受两个参数：(key，word)，在字典中寻找key，若无key则返回word
print('-' * 10)
state = states.get('Texas')

if not state:
    print('Soory, no Texas.')

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is {city}")