def transactionBankLog():
    transactionType={"D":0,"W":0}
    netAmount=0
    givenLog=[x for x in input("Enter The transaction value").split(" ")]
    totolDeposit=0
    totalWithdraw=0
    print(givenLog)
    for x in range(len(givenLog)):
        transactionType["D"]=[givenLog[x]]
        netAmount+=int(givenLog[x])
    #print(totolDeposit)

    givenLog = [x for x in input("Enter The withdraw value").split(" ")]

    for y in range(len(givenLog)):
        transactionType["W"]=[givenLog[y]]
        netAmount-=int(givenLog[y])
    #print(totalWithdraw)

    print(netAmount)
    print(transactionType)


def gitTransactionBankLog():
    netAmount = 0
    while True:
        s = input()
        if not s:
            break
        values = s.split(" ")
        operation = values[0]
        amount = int(values[1])
        if operation == "D":
            netAmount += amount
        elif operation == "W":
            netAmount -= amount
        else:
            pass
    print(netAmount)

transactionBankLog()
gitTransactionBankLog()
