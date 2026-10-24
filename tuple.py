print("Tupple in python")
# tuple is a collection of data which is ordered and unchangeable
# tuple is a built in data type in python
a=() # empty tuple
b=(1,2,3) # tuple with elements
c=("apple","banana","cherry") # tuple with strings
print(a)
print(b)
print(c)

print("===========================================================")

# slicing in tuple is same as list slicing
a=(1,2,3,4,5)
print(a[1:4])# they will print 2,3,4
print(a[ :4]) # they will strt 0 and end on 4
print(a[1 :] ) # they will strt from 1 and end where the list end
print(a[-3:-1]) # they negative sign act as a revrse

print("===========================================================")
# indexing in tuple is same as list indexing
a=(1,2,3,4,5)
print(a[0]) # they will print 1
print(a[1]) # they will print 2
print(a[2]) # they will print 3
print(a[3]) # they will print 4
print(a[4]) # they will print 5

print("===========================================================")

# tuple methods are same as list methods but we can not change the 
# value of tuple because tuple is immutable

# 1 # count method is used to count the number of occurrences of an element in a tuple
a=(1,2,3,4,5,1,2,3,4,5)
print(a.count(1)) # they will print 2

#2 # index method is used to find the index of an element in a tuple
a=(1,2,3,4,5,1,2,3,4,5)
print(a.index(1)) # they will print 0

# 3 # len method is used to find the length of a tuple
a=(1,2,3,4,5,1,2,3,4,5)
print(len(a)) # they will print 10
