def leap(yy):
    if(yy%4==0):
        if(yy%100==0):
            if(yy%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def odd(mm):
    if(mm in (1,3,5,7,8,10,12)):
        return 31
    else:
        return 30

date=input()
l=list(map(int,date.split("/")))
dd=l[0]
mm=l[1]
yy=l[2]

if((mm>0 and mm<13) and (dd>0 and dd<=31)):
    if(mm==2):
        if(leap(yy) and dd<30):
            print("Valid")
        elif(not leap(yy) and dd<29):
            print("Valid")
        else:
            print("Invalid")
    elif(dd<=odd(mm)):
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")

