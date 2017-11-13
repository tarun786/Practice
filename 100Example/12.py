def binarytodecimal(binaryNum):
    binVal=binaryNum.split(",")
    #print(binVal)
    #binaryNum=binaryNum[::-1]
    result=0
    allResults=[]
    listofBinLen=len(binVal)
    for singleBinValue in binVal:
        result = 0
        for ii in range(len(singleBinValue)-1,-1,-1):
            result=result + int(singleBinValue[len(singleBinValue)-1-ii])*pow(2,ii)
        if(int(result)%5==0):
            allResults.append(singleBinValue)
    return " ".join(allResults)


input="1111,1010,0101,1001"

print(binarytodecimal(input))