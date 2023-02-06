# Challenge 1

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

ipv6 = my_str.split()[-1]
print(ipv6)

ipv6 = my_str[-17:]
print(ipv6)

# Challenge 2

print("It displayed: \"You've got an error!\"\n\\n means a new line.\n\\ is known as the escape character.")

# Challenge 3

# foot = input("Please enter the value in ft: ")
# print(f'{foot} foot = {int(foot) * 30.48:.2f} centimeters')

# Challenge 4

# string = input("Please enter a word: ")
# palindrome = string == string[::-1]
# print(f'{string} is a palindrome: {palindrome}')

# Challenge 5

# string = input("Please enter a word: ").lower().strip()
# print(string)
# palindrome = string == string[::-1]
# print(f'{string.strip()} is a palindrome (ignoring leading and trailing white spaces, letter case): {palindrome}')

# Challenge 6

exampleString = "I am a string"
res = exampleString[0] + exampleString[-2:]
print(res)

# Challenge 7

exampleString = "exampleString"
res = exampleString[0] + exampleString[1:].replace(exampleString[0], '$')
print(res)

# Challenge 8

# n = input("Please enter an index: ")
# exampleString = "I am a string"
# res = exampleString[:int(n)] + exampleString[int(n)+1:]
# print(res)

# Challenge 9

# exampleString = input("Please enter a string: ")
# res = exampleString[::2]
# print(res)

# Challenge 10

# radius = input("Please enter a radius: ")
# print(f'A circle with the radius {radius} has an area of {3.1415 * float(radius) ** 2:.4f}')

# Challenge 11

# exampleString = input("Please enter a string: ").lower()
# count = exampleString.count("e")
# print(f'The given string has {count} occurrences of the letter e')

# Challenge 12

sample = input("Please enter a digit: ")
sample_comma = f'{int(sample):,}'
print(f"EU Format: '{sample_comma}', US Format: '{sample_comma.replace(',', '.')}'")