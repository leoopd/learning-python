# Challenge #1
# Write a Python function that takes a list as an argument and returns a new list with unique elements of the first list in the same order.
# Sample List : [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5] 
# Unique List : [1, 2, 3, 4, 5]3

def unique_elements(original_list):
  '''This function returns a list containing only the unique elements of the original list.'''
  tmp = set(original_list)
  return list(tmp)

print(unique_elements(sample))

# Challenge #2
# Write a Python function to check whether a number is perfect or not. The function should return True if the number is perfect and False otherwise.

def divisors (n):
  divisor_list = []
  for i in range(1, int(n/2)+1):
    if n%i == 0:
      divisor_list.append(i)
  return divisor_list


def perfect_check (n):
  divisor_list = divisors(n)
  tmp = 0
  for divisor in divisor_list:
    tmp += divisor
  if tmp == n:
    return True
  return False

# print(perfect_check(8128))

# Challenge #3
# Write a function that returns the factorial of a number n which is the function's argument.

def factorial (n):
  factorial = 1
  for i in range(2, n+1):
    factorial *= i
  return factorial

# print(factorial(8))

# Challenge #4
# Create a function that takes an integer as an argument and returns True if it’s a prime number and False otherwise.

def is_prime (n):
  if n <= 3:
    return n > 1
  if n % 2 == 0 or n % 3 == 0:
    return False
  limit = int(n**0.5)
  for i in range(5, limit+1, 6):
    if n % i == 0 or n % (i+2) == 0:
      return False
  return True

# print(is_prime(100057))

# Challenge #5
# Using the function defined in the previous challenge find 5 prime numbers greater than 1,000,000

def primes_above_100k(n):
  prime_numbers = []
  i = 100001
  while len(prime_numbers) < int(n):
    if is_prime(i) == True:
      prime_numbers.append(i)
    i += 1
  return prime_numbers

# print(primes_above_100k(5))

# Challenge #7
# Write a function that takes a list as an argument and returns the Equilibrium Index of the list. If there isn't such an index it returns False.

def equilibrium(l):
    total_sum = sum(l)
    leftsum = 0
    for i, num in enumerate(l):
        total_sum -= num
 
        if leftsum == total_sum:
            return i
        leftsum += num
    return False

# print(equilibrium([1, 2, 3]))

# Challenge #8
# Change the solution of the previous challenge so that the function receives a string of numbers separated by a comma.

def equilibrium_string(s):
    tmp = s.split(",")
    print(tmp)
    l = [eval(i) for i in tmp]
    total_sum = sum(l)
    leftsum = 0
    for i, num in enumerate(l):
        total_sum -= num
 
        if leftsum == total_sum:
            return i
        leftsum += num
    return False

# print(equilibrium_string('-7, 1, 5, 2, -4, 3, 0'))

# Challenge #9
# Define a function that draws a Christmas tree using asterisks (*). The function takes a single argument, which is the height of the tree.

def christmas_tree (height):
    ctr = 1
    for i in range(1, height+1):
        print('*' * ctr)
        ctr += 2
        
# christmas_tree(10)
