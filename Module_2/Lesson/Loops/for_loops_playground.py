

# #Use for loop to print numbers
# #0 to 100 (inclusive)
# for number in range(0,101):
#     print(number)

# #Use for loop to print numbers
# #0 to 100 (skip 5) , 0,5,10,15
# for number in range(0,101,5):
#     print(number)

# result = ""

# letters = ["a", "b", "c", "d", "e", "f"]
# for letter in letters:
#     result+= letter
#     print(result)
# # print(result)

chilli_wishlist = ["igloo", "chicken", "donut toy","cardboard box"]

# for item in range(len(chilli_wishlist)):
#     print(chilli_wishlist[item])
    
# for item in chilli_wishlist:
#     print(item)

# adapt for loop to print a message for each item in the list e.g chilli wants: item

for item in chilli_wishlist:
    print(f"Chilli wants: ", item)

# use a for loop to print each item in a list from a previous exercise

secondList = ['donut toy','tennis ball', 'crocodile toy']
for i in range(len(secondList)):
    print("Chilli likes", secondList[i])

for i in reversed(range(10)):
    print(i)