# Challenge 1
# Create a Python script that asks the user for a number and then prints out a
# list of all the divisors of each number less than the asked number.

# number = int(input('Please enter a number: '))
# all_divisors = list()
# for i in range(2, number//2+1):
#     if number % i == 0:
#         all_divisors.append(i)

# print(all_divisors)

# Challenge 2
# Write a Python program to check if an integer (x) is the power of another 
# integer (y). Prompt the user to input both integers.

# sum = int(input('Please enter the total sum: '))
# x = int(input('Please enter the number to check: '))
# n = 0
# while x ** n < sum+1:
#     if x ** n == sum:
#         print(f'The integer we are looking for is {n}')
#         break
#     n += 1
# else:
#     print(f'No integer found')

# Challenge 3
# Write a Python program that counts and displays the vowels of a given 
# string ignoring the letter case.

# given_string = input('Please enter a string: ')
# vowels = 'aeiouAEIOU'
# ctr = 0
# for letter in given_string:
#     if letter in vowels:
#         ctr += 1
# print(ctr)

# Challenge 4
# Write a Python script that checks if a triangle is equilateral, isosceles or
# scalene.

# 4

# Challenge 5
# Write a Python program that calculates and displays the sum, the product 
# and the average of n float numbers entered by the user, each on a separate 
# line. Enter 0 to finish.

# sum, ctr = 0, 0
# product = 1
# while (x := int(input('Please enter a number or enter 0 to finish: '))) != 0:
#     sum += x
#     product *= x
#     ctr += 1
# print(f'Sum: {sum}, Product: {product}, average: {sum/ctr}')

# Challenge 6
# Given the string s1, write a program to return the sum and the average of 
# the digits that appear in the string, ignoring all other characters.

# given_string = input('Please enter a string: ')
# sum, ctr = 0, 0
# digits = '1234567890'
# for char in given_string:
#     if char in digits:
#         sum += int(char)
#         ctr += 1
# print(f'Sum: {sum}, average: {sum/ctr}')

# Challenge 7
# Write a Python program that displays the multiplication table 
# (from 1 to 10) of a specific integer number entered by the user.

# x = int(input('Please enter a number: '))
# n = 0
# for n in range(1, 11):
#     print(f'{x} x {n} = {x*n}')

# Challenge 8
# Write a Python script that displays the following pattern from 1 to n where 
# n is entered by the user.

# x = int(input('Please enter a number: '))
# n = 0
# for n in range(1, x+1):
#     print(str(n)*n)

# Challenge 9
# Write a Python program that finds the common characters that appear in two 
# given strings.

# string_one = input('Please enter the first string: ')
# string_two = input('Please enter the second string: ')

# for letter in string_one:
#     if letter in string_two:
#         print(letter)

# Challenge 10
# Write a Python program that iterates over the integers from 1 to 50.
# For multiples of three print "Foo" instead of the number and for multiples 
# of five print "Bar".
# For numbers that are multiples of both three and five print "FooBar".

# n = 0
# for n in range(1, 50):
#     if n % 3 == 0 and n % 5 == 0:
#         print('FooBar')
#     elif n % 3 == 0:
#         print('Foo')
#     elif n % 5 == 0:
#         print('Bar')
#     else:
#         print(n)

# Challenge 11
# Write a Python script that prints out the Fibonacci series up to a given 
# number n.

# n = int(input('Please enter a number: '))
# a, b = 0, 1
# while a <= n:
#     print(a)
#     a, b = b, a + b

# Challenge 12
# Write a Python script that draws the following pattern using for loops.

for _ in range(1, 6):
    print('*' * _)
for _ in range(4, 0, -1):
    print('*' * _)
