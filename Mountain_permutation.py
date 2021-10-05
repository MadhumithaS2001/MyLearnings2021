'''
Input: 
3

Output:
2

Explanation:
as 3
1 2 3 is the array

its permutations are 

1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

in these only

2 3 1
1 3 2

are have one part as assending and second part as decending ( 2 3  and  3 1  //  1 3  and  3 2)

'''
from itertools import permutations as p
n=3
l=[]
for i in range(1,n+1):
    l.append(i)
m=list(map(list,p(l)))
# print(*m)
c=0
for i in m:
    ma=max(i)
    in1=i.index(ma)
    if(in1>0 or in1<len(i)-1):
        p1=(sorted(i[in1+1:],reverse=True)==i[in1+1:])
        p2=sorted(i[:in1])==i[:in1]
        p3=((i[in1+1:])!=[] and i[:in1]!=[])
        if(p1 and p2 and p3):
            c+=1
print(c)

#End
