# Challenge #30
# Calculate the number of digits in the total number of IPv6 addresses. 
# Each IPv6 uses 128 bits and the total number of IPv6 is 2 raised to the power of 128.
# Save the number of digits in the total number of IPv6 in a variable called no_of_digits.

no_of_digits = len(str(2**128))
print(no_of_digits)

# Challenge #31
# Consider the following dictionary:  phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}
# Using a single method add the following key:value pairs to the dictionary:  'OS':'Android' and  'Color': 'Black'

phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}
phone.update({'OS':'Android', 'Color': 'Black'})
print(phone)

# Challenge #32
# Consider the following dictionary: phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}
# Your task is to extract the price in a variable called price and calculate the VAT knowing that 
# the VAT percentage is 19%. Use only 2 decimal points for the VAT value.
# The VAT value will be stored in a variable called vat and will be a float.

phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}
price = phone['Price']
price_vat = round(price * .19, 2)
print(f'price: {price}, vat: {price_vat}')

# Challenge #33
# Consider the following list: my_list = [1, 2.3, 'abc', (5, 6, 'x', 'y')]
# Create a variable called my_var that contains the second element of the list as a string ('2.3') 
# concatenated to the first letter of the third element of the list which is 'a' and the last element 
# of the tuple which is the last element of the list.
# my_var should store the string: 2.3ay

my_list = [1, 2.3, 'abc', (5, 6, 'x', 'y')]
my_var = str(my_list[1]) + my_list[2][0] + my_list[3][3]
print(my_var)

# Challenge #34
# Consider the following list: languages = ['English', 'Python', 'Java', 'Golang', 'German']
# Using list slicing, eliminate the first and the last element from the list called language.

languages = ['English', 'Python', 'Java', 'Golang', 'German']
languages = languages[1:len(languages)-1]
print(languages)

# Challenge #35
# Using the range() built-in function create a list called my_list that stores 
# the following numbers: -20, -17, -14, -11, -8, -5, -2, 1, 4, 7

my_list = list(range(-20, 10, 3))
print(my_list)

# Challenge #36
# Consider the following list:  days = [10, 11, 13, 14, 15]
# Using a list method insert the value 12 between 11 and 13.

days = [10, 11, 13, 14, 15]
days.insert(2, 12)
print(days)

# Challenge #37
# Consider the following string: message = 'Wow! Python is great'
# Using list comprehension create a list called no_vowels that contains as elements 
# the characters from the string above that are not vowels or whitespace. We consider vowels: 'aeio'

message = 'Wow! Python is great'
no_vowels = [char for char in message if char not in 'aeiouAEIOU ']
print(no_vowels)

# Challenge #38
# Consider the following sets: 
# names1 = {'John', 'Marry', 'Lena', 'Pollux' and  
# names2 = {'Dan', 'Arthur', 'Marry', 'Lena', 'Castor'}
# Using set methods and operations create a list called names that contains the 
# elements that belong to both sets. names will be  ['Lena', 'Marry']

names1 = {'John', 'Marry', 'Lena', 'Pollux'} 
names2 = {'Dan', 'Arthur', 'Marry', 'Lena', 'Castor'}
names = names1.intersection(names2)
print(names)

# Challenge #39
# Consider the following lists:  
# phone1 = ['1111', '2222', '2222', '1111'] and 
# phone2 = ['1111', '3333', '3333', '1111']
# Using set methods create a new set called phone_numbers that contains all unique elements present in both lists.

phone1 = ['1111', '2222', '2222', '1111']
phone2 = ['1111', '3333', '3333', '1111']
phone_numbers = set(phone1).union(set(phone2))
print(phone_numbers)

# Challenge #40
# Consider the following string variable: my_str  = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'
# Using string methods and list operations create a variable of type string called interface_mac that stores 
# the name of the interface which is wlo1, an exclamation mark, and the MAC address which is b4:6d:83:77:85:f3

my_str  = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'
tmp = my_str.split(' ')
interface_mac = tmp[0] + '!' + tmp[-1]
print(interface_mac)

# Challenge #41
# Write a function called my_function() that takes exactly one argument which is an integer written between single 
# or double quotes (this is in fact a string). If the argument is integer 'n', the function should return the result of n + nn + nnn
# Example: my_function('5') returns 5 + 55 + 555 which is 615 and my_function('9') returns 9 + 99 + 999 which is 1107

def my_function(x):
    res = int(x) + int(x*2) + int(x*3)
    return res

print(my_function('5'))
print(my_function('9'))

# Challenge #42
# Consider the following list with duplicates what stores MAC addresses: 
# mac = ['b4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3', 'a4:6d:83:77:85:f4', 'c4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3']
# Write a Python script that uses a for loop, iterates over the list and creates a new list called mac_unique that 
# stores only unique MAC addresses (unique elements).

mac = ['b4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3', 'a4:6d:83:77:85:f4', 'c4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3']
mac_unique  = []
for adr in mac:
    if adr not in mac_unique :
        mac_unique .append(adr)
print(mac_unique )

# Challenge #43
# Consider the following list with duplicate elements: years = [2010, 2010, 2011, 2011, 2012, 2012, 2012]
# Write a Python script that uses list comprehension and appends only unique elements from the years list to a new list called years_unique.

years = [2010, 2010, 2011, 2011, 2012, 2012, 2012]
years_unique = []
[years_unique.append(item) for item in years if item not in years_unique]
print(years_unique)

# Challenge #44
# Consider the following list of words: words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom']
# Some words are palindromes and some are not.  Using list comprehension, create a list called palindromes 
# that contains only words from the list above that are palindromes.  Ignore the letter case when checking for palindromes.

words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom']
palindromes = [word for word in words if word.lower() == word[::-1].lower()]
print(palindromes)

# Challenge #45
# Create a function called reverse() that accepts a string as an argument and returns a new string with all characters reversed.

def reverse(s):
    return s[::-1]

print(reverse('Python'))

# Challenge #46
# Write a function called remove_from_list() that takes 2 arguments: a list and the value that should be removed from the list.  
# After calling the function, all occurrences of the second argument should have been removed from the list.
list1 = [1, 2, 1, 1, 3]
def remove_from_list(l, v):
    while v in l:
        l.remove(v)

remove_from_list(list1, 1)
print(list1)

# Challenge #47
# Write a function called vowel_count() that takes a string as an argument and returns a dictionary with the keys as the vowels in the 
# string and the values as the count of times a vowel appears in the string.  The function ignores the case and considers only lower-case letters.

def vowel_count(s):
    my_dict = {}
    for vowel in 'aeiou':
        if vowel in s.lower():
           my_dict[vowel] = s.lower().count(vowel)
    return my_dict

print(vowel_count('Python JAVA Go'))

# Challenge #48
# Write a function called counter() that takes a string as an argument and returns the number of vowels and consonants in the string as a tuple.
# Letter case doesn't matter (both 'a' and 'A' will be counted as a vowel).

def counter(s):
    vowels = 'aeiou'
    vowel_count = 0
    for vowel in vowels:
        if vowel in s:
            vowel_count += s.count(vowel)
    return (len(s)-vowel_count, vowel_count)

print(counter('Python'))
print(counter('Beautiful'))

# Challenge #49
# Consider the following list of countries with duplicates: 
# countries = ['USA', 'UK', 'France', 'Romania', 'France', 'Germany', 'USA', 'Canada', 'India', 'UK']
# Your task is to eliminate duplicates and sort the list in alphabetic order.
# P.S. Solve the exercise by writing only two lines of code.

countries = ['USA', 'UK', 'France', 'Romania', 'France', 'Germany', 'USA', 'Canada', 'India', 'UK']
countries = list(set(countries))
countries.sort()
print(countries)

# Challenge #50
# Having the show_arp.txt file below, create a Python script that reads the file and extracts IP and MAC addresses 
# in a list called ip_mac. Each element of the list should be a tuple with 2 items: (ip, mac)

with open('python/challenges/files/show_arp.txt') as f:
    content = f.read().splitlines()
    result = []
    head = [element for element in content[0].split(' ') if element != '']
    print(head)
    for line in content[1:]:
        tmp = line.split(' ')
        tmp2 = [element for element in tmp if element != '']
        ip = tmp2[head.index('Address')]
        mac = tmp2[head.index('Hardware')-1]
        result.append((ip, mac))

print(result)

# Challenge #51
# Create a lambda expression that calculates the area of a square. Lambda has one argument, the length of one side.
# Assign the lambda expression to a variable called area.

area = lambda x: x*x
print(area(2))

# Challenge #52
# Consider the value of constant PI with many decimal points: PI = 3.141592653589793
# Using the format() built-in function, convert PI to a value formatted with 5 decimals. PI will be 3.14159 and remains a float.

PI = 3.141592653589793
PI = float(format(PI, '.5f'))
print(PI)

# Challenge #53
# Consider the following dictionary: 
# countries = {'us': 'United States of America', 'br': 'Brazil', 'de': 'Germany', 'at': 'Austria'}
# Write a Python script that prints out the values of the dictionary sorted by the keys in alphabetical order. Each value should be on its own line.

countries = {'us': 'United States of America', 'br': 'Brazil', 'de': 'Germany', 'at': 'Austria'}
countries_sorted = sorted(countries, key=lambda x:countries[x])
for country in countries_sorted:
    print(countries[country])

# Challenge #54
# Consider the following dictionary. The keys are the names of the employees and the values are their salaries before taxes.
# salaries = {'John': 50000, 'Anne': 66000, 'Antonio': 48000}
# Using dictionary comprehension create a new dictionary called taxes that stores the names of the employees as keys and the tax for each employee as value. We consider the tax as being 10% of the salary.

salaries = {'John': 50000, 'Anne': 66000, 'Antonio': 48000}
taxes = {key:salary*.10 for key, salary in salaries.items()}
print(taxes)

# Challenge #55
# Consider a text file called a.txt in the current working directory.
# Create a Python script that opens the file in read-only mode, and reads only the word "first" (the 2nd word) from the file in a variable called word.

with open('python/challenges/files/a.txt') as file:
    word = file.read().splitlines()[0].split(' ')[1]

print(word)

# Challenge #56
# Consider a text file called workout.txt in the current working directory. 
# This is used by a fitness application written in Python that writes to the file the date and how many steps per day a person takes.
# Take care not to overwrite the file!

with open('python/challenges/files/workout.txt', 'a') as file:
    file.write('May 25:8800\n')
