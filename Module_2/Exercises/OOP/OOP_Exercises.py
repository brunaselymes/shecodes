# Q1)Together, we wrote a class for a Book object.Update this class to add the ability to:
# 1.Go directly to a specific page number.
# 2.Bookmark a specific page number, i.e. not just thecurrent page.
# 3.Automatically go back to the start of the book (i.e.page 1) when the user turns the final page.
class Book:
    def __init__(self, title, author, pages, current_page):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.bookmark = 1
        
    def bookmark_page(self):
        self.bookmark = self.current_page
    
    def turn_page(self, forward):
        if forward:
            if self.current_page < self.pages:
                self.current_page += 1
            else:
                self.current_page = 1
        else:
            self.current_page -= 1
    
    # def go_to_page(self,pageNo):
    #     self.current_page == pageNo

    def back_to_start(self):
        if self.current_page == self.pages:
            self.current_page == 1    

    def __str__(self):
        return f"Title:{self.title}, Author:{self.author},Pages:{self.pages}"
    
    def __len__(self):
        return self.pages
    

# my_book = Book("A great book", "me", 198, 1)
# my_book.go_to_page(200)
# print(my_book.current_page)
# print(my_book)
# my_book.bookmark_page()
# print(my_book.bookmark)
# my_book.turn_page(True)
# my_book.bookmark_page()
# print(my_book.bookmark)

# Q2)Write a class that represents a rectangle shapeand has a method for each of the following:
# 1.Calculating the area.
# 2.Calculating the perimeter
# 3.Calculating the length of the diagonal.
# 4.Determining whether or not the rectangle is a square.
# Here’s the initialiser method to help get you started:
# def __init__(self, width, height):
#     self.width = width
#     self.height = height
import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def calculate_lenght_diagonal(self):
        return math.sqrt((self.height ** 2) + (self.width ** 2 ))
    
    def is_square(self):
        if self.width == self.height:
            

my_rectangle = Rectangle(10, 2)
print(my_rectangle.calculate_area())
print(my_rectangle.calculate_perimeter())
print(my_rectangle.calculate_lenght_diagonal())

# Q3)Create a class to represent Vehicle objects. Attributesthat you may want to include:
# ●Make and model
# ●Colour●
# Seating capacity●
# Maximum speed

# Include__str__method to print a summary of the Vehicle.
# Include rev_enginemethod to print the noise the vehicle makes (print(“VRRRMMMM!”)is a good approximation :P)

# Q4) Bonus challenge!
# Adapt your Vehicle class to keep track of the amount of fuel available.There are no parameters here, get creative and see if you can think of a suitable way to approach this problem. Things to consider:
# It’s totally fine to make an assumption about consistent fuel consumption per km.●
# The vehicle can also be refuelled (and the fuel tankobviously has a maximum capacity).
# ●Perhaps the user should be warned if they are nearingan empty fuel tank.