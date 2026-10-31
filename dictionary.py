print("  Dictionary in python")
# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.

# properties of dictionary
# Dictionaries are unordered, mutable, and indexed collections. 
# Dictionaries are defined using curly braces {} and consist
#  of key-value pairs separated by colons (:).

# Example of a dictionary
d = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print ("Dictionary:", d)
print ("Name:", d["name"])
print (d["age"])

# methos of dictioary
# 1. Adding an item to a dictionary
d={"name": "John", "age": 30, "city": "New York"}
d["country"] = "USA"
print ("Updated Dictionary:", d)
# output: Updated Dictionary: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}

# 2. Removing an item from a dictionary
d={"name": "John", "age": 30, "city": "New York"}
d.pop("age")
print ("Updated Dictionary:", d)
# output: Updated Dictionary: {'name': 'John', 'city': 'New York'}

# 3. Accessing items in a dictionary
d={"name": "John", "age": 30, "city": "New York"}
print ("Name:", d["name"])
# output: Name: John

# 4. Iterating through a dictionary
# iterating means going through each item in the dictionary one by one.
#  You can iterate through a dictionary using a for loop.
d={"name": "John", "age": 30, "city": "New York"}
for key in d:
    print (key, ":", d[key])
    # output will be:
# name : John
# age : 30
# city : New York

# 5. Checking if a key exists in a dictionary
d={"name": "John", "age": 30, "city": "New York"}
if "name" in d:
    print ("Name exists in the dictionary")

# 6. Getting the length of a dictionary
d={"name": "John", "age": 30, "city": "New York"}
print ("Length of dictionary:", len(d))
