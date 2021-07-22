def multiply_by_3(num):
    return int(num) * 3

print(multiply_by_3(input("Enter a number: ")))


def convert_cm_to_in(length_cm):
    length_in_inch = length_cm / 2.54
    return length_in_inch
print(convert_cm_to_in(20))
# print(length_in_inch) #is not defined, local var
# Write a function that converts inches to
# centimeters

def convert_cm_to_in(length_in_inch):
    length_cm = length_in_inch * 2.54
    return length_cm