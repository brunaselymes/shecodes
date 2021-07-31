# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Bacon": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08
# }
# quantity = {
#     "Baby Spinach": 1,
#     "Hot Chocolate": 3,
#     "Crackers": 2,
#     "Bacon": 1,
#     "Carrots": 4,
#     "Oranges": 2
# }
# for item in groceries:
#     print(f"{quantity[item]} {item} @ ${groceries[item]} = ${round(quantity[item] * groceries[item],2)} ")

# quantity2 = {"Baby Spinach": 2,"Hot Chocolate": 1,"Crackers": 4,"Bacon": 0,"Carrots": 8,"Oranges": 5}
# for item in groceries:
#     print(f"{quantity2[item]} {item} @ ${groceries[item]} = ${round(quantity2[item] * groceries[item],2)} ")

############################################################################################################

# colour_counts = {"blue": 0,"green": 0,"yellow": 0,"red": 0,"purple": 0,"orange": 0,}
# colours = ["purple","red","yellow","blue","purple", "orange","blue","purple","orange","green"]

# for color in colours:
#     colour_counts[color] += 1
# print(colour_counts)

##############################################################################################################

# names = ["Maddy", "Bel", "Elnaz", "Gia", "Izzy","Joy", "Katie", "Maddie", "Tash", "Nic","Rachael", "Bec", "Bec", "Tabitha", "Teagen","Viv", "Anna", "Catherine", "Catherine", "Debby","Gab", "Megan", "Michelle", "Nic", "Roxy","Samara", "Sasha", "Sophie", "Teagen", "Viv"]
# namesDictionary = {}.fromkeys(names, 0)

# for name in names:
#     namesDictionary[name] += 1
# print(namesDictionary)

##################################################################################################################
# import csv
# dictColour = {}
# with open("../Reading_files/data/colours_20_simple.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     header = next(csv_reader)
#     for line in csv_reader:
#         dictColour[line[1]] = line[2]
# print(dictColour)
# #################################################################################################################
# import csv
# dictColour = {}
# with open("../Reading_files/data/colours_20_simple.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     header = next(csv_reader)
#     for line in csv_reader:
#         dictColour[line[1]] = [line[0],line[2]]
# print(dictColour)
##################################################################################################################
