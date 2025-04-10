# Creating a Dict
my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["Red", "White", "Black"]
}

my_sec_dict = dict(name = "John", age = 36, country = "Norway")

# Accessing a Dict
print(my_dict["brand"], len(my_dict))
print(my_sec_dict["name"], len(my_sec_dict))
print("Accessing Dict Using 'get' Method: ", my_dict.get("year"))

# The keys() method will return a list of all the keys in the dictionary.
my_dict_keys = my_dict.keys()
print("Dict Keys: ", my_dict_keys)

# The values() method will return a list of all the values in the dictionary.
my_dict_values = my_dict.values()
print("Dict Values: ", my_dict_values)

# The items() method will return each item in a dictionary, as tuples in a list.
my_dict_items = my_dict.items()
print("Dict Items: ", my_dict_items)

if "model" in my_dict:
  print("Yes, 'model' is one of the keys in the my_dict dictionary")

# Changing Dict Items
my_dict["brand"] = 'Suzuki'
my_dict.update({"year": 2020})
print("Changed Brand: ", my_dict)

# Adding Items in Dict
my_dict["colors"] = "Yellow" # NEED TO FIND OUT
my_dict["wheels"] = 4
my_dict.update({"fuel": "Gasoline"})
print("Added Items: ", my_dict)

# Removing Items in Dict
my_dict.pop("wheels")
my_dict.popitem()
del my_dict['brand']
# del my_dict # Completely Remove The Dict
print("Removed Items: ", my_dict)

# Looping a Dict
for x in my_sec_dict:
  print(my_sec_dict[x])

for x in my_sec_dict.values():
  print(x)

for x in my_sec_dict.keys():
  print(x)

for x, y in my_sec_dict.items():
  print(x, y)

# Copy a Dict
copied_dict = my_dict.copy()
print("Copied Dict: ", copied_dict)

# Nested Dicts
child_1 = {
  "name" : "Emil",
  "year" : 2004
}
child_2 = {
  "name" : "Tobias",
  "year" : 2007
}
child_3 = {
  "name" : "Linus",
  "year" : 2011
}

my_family = {
  "child_1" : child_1,
  "child_2" : child_2,
  "child_3" : child_3
}

print("Accessing Nested Dict: ",my_family["child_2"]["name"])

print("""
Dictionary Methods:
Python has a set of built-in methods that you can use on dictionaries.
----------------------------------------------------------------------------------------
Method	        Description
----------------------------------------------------------------------------------------
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. 
                If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
""")