groceries = {
    "Baby Spinach": 2.8,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10, 
    "Carrots": 0.56,
    "Oranges": 3.08,
    "Bacon": 9.00
}

#Search for a value
print(groceries)
print(groceries["Baby Spinach"])

#Adding a new item
groceries["Avocadoes"] = 1.00
print(groceries)

# changing the value of an existing item
groceries["Hot Chocolate"] = 2.70
print(groceries)

# removing an item from the dictionary
del groceries["Crackers"]
print(groceries)

# iterating over the dictionary
for item in groceries:
    print(f"{item}: ${groceries[item]}")
print()