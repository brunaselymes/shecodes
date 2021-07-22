import csv

with open("dogs_are_awesome.txt", mode = "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        print(line)
        