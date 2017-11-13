def sortalfanumericlist(inputList):
    output=list(set(inputList.split(" ")))
    output.sort()
    return " ".join(output)

values="rajdeep is sitting next tb tarun and tarun is next sitting tb rajdeep"
# rajdeep is sitting next to tarun and
#and is next rajdeep sitting to tarun
print(sortalfanumericlist(values))

