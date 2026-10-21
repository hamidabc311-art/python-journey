# conditional statement
#conditional statements are used to perform different actions based on different conditions.

#type of conditional statements
  # 1. if statement
if 3>1:
    print ("greator ")
    # when the conditon is ture the print greator if condtiton is wrong it did not show anything in output 

print ("if-else statment")
number=int (input("entir your number :"))
if 67>number:
    print("the number is smalller")
else :
    print("the number is greator")


print("====================================================================================")

# problem 1
# write a program to check if a number is positive, negative or zero

number= int(input("entir the number:"))
if number>=1:
    print ("the number is positive:")
else:
    if number==0:
        print ("the number is zero:")
    else:
        print ("the number is negative:")


print("=========================================================================")

# problem 2
# write a program to check if a number is even or odd

number = int(input("entir your number:"))
if number %2==0:
    print ("the number is even:")
else:
    if number %2==1:
        print ("the nunber is odd:")

print ("===================================================================")

#problem 3
# write a progarm to cheak the mobile password is correct or not

password = int(input("entir your password:"))
if password ==(7777):
    print (" the password is correct:")
else :
    if password != (7777):
        print ("the password is incorrect:")
