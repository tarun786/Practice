#Tarun
list1=[]
for num in range(2000,3201):
    if((num%7==0) and (num%5!=0)):
       print(num,end=",")


#GitHub
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))