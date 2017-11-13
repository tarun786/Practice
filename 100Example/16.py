def oddnumSquare():
    allOddNum=[]
    allNumbers=[x for x in input("Enter the num").split(",")]
    for num in allNumbers:
        if(int(num)%2==1):
            squareNum=int(num)*int(num)
            allOddNum.append(str(squareNum))
        else:
            pass

    print(",".join(allOddNum))


def gitoddnumSquare():
    numbers = [x for x in input().split(",") if int(x) % 2 != 0]
    
    print(",".join(numbers))

#oddnumSquare()
gitoddnumSquare()