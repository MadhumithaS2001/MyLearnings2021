'''
ip:     S="231*+9-"     S="123+*8-"
op:     -4              -3
'''


def lis(s,l):
    for i in range(len(s)):
        if(s[i].isnumeric()):
            l.append(int(s[i]))
        else:
            s=s[i:]
            break
    return l,s

def oper(a,b,o):
    if(o=='+'):
        return a+b
    elif(o=='-'):
        return a-b
    elif(o=='*'):
        return a*b
    elif(o=="/"):
        return a//b
def fun(l,s):
    for i in range(len(s)):
        if(not s[i].isnumeric()):
            ans=oper(l[-2],l[-1],s[i])
            l.pop()
            l.pop()
            l.append(ans)
        
        else:
            s=s[i:]
            return l,s
        if(len(s)==1):
            
            return l,None
            break
ip1,ip2=input().strip("\"").split("=\"")

s=ip2
l=[]
while(len(s)):
    l,s=lis(s,l)
    l,s=fun(l,s)
    if(s==None):
        break
print(*l)
