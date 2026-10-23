# TODAY I WILL LERAN THE LIST OF PYTHON
print ("list  in  python")
# list is a built in  data type where we store value
# it  can store  the value of dfiffernt data type (int ,flot , and string etc)
a=[]
b=[1,2,3,4,5]
c=["apple","banana","mango"]
print(a)
print(b)
print(c)
print("==========================================================")

# list is a mutable data type we can change the value of list
a=[1,2,3,4,5]
a[2]=10  # changing the value at index 0
print(a)

print("==========================================================")


print(" list slicing")
# list slicing is used to get the sub list from the list
# for example
marks=[97,34,67,23,88]
print(marks[2:5])# they will print 67,23,88
print(marks[ :5]) # they will strt 0 and end on 5 
print(marks[1 :] ) # they will strt from 1 and end where the list end
print(marks[-3:-1]) # they negative sign act as a revrse


print("===========================================================")

print("Method in list")

# appending mean add somethig into list at end
t=[1,4,6,5,3]
t.append(7)
print(t)
print("===========================================================")

# sorting  mean the list in ascending order
t=[1,4,6,5,3] # the answer is [1,3,4,5,6]
t.sort()
print(t)
print("===========================================================")

# for desinding order we use reverse method
t=[1,4,6,5,3] # output will be [6,5,4,3,1]
t.sort(reverse=True)
print(t)
print("===========================================================")

# for completely reverse the list we use reverse method
t=[1,4,6,5,3] # output will be [3,5,6,4,1]
t.reverse()
print(t)
print("===========================================================")

# list insert method is used to insert the value at specific index
t=[1,4,6,5,3]
t.insert(2,10)  # inserting 10 at index 2
print(t)
print("===========================================================")

# for removing the value from list we use remove method
t=[1,4,6,5,3]
t.remove(6)  # removing 6 from the list
print(t)

print("===========================================================")

# list pop method is used to remove the last value from the list
t=[1,4,6,5,3]
t.pop(2) # removing the value at index 2
print(t)

print("===========================================================")
# we cover the list in python
