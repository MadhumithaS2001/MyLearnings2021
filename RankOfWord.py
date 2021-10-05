'''
Given a string, find its rank among all its permutations sorted lexicographically. For example, rank of “abc” is 1, rank of “acb” is 2, and rank of “cba” is 6. 

Examples:  

Input : str[] = "acb"
Output : Rank = 2

Input : str[] = "string"
Output : Rank = 598

Input : str[] = "cba"
Output : Rank = 6

'''
import math
def min_count(i,l):
    ind=i
    c=0
    for j in range(ind+1,len(l)):
        if(l[ind]>l[j]):
            c+=1
    return c

word=input()
list1=list(word)
list2=sorted(list1)
l1=[]
l2=[]
for i in range(len(list1)):
    l1.append(list2.index(list1[i]))
# print(l1)
for i in range(len(l1)):
    l2.append(min_count(i,l1))
# print(l2)
def uniq(l):
    s=list(set(l))
    for i in s:
        if(l.count(i)>1):
            s.remove(i)
        # print(s)
    return len(s)
# print(list1)
# print(list2)
# print(l1)
# print(l2)
for i in range(len(l2)-1):
    d=(len(list1[i:])-uniq(list1[i:]))
    if(d):
        l2[i]//=(math.factorial(d))
j=0
res=0
for i in range(len(l2)-1,-1,-1):
    res+=l2[j]* math.factorial(i)
    j += 1
print(res+1)
