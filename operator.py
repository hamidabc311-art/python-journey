# today i learn all type of operators in python
""""

from operator import is_


print("===========================================")
print ("1. Arithmetic operators")
# in this we perform basic mathimatical operatiion

print (" ADDTION")
x=2
y=4
print ("THE ANSWER OF X AND Y IS :" ,(x+y)) # anwser = 6
print("===========================================")

print (" SUBTRICTION")
a = 7
b= 9
print ("THE ANSWER OF a AND b IS :" ,(a-b)) # anwser = -2
print("===========================================")

print (" MULTIPLACTION")
c = 5
d = 6
print ("THE ANSWER OF c AND d IS :" ,(c*d)) # anwser = 30
print("===========================================")

print (" DIVISION")
e = 10
f = 2
print ("THE ANSWER OF e AND f IS :" ,(e/f)) # anwser = 5.0
print("===========================================")

print (" MODULUS") # reminder 
g = 10
h = 3
print ("THE ANSWER OF g AND h IS :" ,(g%h)) # anwser = 1
print("===========================================")

print (" EXPONENTIAL")
i = 2
j = 3
print ("THE ANSWER OF i AND j IS :" ,(i**j)) # anwser = 8
print("===========================================")

print (" FLOOR DIVISION") # means how many times the divisor fits into the dividend
k = 17
l = 2
print ("THE ANSWER OF k AND l IS :" ,(k//l)) # anwser = 8
print("===========================================")

print ("2. Comparison operators")
# in this we compire two value and give answer in boolen
x=5
y=8

print (x==y) # false
print (x != y)# true
print (x>y)# false
print (x<y) # true
print (x>=y) # false
print (x<=y) # true
""

print ("===========================================")
print ("3. Logical opreaetor")
# this is used for combine multiple condition and it give answer in boolean
"""
""""
and _ all conditon will true than it give true return 
or _  at list give one condition ture than it give true return
not _  is reverse oprend 
suppose the conditon is ture the not opretor make him false 
and to false condtion convert to true seem it work as reverse
"""

 
age = 19
is_hamid = True

print (age>18 and is_hamid)
print (age<18 or is_hamid)
print ( not is_hamid)