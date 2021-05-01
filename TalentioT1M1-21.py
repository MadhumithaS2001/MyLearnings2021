'''
Program Statement
Consider a non – empty array of integers inarr with the elements separated by comma
and an integer innum. Find and print a number outnum based on the below logic:
-> identify all possible unique combinations of four elements from inarr
-> A unique combination is one where , irrespective of the order, the same set of
elements in the combination will not appear in any other combination
-> if there are one or more combinations whose sum of elements is equal to innum, set
outnum with the count of combinations
-> if there is no Combination whose sum is equal to innum, print -1 Assumption: • inarr
will contain at least 4 elements
Input Format
First line contains the array inarr with the elements separated by ‘ , ‘ ( comma ) Second
line contains the integer innum
Read the input from the standard input steam
Output Format
Print outnum to the standard output stream

'''



from itertools import combinations
inarr=list(map(int,input().split(',')))
innum=int(input())
outnum=0
com=combinations(inarr,4)
for i in com:
  if(sum(i)==innum):
    outnum+=1
if(outnum==0):
  print('-1')
else:
  print(outnum)
