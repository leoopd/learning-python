import math

# Challenge 1
num = 5
num_f = 5.5
is_true = True
is_string = 'string'
is_list = [1,2,3]

print(num)
print(num_f)
print(is_true)
print(is_string)
print(is_list)

# Challenge 2
# Change this script so that it follows the Python naming and style conventions described in PEP8.

my_name = 'Andrei'
value = 100


# This is 
# an example of a multiline
# comment in Python.


greeting = 'Hello'
print(greeting)

# Challenge 3
# This script contains some syntax errors.
# Modify the script so that it runs without any errors.

best_friend = 'Anne'
print('My best friend is', best_friend)

age = 18
print(age == 10)

a, b = '10', '20'
print(a + b)

#print('To comment a line of code you # at the beginning of the line.'#)

# Challenge 4

a = 5
b = 7 
c = 9
d = 11

a = b

print(a == b)
print(a >= b)
print(a * c)
print(c ** d)
print(d // a)
print(b / c)
print(a%c)
b += d
print(b)
b *= b
print(b)

# Challenge 5

a = (16 / (2 + 6) / 2) ** 2
print(a)

# Challenge 6

a = 2 ** 128
print('There are', a, 'IPv6 addresses in the world')

# Challenge 7

revenue = 45_897_513
margin = 0.127
profit = revenue * margin
print(round(profit, 2))

# Challenge 8

a = 0.1
b = 0.3
print(math.isclose(a * 3, b, abs_tol=0.01))

# Done