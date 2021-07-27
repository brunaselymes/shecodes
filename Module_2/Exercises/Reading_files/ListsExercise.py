import csv

colours = []

with open("./data/colours_20_simple.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # Q1
    # for line in csv_reader:
    #     print(line[0], line[1], line[2])
    # Q2
    # csv_reader = csv.reader(csv_file)
    # for line in csv_reader:
    #     print(line[2], ", Hex:", line[1], ", RGB:", line[0])
blue = 0
green = 0
yellow = 0
red = 0
with open("./data/colours_20.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    # Q3
    header = next(csv_reader)
    for line in csv_reader:
        # print(line[4], ", Hex:", line[2],", RGB:", line[1])
        # Q4 
        # #strip() trims the spaces
        if line[4].lower().strip().endswith("blue"):
            blue+=1
        elif line[4].lower().strip().endswith("green"):
            green+=1
        elif line[4].lower().strip().endswith("yellow"):
            yellow+=1
        elif line[4].lower().strip().endswith("red"):
            red+=1
# print(f"Blue: ", blue)
# print(f"Green: ", green)
# print(f"Yellow: ", yellow)
# print(f"Red: ", red)
# blue = 0
# green = 0
# yellow = 0
# red = 0
# #Q4/b
# with open("./data/colours_213.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     header = next(csv_reader)
#     for line in csv_reader:
#         if line[4].lower().strip().endswith("blue"):
#             blue+=1
#         elif line[4].lower().strip().endswith("green"):
#             green+=1
#         elif line[4].lower().strip().endswith("yellow"):
#             yellow+=1
#         elif line[4].lower().strip().endswith("red"):
#             red+=1
# print(f"Blue: ", blue)
# print(f"Green: ", green)
# print(f"Yellow: ", yellow)
# print(f"Red: ", red)

#RAL 2008,247-094-037,#F75E25,Hellrotorange,Bright red orange,Orangé rouge clair,Rojo claro anaranjado,Rosso arancio chiaro,Licht roodoranje
#Does this count as red or orange?

slowest = 0
fastest = 0

with open("./data/galaxies.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if int(line[1]) < slowest:
            slowest = int(line[1])
        if int(line[1]) > fastest:
            fastest = int(line[1])
print(f"Slowest galaxy has the min velocity of {slowest}")
print(f"Fastest galaxy has the max velocity of {fastest}")