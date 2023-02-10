# Challenge #1
# Create a Python script that removes all the occurrences of a given element of a list.

# l = [1,2,2,3,2,4,5,2,6]
# n = int(input('Please enter a number to remove from the list: ')
# wile n in l:
#        l.remove(n)

# Challenge 2
# Create a Python script that removes all the elements of a list that are duplicates.

# l1 = [10, 20, 10, 30, 40, 10, 70, 10]
# clean_l1 = []
# for n in l1:
#     if n not in clean_l1:
#         clean_l1.append(n)
# print(clean_l1)

# Challenge 3
# Create a Python script that creates a list of integers from the string.

# nums = '10,20,30,40,50'
# nums_list = nums.split(',')
# nums_int =  [int(n) for n in nums_list]
# print(nums_int)

# Challenge 4
# Write a Python script that finds all numbers that are divisible by 7 but are
# not a multiple of 5, between 1500 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence (CSV) on 
# a single line.

# for n in range(1500, 3201):
#     if n % 7 == 0 and n % 5 != 0:
#         print(n, end=',')

# Challenge 5
# Write a program that prompts the user for a long string containing multiple 
# words separated by whitespaces and prints back the same string with the 
# words in backward order.

# s1 = input('Please enter a string consisting of multiple words: ').split(' ')
# s2 = []
# for word in s1[::-1]:
#     s2.append(word)
# print(s2)

# Challenge 6
# Write a Python program that accepts a hyphen-separated sequence of words as 
# input and prints the words in a hyphen-separated sequence after sorting 
# them alphabetically.

# s1 = input('Please enter a string consisting of multiple words divided by hyphens: ').split('-')
# s1.sort()
# s2 = '-'.join(s1)
# print(s2)

# Challenge 7
# Write a Python program that accepts as input a sequence of words 
# separated by whitespaces and prints out the same words with the letters 
# in reversed order. Do not use list comprehension.

# s1 = input('Please enter a string consisting of multiple words: ').split(' ')
# s2 = []
# for word in s1:
#     tmp = ''
#     for letter in word[::-1]:
#         tmp += letter
#     s2.append(tmp)
# print(' '.join(s2))

# Challenge 8
# Create an alternative solution for the previous challenge using list comprehension.

# s1 = input('Please enter a string consisting of multiple words: ').split(' ')
# s2 = [letter[::-1] for letter in s1]
# print(s2)

# Challenge 9
# Create a Python script that calculates and displays the number of 
# occurrences of each element of a list.

# sample_list = list('mamma mia mm')
# elements = []
# for letter in sample_list:
#     if letter not in elements:
#         elements.append(letter)
# for letter in elements:
#     print(f'{letter} ---> {sample_list.count(letter)}')

# Challenge 10
# Consider a list of words(strings). Write a Python script that generates a 
# list of tuples where the first element of the tuple is the word in the list 
# and the second element is its length.

# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# res = []
# for word in words:
#     res.append((word, len(word)))
# print(res)
