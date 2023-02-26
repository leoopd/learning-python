# Challenge #1
# Write a Python function that takes a list as an argument and returns a new list with unique elements of the first list in the same order.
# Sample List : [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5] 
# Unique List : [1, 2, 3, 4, 5]3

def unique_elements(original_list):
  '''This function returns a list containing only the unique elements of the original list.'''
  tmp = set(original_list)
  return list(tmp)

print(unique_elements(sample))
