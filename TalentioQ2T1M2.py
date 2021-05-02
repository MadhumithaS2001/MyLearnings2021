'''
Problem Statement

Nobel Prize-winning Austrian-Irish physicist Erwin Schrödinger developed a machine
and brought as many Christopher Columbus from as many parallel universes he could.
Actually he was quite amused by the fact that Columbus tried to nd India and got
America. He planned to dig it further. Though totally for research purposes, he made a
grid of size n X m, and planted some people of America in a position (x,y) in 1 based
indexing of the grid, and then planted you with some of your friends in the (n,m)
position of the grid. Now he gathered all the Columbus in 1,1 positions and started a
race.

Given the values for n, m, x, y, you have to tell how many different Columbus(s) together
will explore you as India for the rst time.
Remember, the Columbus who will reach to the people of America, will be thinking that
as India and hence wont come further.

Function Description

Complete the markgame function in the editor below. It has the following parameter(s):

Constraints

1 <= n <= 10^2
1 <= m <= 10^2
1 <= x <= n
1 <= y <= m

Input Format

The rst line contains an integer, n, denoting the number of rows in the grid.
The next line contains an integer m, denoting the number of columns in the grid.
The next line contains an integer, x, denoting the American cell’s row.
The next line contains an integer, y, denoting the American cell’s column.
'''

import math
n=int(input())-1
m=int(input())-1
x=int(input())-1
y=int(input())-1

ans=math.factorial(n+m)
ans=ans//(math.factorial(n))
ans=ans//(math.factorial(m))

ans1=math.factorial(x+y)
ans1=ans1//(math.factorial(x))
ans1=ans1//(math.factorial(y))
x1=n-x
y1=m-y

ans2=math.factorial(x1+y1)
ans2=ans2//(math.factorial(x1))
ans2=ans2//(math.factorial(y1))
print(ans-(ans1*ans2))
