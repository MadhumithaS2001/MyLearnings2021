n,k=map(int,input().split())
ar=list(map(str,input().split()))
l=[]
for i in range(n-1):
  co=1
  for j in range(i+1,n):
    if(ar[i]==ar[j]):
      co=co+1
    l.append(int(co==k))
if(any(l)):
  print("yes")
else:
  print("no")
