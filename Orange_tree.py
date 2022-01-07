"""
Background and Objectives:
Let’s create an OrangeTree class which models the life of an orange tree (its birth, life cycle and death).
Our class should include the following attributes: age, height, fruits (all integers) and dead a boolean.

To simulate time passing, you will need to implement the following instance methods:

- one_year_passes
- pick_a_fruit

def one_year_passes(self):
  # TODO: age the tree by one year
  # TODO: check if the tree has survived
  # TODO: if so, make the tree height grow
  # TODO: if so, make the tree grow fruits


Specs:
- Each year, the tree should age by 1 year (it becomes older and taller, and eventually dies).
- A tree grows 1 meter per year up to and including the 10th year. Then it stops growing
- The orange tree cannot die until it reaches 50 years old.
- After 50 years, the probability of dying increases each year Pyhon’s random library might come in handy.
- No tree can live more than 100 years.
- A tree will produce 100 fruits a year once it is more than 5 years old.
- A tree will produce 200 fruits a year when it reaches 10 years old.
- A tree will not produce fruits once it reaches 15 years old.
- You should be able to pick a single fruit from the tree by calling the pick_a_fruit method on your tree (but only if there are some left).
- At the end of each year, the fruits which have not been picked will fall off.
"""
import random

class OrangeTree:

  def __init__(self, age=0, height=0, fruits=0, dead=False):
    self.age = age
    self.height = height
    self.fruits = fruits
    self.dead = dead
        
  def one_year_passes(self):
    self.fruits = 0
    self.age += 1
    
    if self.age > 50: self.dead = (self.age > random.randint(50, 101))
    
    if not self.dead:
      if self.age <= 10: self.height += 1
      if self.age < 15:
        if self.age > 5: self.fruits += 100
        if self.age >= 10: self.fruits += 100

  def pick_a_fruit(self):
    if self.fruits > 0 : self.fruits -= 1

      
      
      

            
# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
method_list = [func for func in dir(OrangeTree()) if callable(getattr(OrangeTree(), func))]

print("Testing your Class attributes and methods")
print("-----------------------------------------")
print("Your class should have a 'one_year_passes' method")
if 'one_year_passes' in method_list:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Your class should have a 'pick_a_fruit' method")
if 'pick_a_fruit' in method_list:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

test_tree = OrangeTree()
print("Your class should have an integer 'age' attribute")
if isinstance(test_tree.age, int):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Your class should have an integer 'height' attribute")
if isinstance(test_tree.height, int):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Your class should have an integer 'fruits' attribute")
if isinstance(test_tree.fruits, int):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Your class should have a boolean 'dead' attribute")
if isinstance(test_tree.dead, bool):
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Your tree should start at age 0")
if test_tree.age == 0:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")

print("Your tree should be 0 meters tall when planted")
if test_tree.height == 0:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
    os.system("echo '\e[31mIncorrect\e[0m'")



print("\n Testing your tree's growth")
print("--------------------------------------")
pre_r = "'\e[31m'"
pre_g = "'\e[32m'"
post = "'\e[0m'"
test_tree = OrangeTree()
for i in range(15):
    test_tree.one_year_passes()
    correct = True
    if i <=4 and test_tree.fruits != 0:
        os.system(str('echo ' + pre_r + f"Tree should not grow fruits at {i+1} years old" + post))
        correct = False
    if i > 4 and i < 9 and test_tree.fruits != 100:
        os.system(str('echo ' + pre_r + f"Tree should grow 100 fruits {i+1} years old" + post))
        correct = False
    if i >= 9 and i <=13 and test_tree.fruits != 200:
        os.system(str('echo ' + pre_r + f"Tree should grow 200 fruits at {i+1} years old" + post))
        correct = False
    if i >=14 and test_tree.fruits != 0:
        os.system(str('echo ' + pre_r + f"Tree should not grow fruits at {i+1} years old" + post))
        correct = False
    if i < 9 and test_tree.height != i +1 :
        os.system(str('echo ' + pre_r + f"Tree should be {i+1} meters tall at {i+1} years old" + post))
        correct = False
    if i > 9 and test_tree.height != 10:
        if test_tree.age <= 10:
            height = i + 1
        else:
            height = 10
        os.system(str('echo ' + pre_r + f"Tree should be {height} meters tall at {i+1} years old" + post))        
        correct = False
    if correct:
        os.system(str('echo ' + pre_g + f"Correct for {i+1} years old" + post))

print("\n Testing your tree's pick_a_fruit")
print("--------------------------------------")
test_tree = OrangeTree()
test_tree.pick_a_fruit()
if test_tree.fruits == 0:
	os.system("echo '\e[32mCorrect for non-fruit bearing trees\e[0m'")
else:
    os.system("echo '\e[31mShould not allow us to pick fruits when there are none\e[0m'")
for i in range(6):
    test_tree.one_year_passes()
test_tree.pick_a_fruit()
if test_tree.fruits == 99:
	os.system("echo '\e[32mCorrect for fruit bearing trees\e[0m'")
else:
    os.system("echo '\e[31mShould allow us to pick fruits when there are some\e[0m'")
    
print("\n Testing your tree's ageing")
print("--------------------------------------")
correct = True
for i in range(5):
    test_tree = OrangeTree()
    for i in range(50):
        test_tree.one_year_passes()
    if test_tree.dead:
    	correct = False
if correct:
    os.system("echo '\e[32mTree should always live to 50 years old\e[0m'")
else:
    os.system("echo '\e[31mTree should always live to 50 years old\e[0m'")

death_age = []
for i in range(10):
    test_tree = OrangeTree()
    test_tree.age = 50
    dead = test_tree.dead
    loop_count = 0
    while not dead and loop_count < 51:
        test_tree.one_year_passes()
        loop_count += 1
        if dead := test_tree.dead:
            death_age.append(test_tree.age)

if death_age:
    if sorted(death_age)[-1] < 101:
         os.system("echo '\e[32mTree should not live more than 100 years\e[0m'")
    else:
        os.system("echo '\e[31mTree should not live more than 100 years\e[0m'")
else:
    os.system("echo '\e[31mTree should not live more than 100 years\e[0m'")


if len(set(death_age)) > 1:
    os.system("echo '\e[32mChances of death should increase each year\e[0m'")
else:
    os.system("echo '\e[31mChances of death should increase each year\e[0m'")
