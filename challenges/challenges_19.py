import string
# import time

# with open('challenges/files/macs.txt', 'r') as file:
#     content = file.read().splitlines()
#     unique_macs = set(content)
#     seperated_macs = []
#     for line in unique_macs:
#         seperated_macs.extend(line.split(' '))
    
#     with open('challenges/files/unique_macs.txt', 'w') as f:
#         for mac in seperated_macs:
#             f.write(mac + '\n')


# Challenge #2
# Create a Python script that reads a text file into a list and then converts 
# the list into a string that has the entire file content.

# with open('challenges/files/textfile1.txt') as file:
#     content = file.read().splitlines()
#     res = '\n'.join(content)

# Challenge #3
# Create a Python script that removes all empty lines including those that 
# contain only spaces from a file.

# with open('challenges/files/textfile1.txt') as file:
#     content = file.read().splitlines()
#     with open('challenges/files/texfile1_clean.txt', 'w') as output:
#         for line in content:
#             if len(line.strip()) == 0:               
#                 continue
#             output.write(line+'\n')

# Challenge #4
# Create a Python function called tail that reads the last n lines of a text 
# file. The function has two arguments: the file name and n (the number of 
# lines to read). This is similar to the Linux `tail` command.

# def tail (filename, n):
#     with open(filename) as f:
#         content = f.read().splitlines()
#         tail_lines = content[len(content)-n:]
        
#     return '\n'.join(tail_lines)

# path = 'challenges/files/textfile1.txt'
# print(tail(path, 5))

# Challenge #5
# Change the solution from the previous challenge so that the script that 
# prints out the last n lines of the file refreshes the output every 3 seconds
# (as the file changes or updates). This is similar to the tail -f Linux command.

# def tail (filename, n):
#     with open(filename) as f:
#         content = f.read().splitlines()
#         tail_lines = content[len(content)-n:]
        
#     return '\n'.join(tail_lines)

# path = 'challenges/files/textfile1.txt'
# print(tail(path, 5))

# while True:
#     t = tail('challenges/files/textfile1.txt', 3)
#     print(t)
#     time.sleep(3)
#     print('')

# Challenge #6
# Write a Python program to count the number of lines, words, and characters 
# in a text file. This is similar to the Linux `wc` command. Create a 
# function, if possible.

# def lengths(path):
#     with open(path) as file:
#         chars = len(file.read())
#         file.seek(0)
#         lines = len(file.read().splitlines())
#         file.seek(0)
#         words = len(file.read().split())
#     return lines, words, chars

# print(lengths('challenges/files/textfile1.txt'))

# Challenge #7
# Write a Python program that calculates the net amount of a bank account 
# based on the transactions that are saved in a text file.

# def balance(path):
#     deposited = 0
#     withdrawn = 0
#     with open(path) as file:
#         content = file.read().splitlines()
#         for line in content:
#             if line[0] == 'D':
#                 deposited += int(line[2:])
#             else:
#                 withdrawn += int(line[2:])
#     return deposited - withdrawn

# print(balance('challenges/files/transactions.txt'))

# Challenge #8
# Write a Python script that compares line by line two text files and displays
# the lines that differ.

# def comparing(path1, path2):
#     with open(path1) as file1:
#         with open(path2) as file2:
#             content1 = set(file1.read().splitlines())
#             content2 = set(file2.read().splitlines())
#     return content1.symmetric_difference(content2)

# print(comparing('challenges/files/textfile1.txt', 'challenges/files/textfile2.txt'))

# Challenge #9
# Write a Python script that reads the file in a dictionary. The words in the 
# file will be the dictionary keys and the length of each word the 
# corresponding values.

# def dict_maker(path):
#     with open(path) as f:
#         content = f.read().splitlines()
#         result = {key: len(key) for key in content}
#         return result
    
# print(dict_maker('python/challenges/files/dict1.txt'))

# Challenge #10
# Write a Python script that finds the first 100 longest words in the file.

# def word_finder(path):
#     '''Finds the 100 largest words in the file specified.'''
#     tmp = dict_maker(path)
#     tmp2 = sorted(tmp.items(), key=lambda x:x[1])
#     result = []
#     for i in range(-1, -102, -1):
#         result.append(tmp2[i])
#     return result

# print(word_finder('python/challenges/files/dict1.txt'))

# Challenge #11
# Write a Python script that finds the number of occurrences of each letter of 
# the alphabet in all the words of the dictionary. Make a distinction between 
# lower and uppercase letters.
# You want to see how many times 'a', 'A', 'b', 'B', 'c', 'C', 'd' and so on 
# appear in all the words in the dictionary.
# Which is the most frequently used letter in English words? But the least 
# frequently used one?

# def counting_chars(path):
#     with open(path) as f:
#         content = f.read()
#         result_dict = {}
#         for char in string.ascii_letters:
#             result_dict[char] = content.count(char)
#         sorted_result = sorted(result_dict.items(), key=lambda x:x[1])
#         return sorted_result
    
# print(counting_chars('python/challenges/files/dict1.txt'))

# Challenge #12
# Change the solution from the previous challenge so that the script considers 
# all letters lowercase (it makes no distinction between lower and uppercase 
# letters).

# def counting_chars(path):
#     with open(path) as f:
#         content = f.read()
#         result_dict = {}
#         for char in string.ascii_lowercase:
#             result_dict[char] = content.lower().count(char)
#         sorted_result = sorted(result_dict.items(), key=lambda x:x[1])
#         return sorted_result
    
# print(counting_chars('python/challenges/files/dict1.txt'))

# Challenge #13
# Continue the previous challenge and find the 3 most frequently used letters 
# in all English Words.
# You should get: ('e', 67681), ('s', 50872), ('i', 50818)

def counting_chars(path):
    with open(path) as f:
        content = f.read()
        result_dict = {}
        for char in string.ascii_letters:
            result_dict[char] = content.count(char)
        sorted_result = sorted(result_dict.items(), key=lambda x:x[1])
        return sorted_result[-1], sorted_result[-2], sorted_result[-3]
    
print(counting_chars('python/challenges/files/dict1.txt'))
