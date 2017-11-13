def findalphanumeric():
    letter=[]
    numeric=[]
    countNum=0
    countLetter=0
    inputVal=input("enter the string")
    for x in inputVal:
        ordval=ord(x)
        #print(x)
        if(ordval>=48 and ordval<=57):
            countNum=countNum+1
        if(ordval>=97 and ordval<=122):
            countLetter=countLetter+1
    print("LETTERS {0} ".format(countLetter))
    print("DIGITS {0}".format(countNum))


def gitalphanumeric():
    s = input("Enter input")
    d = {"DIGITS": 0, "LETTERS": 0}
    for c in s:
        if c.isdigit():
            d["DIGITS"] += 1
        elif c.isalpha():
            d["LETTERS"] += 1
        else:
            pass
    print("LETTERS", d["LETTERS"])
    print("DIGITS", d["DIGITS"])
findalphanumeric()
gitalphanumeric()