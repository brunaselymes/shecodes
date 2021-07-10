moths_in_house = input("Moths in the house? ")
mitch_is_home = input("Mitch is home? ")

#Q1)Kate’scat,Roary,lovescatchingmoths.WriteaprogramthatdetermineswhetherornotitistimeforRoarycatch moths

if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")

# #Q2)utRoarycan’tactuallygetthemothsbyherself!Amendthepreviousprogramtodeterminewhetherornot it is time for Roary to go moth hunting

if moths_in_house:
    if mitch_is_home:
        print("Hoooman! Help me get the moths!")
    if not mitch_is_home:
        print("Meoooooooooooooow! Hisssss!")
elif mitch_is_home:
    print("Climb on Mitch.")
else:
    print("No threats detected.")


# #Q3)Write a program that implements the algorithmfor Red Light Cameras

light_colour = input("Light colour? ")
car_detected = input("Car detected? ")

if light_colour.capitalize() == "red" and car_detected:
    print("Flash!")
else:
    print("Do nothing")


# #Q4)Write a program that asks the user for their height, and determines whether or not they are tall enough to ride the rollercoaster, which has a height requirementof 120cms
height = input("How tall are you? ")

if float(height) >= 120:
    print("Hop on!")
else:
    print("Sorry, not today :(")

# #Q5)Write a program tha tasks the user to enter their username and password, and output as success message if they are correct, or a failure message if they are incorrect.
username = "Bruna"
password = "bruna123"
usernameInput = input("Enter your username: ")
passwordInput = input("Enter your password: ")

if username == usernameInput and password == passwordInput:
    print("Correct!")
else:
    print("Incorrect!")

# #Q6)Write a program that asks user to enter their email address and checks whether it valid or not. For the purpose of this exercise, you can make the assumption that a valid email address contais a @ symbol and a . symbol.
email = input("Enter your email address: ")

if "." not in email or "@" not in email:
    print("Invalid email addess.")
else:
    print("valid email address.")