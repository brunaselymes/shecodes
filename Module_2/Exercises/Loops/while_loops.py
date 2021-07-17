#Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the numbers.

inputNum = 0
sum = 0
while inputNum != "":
    inputNum = input("Number: ")
    sum += int(inputNum)
    print(sum)

