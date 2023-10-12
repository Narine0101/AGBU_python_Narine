# 1*. Write a Python program that accepts a word from the user and reverse it.
"""
txt = input("Please input txt")
revers_txt = txt[::-1]
print(f"revers_txt of {revers_txt }")
"""


# 2. Write a Python program to count that user inputed number is even or odd.
"""
num = int(input("Please input number"))
if num % 2 == 0:
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")
"""


# 3. Write a Python program to find is inputed number in 100 to 400 (both included). Hint(dont google task description)
"""
num = int(input("Please input number"))
if num >= 100 and num <= 400:
    print(f"The inputed {num} number in 100 to 400 (both included)")
else:
    print(f"The inputed {num} does not in 100 to 400 (both included)")
"""


# 4. Write a Python program that get 2 numbers from user and retur Biggest, Median, Sum, Multiply, Divide and Subtract
"""
num1 = int(input("First number"))
num2 = int(input("Second number"))
if num1 > num2:
    print(f"max = {num1}")
else:
    print(f"max = {num2}")
print(f"average is num1 & num2 = {(num1 + num2) / 2}")
print(f"Sum is num1 & num2 = {num1 + num2}")
print(f"Multiply is num1 & num2 = {num1 * num2}")
print(f"Divide is num1 & num2 = {num1 / num2}")
print(f"Subtract is num1 & num2 = {num1 - num2}")
"""

from datetime import date

# 5. Write a Python program to get next day of a given date.
# 	Expected Output:
#
# 	Input a year: 2016
# 	Input a month [1-12]: 8
# 	Input a day [1-31]: 23
# 	The next date is [yyyy-mm-dd] 2016-8-24
# year = int(input("Year"))
# month = int(input("Month"))
# day = int(input("Day"))
# inputDate = date(year, month, day)
# print(inputDate)

#I working in this  problem

# txt = "Gurguremgy"
# print(txt[0], txt[3], txt[8])
# print(txt[-2], txt[-7], txt[-10])

# txt = "Narine Sahakyan Alberti"
# print(txt[:6])
# print(txt[7:15])
# print(txt[-7:])
# print(txt[:4:-1])

# txt = input("Please input txt")
# if len(txt)>=20:
#     print(txt[::-1])
# else:
#     print("text is less")

# print(bool(None))
# print(bool(15))
# print(bool(" "))
# x = "Hello"
# y = 15
#
# print(bool(x))
# print(bool(y))

# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))


#  1. Write a program that get user input and return  every third element from inputed string.
# txt = input("Please input txt")
# print("Every third element from input string is:", txt[::3])


#   2. Write a program that get user input and return  every second element from inputed string from end.
# txt = input("Please input txt")
# print("Every second element from input string from end is:", txt[::-2])


txt = input("Please input txt")
if len (txt) % 2 == 0:
    print("Reverse txt is:", txt[::-1])
else:
    print("Every second element from input string from end is:", txt[::2])




