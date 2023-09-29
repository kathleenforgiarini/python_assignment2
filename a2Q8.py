"""
    Topic: Assingment 2 Question 8
    Date: 29 Sep 2023
    Author: Kathleen
    
"""

birthday = int(input("Input birthday: "))
month_of_birth = input("Input month of birth (e.g. march, july etc): ").lower()

if (month_of_birth == "december" and 22 <= birthday <= 31) or (month_of_birth == "january" and 1 <= birthday <= 19):
    sign = "Capricorn"
elif (month_of_birth == "january" and 20 <= birthday <= 31) or (month_of_birth == "february" and 1 <= birthday <= 18):
    sign = "Aquarius"
elif (month_of_birth == "february" and 19 <= birthday <= 29) or (month_of_birth == "march" and 1 <= birthday <= 20):
    sign = "Pisces"
elif (month_of_birth == "march" and 21 <= birthday <= 31) or (month_of_birth == "april" and 1 <= birthday <= 19):
    sign = "Aries"
elif (month_of_birth == "april" and 20 <= birthday <= 30) or (month_of_birth == "may" and 1 <= birthday <= 20):
    sign = "Taurus"
elif (month_of_birth == "may" and 21 <= birthday <= 31) or (month_of_birth == "june" and 1 <= birthday <= 20):
    sign = "Gemini"
elif (month_of_birth == "june" and 21 <= birthday <= 30) or (month_of_birth == "july" and 1 <= birthday <= 22):
    sign = "Cancer"
elif (month_of_birth == "july" and 23 <= birthday <= 31) or (month_of_birth == "august" and 1 <= birthday <= 22):
    sign = "Leo"
elif (month_of_birth == "august" and 23 <= birthday <= 31) or (month_of_birth == "september" and 1 <= birthday <= 22):
    sign = "Virgo"
elif (month_of_birth == "september" and 23 <= birthday <= 30) or (month_of_birth == "october" and 1 <= birthday <= 22):
    sign = "Libra"
elif (month_of_birth == "october" and 23 <= birthday <= 31) or (month_of_birth == "november" and 1 <= birthday <= 21):
    sign = "Scorpio"
elif (month_of_birth == "november" and 22 <= birthday <= 30) or (month_of_birth == "december" and 1 <= birthday <= 21):
    sign = "Sagittarius"
else:
    sign = False

if sign:
    print(f"Your Astrological sign is: {sign}")
else:
    print("Invalid birthdate.")