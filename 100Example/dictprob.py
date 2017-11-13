list1=[]
squares={x: x*x for x in range(1,8)}
print(squares)

#method2
squares={}
for x in range(1,11):
    if x%2==1:
     squares[x]=x*x
print(squares)

#method 3
odd_square={x: x*x for x in range(11) if x%2==1}
print(odd_square)