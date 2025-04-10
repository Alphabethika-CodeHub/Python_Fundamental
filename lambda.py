# Syntax
# lambda argumen1, argumen2, ... : ekspresi

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_fruits = [(1, 'Apple'), (3, 'Orange'), (2, 'Banana')]

addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
division = lambda x, y: x / y

print("addition: ", addition(10, 10))
print("subtraction: ", subtraction(10, 10))
print("division: ", division(10, 10))

result_a = list(map(lambda x: x * 2, my_numbers))
result_b = list(filter(lambda x: x % 2 == 0, my_numbers))
result_c = sorted(my_fruits, key=lambda x: x[1])

print("result_a: ", result_a)
print("result_b: ", result_b)
print("result_c: ", result_c)
