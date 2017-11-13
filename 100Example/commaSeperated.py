def commaSep(values):
    valList=[]
    valDict={}
    #for x in range(len(values.split(","))):

    valList=values.split(",")
    valDict=tuple(valList)

    print(valList)
    print(valDict)
num=(input("entet the value"))
commaSep(num)