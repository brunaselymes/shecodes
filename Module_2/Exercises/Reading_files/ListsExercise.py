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
        if line[4].lower().strip().endswith("blue"):
            blue+=1
        elif "green" in line[4].lower():
            green+=1
        elif "yellow" in line[4].lower():
            yellow+=1
        elif "red" in line[4].lower():
            red+=1
print(f"Blue: ", blue)
print(f"Green: ", green)
print(f"Yellow: ", yellow)
print(f"Red: ", red)
# Blue:  0
# Green:  1
# Yellow:  12
# Red:  0

#Q4/b
with open("./data/colours_213.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for line in csv_reader:
        if "blue" in line[4].lower():
            blue+=1
        elif "green" in line[4].lower():
            green+=1
        elif "yellow" in line[4].lower():
            yellow+=1
        elif "red" in line[4].lower():
            red+=1
# print(f"Blue: ", blue)
# print(f"Green: ", green)
# print(f"Yellow: ", yellow)
# print(f"Red: ", red)
# # Blue:  28
# # Green:  32
# # Yellow:  22
# # Red:  25

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