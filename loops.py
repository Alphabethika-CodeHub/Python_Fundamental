# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
while i < 6:
  print(i)
  i += 1


# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


# Looping With for Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  elif x == "cherry":
    print("cherry")
    break
  else:
    print(x)


# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

