#Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the numbers.
#############################AQUI####################################################
inputNum = 0
sum = 0
while inputNum != "":
    inputNum = input("Number: ")
    sum += int(inputNum) if inputNum else 0
print(sum)

#Ask the user to enter a number. Print all theodd numbers between 0 and that number (inclusive)
# inputNum = input("Enter a number: ")
# count = 0
# while count <= int(inputNum):
#     if count % 2 != 0:
#         print(count)
#     count+=1

#Selectanumber.Ask the user to enter a number, output whether their number is less than or greater than the selected number.
# Repeat this process until theuser guesses the correct number.

# secretNumber = 5
# guessedNumber = "1"
# while int(guessedNumber) != secretNumber:
#     guessedNumber = input("Guess my number: ")
#     if int(guessedNumber) < secretNumber:
#         print("Too low!")
#     elif int(guessedNumber) > secretNumber:
#         print("Too high!")
#     else:
#         print("Correct!")