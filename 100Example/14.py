def upperandlowercaseCount():
    inputVal=input("enter the string")
    d={"UPPER CASE":0,"LOWER CASE":0}
    for x in inputVal:
        if(x.isupper()):
            d["UPPER CASE"]+=1
        elif(x.islower()):
            d["LOWER CASE"]+=1
        else:
            pass
    print("UPPER CASE",d["UPPER CASE"])
    print("LOWER CASE",d["LOWER CASE"])

upperandlowercaseCount()
