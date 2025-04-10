# Greeting!
import random

print("Hello","World")

# Using Variables And Casting
# And Variables That Created Outside of a Function
# is a Global Variables
a = 10
b = str(3)

# Single or Double Quote Are The Same
c = int("10")
d = float("2")

# Variable Are Case-Sensitive
E = bool("false")

# Legal Variable
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Many Values to Multiple Variables
f, g, h = "Orange", "Watermelon", "Strawberry"

# Unpacking (Like Object Destructuring in JavaS
fruits = ['Apple', "Banana", 'Cherry']
i,j,k = fruits

myObj = {"name": "John", "age": 36}

# DataTypes in Python
aa = "Hello World"                              # str           String
ab = 20                                         # int           Integer
ac = 20.5                                       # float         Float
ad = 1j                                         # complex       Complex
ae = ["apple", "banana", "cherry"]              # list          List
af = ("apple", "banana", "cherry")              # tuple         Tuple
ag = range(6)                                   # range         Range
ah = {"name" : "John", "age" : 36}              # dict          Dictionary
ai = {"apple", "banana", "cherry"}              # set           Set
aj = frozenset({"apple", "banana", "cherry"})   # frozenset     Frozen Set
ak = True                                       # bool          Boolean
al = b"Hello"                                   # bytes         Bytes
am = bytearray(5)                               # bytearray     Byte Array
an = memoryview(bytes(5))                       # memoryview    Memory View
ao = None                                       # NoneType      None Type

# Get Type of Var
print(type(a), type(b), type(c), type(d), type(E), type(fruits), type(myObj))
print(a,b,c,d,E,f,g,h,i,j,k)

# Condition
if a > 5:
    print("YES")
else:
    print("NO")

# Function
def myFunc():
    # This Variables Will Remains Local, And The Global One Will Still Original
    myFruit = "Fruits"
    global myGlobalVarFromFunc # This Can Change The Value of Global Variables
    myGlobalVarFromFunc = "This is Global From Function"
    print("Python is " + myFruit)

myFunc()

def myRandomNumberGenerator():
    print(random.randrange(1, 10))

myRandomNumberGenerator()

