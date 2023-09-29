"""
    Topic: Assingment 2 Question 4
    Date: 28 Sep 2023
    Author: Kathleen
    
"""
ListOne = [3, 6, 9, 12, 15, 18, 21] 
ListTwo = [4, 8, 12, 16, 20, 24, 28] 

ListOneOdd = ListOne[1::2]
ListTwoEven = ListTwo[::2]

ListThree = ListOneOdd + ListTwoEven

print (ListThree)