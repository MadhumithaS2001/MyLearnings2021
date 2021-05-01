'''
Problem Statement:

Given two integers numbers N and K, the Ayush wants you to nd f(f(..........f(N))) K times,
where f(x) = x XOR (x%10).

Note: XOR represents bitwise xor operation

1. The rst line of the input contains a single integer T denoting the number of test
cases. The description of T test cases follows.
2. The rst line of each test case contains two integers N and K.!
For each test case, print the answer!

Constraints:

1. 1 <= T <= 10
2. 1 <= N <= 105
3. 1 <= K <= 109

'''


def f(n,k):
  if(k==1):
    return(n^n%10)
  else:
    return (f((n^n%10),k-1))

t=int(input())
for i in range(t):
  n,x=map(int,input().split())
  print(f(n,x))
