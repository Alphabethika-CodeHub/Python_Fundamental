import math
import os
import zipfile

myInt = 4
myFloat = 5.0
myPI = 3.14
myString = "Hello World!"

# Calculate Area of Rectangular.
REC_LENGTH = 5
REC_WIDE = 12
areaOfRectangular = REC_LENGTH * REC_WIDE
perimeterOfRectangular = 2 * (REC_LENGTH + REC_WIDE)
diagonalRectangular = math.sqrt((REC_LENGTH ** 2) + (REC_WIDE ** 2))
print("Area of Rectangular: " + str(areaOfRectangular))
print("Perimeter of Rectangular: " + str(perimeterOfRectangular))
print("Diagonal of Rectangular: " + str(diagonalRectangular))

# Concatenated String With Number
myString1 = "Hello "
myString2 = "World "
myInteger3 = 3.0
print(myString1 + myString2 + str(myInteger3))

MULTI_LINE_STRING = """ 
 This is
 Multiline
 String by Python!
 """


def score_checker(score):
    if type(score) == int:
        if score >= 40:
            print("Grade C")
        elif score >= 80:
            print("Grade B")
        elif score >= 90:
            print("Grade A")
        else:
            print("Learn is The Best Way!")
    else:
        print("Please Input Number!")

# Switch Statement Only Support at Python ^3.10
# def score_checker_switch(score):
    # match score

print("Using if Statement")
score_checker(40)

# Lists
print("")
my_arr = ["Pizza", "Spaghetti", "Bakwan"]
my_second_arr = ["Sushi", "Nasi Goreng"]
my_combined_array = my_arr + my_second_arr
print(my_combined_array, "Get One From arr: " + my_combined_array[2])

# 2D Array
my_last_grade_book = [["Math", 90], ["Arts", 90]]
grade_book = [["IPA", 90], ["Physics", 90], ["English", 90]]
final_grade_book = my_last_grade_book + grade_book
popped_grade_book = final_grade_book.pop()
final_grade_book.insert(10, ["Religion", 90])
print(final_grade_book)

# Using :n For Array
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:2]
middle = suitcase[2:4]
print(middle)

# List Comprehensions
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)

com_numbers = [2, -1, 79, 24, -50, 4]
double_com_numbers = [num ** 2 if num <= 0 else num * 3 for num in com_numbers]
print("double_com_numbers", double_com_numbers)

# Carly's Clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_revenue = 0
for price in prices:
    total_price += price

average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue))
average_daily_revenue = total_revenue / 7
print("Average Revenue: " + str(average_daily_revenue))
cuts_under_30 = [new_prices[i] for i in range(len(new_prices)) if prices[i] < 30]
print(cuts_under_30)

# Kinda Tricky
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [num for num in heights if num > 161]
print(can_ride_coaster)

# Functions With Strings
# def (Definition) Known as Function Header
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa," \
          "Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni "
author_names = authors.split(",")
separated_author_name = []


def seperated_names(author_names):
    for name in author_names:
        separated_author_name.append(name.split(" "))


print("Length Author Names: ", len(author_names))
print("Length Separated Author Names: ", len(separated_author_name))


def get_last_name(separated_author_name):
    index = 0
    name = []
    length_of_author = len(separated_author_name)
    while index <= length_of_author - 1:
        removed = separated_author_name[index].pop(-1)
        name.append(removed)
        index += 1
    return name


seperated_names(author_names)
author_last_names = get_last_name(separated_author_name)
print("Get The Last Name of Author: " + str(author_last_names))

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)


# Javascript Ternary Alike
def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
        publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc


my_beard_description = poem_description(author="Shel Silverstein", title="My Beard",
                                        original_work="Where the Sidewalk Ends", publishing_date="1974")

# Importing
# from matplotlib import pyplot as plt

# Read Microsoft Office
myDocument = zipfile.ZipFile(os.getcwd() + "\\uploads\\Test Soal.docx")
print(os.getcwd() + "\\uploads\\Test Soal.docs")
print(myDocument.read())

