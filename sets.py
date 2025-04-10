my_set = {"Apple", "Banana", "Cherry", "Watermelon", "Melon", "Strawberry", "Pear"}
my_sec_sets = set(("Apple", "Banana", "Cherry"))

# Accessing a Sets
for x in my_sec_sets:
    print(x)

# Once a set is created, you cannot change its items, but you can add new items.
my_sec_sets.add("Melon")

# Using 'update' to Combine Sets
tropical = {"Pineapple", "Mango", "Papaya"}
my_sec_sets.update(tropical)
print(my_sec_sets)

# Different Ways to Remove a Sets
# Using remove() If the item to remove does not exist, remove() will raise an error.
# Using discard() If the item to remove does not exist, discard() will NOT raise an error.
# Using pop() Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
# Using clear()
# Using del

# Joining a Sets
print("""
Joining a Sets :
There are several ways to join two or more sets in Python.
The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates.

Reference: https://www.w3schools.com/python/python_sets_join.asp
""")

# You can use the | operator instead of the union() method, and you will get the same result.
set_a_1 = {"a", "b", "c"}
set_a_2 = {1, 2, 3}
set_a_3 = set_a_1.union(set_a_2)
print("Using Union to Joining a Sets: ", set_a_3)

# Joining a Multiple Sets
set_b_1 = {"a", "b", "c"}
set_b_2 = {1, 2, 3}
set_b_3 = {"John", "Elena"}
set_b_4 = {"apple", "bananas", "cherry"}

# There is 2 Other Ways to Joining a Sets
my_b_set = set_b_1.union(set_b_2, set_b_3, set_b_4)
# my_b_set = set_b_1 | set_b_2 | set_b_3 |set_b_4
print("Multiple Joining Sets: ",my_b_set)

# Set Methods
print("""
Set Methods :
-------------------------------------------------------------------------------------------------------------------------------------
Method	                            Shortcut	    Description
-------------------------------------------------------------------------------------------------------------------------------------
add()	 	                                        Adds an element to the set
clear()	 	                                        Removes all the elements from the set
copy()	 	                                        Returns a copy of the set
difference()	                    -	            Returns a set containing the difference between two or more sets
difference_update()	                -=	            Removes the items in this set that are also included in another, specified set
discard()	 	                                    Remove the specified item
intersection()	                    &	            Returns a set, that is the intersection of two other sets
intersection_update()	            &=	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                                Returns whether two sets have a intersection or not
issubset()	                        <=	            Returns whether another set contains this set or not
 	                                <	            Returns whether all items in this set is present in other, specified set(s)
issuperset()	                    >=	            Returns whether this set contains another set or not
 	                                >	            Returns whether all items in other, specified set(s) is present in this set
pop()	 	                                        Removes an element from the set
remove()	 	                                    Removes the specified element
symmetric_difference()	            ^	            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	    ^=	            Inserts the symmetric differences from this set and another
union()	                            |	            Return a set containing the union of sets
update()	                        |=	            Update the set with the union of this set and others
""")

