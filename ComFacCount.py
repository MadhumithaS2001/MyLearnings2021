def fac(a):
    l=[a]
    for i in range(2,(a//2)+1):
        if(a%i==0):
            l.append(i)
    return (set(l))
n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(input())
a.sort()
d={}
q=0
for i in a:
    d[q]=fac(i)
    q+=1
s=d[0]
for i in range(1,n):
    s=s&d[i]
print(len(s))
