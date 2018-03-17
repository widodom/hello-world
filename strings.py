
name = input('enter your name: ')
age = input('enter your age: ')

print('My name is %s and I am %s years old' % (name, age))
print('My name is {} and I am {} years old'.format(name, age))
print('My name is {name} and I am {age} years old'.format(age=99, name='Ryan'))

# This last one is more fancy than most people use
my_info = {
    'name': 'Ryan',
    'age': 99,
    'favorite_color': 'red'
}
print('My name is {name} and I am {age} years old'.format(**my_info))

# Naming conventions:
snake_case = 'is the normal python standard'
camelCase = 'is more typical in Java or C#'
