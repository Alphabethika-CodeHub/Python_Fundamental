my_list = ["Apple", "Banana", "Cherry"]
my_list_two = list(("abc", 34, True, 40, "male"))
change_my_list = ["Apple", "Banana", "Cherry", "Orange", "Kiwi", "Mango"]
extend_my_list = ["Pineapple", "Melon", "Papaya"]

print(my_list, my_list_two)
print("Length of a List: ", len(my_list), len(my_list_two))

# Accesing Lists
print(my_list[0], my_list[-1])
print(my_list[1:3])
print(my_list[:2])

# Check if Item
if "Apple" in my_list:
    print("YES!, Apple is in 'my_list'")

# Change a Range of Item Values
change_my_list[1:3] = ["Blackcurrant", "Watermelon"]
print("Change a Range of Item Values: ",change_my_list)

# Insert Item, Adding Item in Specified Index
change_my_list.insert(1, "Pear")
print("Insert Pear to The List: ", change_my_list)

# Append Item, Adding Item to The End of The List
change_my_list.append("Strawberry")
print("Append Strawberry to The List: ", change_my_list)

# Extend List, Like Concate an Array in Javascript
extend_my_list.extend(change_my_list)
print("Extended List: ", extend_my_list)

# Adding Any Iterable
my_tuple = ("Ay", "Clap")
extend_my_list.extend(my_tuple)
print("Adding Any Iterable to The List: ", extend_my_list)

# Removing With Specified Item
extend_my_list.remove("Ay")
extend_my_list.remove("Clap")
print("Removed Some of Items: ", extend_my_list)

# Removing With Specified Index
extend_my_list.pop(0)
# extend_my_list.pop() # Removing Last Item in The List
print("Remove Some Item With 'pop' Method: ", extend_my_list)

# Remove Variable Entirely From Memory
# del extend_my_list
# print("Removing All The Items in The List: ", extend_my_list)

# Clearing an List
# extend_my_list.clear()
# print("Cleared List: ", extend_my_list)

# Looping a List
print("Looping a List: ")
i = 0
for x in my_list:
    i += 1
    print(i, "-", x)

# Looping Through The Index Numbers
print("Looping Through The Index Numbers: ")
for x in range(len(my_list)):
    print(x, "-", my_list[x])

# Using a While Loop
print("Using a While Loop: ")
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# Looping Using List Comprehension
print("Looping Using List Comprehension: ")
[print(x) for x in my_list]


# List Comprehension
# List comprehension offers a shorter syntax when you want to
# create a new list based on the values of an existing list.
# Reference: https://www.w3schools.com/python/python_lists_comprehension.asp

new_list = []
# Long Way to do a Looping
for x in extend_my_list:
    if "p" in x:
        new_list.append(x)

# Short Way to do a Looping
new_short_list = [x for x in extend_my_list if "p" in x]
print(new_short_list)

# Sorting a Lists
print("Sorting a Lists")
my_numbers = [5,10,24,136,120,15,1,43,566,12,5,326,1234,67,4,0]
my_numbers.sort()
extend_my_list.sort()
# extend_my_list.sort(reverse=True) # Descending
print("Sorted Lists: ", my_numbers)
print("Sorted Lists: ", extend_my_list)

# Customize Sort Function
def my_custom_sort(n):
    return abs(n - 50)

my_numbers.sort(key=my_custom_sort)
print("Customize Sort Function: ", my_numbers)

# Reversing a Lists
extend_my_list.reverse()
print("Reversed List: ", extend_my_list)

# Different Ways to Copy a List
print("Different Ways to Copy a List")
copied_extended_list_1 = extend_my_list.copy()
copied_extended_list_2 = list(extend_my_list)
copied_extended_list_3 = extend_my_list[:]

print("1 Copied List: ", copied_extended_list_1)
print("2 Copied List: ", copied_extended_list_2)
print("3 Copied List: ", copied_extended_list_3)

# Different Ways to Joining a Lists
joined_list = my_numbers + extend_my_list

for x in extend_my_list:
    my_numbers.append(x)

print("Joined List Using Loops: ", my_numbers)
print("And Using 'extend()'")

print("""
List Methods :
---------------------------------------------------------------------------------------------
Method	        Description
---------------------------------------------------------------------------------------------
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
""")