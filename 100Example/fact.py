def factval(val):
    f=1
    for i in range(1,val+1):
        f=f*i;
    print(f)

factval(8)


def fact1(n):
    if n==0:
        return 1

    return n*fact1(n-1)
print(fact1(8))