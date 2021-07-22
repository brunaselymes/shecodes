#Q1 Write a function that takes a temperature in fahrenheitand returns the temperature in celsius.
# def convert_to_celsius(fahrenheit):
#     return (int(fahrenheit)-32) * (float(5/9))

# print(convert_to_celsius(input("Enter temperature in F: ")))

#Q2 Writeafunctionthatacceptsoneparameter(aninteger)andreturnsTruewhenthatparameterisoddandFalse when that parameter is even
# def is_odd(num):
#     if float(num) % 2 == 0:
#         return False
#     else:
#         return True

# print(is_odd(11))

#Q3)Write a function that returns the mean of a listof numbers.

# def find_average(listOfNumbers):
#     sumOfNumbers = 0
#     for number in listOfNumbers:
#         sumOfNumbers += number
#     return sumOfNumbers / len(listOfNumbers)
# print(find_average([10, 5, 6]))

#Q4)Write a function that takes two parameters; the unit price of an item, and how many units were purchased. Return the total cost as a string.
# def findTotal(price, quantity):
#     total = price * quantity
#     return "$ " + str(total)

# print(findTotal(1.49,7))