user_text = int(input('Please enter a number:'))

if user_text <50:
    print('Number too small')
elif user_text <100:
    print('Number in range')
else:
    print('Number too big')

#expressions

#first letter capital in python
a = False
b = True

if(a and b):
    print('hi')

if(a or b):
    print('bye')

if(a == b):
    print('hello')

if(a != b):
    print('x')

c = 4
d = 5

if(c >= d):
    print('bad')

if(c <= d):
    print('good')