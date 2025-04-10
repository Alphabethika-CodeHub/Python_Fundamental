print("Most Values Are True :")
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print("")

print("Some Values Are False :")
print("Boolean :",bool(False))
print("None Type :",bool(None))
print("Integer :",bool(0))
print("String :",bool(""))
print("Tuple :",bool(()))
print("List :",bool([]))
print("Dictionary :",bool({}))

print("")

class MyClass():
    def __len__(self):
        return 0

my_obj = MyClass()
print("Class: ", bool(my_obj))

# Check if an Object is an Integer or Not
x = "Test"
print(isinstance(x, int))