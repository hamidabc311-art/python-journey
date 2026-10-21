# Today i lern the loop in detail with all type
print(" what is loop")
# loop is the sturture with help we repite the bloak of code multiple time
# types of loop is 
print("while loop")
# while loop repit the code  until unless the condition the true 

v = 1
while v <=11 :
    print (v)
    v+=3
# this will stop the code when the condition become false as u see in example 
# bcz the condition become false on 11 thats why it stop 


# so we many question thorough which we lern this 
# print number from 1 to 100 
i = 0 
while i<=100:
    print (i)
    i+=1
    
# question 2
# print number from 100 to 1
i = 100
while i>=1:
    print (i)
    i -=1

# print the following list using loop
#[1,4,9,16,25,36,49,64,81,100]
number=[1,4,9,16,25,36,49,64,81,100,]
idx=0
while idx< len(number):

    print (number[idx])
    idx+=1
    
# what is break and continoue statement in while loop 
# break statement is used to break the loop when the condition become true
i=0
while i<=10:
    print (i)
    if (i==9):# this will stop on 9 and print from 0 to 9
        break
    i+=1
  
# continoue statment is used to skip the current iteration and
#  continue with the next iteration of the loop
i = 0
while i<=15:
    if (i==10):# this will skip the 10 and print from 0 to 15 except 10
        i+=1
        continue
    print (i)
    i+=1
    
      
    #questio print only even number from 1 to 10
a=1
while a<=15:
    if (a%2 !=0):
       a+=1
       continue
    print (a) 
    a+=1

print("For loop")
# A for loop repeats code for each item in a sequence.(list, tuple, string)
a=[1,2,3,4,5,6]
for list in a:
    print (list) # this is sytenx is for string and tuple 
    
i='hamidkhan'
print (len(i))
for num in i:
    if num=='d':
        
        break
    print(num)
     
print("Range in loop")
# range function () return the squense  of number from 0 by defult  and increment by 1 
# by deflut and stop before a sepicefied number
# range (start,stop,step)
for i in range(2,78,5):
    print(i)
    
# questuin 
# print the multiple table of n

a=int(input("entir the number :: "))
for i in range(1,11):
    print(a*i) # the anser will be 5 to 50 

 
# last assigment of loop 
# write the programe from which find the facotrial of first natural number(using for loop)
n=3
fact=1

for  i in range(1,n+1):
    fact*=i
    print(fact )