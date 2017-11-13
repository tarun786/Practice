
def numComputes():
    num=str(input('ENTER THE NUMBER'))
    val=""
    newVal=0
    for x in range(1,5):
          val=num*int(x)
          #print(val)
          newVal+=int(val)
    print(newVal)

def gitnumComputes():
    a = input()
    n1 = int( "%s" % a )
    n2 = int( "%s%s" % (a,a) )
    n3 = int( "%s%s%s" % (a,a,a) )
    n4 = int( "%s%s%s%s" % (a,a,a,a) )
    print(n1,n2,n3,n4)
    print(n1+n2+n3+n4)
gitnumComputes()
numComputes()