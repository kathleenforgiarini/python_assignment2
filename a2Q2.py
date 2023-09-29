"""
    Topic: Assingment 2 Question 2
    Date: 28 Sep 2023
    Author: Kathleen
    
"""

string = input("Enter a string: ")

lowers = 0
uppers = 0
digits = 0
special = 0

for char in string:
    if char.islower():
        lowers += 1
    elif char.isupper():
        uppers += 1
    elif char.isdigit():
        digits += 1
    else:
        special +=1 

print (f"In the string {string}, there are {lowers} lower case letters, {uppers} upper case letters, {digits} digits and {special} special symbols")
