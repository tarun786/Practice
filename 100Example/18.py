import re
def passwordChecking():
    passwords=[x for x in input("Enter the multiple password").split(",")]
    minPass=6
    maxPass=12
    totalCustom=0
    sumSpecial=0
    listOfpass=[]
    for passStr in passwords:
        ndgits,nlower,nuper,sumSpecial=0,0,0,0
        ndgits=sum(c.isdigit() for c in passStr)
        nlower=sum(c.islower() for c in passStr)
        nuper=sum(c.isupper() for c in passStr)
        for x in passStr:
            if((x == '}') or (x == '#') or (x == '%')):
                sumSpecial+=1

        #nspecial=sum(c for c in passStr if(c=='}' or (c=='#') or (c=='%')))
        if(ndgits>0 and nlower>0 and nuper>0 and sumSpecial>0):

            totalCustom+=ndgits+nlower+nuper+sumSpecial
            if(totalCustom>=minPass or totalCustom<=maxPass):
               print(passStr)
               listOfpass.append(passStr)
            else:
               print("Wroung")

        else:
            print("Wroung")

    print(",".join(listOfpass))

    '''
        for x in passStr:
            ordNum=ord(x)
            if(x.isdigit()):
                pass
            elif(x.isupper()):
                pass
            elif(x.isdigit()):
                pass
            elif(ordNum>=33 and ordNum<=41):
                pass
            else:
                break
        if(len(passStr)>=minPass and len(passStr)<=maxPass):
           print("Pass is good")
        else:
           print("Pass is not good")
    '''


def gitpasswordChecking():
     value = []
     items = [x for x in input().split(',')]
     for p in items:
         if len(p) < 6 or len(p) > 12:
             continue
         else:
             pass
         if not re.search("[a-z]", p):
             continue
         elif not re.search("[0-9]", p):
             continue
         elif not re.search("[A-Z]", p):
             continue
         elif not re.search("[$#@]", p):
             continue
         elif re.search("\s", p):
             continue
         else:
             pass
         value.append(p)
     print(",".join(value))
#passwordChecking()
gitpasswordChecking()