"""
Background and Objectives
Let’s use dictionarys to help us quickly convert Roman Numerals to integers.
Take a look at this table to brush up on Roman Numerals:
https://loudexpose.files.wordpress.com/2011/02/roman-numerals.jpg

Do you notice any patterns we could take advantage of?

Specs
Write a function roman_to_int It should take one argument, a string, and convert it into its corresponding integer eg:

roman_to_int(‘IV’) #=> 4
roman_to_int(‘XVI’) #=> 16
roman_to_int(‘MI’) #=> 1001
Hint - you might consider including 4/40/400 and 9/90/900 in your dictionary
"""

ROMAN_DICT = {
  'I' : 1,
  'IV': 4,
  'V' : 5,
  'IX': 9,
  'X' : 10,
  'XL': 40,
  'L' : 50,
  'XC': 90,
  'C' : 100,
  'CD': 400,
  'D' : 500,
  'CM': 900,
  'M' : 1000
}


def roman_to_int(r_num):
  d_num = 0
  i=0
    
  while i < len(r_num):

    if ROMAN_DICT.get(r_num[i:i+2],"nf") != "nf":
      d_num += ROMAN_DICT[r_num[i:i+2]]
      i += 2

    else:
      d_num += ROMAN_DICT[r_num[i]]
      i += 1

  return d_num


###################################
print("What Roman number would you like to convert?\nYour answer: ",end="")
roman_number=input()
print(roman_to_int(roman_number))
