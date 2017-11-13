class Squr:
    def squareRoot(self):
       num = input("enter the value").split(",")
       print(num) #this is goes in list
       value=""
       c=50
       h=30
       i = 0
       for d in num:

            q=((2*c*int(d))/h)**(.5)
            #print(int(q))
            dd=str(int(q))
            if(i==0):
                value=value+dd
            else:
                value=value+","+dd
            i=i+1
       print(value)

    def gitSquar(self):
         import math
         c = 50
         h = 30
         value = []
         items = [x for x in input().split(',')]
         for d in items:
             value.append(str(int(round(math.sqrt(2 * c * float(d) / h)))))

         print(','.join(value))

obj=Squr()
obj.squareRoot()
obj.gitSquar()