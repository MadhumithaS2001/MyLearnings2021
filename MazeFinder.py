'''
Raj is stuck in a maze which is a rectangle having m number of rows and n number of columns and each cell in the maze has a value associated with it(say arr[i]). First he has to find the maximum(say max) and minimum(say min) value in the entire maze. Once he found these values, all the rows and columns which aligned with the cells( having values max or min) vanished. Now, he has to tell the number of cells which he will have to go through in order to come out of the maze.

Input Format

First line contains t, denoting the number of test cases. The first line of each test case will have 2 numbers m,n. Next m lines contain n separated integers denoting the value of each cell.

Constraints

1<=T<= 100000

1<=m*n<=100000

1<=arr[i][j]<=100000 for all 1<=i<=m and 1<=j<=n

Output Format

Each new line should print 1 integer, telling the number of cells left

Sample Input 0

1
3 3
8 8 3
6 2 4
12 1 2
Sample Output 0

2
Explanation 0

max= 12, min= 1 For max, 3rd row, 1st column will vanish For min, 3rd row and second column will vanish Total number of cells left 2: (1,3) and (2,3)

Sample Input 1

1
3 3
8 8 1
6 2 4
12 1 2
Sample Output 1

0
Explanation 1

max= 12, min= 1 Total number of cells left =0

'''

t=int(input())
for _ in range(t):
    r,c=map(int,input().split())
    maze=[]
    ma=[]
    mi=[]
    out=[]
    for i in range(r):
        maze.append(list(map(int,input().split())))
        out.append(maze[i].copy())
        ma.append(max(maze[i]))
        mi.append(min(maze[i]))
    _max=max(ma)
    _min=min(mi)
    del(ma)
    del(mi)
    for i in range(r):
        if(_max in maze[i]):
            for j in range(r):
                out[j][maze[i].index(_max)]=0
            out[i]=[0 for j in range (c)]
    for i in range(r):
        if(_min in maze[i]):
            for j in range(r):
                out[j][maze[i].index(_min)]=0
            out[i]=[0 for j in range (c)]
    c=0
    for i in out:
        for j in i:
            if(j>0):
                c+=1
    print(c)
