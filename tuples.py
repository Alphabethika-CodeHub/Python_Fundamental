my_tuple = ("Apple", "Banana", "Cherry", "Orange", "Kiwi", "Mango", "Strawberry", "Blueberries", "Blackberries", "Papaya")
my_random_tuple = ("abc", 34, True, 40, "male")

# Create a Tuple With 1 Item
# Don't Forget With The Comma
single_tuple_1 = ("apple",) # This is Tuple
print(type(single_tuple_1))

# NOT a tuple
single_tuple_2 = ("apple") # This is String
print(type(single_tuple_2))

# Create Tuple With Constructor
my_constructed_tuple = tuple(("A", "B", "C"))
print("Tuple Constructor: ", my_constructed_tuple)

print("Accesing Tuple Similar to Lists: https://www.w3schools.com/python/python_tuples_access.asp")

print("""
Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
""")
x = ("Apple", "Banana", "Cherry")
y = list(x)
y[1] = "Kiwi"
x = tuple(y)
print(x)

print('Tuple Manipulation Needs to Convert The Tuple to List')

# Unpacking a Tuple
# Using * to Assign All Unused Item
# (fruit_a, fruit_b, *fruit_c) = my_tuple
(fruit_a, *fruit_b, fruit_c) = my_tuple
print("Destructuring a Tuple: ", fruit_a, fruit_b, fruit_c)

print("Looping a Tuple is Similar to Looping a Lists")

# Join a Tuple
print("Joining a Tuple")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print("""
Tuple Methods :
------------------------------------------------------------------------------------------------ 
Method	    Description
------------------------------------------------------------------------------------------------
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
""")


