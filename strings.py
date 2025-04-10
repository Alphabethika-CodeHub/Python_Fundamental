# Strings Are Array
greet = "Hello World!"
print(greet[0], "This is The First Array of a Var Named 'greet'")

# Looping Through a String
my_abc = 'ABC'
for x in my_abc:
    print(x)

print("Length of a String: ", len(my_abc))

# Check if String Contains Provided Text
print("B" in my_abc, "Its True Because 'my_abc' Contain 'B' Character")
print("B" not in greet, "Its False Because 'greet' is Not Contain 'B' Character")

# Slicing a String
print(greet[1:5])

# Slice From Start
print(greet[:5])

# Slice to The End
print(greet[6:])

# Negative Indexing
print(greet[-6:-1])

# Uppercase & Lowercase
print(greet.upper(), greet.lower())

# Remove Whitespace or Stripping a String From Start And End
# From " Hello, World! "
# To "Hello, World!"
print(greet.strip(''))

# Replace String
print(greet.replace("H", "J"))

# Split a String
print(greet.split())

# Escape Characters
# Code	    Result
# \'	    Single Quote
# \\	    Backslash
# \n	    New Line
# \r	    Carriage Return
# \t	    Tab
# \b	    Backspace
# \f	    Form Feed
# \ooo	    Octal value
# \xhh	    Hex value

print("String Methods Reference: https://www.w3schools.com/python/python_strings_methods.asp")