groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

#Ask the user how many units of each item they bought, then output the corresponding receipt.
# For the input below, assume that the input is providedin the same order as defined in the list above.

# total = 0
# newlist = []
# for item in range(len(groceries)):
#     qtts = input(f"How many of {groceries[item][0]}: ")
#     newlist.append(int(qtts))

# print("\n====Izzy's Food Emporium====\n")
# for item in range(len(groceries)):
#     newlist.append(int(qtts))
#     total += (groceries[item][1]*newlist[item])
#     print(f"{groceries[item][0]} ${groceries[item][1]*newlist[item]}")
# print("\n============================")
# format_float = "{:.2f}".format(total)
# print(f"                    ${format_float}\n")

# Ask the user to enter a string. Output the string one character at a time, as well as it’s positionin the string
# strInput = input("Enter a string: ")
# for char in range(len(strInput)):
#     print(char,strInput[char])

#Ask the user for a number and use this to generatea pyramid of that height.
# num = input("Pyramid size: ")

# for i in range(1,int(num)+1):
#     print(i * "*")

# #Ask the user for a number and use this to generatea (different) pyramid of that height.
# num = input("Pyramid size: ")

# for i in range(0,int(num)):
#     for j in range(0,int(num)-i-1):
#         print(end=" ")
#     for j in range(0, i+1):
#         print("*",end=" ")
#     print() 