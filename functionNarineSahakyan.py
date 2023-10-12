# 1. Write a function to multiply all the numbers in a given list
# def multiply_given_list_elements(givenList):
#     result = 1
#     for i in givenList:
#         result *= i
#     return result
#
#
# givenList = [5, 10, 7, 2, 6]
# print(multiply_given_list_elements(givenList))


# 2. Write a function that takes a list and returns a new list with unique elements of the first list
# def get_list_unique_elements(someList):
#     result = []
#     for i in someList:
#         if i not in result:
#             result.append(i)
#     return result
#
# someList = [1, 2, 1, 4, 3, 2]
# print(get_list_unique_elements(someList))


# 3. Write a function to print the even numbers from a given list.
# def get_even_numbers(givenlist):
#     result = []
#     for i in givenlist:
#         if i % 2 == 0:
#             result.append(i)
#     return result
#
# givenlist = [8, 2, 3, 4, 7, 6]
# print(get_even_numbers(givenlist))


# 4.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#       Sample String : 'The quick Brow Fox'
#       Expected Output :
#       No. of Upper case characters : 3
#       No. of Lower case Characters : 12

# def get_upper_lower_letters_count(myString):
#     upperCount = 0
#     lowerCount = 0
#     for i in myString:
#         if i.islower():
#             lowerCount += 1
#         elif i.isupper():
#             upperCount += 1
#
#     print(f"No. of Upper case characters : {upperCount}")
#     print(f"No. of Lower case Characters : {lowerCount}")
#
#
# myString = 'The quick Brow Fox'
# get_upper_lower_letters_count(myString)


# 5. Write a Python function that takes a number as a parameter and check the number is prime or not
# def number_is_prime_or_not(num):
#     if num > 1:
#         for i in range(2, int(num/2)+1):
#             if (num % i) == 0:
#                 print(num, "is not a prime number")
#                 break
#         else:
#             print(num, "is a prime number")
#     else:
#         print(num, "is not a prime number")
#
# num = int(input("Please input some number"))
# number_is_prime_or_not(num)
