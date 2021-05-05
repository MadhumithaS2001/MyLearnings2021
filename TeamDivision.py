'''
Consider an array inarr containing at least two non-zero positive integers ranging between 1 to 300 (inclusive of the boundary values). Divide the integers in inarr into two groups based on the below rules:

Each of the integers should belong to either of the two groups The total sum of integers in each of the groups must be as nearly equal as possible The total number of integers between the two groups should not differ by more than 1 Print, outnum1 and outnum2, the sum of the integers of two groups separated by a space. If outnum1 and outnum2 are not equal, then print the smaller sum followed by the larger sum.

Input Format

Read the array inarr elements separated by (‘,’) comma.

Constraints

1<=array elements<=1000

Output Format

Print outnum1 and outnum2 in the required order separated by a space.

For example, int the first sample test case,the two groups that can be formed following the mentioned rules are:

Group 1: 87 100 41 1 Group 2: 28 67 68 67 The total sum of integers in each of the groups which is as nearly equal as possible is:

Group 1-Total Sum:229 Group 2-Total Sum:230

The total number of integers between group 1 and 2 differ by 0 integer.

Sample Input 0

87,100,28,67,68,41,67,1
Sample Output 0

229 230
Sample Input 1

65,43,64,32,61,32
Sample Output 1

140 157

'''

a=list(map(int,input().split(',')))
s=sum(a)//2
global l
l={}
def findTwoGroup(n):
    group1Sum = s
    group1=[]
    group2=[]
    for i in a:
        if (group1Sum - i >= 0) :
            group1.append(i)
            group1Sum -= i
        else :
            group2.append(i)
    x=sum(group1)
    y=sum(group2)
    l[abs(x-y)]=[x,y]
findTwoGroup(a)
a.sort()
findTwoGroup(a)
a.sort(reverse=1)
findTwoGroup(reversed(a))
print(*l[min(l)])
