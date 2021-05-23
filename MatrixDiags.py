'''
SUM OF MATRIX DIAGNOL ELEMENTS
'''
n=int(input())
l=[]
m=n//2
su=0
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if(i==j or (i==n-j-1 and j==n-i-1)):
            su+=l[i][j]
print(su)
