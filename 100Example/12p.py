def evenNumbers():
    numList=[]
    #num=[x for x in input("enter number").split(",")]
    for val in range(1000,3001):
        if(((val)>1000) and ((val)<3001)):
            if(int(val)%2==0):
                numList.append(str(val))
    return(",".join(numList))

def gitevenNumbers():
    values = []
    for i in range(1000, 3001):
        s = str(i)
        print(s[0],s[1],s[2],s[3])
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
            values.append(s)
    print(",".join(values))


print(evenNumbers())
gitevenNumbers()


