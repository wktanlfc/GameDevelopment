# .py files are Python scripts that contain Python codes. Python scripts can
# be run in interactive REPL mode.
# Go to File > Preferences > Settings.
# Search and enable the setting jupyter.sendSelectionToInteractiveWindow
# Point the cursor at line 4 and press Shift+Enter to run the line of code and
# see the results immediately in the interactive window.
print("Hello world! Welcome to the NCS Nucleus Data Science Bootcamp!")


# Python comes with various features common to modern programming languages.
# Learn more about Python at websites such as
# https://www.w3schools.com/python/.


# Variables
# Python variables are created and stored in Python's working memory by
# assigning a value to it. They are dynamically typed; the programmer does not
# need to explicitly set the variable data type.
var_a = "Variable A"
var_b = "Variable B"
var_a + var_b
var_a = 1
var_b = 2
var_a + var_b


# If then else
# Python uses identation to separate code blocks instead of curly braces used
# in other programming languages. To run the follow codes, highlight the entire
# section and press Shift+Enter.
if var_a > var_b:
    print("var_a is greater than var_b")
elif var_a < var_b:
    print("var_a is greater than var_b")
else:
    print("var_a is equal to var_b")

if var_a == 1 and var_b == 2:
    print("Variable A is 1 and variable B is 2")
else:
    print("Did you set the variable values correctly?")


# Lists
# Lists is a data structure that stores multiple values in a single variable.
# Use square braces to create lists.
car_list = ["Toyota", "Mercedes", "Honda", "BMW"]
# Indexing starts from 0.
car_list[0]
# Use the colon operator (:) to slice out elements in the list.
# [from_inclusive:to_exclusive]
car_list[1:3]
# Python lists can contain mixed data types.
mixed_list = ["string", 123]
mixed_list


# For loops
for car in car_list:
    print(car)


# Dictionaries
# Dictionary is a data structure that contains a collection of key-value pairs.
# Use curly braces {} and colons : to create dictionaries.
# {key_1:value_1, key_2:value_2}
my_dictionary = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dictionary["model"]
my_dictionary["year"] = 2020
my_dictionary


# Functions
# Functions contain reusuable codes. Functions can be defined with parameters.
# Data can be passed into functions for processing.
def my_multiplication_function(a, b):
    return a * b


my_multiplication_function(3, 6)
my_multiplication_function(var_a, var_b)


# Classes and objects
# Classes and objects are central to a concept called "object oriented
# programming", which is a way of organising programming codes into objects
# that contain data (properties) and have a set of behaviour (functions).
# Think of classes like a cooking recipe, and objects like a dish created using
# the recipe.
class NucleusCat:
    # The __init__ function is automatically called when we create a new
    # NucleusCat object. The self variable refers to the NucleusCat object
    # itself. When we create a NucleusCat object, we can give it a name.
    def __init__(self, name_by_owner):
        self.name = name_by_owner

    # A NucleusCat can meow and say its name.
    def meow(self):
        print("Meow! My name is " + self.name + "!")

    # A NucleusCat can eat food.
    def eat(self, food):
        print(self.name + " is eating " + food + "...")


# Create a new NucleusCat, give it a name and store it in the my_cat variable.
my_cat = NucleusCat("Grumpy Cat")
# Access the name property of my_cat.
my_cat.name
# Call the meow function of my_cat.
my_cat.meow()
# Call the eat function of my_cat.
my_cat.eat("tuna")

# We can create another NucleusCat.
my_other_cat = NucleusCat("Nala")
my_other_cat.name
my_other_cat.meow()
my_other_cat.eat("kibbles")

# Besides running Python codes in interactive REPL mode, Python codes can be
# embedded in formatted documents called Jupyter Notebooks with file extension
# .ipynb. These documents can contain Python codes, formatted text and images,
# and can be an effective way to share your data analysis ideas and results
# with your colleagues.
