def my_function():
  print("Hello from a function")


def my_arbitrary_function(*kids):
  print("The youngest child is " + kids[2])


my_arbitrary_function("Emil", "Tobias", "Linus")


# Built-in Function in Python
print("Hello")
len("Python")
type(123)


# User Defined Function
def greet(name):
    return f"Hello, {name}"

greet("John")


# Function With Parameter / Argument With Return Value
def addition(a,b):
    return a + b

addition(5, 7)


# Function Without Parameter
def say_hello():
    print("Hello, World!")


# Recursive Function
def factorial(n):
    if n == 1:
        return 1
    else :
        return n * factorial(n - 1)

print("Factorial: ", factorial(12))

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)