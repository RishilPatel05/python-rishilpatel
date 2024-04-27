sname=input("enter student name:")
rno=int(input("enter roll no:"))
s1=int(input("enter the marks of subject 1:"))
s2=int(input("enter the marks of subject 2:"))
s3=int(input("enter the marks of subject 3:"))

total=s1+s2+s3
per=total/3

print("student name :",sname)
print("roll no :",rno)
print("total :",total)
print("percentage :",per)

if per>=70:
    print("distinction")
elif per>=60:
    print("first class")
elif per>=50:
    print("second class")
else:
    print("fail")
