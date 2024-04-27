l=[1,2,1.1,2.2,"tops",True,"python",10,20,1,2,"java",False,100,200,400,60]

print(len(l))
print(l[1:3:4])       #1,2
print(l[15::5])       #400
print(l[:1:5])        #1
print(l[::10])        #1,2
print(l[10:15])       #2,"java",False,100,200


print(l[-17:-15:3])   #1
print(l[-7::7])       #2
print(l[:-16:12])     #1
print(l[::-5])        #60,"java","python",2
print(l[-14:-12])     #2.2,"tops"

for i in l:
    print(i)
print(10 in l)
