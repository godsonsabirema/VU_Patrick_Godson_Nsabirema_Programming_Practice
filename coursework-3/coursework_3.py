# author - Patrick Godson Nsabirema 

# conditional statements (if-else, nested conditions)
a, b = 3, 3 # variables

if a > b:
    print("a greater than b")
elif a < b:
    print("a less than b")
else:
    print("a equal to b \n")


# loops (for-while, and iteration)
animals = ["lion", "elephant", "tiger", "zebra \n"]

for animal in animals: # for loop
    print(animal)

count = 0
while count < 5: # while loop
    print(count)
    count += 1


# functions
def sum_function(a,b):
    print("\nThis function calculates the sum of two numbers.")
    print(f"It took in {a} and {b} as parameters,")
    print(f"and found their sum to be {a + b}.\n")

sum_function(2, 3)


sum = lambda x, y: x + y # lambda function
print(sum(4, 7))

check_if_positive = lambda num: "\npositive" if num > 0 else "negative" # lambda with condition
print(check_if_positive(2))


def write_animals(n): # recursive function
    animals = ["lion", "tiger", "zebra"]
    if n < len(animals):
        print(animals[n], end = " ")
        return write_animals(n + 1)
    else:
        return

write_animals(0)

# lists
fruits = ["orange", "mango", "apple"]
numbers = [1, 2, 3, 4, 5]
fruits.append("lemon")
fruits.count("orange")
fruits.reverse()
print(fruits)
print(fruits[0:2])

# sets
set1 = {1, 2, 2, 3, 4, 5}
set2 = set([6,7, 8, 9, 10])
print(set1)
print(set2)

# tuples
tuple1 = (1, 2)
print(tuple1)
a, b = tuple1
print(a, b)

# dictionaries
car = {
    "brand": "toyota",
    "model": "corolla",
    "year": 2020
}

print(car)
print(car["brand"])

# OOP - object oriented programming
class Man: # example of a class
    gender = "male"
    has_wife = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

new_man = Man("patrick", 22) # an instance of the class Man
print(new_man.name, new_man.age, new_man.gender)

class Boy(Man): # inheritance in python
    has_wife = False

new_boy = Boy("godson", 22)
print(new_boy.name, new_boy.age, new_boy.has_wife)


# numpy
import numpy as np
food = ["matooke", "rice", "chicken", "meat"]
fd = np.array(food) # creating numpy array from list
print(fd)

randomn_int_array = np.random.randint(0, 5, size = (2, 2)) # generating a random array of integers
print(randomn_int_array.shape)
print(randomn_int_array)

# pandas
import pandas as pd

marks = [10, 20, 30, 40, 50]
df = pd.DataFrame(marks) # creating a pandas dataframe from list
print(df)

df = pd.DataFrame(marks, index=["ten", "twenty", "thirty", "forty", "fifty"]) # assigning custom indices
print(df)