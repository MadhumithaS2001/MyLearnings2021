'''
Sum of digits till we get single digit

ip:
987511

op:
4

explanation:
9+8+7+5+1+1=31
3+1=4

'''

def ad(s):
    l=[]
    for i in s:
        l.append(int(i))
    print(l)
    return str(sum(l))
s=input().strip()
res=-1
while(len(s)!=1):
    res=ad(s)
    s=res
print(s)
