"""
    Topic: Assingment 2 Question 3
    Date: 28 Sep 2023
    Author: Kathleen
    
"""
s1 = "yn"
s2 = "Pynative"
s1 = s1.lower()
s2 = s2.lower()
len_s1 = len(s1)
count = 0

for char in s1:
    if char in s2:
        count += 1
    
if count == len_s1:
    print ("s1 and s2 are balanced True")
else:
    print ("s1 and s2 are balanced False")