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

with open('data/galaxies.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    slow = [None, float('inf')]    #ignores first. Variable value = infinity (huge) 
    fast = [None, 0]   #ignores first. Variable value = 0 (low)
    for i, row in enumerate(csv_reader):    #i means index (naming convention). Row is row.
        if i != 0:  #this first 'if' in the loop ensures each value is checked when the loop iterates because no rows = 0.
            if int(row[1]) < slow[1]: #this 'if' (within the first'if') targets velocity data in each row: e.g. row[1] for row (18,19349) gets (19349). If velocity value is less than current slow value, do this:
                slow =  [row[0], int(row[1])]  #this line re-defines the slow var value: it's now galaxy ([0]) + the velocity value just stored (because it was found to be lower than the last one stored)
            if int(row[1])> fast[1]: #this 'if' (within the first'if') says if velocity is greater than current fast value, do this:
                fast = [row[0], int(row[1])] #this line re-defines the fast var value: it's now galaxy ([0]) + the velocity value just stored (because it was found to be faster than the last one stored)
    print(f'Galaxy {slow[0]} has a min velocity of {slow[1]}km/sec.') #formatted print returns the new slow variable - galaxy + value