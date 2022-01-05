"""
Implement a compute_name function.
Given the first_name, middle_name, and last_name, it should return the full name of the person.
constraint: You must use string interpolation with f"{}" to build this full name.
"""


# Implement your compute_name method below:
def compute_name(first_name, middle_name, last_name):
    return f"{first_name} {middle_name} {last_name}"



# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing compute_name with benjamin romain baranger:")
if compute_name('benjamin', 'romain', 'baranger') == 'benjamin romain baranger':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
print("Testing compute_name with chris james westerman:")
if compute_name('chris', 'james', 'westerman') == 'chris james westerman':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
