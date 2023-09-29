"""
    Topic: Assingment 2 Question 1
    Date: 28 Sep 2023
    Author: Kathleen
    
    Input: "PyNaTive" Output: "aeivyNPT" 
"""

string = "PyNaTive"

lowers = ""
uppers = ""
for char in sorted(string):
    if char.islower():
        lowers += char
    else:
        uppers += char

output = lowers + uppers
print (output)