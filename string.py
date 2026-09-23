# today i lern strings

print ("==================================================")

print ("1. String creation")
s1= "Hello, World!" # double quotes
s2= 'name' # single quotes
s3= """
this is used for multiple line string

"""
print (s1,s2,s3)

print("====================================================")

print ("2. Length of string ")

# in this we find the lenght of string

string = "hamid khan"
print (len(string)) # 10

print ("======================================================")

print("3. String indexing")
string= " hamid"
print (string[-5]) # h
print (string[+5]) # d

print ("=======================================================")
print ("4. String slicing")
# in this we slice the string and get the part of string
# string[start:stop:step]
string = "i lern the python"
print (len(string))
print (string[0:5]) # i lern
print (string[6:9]) # the
print (string[10:16]) # python
print (string[0:16:2]) # i er h yhn

print ("========================================================")

print ("5. string repetition")
# in this we repeat the string
string = "hamid khan "
print (string*6) # hamid khan hamid khan hamid khan hamid khan hamid khan hamid 

print ("=========================================================")

# string concatenation
# in this we join the string
s4 = "Hello"
s5 = "World"
s6 = s4 + " " + s5
print(s6)

print ("==========================================================")
# string membership
# in this we check the string is present or not
string = "hamid khan"
print("hamid" in string) # True
print("khan" in string) # True
print("Alice" in string) # False

print ("===========================================================")

# string methods
# in this we use the string methods
string = "Hello, World!"
print(string.upper()) # HELLO, WORLD!
print (string . capitalize()) # Hello, world!
print (string.lower()) # hello, world!

print ("=============================================================")

print ("6. String formatting")
# in this we format the string
name = "Alice"
age = 25
print(f"Hello, my name is {name} and I am {age} years old.")


