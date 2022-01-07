"""
Background and Objectives
We can break a number into different contiguous sub-subsequence parts. For example, the number 324 can be broken into parts like (3, 2, 4, 32, 24, 324). A colorful number is a number where the products of all the subsets of the digits are different.

eg:
	263 is a colorful number (2, 6, 3, 2x6, 6x3, 2x6x3) are all different
	236 is not (2, 3, 6, 2x3, 3x6, 2x3x6) has 6 twice (6 and 2x3)

Specs
We want you to write a function is_colorful which takes a single number as an argument and returns True if the number is colorful, False otherwise.

For this exercise, only consider numbers with up to 3 digits (not more), eg:
is_colorful(263) #=> True
is_colorful(236) #=> False
"""
import numpy as np

# Implement your is_colorful method below
def is_colorful(number):
    
  # let's convert my number into a list
  number_list = [int(c) for c in str(number)]
    
  # list_of_products is the list containing the products of all the subsets of digits of my number.
  # first, let's add in the list the digits of my number
  list_of_products = number_list.copy()
    
  i = 0
  j = 2

  # The nested loops below browse all the contiguous sub-subsequence parts of my number
  while i < len(number_list):

    while j <= len(number_list):      
      # Let's append the list_of_products with the product of the current sub-sequence
      list_of_products.append(np.prod(number_list[i:j]))
      j+=1

    i += 1
    j = i + 2
        
  return len(set(list_of_products))==len(list_of_products)

for i in range(10, 200):
  print(f"{i} is a colorfull number? {is_colorful(i)}")
