
list1=[]
val=""

values=(input("enter the name").split(","))
values.sort()
print(','.join(values))
'''for x in sorted(values):
    list1.append(x)
    val=",".join(list1)
'''
print(val)


#git
items=[x for x in input().split(',')]
items.sort()
print(','.join(items))