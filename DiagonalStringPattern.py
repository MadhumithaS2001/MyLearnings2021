s=input().strip()
l=len(s)
for i in range((l//2)+1):
    for j in range(l):
        if(i==j or i==(l-1-j)):
            print(s[j],end="")
        else:
            print(" ",end="")
    print()
for i in range((l//2)+1,l):
    for j in range(l):
        if(i==j or i==(l-1-j)):
            print(s[j],end="")
        else:
            print(" ",end="")
        
    print()
