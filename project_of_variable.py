# Student grade calculator
print("============================================================")
student = input("student name:")
# hamid khan
print (student)

subject1=input("first subject marks :")
# marks is 66
subject2=input("second subject marks:")
# marks is 77
subject3=input("third subject marks:")
# marks is 88


total_marks=300
obtain_marks=int(subject1)+int(subject2)+int(subject3)
# obtain marks is 66+77+88=231

passing_marks=250
print("total marks:",total_marks)
print("obtain marks:",obtain_marks)
print("passing marks:",passing_marks)
# so hamid khan get less than passing marks
print("hamid is fail")