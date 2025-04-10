my_cars = ['Ford', "Volvo", "Suzuki", "Honda", "Hyundai"]

# Accessing Array
print(my_cars[0])

# Modify Array From Specified Index
my_cars[0] = "Toyota"

print("Modified Cars: ", my_cars, len(my_cars))

# Looping an Array
for x in my_cars:
    print(x)

# Adding Data to Array
my_cars.append("Caterpillar")

# Removing Array by Index Element
my_cars.pop(3)

# Removing Array by Specified Element
my_cars.remove("Suzuki")

print("Removed Elements: ", my_cars)

print("Reference to Array Methods: https://www.w3schools.com/python/python_arrays.asp")
